# Cross-Editor Usage Guide

The `local-ocr` skill is editor-agnostic. The OCR logic lives in `ocr.py` (a plain Python script using only the standard library), so any AI editor that can run shell commands can use it. Below are setup notes for popular editors.

## Universal Principle

The skill is just **a folder + a Python script**. The SKILL.md tells the AI *when* and *how* to call `ocr.py`. As long as the editor loads SKILL.md and lets the agent run shell commands, the skill works.

```
local-ocr/
├── SKILL.md          # Instructions for the AI (when/how to invoke)
├── ocr.py            # The actual OCR script (run via `python ocr.py ...`)
├── INSTALL.md        # Setup & rollback
└── CROSS_EDITOR.md   # This file
```

---

## trae (Trae / Trae CN)

**Skill location** (pick one):

- Global: `C:\Users\<you>\.trae-cn\skills\local-ocr\`
- Project: `<project>\.trae\skills\local-ocr\`

trae auto-discovers skills on startup. After copying the folder, restart trae.

**Default script path in SKILL.md** is already set for trae:
```
C:\Users\UserX\.trae-cn\skills\local-ocr\ocr.py
```

If your Windows username differs, search-replace `UserX` in `SKILL.md` and `INSTALL.md` with your actual username, or use the `%USERPROFILE%` form:

```bash
python "%USERPROFILE%\.trae-cn\skills\local-ocr\ocr.py" -i image.png
```

---

## Qoder

Qoder supports project-level skills via the `.qoder/skills/` directory.

**Setup**:

1. Copy the skill folder:
   ```powershell
   Copy-Item -Recurse "C:\Users\UserX\.trae-cn\skills\local-ocr" ".qoder\skills\local-ocr"
   ```
2. In Qoder, the agent will read `.qoder/skills/local-ocr/SKILL.md`.
3. The script path in SKILL.md needs to match Qoder's working directory. Either:
   - Use relative path: `python ".qoder/skills/local-ocr/ocr.py" -i image.png`
   - Or use absolute path: `python "C:\Users\<you>\.qoder\skills\local-ocr\ocr.py" -i image.png`

**Tip**: If you want the skill globally available in Qoder, place it in `C:\Users\<you>\.qoder\skills\local-ocr\` (create the folder if it doesn't exist).

---

## OpenCode

OpenCode (the terminal-based AI coding agent) supports skills via the `.opencode/` directory or its global config.

**Setup**:

1. Copy the skill folder:
   ```powershell
   Copy-Item -Recurse "C:\Users\UserX\.trae-cn\skills\local-ocr" ".opencode\skills\local-ocr"
   ```
2. OpenCode reads `SKILL.md` from `.opencode/skills/<name>/SKILL.md`.
3. Adjust paths in SKILL.md to match (relative paths work well for OpenCode):
   ```bash
   python ".opencode/skills/local-ocr/ocr.py" -i image.png
   ```

**For global use** in OpenCode, check `~/.config/opencode/` (Linux/macOS) or `%APPDATA%\opencode\` (Windows) and create a `skills/` subfolder there.

---

## Cursor

Cursor doesn't have a native "skill" system, but you can achieve the same effect via **Cursor Rules** or **project docs**.

**Option A: Project-level rule**

1. Copy `ocr.py` to your project:
   ```powershell
   Copy-Item "C:\Users\UserX\.trae-cn\skills\local-ocr\ocr.py" ".cursor\ocr.py"
   ```
2. Create `.cursorrules` (or `.cursor/rules/ocr.md`) with the content of `SKILL.md`, adjusting the script path to `.cursor/ocr.py`.

**Option B: Global rule**

Place `ocr.py` in a stable location (e.g. `C:\tools\ocr.py`) and reference it in your global Cursor settings.

---

## GitHub Copilot (VS Code)

Copilot doesn't have a skill system, but you can:

1. Save `ocr.py` somewhere stable, e.g. `C:\tools\local-ocr\ocr.py`.
2. Add a `.github/copilot-instructions.md` file in your repo with the content of `SKILL.md`, paths adjusted.
3. Copilot Chat will then follow those instructions when you ask about images.

---

## Cline / Roo Code / other VS Code extensions

These extensions usually support custom tools via MCP or workspace files. The simplest approach:

1. Save `ocr.py` in the workspace (e.g. `.tools/ocr.py`).
2. Add instructions to the extension's config (e.g. `.clinerules` for Cline) telling it when to call `python .tools/ocr.py -i <path>`.

---

## Generic Agent / Custom Workflow

For any AI agent that can read markdown and run shell commands:

1. Place `SKILL.md` and `ocr.py` somewhere the agent can read.
2. Add to the agent's system prompt or instruction file:
   ```
   When the user asks to read/OCR an image, follow the instructions in
   <path>/SKILL.md and run <path>/ocr.py.
   ```
3. Make sure `python` is on PATH and LM Studio is running.

---

## Path Portability Tips

To make the skill work across machines without editing paths:

1. **Use environment variables**:
   ```bash
   python "%USERPROFILE%\.trae-cn\skills\local-ocr\ocr.py" -i image.png
   ```
   (Windows) or
   ```bash
   python "${HOME}/.local/share/skills/local-ocr/ocr.py" -i image.png
   ```
   (Linux/macOS)

2. **Set a `LOCAL_OCR_DIR` env var** in your shell profile:
   ```powershell
   # PowerShell profile
   $env:LOCAL_OCR_DIR = "C:\Users\UserX\.trae-cn\skills\local-ocr"
   ```
   Then in SKILL.md:
   ```bash
   python "%LOCAL_OCR_DIR%\ocr.py" -i image.png
   ```

3. **Use a wrapper script** on PATH:
   Create `C:\tools\ocr.bat`:
   ```bat
   @echo off
   python "C:\Users\UserX\.trae-cn\skills\local-ocr\ocr.py" %*
   ```
   Then any editor can call `ocr -i image.png`.

---

## Verifying Cross-Editor Setup

After configuring for a new editor, test with a known image:

```bash
# Replace <SKILL_DIR> with the path used by that editor
python "<SKILL_DIR>/ocr.py" --check
python "<SKILL_DIR>/ocr.py" -i "C:\Users\UserX\Downloads\数学\三角形\extracted_images\image_001.png"
```

Expected output should include "三角形的分类" (Chinese text from the test image).

---

## Summary Table

| Editor | Skill folder | Path style in SKILL.md |
|---|---|---|
| trae (CN) | `C:\Users\<you>\.trae-cn\skills\` | Absolute or `%USERPROFILE%` |
| Qoder | `.qoder\skills\` (project) or `C:\Users\<you>\.qoder\skills\` | Relative or absolute |
| OpenCode | `.opencode\skills\` | Relative |
| Cursor | `.cursor\` + `.cursorrules` | Absolute |
| Copilot | `.github\copilot-instructions.md` | Absolute |
| Cline | `.clinerules` | Absolute |

The OCR script itself never changes — only the path you tell the AI to use.
