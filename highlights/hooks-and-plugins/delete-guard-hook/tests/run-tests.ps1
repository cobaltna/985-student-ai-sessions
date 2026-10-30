# delete-guard 自测：逐用例把 stdin JSON 喂给守卫脚本，比对退出码。
# 输出仅 ASCII：name / expect / got / PASS|FAIL
$ErrorActionPreference = 'Stop'
$guard  = 'C:\Users\UserX\.zcode\hooks\delete-guard.ps1'
$pwsh   = 'C:\Program Files\PowerShell\7\pwsh.exe'
$stateDir = Join-Path $env:USERPROFILE '.zcode\hooks\state'
$WS     = 'C:\Users\UserX\.zcode\workspace\default'

$cases = @(
    # ---- 应拦截 (expect 2) ----
    @{ name='blk-win-system-dir-rm';      cmd='rm -rf C:\Windows\System32';                          cwd='C:\proj'; expect=2 }
    @{ name='blk-win-system-dir-gb';      cmd='rm -rf /c/Windows/Fonts';                             cwd='C:\proj'; expect=2 }
    @{ name='blk-posix-root';             cmd='rm -rf /';                                            cwd='C:\proj'; expect=2 }
    @{ name='blk-posix-root-wild';        cmd='rm -rf /*';                                           cwd='C:\proj'; expect=2 }
    @{ name='blk-no-preserve-root';       cmd='rm -rf --no-preserve-root /';                         cwd='C:\proj'; expect=2 }
    @{ name='blk-no-preserve-root-bare';  cmd='rm --no-preserve-root';                               cwd='C:\proj'; expect=2 }
    @{ name='blk-tilde-root';             cmd='rm -rf ~';                                            cwd='C:\proj'; expect=2 }
    @{ name='blk-home-var';               cmd='rm -rf $HOME';                                        cwd='C:\proj'; expect=2 }
    @{ name='blk-userprofile-var';        cmd='Remove-Item -Recurse -Force $env:USERPROFILE';        cwd='C:\proj'; expect=2 }
    @{ name='blk-users-root';             cmd='Remove-Item -Recurse -Force C:\Users';                cwd='C:\proj'; expect=2 }
    @{ name='blk-profile-root';           cmd='rm -rf C:\Users\UserX';                               cwd='C:\proj'; expect=2 }
    @{ name='blk-zcode-root';             cmd='rm -rf ~/.zcode';                                     cwd='C:\proj'; expect=2 }
    @{ name='blk-drive-root-wild';        cmd='del /f /s /q C:\*.*';                                 cwd='C:\proj'; expect=2 }
    @{ name='blk-drive-root-rd';          cmd='rd /s /q D:\';                                        cwd='C:\proj'; expect=2 }
    @{ name='blk-drive-root-remove';      cmd='Remove-Item C:\* -Recurse -Force';                    cwd='C:\proj'; expect=2 }
    @{ name='blk-format-c';               cmd='format C:';                                           cwd='C:\proj'; expect=2 }
    @{ name='blk-format-volume';          cmd='Format-Volume -DriveLetter D';                        cwd='C:\proj'; expect=2 }
    @{ name='blk-diskpart-clean';         cmd='echo select disk 0 | diskpart; echo clean';           cwd='C:\proj'; expect=2 }
    @{ name='blk-vssadmin';               cmd='vssadmin delete shadows /all /quiet';                 cwd='C:\proj'; expect=2 }
    @{ name='blk-wsl-unregister';         cmd='wsl --unregister Ubuntu-22.04';                       cwd='C:\proj'; expect=2 }
    @{ name='blk-wsl-inner-rm';           cmd='wsl -d Ubuntu rm -rf /';                              cwd='C:\proj'; expect=2 }
    @{ name='blk-dd-dev';                 cmd='dd if=/dev/zero of=/dev/sda';                         cwd='C:\proj'; expect=2 }
    @{ name='blk-dd-physdrive';           cmd='dd if=big.img of=\\.\PhysicalDrive1';                 cwd='C:\proj'; expect=2 }
    @{ name='blk-mkfs';                   cmd='mkfs.ext4 /dev/sdb1';                                 cwd='C:\proj'; expect=2 }
    @{ name='blk-wipefs';                 cmd='wipefs -a /dev/sdb';                                  cwd='C:\proj'; expect=2 }
    @{ name='blk-shred-dev';              cmd='shred -v -n 3 /dev/sda';                              cwd='C:\proj'; expect=2 }
    @{ name='blk-find-root-delete';       cmd='find / -name "*.bak" -delete';                        cwd='C:\proj'; expect=2 }
    @{ name='blk-cd-root-then-del';       cmd='cd /d C:\ && del /f /s /q *.*';                       cwd='C:\proj'; expect=2 }
    @{ name='blk-cd-windows-then-rm';     cmd='cd C:\Windows && rm -rf *';                           cwd='C:\proj'; expect=2 }
    @{ name='blk-removeitem-win-temp';    cmd='Remove-Item -Path C:\Windows\Temp -Recurse -Force';   cwd='C:\proj'; expect=2 }
    @{ name='blk-bash-c-usr';             cmd='bash -c ''rm -rf /usr''';                             cwd='C:\proj'; expect=2 }
    @{ name='blk-pwsh-c-root';            cmd='pwsh -Command "Remove-Item C:\ -Recurse -Force"';     cwd='C:\proj'; expect=2 }
    @{ name='blk-program-files';          cmd='rm -rf "C:\Program Files\App"';                       cwd='C:\proj'; expect=2 }
    @{ name='blk-cmd-c-users';            cmd='cmd /c "rd /s /q C:\Users"';                          cwd='C:\proj'; expect=2 }
    @{ name='blk-etc-prefix';             cmd='rm -rf /etc/nginx';                                   cwd='C:\proj'; expect=2 }
    @{ name='blk-sudo-etc';               cmd='sudo rm -rf /etc';                                    cwd='C:\proj'; expect=2 }
    @{ name='blk-del-single-win-file';    cmd='del C:\Windows\notepad.exe';                          cwd='C:\proj'; expect=2 }
    @{ name='blk-rel-traverse-above';     cmd='rm -rf ../../*';                                      cwd='C:\proj'; expect=2 }
    # ---- 应放行 (expect 0) ----
    @{ name='ok-node_modules';            cmd='rm -rf node_modules';                                 cwd='C:\proj'; expect=0 }
    @{ name='ok-workspace-sub';           cmd='rm -rf C:\Users\UserX\.zcode\workspace\default\build'; cwd=$WS;      expect=0 }
    @{ name='ok-workspace-gb-path';       cmd='rm -rf /c/Users/UserX/.zcode/workspace/default/dist'; cwd='C:\proj'; expect=0 }
    @{ name='ok-venv-lib';                cmd='rm -rf /c/Users/UserX/.venv/lib';                     cwd='C:\proj'; expect=0 }
    @{ name='ok-venv-seg';                cmd='rm -rf C:\proj\.venv';                                cwd='C:\proj'; expect=0 }
    @{ name='ok-downloads-sub';           cmd='rm -rf ~/Downloads/old_stuff';                        cwd='C:\proj'; expect=0 }
    @{ name='ok-temp-var';                cmd='Remove-Item $env:TEMP\log.txt';                       cwd='C:\proj'; expect=0 }
    @{ name='ok-git-clean';               cmd='git clean -fdx';                                      cwd='C:\proj'; expect=0 }
    @{ name='ok-npm-cache-clean';         cmd='npm cache clean --force';                             cwd='C:\proj'; expect=0 }
    @{ name='ok-format-table';            cmd='Get-ChildItem | Format-Table -AutoSize';              cwd='C:\proj'; expect=0 }
    @{ name='ok-plain-file';              cmd='rm build.o';                                          cwd='C:\proj'; expect=0 }
    @{ name='ok-echo-format';             cmd='echo "format C: is dangerous"';                       cwd='C:\proj'; expect=0 }
    @{ name='ok-docker-prune';            cmd='docker system prune -af';                             cwd='C:\proj'; expect=0 }
    @{ name='ok-del-txt';                 cmd='del result.txt';                                      cwd='C:\proj'; expect=0 }
    @{ name='ok-shred-file';              cmd='shred -u secret.txt';                                 cwd='C:\proj'; expect=0 }
    @{ name='ok-find-cwd-delete';         cmd='find . -name "*.tmp" -delete';                        cwd=$WS;       expect=0 }
    @{ name='ok-windows-old';             cmd='rm -rf C:\Windows.old';                               cwd='C:\proj'; expect=0 }
    @{ name='ok-registry';                cmd='Remove-Item HKLM:\SOFTWARE\TestKey';                  cwd='C:\proj'; expect=0 }
    @{ name='ok-docs-file';               cmd='del C:\Users\UserX\Documents\notes.txt';              cwd='C:\proj'; expect=0 }
    @{ name='ok-tmp-posix';               cmd='rm -rf /tmp/build';                                   cwd='C:\proj'; expect=0 }
    @{ name='ok-cd-workspace-then-rm';    cmd='cd C:\Users\UserX\.zcode\workspace\default && rm -rf *'; cwd='C:\proj'; expect=0 }
)

$fail = 0
foreach ($c in $cases) {
    if (Test-Path $stateDir) { Remove-Item $stateDir -Recurse -Force }
    $payload = @{ tool_name = 'Bash'; tool_input = @{ command = $c.cmd }; cwd = $c.cwd } | ConvertTo-Json -Depth 5
    $null = $payload | & $pwsh -NoProfile -ExecutionPolicy Bypass -File $guard 2>&1
    $got = $LASTEXITCODE
    $ok = ($got -eq $c.expect)
    if (-not $ok) { $fail++ }
    '{0,-26} expect={1} got={2} {3}' -f $c.name, $c.expect, $got, $(if ($ok) { 'PASS' } else { 'FAIL' })
}

# ---- 审查重试机制：同命令第二次应放行 ----
if (Test-Path $stateDir) { Remove-Item $stateDir -Recurse -Force }
$payload = @{ tool_name = 'Bash'; tool_input = @{ command = 'rm -rf C:\Windows\System32' }; cwd = 'C:\proj' } | ConvertTo-Json -Depth 5
$null = $payload | & $pwsh -NoProfile -ExecutionPolicy Bypass -File $guard 2>&1
$first = $LASTEXITCODE
$null = $payload | & $pwsh -NoProfile -ExecutionPolicy Bypass -File $guard 2>&1
$second = $LASTEXITCODE
$retryOk = ($first -eq 2 -and $second -eq 0)
if (-not $retryOk) { $fail++ }
'{0,-26} expect=2->0 got={1}->{2} {3}' -f 'retry-after-review', 2, 0, "$first->$second", $(if ($retryOk) { 'PASS' } else { 'FAIL' })

if (Test-Path $stateDir) { Remove-Item $stateDir -Recurse -Force }
'---'
"TOTAL_FAIL=$fail"
