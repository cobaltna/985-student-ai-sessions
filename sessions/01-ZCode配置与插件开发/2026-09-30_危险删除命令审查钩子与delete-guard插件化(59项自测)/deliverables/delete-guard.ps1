# =============================================================================
# delete-guard.ps1 — ZCode PreToolUse 钩子：拦截“极度危险”的删除命令，强制模型先审查
#
# stdin  : {"tool_name":"Bash","tool_input":{"command":"..."},"cwd":"..."}
# exit 0 : 放行（正常命令、豁免路径、或已审查后的原样重发）
# exit 2 : 拦截（stderr 上的审查指令会反馈给模型）
# 任何内部异常：放行（fail-open，绝不因脚本自身故障卡住正常工作）
#
# 拦截范围（仅极度危险，按用户 2026-09-30 确认的方案）：
#   - 磁盘/分区级：format X:、diskpart+clean、Clear-Disk/Format-Volume/Remove-Partition 等、
#     dd 直写设备、mkfs*、wipefs、shred 设备
#   - Windows 系统目录：C:\Windows、Program Files(±x86)、ProgramData、C:\Recovery、C:\Boot
#   - 根/主目录：盘根（C:\、C:\*、POSIX /、/*）、C:\Users 根、用户主目录根、~/.zcode 本身、
#     --no-preserve-root
#   - 其它：vssadmin delete shadows、wsl --unregister、find <危险路径> -delete
# 豁免（优先于拦截）：会话工作目录子树、~/.zcode\workspace 子树、一切 venv
#   （.venv/venv/env/site-packages/node_modules/__pycache__/.tox/conda envs）
# =============================================================================

