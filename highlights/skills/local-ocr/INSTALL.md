# Installation & Rollback Guide

This guide covers setting up the local-ocr skill from scratch, and how to fully uninstall it.

## Prerequisites

| Component | Requirement |
|---|---|
| OS | Windows 10/11, macOS, or Linux |
| Python | 3.7+ (no extra packages needed — script uses stdlib only) |
| GPU | Optional but recommended (NVIDIA ≥ 4GB VRAM, or Apple Silicon, or CPU) |
| Disk | ~1.8 GB for the model |
| LM Studio | Latest version from https://lmstudio.ai |

## Part 1 — Install LM Studio and Load PaddleOCR-VL

### Step 1: Install LM Studio

Download from https://lmstudio.ai and install. No special options needed.

### Step 2: Download PaddleOCR-VL-1.5 GGUF

Three files are required (total ~1.73 GB):

| File | Size | Purpose |
|---|---|---|
| `PaddleOCR-VL-1.5.gguf` | ~893 MB | Main text model |
| `mmproj-model-f16.gguf` | ~841 MB | Vision projector (**naming is critical**) |
| `chat_template.jinja` | ~1 KB | Chat template (required for image input) |

**Sources** (pick one):

- **Official HuggingFace** (use a mirror in China):
  ```
  https://hf-mirror.com/PaddlePaddle/PaddleOCR-VL-1.5-GGUF
  ```
- **Inside LM Studio**: search `PaddleOCR-VL-1.5` in the Discover tab (LM Studio auto-names `mmproj-*` correctly).

Place the three files in:
```
C:\models\PaddlePaddle\PaddleOCR-VL-1.5-GGUF\
```

> ⚠️ **CRITICAL**: The vision projector MUST be named `mmproj-*.gguf` (e.g. `mmproj-model-f16.gguf`). LM Studio uses this prefix to auto-link it with the main model. If named `PaddleOCR-VL-1.5-mmproj.gguf`, rename it. Without correct naming, you will get `"Model does not support images"` errors.

### Step 3: Load the Model in LM Studio

1. Open LM Studio
2. Go to the **folder icon** (My Models) in the left sidebar
3. Navigate to `PaddlePaddle/PaddleOCR-VL-1.5-GGUF`
4. Click **Load** next to `PaddleOCR-VL-1.5`
5. In the load dialog:
   - **GPU Offload**: set to **Max** (e.g. 99 layers) for NVIDIA/Apple Silicon
   - **Context Length**: **16384** (4096 truncates long pages mid-sentence around ~1200 output tokens; the model supports up to 131072). To make this the default for every (re)load, set `defaultContextLength.value` to 16384 in `~/.lmstudio/settings.json`
   - Check that LM Studio shows "Vision projector loaded" in the status

### Step 4: Start the Local Server

1. Click the **↗ icon** (Local Server / Developer) in the left sidebar
2. Click **Start Server**
3. Confirm the server is running on `http://127.0.0.1:1234`
4. Verify:
   ```bash
   curl http://127.0.0.1:1234/v1/models
   ```
   Should return JSON containing `"paddleocr-vl-1.5"`.

### Step 5: Test the Skill

```bash
python "C:\Users\UserX\.trae-cn\skills\local-ocr\ocr.py" --check
# Expected: [OK] LM Studio reachable, model 'paddleocr-vl-1.5' is loaded.

python "C:\Users\UserX\.trae-cn\skills\local-ocr\ocr.py" -i "C:\path\to\test.png"
# Expected: recognized text + timing
```

## Part 2 — Install the Skill Itself

The skill is just a folder with three files (`SKILL.md`, `ocr.py`, this `INSTALL.md`, plus `CROSS_EDITOR.md`). No installation script is needed.

### For trae (Windows)

Place the skill folder at either:
- **Global** (all projects): `C:\Users\<you>\.trae-cn\skills\local-ocr\`
- **Project-only**: `<project>\.trae\skills\local-ocr\`

Restart trae. The skill appears in the skill list automatically.

### For other editors

See `CROSS_EDITOR.md`.

## Part 3 — Rollback / Uninstall

### Option A: Remove only the skill (keep the model)

Delete the skill folder:
```powershell
Remove-Item -Recurse -Force "C:\Users\UserX\.trae-cn\skills\local-ocr"
```

Done. LM Studio and the model are untouched.

### Option B: Remove the model too (frees ~1.73 GB)

1. In LM Studio: unload the model, stop the server.
2. Delete the model files:
   ```powershell
   Remove-Item -Recurse -Force "C:\models\PaddlePaddle"
   ```
3. Optionally delete the skill folder (see Option A).

### Option C: Uninstall everything (including LM Studio)

1. Do Option B first.
2. Uninstall LM Studio via Windows Settings → Apps → LM Studio → Uninstall.
3. Delete leftover config:
   ```powershell
   Remove-Item -Recurse -Force "$env:USERPROFILE\.lmstudio"
   Remove-Item -Recurse -Force "$env:LOCALAPPDATA\LM-Studio"
   ```

## Troubleshooting

### "Model does not support images" (HTTP 400)

The `mmproj` file is missing or misnamed. Fix:
```powershell
# Check files
Get-ChildItem "C:\models\PaddlePaddle\PaddleOCR-VL-1.5-GGUF"
# The mmproj file MUST start with "mmproj-"
# If it's named "PaddleOCR-VL-1.5-mmproj.gguf", rename it:
Rename-Item "C:\models\PaddlePaddle\PaddleOCR-VL-1.5-GGUF\PaddleOCR-VL-1.5-mmproj.gguf" "mmproj-model-f16.gguf"
```
Then reload the model in LM Studio.

### "Connection refused"

LM Studio server not started. Open LM Studio → Developer tab → Start Server.

### "Model not found"

PaddleOCR-VL not loaded. In LM Studio → My Models → click Load next to PaddleOCR-VL-1.5.

### Very slow (>10s per image)

GPU offload not enabled. In LM Studio load dialog, set GPU Offload to Max. For RTX 4060 8GB, all 19 layers fit easily.

### Empty output

- Try `--prompt "OCR:"` explicitly (official task prompt, colon included).
- Verify the image file is valid and not corrupted.
- Try a different image format (PNG is most reliable).

### Repeated text / infinite repetition

- The GGUF model occasionally loops on figure-heavy pages. `ocr.py` (as of
  2026-09-30) screens output and auto-retries; make sure you are running the
  updated script. If `[WARN]` still shows, crop the image or use
  `--prompt "Formula Recognition:"` for formula-only regions.
- Keep the llama.cpp runtime current: `lms runtime update`.

## Verification Checklist

After install, run all of these:

```powershell
# 1. Server reachable
python "C:\Users\UserX\.trae-cn\skills\local-ocr\ocr.py" --check

# 2. Single image OCR
python "C:\Users\UserX\.trae-cn\skills\local-ocr\ocr.py" -i "C:\path\to\test.png"

# 3. JSON output (for programmatic use)
python "C:\Users\UserX\.trae-cn\skills\local-ocr\ocr.py" -i "C:\path\to\test.png" --json
```

All three should succeed. If step 1 fails, fix LM Studio first. If step 1 passes but step 2 fails, check the image file.