[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$ErrorActionPreference = 'Stop'

$script:EnvDirMap = @{
    'windir'            = 'c:\windows'
    'systemroot'        = 'c:\windows'
    'programfiles'      = 'c:\program files'
    'programfiles(x86)' = 'c:\program files (x86)'
    'programdata'       = 'c:\programdata'
    'systemdrive'       = 'c:'
}
$script:DeleteVerbs = @('rm', 'rmdir', 'del', 'erase', 'rd', 'ri', 'remove-item', 'unlink', 'shred', 'find')
$script:DiskVerbs   = @('clear-disk', 'format-volume', 'remove-partition', 'remove-physicaldisk', 'remove-volume', 'clear-volume')
$script:CdVerbs     = @('cd', 'chdir', 'set-location', 'sl', 'pushd')

function Get-Sha256Hex([string]$text) {
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try {
        $bytes = [System.Text.Encoding]::UTF8.GetBytes($text)
        ([System.BitConverter]::ToString($sha.ComputeHash($bytes)) -replace '-', '').ToLowerInvariant()
    }
    finally { $sha.Dispose() }
}

# 主目录别名：ZCode 会话里的 USERPROFILE 可能是 junction 名（如 C:\Users\UserX），
# 也可能是真实目录名，两者都必须被识别为“主目录根”。
function Get-ProfileAliases {
    $set = [System.Collections.Generic.List[string]]::new()
    $p = $env:USERPROFILE
    if ($p) {
        $a = $p.TrimEnd('\').ToLowerInvariant()
        if (-not $set.Contains($a)) { $set.Add($a) }
        try {
            $t = (Get-Item $p -Force).Target
            if ($t) {
                if ($t -is [System.Array]) { $t = $t[0] }
                $b = ([string]$t).TrimEnd('\').ToLowerInvariant()
                if ($b -and -not $set.Contains($b)) { $set.Add($b) }
            }
        }
        catch { }
    }
    return $set.ToArray()
}

function Get-VerbOf([string]$tok) {
    $t = $tok.Trim().Trim('"', "'")
    if (-not $t) { return '' }
    $leaf = Split-Path -Leaf $t
    return ($leaf.ToLowerInvariant() -replace '\.(exe|com)$', '')
}

# 令牌 → 归一化路径：小写、统一反斜杠、展开 ~/$HOME/$env:*/%VAR%/Git-Bash 盘符。
# 返回 @{ base = 归一化小写路径; rel = 是否相对路径; device = 是否设备对象 }
function ConvertTo-NormPath {
    param([string]$Token, [string[]]$ProfileAliases)
    $s = $Token.Trim()
    if ($s.Length -ge 2) { $s = $s.Trim('"', "'") }
    if (-not $s) { return $null }
    $lower = $s.ToLowerInvariant()

    if ($lower -eq '~' -or $lower -eq '$home' -or $lower -eq '$env:userprofile' -or $lower -eq '%userprofile%') {
        return @{ base = $ProfileAliases[0]; rel = $false; device = $false }
    }
    foreach ($k in $script:EnvDirMap.Keys) {
        $p1 = '$env:' + $k; $p2 = '${env:' + $k + '}'; $p3 = '%' + $k + '%'
        if ($lower -eq $p1 -or $lower -eq $p2 -or $lower -eq $p3) {
            return @{ base = $script:EnvDirMap[$k]; rel = $false; device = $false }
        }
        foreach ($pref in @($p1 + '\', $p1 + '/', $p2 + '\', $p2 + '/', $p3 + '\', $p3 + '/')) {
            if ($lower.StartsWith($pref)) {
                $s = $script:EnvDirMap[$k] + $s.Substring($pref.Length)
                $lower = $s.ToLowerInvariant()
                break
            }
        }
    }
    if ($lower.StartsWith('~\') -or $lower.StartsWith('~/')) {
        $s = $ProfileAliases[0] + $s.Substring(1); $lower = $s.ToLowerInvariant()
    }
    elseif ($lower.StartsWith('$home\') -or $lower.StartsWith('$home/')) {
        $s = $ProfileAliases[0] + $s.Substring(5); $lower = $s.ToLowerInvariant()
    }
    elseif ($lower.StartsWith('$env:userprofile\') -or $lower.StartsWith('$env:userprofile/')) {
        $s = $ProfileAliases[0] + $s.Substring(17); $lower = $s.ToLowerInvariant()
    }

    # Git Bash 风格 /c/... → c:\...
    $m = [regex]::Match($s, '^/([a-zA-Z])(/|$)(.*)$')
    if ($m.Success) {
        $s = $m.Groups[1].Value.ToLowerInvariant() + ':' + $(if ($m.Groups[2].Value -eq '/') { '\' + $m.Groups[3].Value } else { '' })
    }

    $s = $s -replace '/', '\'
    $isDevice = ($s -match '^\\\\\.\\') -or ($s -match '^\\dev(\\|$)')
    $s = $s -replace '\\{2,}', '\'
    if ($s -eq '\') { return @{ base = '\'; rel = $false; device = $false } }   # POSIX 根 /
    $s = $s.TrimEnd('\')
    if (-not $s) { return $null }

    $rel = -not ($s -match '^[a-zA-Z]:' -or $s.StartsWith('\'))
    return @{ base = $s.ToLowerInvariant(); rel = $rel; device = $isDevice }
}

# 目录拼接 + 解析 .. 与 .（DirNorm 为归一化绝对目录；RelNorm 可为相对或绝对）
function Join-Norm([string]$DirNorm, [string]$RelNorm) {
    $posix = $false
    $parts = [System.Collections.Generic.List[string]]::new()
    if ($RelNorm -match '^[a-zA-Z]:' -or $RelNorm.StartsWith('\')) {
        $posix = $RelNorm.StartsWith('\')
        foreach ($p in ($RelNorm -split '\\')) { if ($p) { $parts.Add($p) } }
    }
    else {
        if (-not $DirNorm) { return $null }
        $posix = $DirNorm.StartsWith('\')
        foreach ($p in ($DirNorm -split '\\')) { if ($p) { $parts.Add($p) } }
        foreach ($p in ($RelNorm -split '\\')) { if ($p) { $parts.Add($p) } }
    }
    $out = [System.Collections.Generic.List[string]]::new()
    foreach ($p in $parts) {
        if ($p -eq '.') { continue }
        if ($p -eq '..') {
            if ($out.Count -gt 0 -and $out[$out.Count - 1] -notmatch ':$') { $out.RemoveAt($out.Count - 1) }
            continue
        }
        $out.Add($p)
    }
    $joined = ($out -join '\')
    if ($posix) { if ($joined) { return '\' + $joined } else { return '\' } }
    if (-not $joined) { return $null }
    return $joined
}

# 判定归一化路径是否“极度危险”。返回类别字符串或 $null。
function Get-PathDanger {
    param([string]$Base, [bool]$Device, [string[]]$ProfileAliases)
    if ($Device) { return '磁盘/设备对象' }
    if (-not $Base) { return $null }
    if ($Base -match '^[a-z]:$') { return '盘根（整盘删除）' }
    if ($Base -eq '\') { return '文件系统根（/）' }
    foreach ($p in @('c:\windows', 'c:\program files', 'c:\program files (x86)', 'c:\programdata', 'c:\recovery', 'c:\boot')) {
        if ($Base -eq $p -or $Base.StartsWith($p + '\')) { return 'Windows 系统目录' }
    }
    if ($Base -eq 'c:\users') { return 'C:\Users 根（所有用户主目录）' }
    foreach ($pa in $ProfileAliases) {
        if ($Base -eq $pa) { return '用户主目录根' }
        if ($Base -eq ($pa + '\.zcode')) { return '~/.zcode 配置目录' }
    }
    foreach ($p in @('\bin', '\boot', '\etc', '\lib', '\lib64', '\sbin', '\usr', '\var', '\root')) {
        if ($Base -eq $p -or $Base.StartsWith($p + '\')) { return 'POSIX 系统目录' }
    }
    if ($Base -eq '\home') { return 'POSIX /home 根' }
    return $null
}

function Test-VenvSegment([string]$Base) {
    if (-not $Base) { return $false }
    if ($Base -match '(^|\\)(\.venv|venv|env|site-packages|node_modules|__pycache__|\.tox)(\\|$)') { return $true }
    if ($Base -match '\\(anaconda3|miniconda3)\\envs(\\|$)') { return $true }
    return $false
}

function Test-SafeZone([string]$Base, [string[]]$SafeRoots) {
    if (-not $Base) { return $false }
    foreach ($r in $SafeRoots) {
        if ($Base -eq $r -or $Base.StartsWith($r + '\')) { return $true }
    }
    return $false
}

function Get-Tokens([string]$Seg) {
    $list = [System.Collections.Generic.List[string]]::new()
    foreach ($m in [regex]::Matches($Seg, '(''[^'']*''|"[^"]*"|\S+)')) { $list.Add($m.Value) }
    return $list
}

# 去掉整体包裹的一层引号（解释器 -c 参数常为整段引号字符串）
function Unwrap-Quotes([string]$s) {
    $t = $s.Trim()
    if ($t.Length -ge 2) {
        if (($t[0] -eq '"' -and $t[$t.Length - 1] -eq '"') -or ($t[0] -eq "'" -and $t[$t.Length - 1] -eq "'")) {
            return $t.Substring(1, $t.Length - 2)
        }
    }
    return $t
}

# 单段命令分析。返回 @{ category; detail } 或 $null。
function Get-SegmentVerdict([string]$Seg, [hashtable]$Ctx) {
    $tokens = Get-Tokens $Seg
    if ($tokens.Count -eq 0) { return $null }

    $i = 0
    while ($i -lt $tokens.Count -and $tokens[$i] -match '^[A-Za-z_][A-Za-z0-9_]*=') { $i++ }
    while ($i -lt $tokens.Count -and (Get-VerbOf $tokens[$i]) -in @('sudo', 'nohup', 'env', 'command', 'nice', 'time')) { $i++ }
    if ($i -ge $tokens.Count) { return $null }
    $head = Get-VerbOf $tokens[$i]
    if (-not $head) { return $null }

    # ---- 解释器包装：递归分析内层命令 ----
    if ($head -in @('pwsh', 'powershell')) {
        for ($k = $i + 1; $k -lt $tokens.Count; $k++) {
            $t = $tokens[$k].Trim('"', "'").ToLowerInvariant()
            if ($t -eq '-encodedcommand' -and ($k + 1) -lt $tokens.Count) {
                try {
                    $inner = [System.Text.Encoding]::Unicode.GetString([Convert]::FromBase64String((Unwrap-Quotes $tokens[$k + 1])))
                    return (Get-SegmentVerdict $inner $Ctx)
                }
                catch { return $null }
            }
            if ($t -in @('-c', '-command')) {
                if (($k + 1) -lt $tokens.Count) {
                    $rest = Unwrap-Quotes (($tokens[($k + 1)..($tokens.Count - 1)] -join ' '))
                    if ($rest) { return (Get-SegmentVerdict $rest $Ctx) }
                }
                return $null
            }
        }
        return $null
    }
    if ($head -in @('bash', 'sh', 'zsh', 'dash', 'ksh')) {
        for ($k = $i + 1; $k -lt $tokens.Count; $k++) {
            if ($tokens[$k] -match '^-[a-zA-Z]*c[a-zA-Z]*$') {
                if (($k + 1) -lt $tokens.Count) {
                    $rest = Unwrap-Quotes (($tokens[($k + 1)..($tokens.Count - 1)] -join ' '))
                    if ($rest) { return (Get-SegmentVerdict $rest $Ctx) }
                }
                return $null
            }
        }
        return $null
    }
    if ($head -in @('cmd')) {
        for ($k = $i + 1; $k -lt $tokens.Count; $k++) {
            $t = $tokens[$k].Trim('"', "'").ToLowerInvariant()
            if ($t -in @('/c', '/k')) {
                if (($k + 1) -lt $tokens.Count) {
                    $rest = Unwrap-Quotes (($tokens[($k + 1)..($tokens.Count - 1)] -join ' '))
                    if ($rest) { return (Get-SegmentVerdict $rest $Ctx) }
                }
                return $null
            }
        }
        return $null
    }
    if ($head -in @('wsl')) {
        foreach ($t in $tokens) { if ($t.Trim('"', "'") -eq '--unregister') { return @{ category = 'WSL 发行版注销（整个发行版文件系统删除）'; detail = $Seg.Trim() } } }
        $k = $i + 1
        while ($k -lt $tokens.Count) {
            $t = $tokens[$k].Trim('"', "'").ToLowerInvariant()
            if ($t -eq '-d' -or $t -eq '--distribution') { $k += 2; continue }
            if ($t.StartsWith('-')) { $k += 1; continue }
            break
        }
        if ($k -lt $tokens.Count) {
            $rest = Unwrap-Quotes (($tokens[$k..($tokens.Count - 1)] -join ' '))
            if ($rest) { return (Get-SegmentVerdict $rest $Ctx) }
        }
        return $null
    }

    # ---- 命令级判据 ----
    if ($head -in @('format', 'format.com')) {
        if ($tokens.Count -gt ($i + 1)) {
            foreach ($t in $tokens[($i + 1)..($tokens.Count - 1)]) {
                if ($t -match '^[a-zA-Z]:') { return @{ category = '格式化磁盘（全部数据清空）'; detail = $Seg.Trim() } }
            }
        }
    }
    if ($head -in $script:DiskVerbs) {
        return @{ category = '磁盘/分区级删除（Clear-Disk / Format-Volume / Remove-Partition 等）'; detail = $Seg.Trim() }
    }
    if ($head -eq 'dd') {
        if ($Seg.ToLowerInvariant() -match '\bof\s*=\s*"?(/dev/|\\\\\.\\)') {
            return @{ category = 'dd 直写磁盘设备'; detail = $Seg.Trim() }
        }
    }
    if ($head.StartsWith('mkfs')) { return @{ category = 'mkfs 重建文件系统（覆盖磁盘）'; detail = $Seg.Trim() } }
    if ($head -eq 'wipefs') { return @{ category = 'wipefs 擦除文件系统签名'; detail = $Seg.Trim() } }
    if ($head -eq 'vssadmin' -and $Seg.ToLowerInvariant() -match '\bdelete\b') {
        return @{ category = '删除卷影副本（系统备份点）'; detail = $Seg.Trim() }
    }
    if ($head -notin $script:DeleteVerbs) { return $null }

    # ---- 删除类命令：提取目标路径逐一判定 ----
    $rest = @()
    if ($tokens.Count -gt ($i + 1)) { $rest = $tokens[($i + 1)..($tokens.Count - 1)] }

    foreach ($t in $rest) {
        if ($t.Trim('"', "'") -eq '--no-preserve-root') {
            return @{ category = '绕过根目录保护（--no-preserve-root）'; detail = $Seg.Trim() }
        }
    }

    if ($head -eq 'find') {
        $hasDelete = $false
        foreach ($t in $rest) {
            $lt = $t.ToLowerInvariant()
            if ($lt -eq '-delete' -or $lt -eq '-exec' -or $lt -eq '-execdir') { $hasDelete = $true }
        }
        if (-not $hasDelete) { return $null }
    }

    $targets = [System.Collections.Generic.List[string]]::new()
    $namedNext = $false
    foreach ($t in $rest) {
        $lt = $t.ToLowerInvariant()
        if ($namedNext) { $targets.Add($t); $namedNext = $false; continue }
        if ($lt -in @('-path', '-literalpath', '-lp')) { $namedNext = $true; continue }
        if ($lt.StartsWith('-')) { continue }
        if ($lt -in @('/s', '/q', '/f', '/p', '/y')) { continue }
        if ($lt.StartsWith('/a')) { continue }
        $targets.Add($t)
    }

    foreach ($t in $targets) {
        $n = ConvertTo-NormPath -Token $t -ProfileAliases $Ctx.ProfileAliases
        if (-not $n) { continue }
        $base = $n.base
        if ($n.rel) {
            $base = Join-Norm -DirNorm $Ctx.EffCwd -RelNorm $base
            if (-not $base) { continue }
        }
        if ($base -ne '\') {
            $stripped = ($base -replace '\\[*].*$', '')
            if ($stripped) { $base = $stripped }
            elseif ($base.StartsWith('\')) { $base = '\' }
        }
        if (Test-SafeZone $base $Ctx.SafeRoots) { continue }
        if (Test-VenvSegment $base) { continue }
        $cat = Get-PathDanger -Base $base -Device $n.device -ProfileAliases $Ctx.ProfileAliases
        if ($cat) { return @{ category = $cat; detail = $Seg.Trim() } }
    }
    return $null
}

# 顶层 cd/pushd 会改变后续相对路径的基准目录（裸 cd → 主目录）
function Update-EffCwd([string]$Seg, [hashtable]$Ctx) {
    $tokens = Get-Tokens $Seg
    if ($tokens.Count -eq 0) { return }
    $idx = 0
    while ($idx -lt $tokens.Count -and $tokens[$idx] -match '^[A-Za-z_][A-Za-z0-9_]*=') { $idx++ }
    if ($idx -ge $tokens.Count) { return }
    if ((Get-VerbOf $tokens[$idx]) -notin $script:CdVerbs) { return }
    $idx++
    $target = $null
    while ($idx -lt $tokens.Count) {
        $lt = $tokens[$idx].ToLowerInvariant()
        if ($lt -in @('-path', '-literalpath', '-lp') -or $lt.StartsWith('-')) { $idx++; continue }
        if ($lt -match '^/[a-za-z]$') { $idx++; continue }
        $target = $tokens[$idx]; break
    }
    if (-not $target) { $Ctx.EffCwd = $Ctx.ProfileAliases[0]; return }
    $n = ConvertTo-NormPath -Token $target -ProfileAliases $Ctx.ProfileAliases
    if (-not $n) { $Ctx.EffCwd = ''; return }
    $Ctx.EffCwd = Join-Norm -DirNorm $Ctx.EffCwd -RelNorm $n.base
}

function Get-CommandVerdict {
    param([string]$Command, [string]$Cwd, [string[]]$ProfileAliases, [string[]]$SafeRoots)
    $cmdLower = $Command.ToLowerInvariant()
    if ($cmdLower -match 'diskpart' -and $cmdLower -match '\bclean\b') {
        return @{ category = 'diskpart clean（清空磁盘/分区）'; detail = $Command.Trim() }
    }

    $eff = ''
    if ($Cwd) {
        $n = ConvertTo-NormPath -Token $Cwd -ProfileAliases $ProfileAliases
        if ($n -and -not $n.rel) { $eff = $n.base }
    }
    $ctx = @{ ProfileAliases = $ProfileAliases; SafeRoots = $SafeRoots; EffCwd = $eff }

    $segments = [regex]::Split($Command, '[;|&\r\n]+')
    foreach ($seg in $segments) {
        if (-not $seg.Trim()) { continue }
        $v = Get-SegmentVerdict $seg $ctx
        if ($v) { return $v }
        Update-EffCwd $seg $ctx
    }
    return $null
}

# ============================== main ==============================
try {
    # stdin 可能含非 ASCII 路径（junction 真实名等）；[Console]::In 走系统 GBK 会吞字节损坏 JSON，
    # 必须从原始字节流显式按 UTF-8 解码
    $stdinStream = [Console]::OpenStandardInput()
    $ms = [System.IO.MemoryStream]::new()
    $stdinStream.CopyTo($ms)
    $raw = [System.Text.Encoding]::UTF8.GetString($ms.ToArray())
    if ([string]::IsNullOrWhiteSpace($raw)) { exit 0 }
    $raw = $raw.TrimStart([char]0xFEFF)
    $payload = $raw | ConvertFrom-Json

    $toolName = [string]$payload.tool_name
    if ($toolName -and $toolName -ne 'Bash') { exit 0 }
    $cmd = [string]$payload.tool_input.command
    if (-not $cmd -or -not $cmd.Trim()) { exit 0 }
    $cwd = [string]$payload.cwd

    # 快速预筛：绝大多数命令不涉及删除关键词，直接放行
    $prefilter = 'rm\b|\bdel\b|\berase\b|\brd\b|rmdir|remove-item|\bri\b|unlink|shred|format|diskpart|mkfs|wipefs|\bdd\b|vssadmin|unregister|\bclean\b|clear-disk|clear-volume|remove-partition|remove-physicaldisk|remove-volume|\bfind\b|--no-preserve-root'
    if ($cmd.ToLowerInvariant() -notmatch $prefilter) { exit 0 }

    $profileAliases = @(Get-ProfileAliases)
    if ($profileAliases.Count -eq 0) { exit 0 }

    $safeRoots = [System.Collections.Generic.List[string]]::new()
    foreach ($pa in $profileAliases) { $safeRoots.Add($pa + '\.zcode\workspace') }
    if ($cwd) {
        $n = ConvertTo-NormPath -Token $cwd -ProfileAliases $profileAliases
        if ($n -and -not $n.rel) { $safeRoots.Add($n.base) }
    }

    $verdict = Get-CommandVerdict -Command $cmd -Cwd $cwd -ProfileAliases $profileAliases -SafeRoots $safeRoots.ToArray()
    if (-not $verdict) { exit 0 }

    # ---- 审查状态机：首次拦截；15 分钟内原样重发同一命令 → 放行 ----
    $stateDir = Join-Path $env:USERPROFILE '.zcode\hooks\state'
    if (-not (Test-Path $stateDir)) { [void](New-Item -ItemType Directory -Path $stateDir -Force) }
    $key = Get-Sha256Hex ($cwd + '|' + $cmd)
    $stateFile = Join-Path $stateDir ($key + '.json')
    if (Test-Path $stateFile) {
        $ageMin = ((Get-Date) - (Get-Item $stateFile).LastWriteTime).TotalMinutes
        Remove-Item $stateFile -Force -ErrorAction SilentlyContinue
        if ($ageMin -le 15) { exit 0 }   # 模型审查后原样重发 → 放行
    }
    Set-Content -Path $stateFile -Value (Get-Date -Format o) -Encoding utf8

    # 顺带清理 1 小时前的过期状态
    Get-ChildItem -Path $stateDir -Filter '*.json' -ErrorAction SilentlyContinue |
        Where-Object { $_.LastWriteTime -lt (Get-Date).AddHours(-1) } |
        Remove-Item -Force -ErrorAction SilentlyContinue

    $reason = @"
⛔ 已拦截一条高危删除命令（类别：$($verdict.category)）
触发命令：$($verdict.detail)

这是强制审查闸，不是最终拒绝。请立即审查该命令：
1. 确认删除目标的准确路径与递归范围，是否会波及系统文件或用户数据；
2. 确认操作是否可逆、是否有备份；
3. 若审慎评估后确认该命令确属任务必需且风险可控，请原样重发同一条命令（钩子将放行执行）；
   否则请修改命令、缩小删除范围，或先向用户说明风险并征得同意。
"@
    [Console]::Error.WriteLine($reason)
    exit 2
}
catch {
    exit 0
}
