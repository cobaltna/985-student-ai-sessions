#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Local OCR via LM Studio PaddleOCR-VL-1.5
=========================================
Cross-editor skill script. Works in trae, qoder, opencode, Cursor, or any
agent that can execute shell commands.

Self-contained: uses ONLY Python standard library (no pip install needed).
Supports Python 3.7+.

Usage:
    python ocr.py --image "C:\\path\\to\\image.png"
    python ocr.py -i image.png -p "Extract all formulas"
    python ocr.py -i image.png -o result.txt
    python ocr.py -i image.png --json   # machine-readable output

Configuration via environment variables:
    LMSTUDIO_OCR_API         default http://127.0.0.1:1234/v1/chat/completions
    LMSTUDIO_OCR_MODEL       default paddleocr-vl-1.5
    LMSTUDIO_OCR_PROMPT      default "OCR:"   (official task prompt, keep the colon)
    LMSTUDIO_OCR_TEMPERATURE default 0.45     (sampling temp; guard retries may vary it)
    LMSTUDIO_OCR_RETRIES     default 2        (extra attempts if output looks degenerate)
    LMSTUDIO_OCR_PASSES      default 1        (runs per image; the LONGEST result wins)
    LMSTUDIO_OCR_FIX_LATEX   default 0        (1 = repair LaTeX syntax in the output)
    LMSTUDIO_OCR_TIMEOUT     default 180 (seconds)

Anti-repetition guard:
    The PaddleOCR-VL GGUF occasionally degenerates on figure-heavy pages
    (character loops like "S5S5S5..." or whole paragraphs repeated). Each
    output is screened: exact repeated blocks, near-duplicate long lines,
    and token-cap hits. If degenerate, the request is retried with a
    different temperature/seed (up to LMSTUDIO_OCR_RETRIES times) and the
    cleanest attempt is returned. A "[WARN]" line on stderr tells you when
    even the best attempt still looked suspect.

Completeness (multi-pass):
    On formula-dense pages the model sometimes stops early (silent omission
    of a column/section — nothing repeats, so the repetition guard cannot
    see it). Passes > 1 run the OCR several times and return the LONGEST
    result, which reliably recovers the missed content. Use --passes 3 for
    critical full-page captures; keep 1 for quick single shots.

LaTeX post-processing (--fix-latex):
    PaddleOCR-VL emits LaTeX for math; ~1% of the emitted math fragments have
    mechanical syntax defects (validated against KaTeX on a 2400+ fragment
    corpus). --fix-latex repairs them in place: repeated/missing-brace
    sub-superscripts (\\int_0^T_* -> \\int_0^{T_*}), unclosed \\( \\[ spans,
    unclosed \\begin/\\left/braces, stray "\\g_" style backslashes, doubled
    scripts, and \\tag inside inline math (promoted to display). Text outside
    math spans is never touched. A "[FIX]" line on stderr reports the count.
"""
from __future__ import annotations

import argparse
import base64
import difflib
import json
import os
import random
import re
import sys
import time
import urllib.error
import urllib.request
from typing import Optional

# --------------------------------------------------------------------------- #
# Configuration
# --------------------------------------------------------------------------- #
API_URL = os.environ.get(
    "LMSTUDIO_OCR_API", "http://127.0.0.1:1234/v1/chat/completions"
)
MODEL_ID = os.environ.get("LMSTUDIO_OCR_MODEL", "paddleocr-vl-1.5")
# PaddleOCR-VL is trained with task prompts like "OCR:" / "Table Recognition:".
# The colon matters; plain "OCR" is out-of-distribution for the model.
DEFAULT_PROMPT = os.environ.get("LMSTUDIO_OCR_PROMPT", "OCR:")
DEFAULT_TEMPERATURE = float(os.environ.get("LMSTUDIO_OCR_TEMPERATURE", "0.45"))
DEFAULT_RETRIES = int(os.environ.get("LMSTUDIO_OCR_RETRIES", "2"))
DEFAULT_PASSES = int(os.environ.get("LMSTUDIO_OCR_PASSES", "1"))
DEFAULT_FIX_LATEX = os.environ.get(
    "LMSTUDIO_OCR_FIX_LATEX", "0"
).strip().lower() in ("1", "true", "yes", "on")
DEFAULT_TIMEOUT = int(os.environ.get("LMSTUDIO_OCR_TIMEOUT", "180"))
# Temperatures used for retry attempts after the first one fails screening.
RETRY_TEMPERATURES = [0.65, 0.3, 0.8]

# Supported image extensions -> MIME subtype
EXT_TO_MIME = {
    ".png":  "png",
    ".jpg":  "jpeg",
    ".jpeg": "jpeg",
    ".webp": "webp",
    ".bmp":  "bmp",
    ".gif":  "gif",
}


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def encode_image(image_path: str) -> str:
    """Read image file and return a base64 data URL."""
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    ext = os.path.splitext(image_path)[1].lower()
    mime = EXT_TO_MIME.get(ext, "octet-stream")

    with open(image_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("ascii")
    return f"data:image/{mime};base64,{b64}"


# --------------------------------------------------------------------------- #
# Degeneracy screening (infinite / repeated output detector)
# --------------------------------------------------------------------------- #
def _norm_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def exact_repeat_run(text: str) -> tuple:
    """Max (run_length, block) of one block repeated consecutively.

    Checks block lengths 1..1500 chars on whitespace-normalized text so both
    char-level loops ("S5S5S5...") and paragraph-level loops are caught.
    """
    norm = _norm_ws(text)
    n = len(norm)
    best_run, best_block = 1, ""
    for L in (1, 2, 3, 4, 5, 6, 8, 10, 15, 20, 30, 50, 80, 120, 200,
              300, 450, 600, 800, 1000, 1200, 1500):
        if 2 * L > n:
            break
        i = 0
        while i + L <= n:
            block = norm[i:i + L]
            if not block.strip():
                i += 1
                continue
            run = 1
            j = i + L
            while j + L <= n and norm[j:j + L] == block:
                run += 1
                j += L
            if run > best_run or (run == best_run and L > len(best_block)):
                best_run, best_block = run, block
            i += 1 if run > 1 else max(1, L // 4)
    return best_run, best_block


def near_dup_line_count(text: str) -> int:
    """Count long lines (>=60 chars) that near-duplicate another long line."""
    lines = [l.strip()[:160] for l in text.splitlines() if len(l.strip()) >= 60]
    if len(lines) < 2:
        return 0
    dups = 0
    for i, l in enumerate(lines):
        for j, l2 in enumerate(lines):
            if j == i:
                continue
            if difflib.SequenceMatcher(None, l, l2).ratio() >= 0.93:
                dups += 1
                break
    return dups


def degeneracy_score(text: str, completion_tokens: int, max_tokens: int) -> tuple:
    """Return (score, reasons). score 0 = clean; higher = worse."""
    score = 0
    reasons = []
    run, block = exact_repeat_run(text)
    if run >= 5:
        score += run
        reasons.append(f"exact-repeat x{run} of {block[:40]!r}")
    dups = near_dup_line_count(text)
    if dups >= 3:
        score += dups
        reasons.append(f"near-duplicate long lines x{dups}")
    if completion_tokens >= 0.98 * max_tokens:
        score += 100
        reasons.append("hit max_tokens cap (possible runaway)")
    return score, reasons


# --------------------------------------------------------------------------- #
# LaTeX post-processing (--fix-latex)
# Syntax-level repair for OCR-produced LaTeX. Validated with KaTeX on a
# 2400+ fragment corpus: mechanical defects 24 -> 1 (remaining is a block
# where prose was merged into display math; not safely repairable).
# --------------------------------------------------------------------------- #
# one math token: a command, a braced group (one nesting level), or a plain char
_TK = r"(?:\\[a-zA-Z]+|\{(?:[^{}]|\{[^{}]*\})*\}|[^\s{}_^\\])"
# \int_0^T_* -> \int_0^{T_*}   (sub, sup, sub: fold third into the superscript)
_LX_P2 = re.compile(rf"([_^])({_TK})([_^])({_TK})\1({_TK})")
# \partial_y_j -> \partial_{y_j}   (same script repeated)
_LX_P1 = re.compile(rf"([_^])({_TK})\1({_TK})")
# stray backslash on a single letter that is NOT a real TeX letter command,
# used as a math base with a script: \g_{1} -> g_{1}
_LX_BAD_LETTER = re.compile(r"\\(?![ijloOLSPHcdbtkruv])([a-zA-Z])(?=[_^{])")
# doubled script characters (always invalid in math): __\rho -> _\rho
_LX_DOUBLE_SCRIPT = re.compile(r"([_^])\1+")
_LX_TEXT_SPAN = re.compile(r"\\text\{[^{}]*\}")
_LX_MATH_SPAN = re.compile(r"\\\[(.*?)\\\]|\\\((.*?)\\\)", re.S)


def _lx_fold_scripts(s: str) -> tuple:
    """Apply stray-backslash strip + P1/P2 folds; \\text{...} is masked."""
    masked = []

    def _mask(m):
        masked.append(m.group(0))
        return f"\x00{len(masked)-1}\x00"

    s0 = s
    s2 = _LX_TEXT_SPAN.sub(_mask, s)
    s2 = _LX_BAD_LETTER.sub(lambda m: m.group(1), s2)
    s2 = _LX_DOUBLE_SCRIPT.sub(lambda m: m.group(1), s2)
    for _ in range(6):
        new = _LX_P2.sub(
            lambda m: f"{m.group(1)}{m.group(2)}{m.group(3)}"
                      f"{{{m.group(4)}{m.group(1)}{m.group(5)}}}", s2)
        new = _LX_P1.sub(
            lambda m: f"{m.group(1)}{{{m.group(2)}{m.group(1)}{m.group(3)}}}",
            new)
        if new == s2:
            break
        s2 = new
    for i, orig in enumerate(masked):
        s2 = s2.replace(f"\x00{i}\x00", orig)
    return s2, (s2 != s0)


def _lx_balance_delimiters(text: str) -> tuple:
    """Type-aware balancing of \\( \\[ spans; orphan closers dropped."""
    out = []
    stack = []  # entries: ")" or "]" — which closer each open still owes
    n = 0
    i = 0
    while i < len(text):
        two = text[i:i + 2]
        if two in (r"\(", r"\["):
            kind = ")" if two == r"\(" else "]"
            if stack and stack[-1] == kind:  # duplicate opener: close previous
                out.append(r"\)" if kind == ")" else r"\]")
                stack.pop()
                n += 1
            stack.append(kind)  # different kind = legal nesting, just push
            out.append(two)
            i += 2
            continue
        if two in (r"\)", r"\]"):
            kind = ")" if two == r"\)" else "]"
            if stack and stack[-1] != kind:  # out-of-order close: inner first
                out.append(r"\)" if stack[-1] == ")" else r"\]")
                stack.pop()
                n += 1
            if stack and stack[-1] == kind:
                out.append(two)
                stack.pop()
            else:  # orphan closer: drop
                n += 1
            i += 2
            continue
        out.append(text[i])
        i += 1
    while stack:
        out.append(r"\)" if stack.pop() == ")" else r"\]")
        n += 1
    return "".join(out), n


def _lx_fix_braces(tex: str) -> tuple:
    """Drop unmatched '}'; close unclosed '{' at span end."""
    n = 0
    out = []
    depth = 0
    for ch in tex:
        if ch == "{":
            depth += 1
            out.append(ch)
        elif ch == "}":
            if depth == 0:
                n += 1          # unmatched closer: drop
                continue
            depth -= 1
            out.append(ch)
        else:
            out.append(ch)
    s = "".join(out)
    if depth:                    # unclosed '{' arguments: close at end
        s += "}" * depth
        n += depth
    return s, n


def _lx_fix_span(tex: str) -> tuple:
    """Env/\\left balancing + brace repair inside one math span."""
    fixes = []
    # nested \( \) inside an outer span is illegal (already in math mode):
    # drop the redundant delimiters, keep the content
    if re.search(r"\\\(|\\\)", tex):
        tex = tex.replace(r"\(", "").replace(r"\)", "")
        fixes.append("nest")
    stack = []
    for m in re.finditer(r"\\(begin|end)\{(\w+\*?)\}", tex):
        if m.group(1) == "begin":
            stack.append(m.group(2))
        elif stack and stack[-1] == m.group(2):
            stack.pop()
    if stack:
        tex = tex + "".join(rf"\end{{{e}}}" for e in reversed(stack))
        fixes.append("env")
    n_left = len(re.findall(r"\\left\b", tex))
    n_right = len(re.findall(r"\\right\b", tex))
    if n_left > n_right:
        tex = tex + r"\right." * (n_left - n_right)
        fixes.append("left")
    tex, n_brace = _lx_fix_braces(tex)
    if n_brace:
        fixes.append("braces")
    return tex, fixes


def fix_latex(text: str) -> tuple:
    """Repair mechanical LaTeX defects. Returns (new_text, n_fixes, details)."""
    total = 0
    details = []
    text, n = _lx_balance_delimiters(text)
    total += n
    if n:
        details.append(f"delimiters:{n}")

    n_span, n_script, n_tag = 0, 0, 0

    def _repair(m):
        nonlocal n_span, n_script, n_tag
        display = m.group(1) is not None
        inner = m.group(1) if display else m.group(2)
        inner, fixes = _lx_fix_span(inner)
        inner, script_changed = _lx_fold_scripts(inner)
        if fixes:
            n_span += 1
        if script_changed:
            n_script += 1
        # \tag is display-only: promote an inline span that carries one
        if not display and r"\tag" in inner:
            display = True
            n_tag += 1
        delim = (r"\[", r"\]") if display else (r"\(", r"\)")
        return delim[0] + inner + delim[1]

    text = _LX_MATH_SPAN.sub(_repair, text)
    if n_span:
        details.append(f"env/left/braces:{n_span}")
    if n_script:
        details.append(f"scripts:{n_script}")
    if n_tag:
        details.append(f"tag-promoted:{n_tag}")
    total += n_span + n_script + n_tag
    return text, total, details


# --------------------------------------------------------------------------- #
# Core OCR call
# --------------------------------------------------------------------------- #
def _post_ocr(payload: dict, timeout: int) -> tuple:
    """Single HTTP call. Returns (text, elapsed, usage)."""
    req = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    start = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = json.loads(resp.read().decode("utf-8"))
        elapsed = time.time() - start
        text = body["choices"][0]["message"]["content"]
        usage = body.get("usage", {})
        return text, elapsed, usage
    except urllib.error.HTTPError as e:
        elapsed = time.time() - start
        err = e.read().decode("utf-8", errors="replace") if e.fp else str(e)
        raise RuntimeError(
            f"HTTP {e.code} after {elapsed:.1f}s\nResponse: {err[:500]}"
        )
    except urllib.error.URLError as e:
        elapsed = time.time() - start
        raise RuntimeError(
            f"Cannot connect to LM Studio at {API_URL} "
            f"(after {elapsed:.1f}s).\n"
            f"Make sure LM Studio is running with PaddleOCR-VL loaded and "
            f"Local Server started.\nError: {e.reason}"
        )


def ocr_image(
    image_path: str,
    prompt: str = DEFAULT_PROMPT,
    timeout: int = DEFAULT_TIMEOUT,
    max_tokens: int = 4000,
    passes: int = 1,
) -> tuple:
    """
    Call PaddleOCR-VL via LM Studio OpenAI-compatible API, with automatic
    retry when the output screens as degenerate (repetition loops etc.),
    and optional multi-pass runs (longest result wins) against silent
    early-stop omissions on formula-dense pages.

    Returns:
        (text, elapsed_seconds, usage_dict, meta_dict)
        meta_dict: {"attempts": int, "degenerate": bool, "reasons": [str]}
    """
    data_url = encode_image(image_path)
    base_messages = [
        {
            "role": "user",
            "content": [
                {"type": "image_url", "image_url": {"url": data_url}},
                {"type": "text", "text": prompt},
            ],
        }
    ]

    attempts = 1 + max(0, DEFAULT_RETRIES)
    total_start = time.time()
    total_requests = 0
    results = []  # (score, len(text), text, usage, reasons)

    for _pass in range(max(1, passes)):
        for attempt in range(1, attempts + 1):
            temperature = (
                DEFAULT_TEMPERATURE
                if attempt == 1
                else RETRY_TEMPERATURES[(attempt - 2) % len(RETRY_TEMPERATURES)]
            )
            payload = {
                "model": MODEL_ID,
                "messages": base_messages,
                "temperature": temperature,
                "seed": random.randint(1, 2**31 - 1),
                "max_tokens": max_tokens,
            }
            text, _elapsed, usage = _post_ocr(payload, timeout)
            total_requests += 1
            score, reasons = degeneracy_score(
                text, usage.get("completion_tokens", 0), max_tokens
            )
            results.append((score, len(text.strip()), text, usage, reasons))
            if score == 0:
                break  # this pass is clean; move on to the next pass
        # a clean result that filled the token budget cannot get longer
        if any(
            r[0] == 0 and r[3].get("completion_tokens", 0) >= 0.98 * max_tokens
            for r in results
        ):
            break

    clean = [r for r in results if r[0] == 0]
    if clean:
        # most complete capture: longest clean text wins
        pool = sorted(clean, key=lambda r: -r[1])
    else:
        # nothing clean: least degenerate, then longest
        pool = sorted(results, key=lambda r: (r[0], -r[1]))
    score, _tlen, text, usage, reasons = pool[0]
    meta = {
        "attempts": total_requests,
        "degenerate": score > 0,
        "reasons": reasons,
        "total_elapsed": time.time() - total_start,
    }
    return text, meta["total_elapsed"], usage, meta


def check_server() -> bool:
    """Quick health check: returns True if server responds with model list."""
    models_url = API_URL.rsplit("/", 2)[0] + "/models"
    try:
        req = urllib.request.Request(models_url, method="GET")
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        model_ids = [m.get("id", "") for m in data.get("data", [])]
        return MODEL_ID in model_ids
    except Exception:
        return False


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def main() -> int:
    parser = argparse.ArgumentParser(
        description="OCR via local LM Studio PaddleOCR-VL-1.5",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            '  python ocr.py -i image.png\n'
            '  python ocr.py -i image.png -p "Formula Recognition:"\n'
            "  python ocr.py -i image.png -o result.txt\n"
            "  python ocr.py -i image.png --json\n"
        ),
    )
    parser.add_argument(
        "--image", "-i",
        help="Path to the image file (.png/.jpg/.jpeg/.webp/.bmp/.gif). "
             "Required unless --check is used."
    )
    parser.add_argument(
        "--prompt", "-p", default=DEFAULT_PROMPT,
        help=f'OCR prompt (default: {DEFAULT_PROMPT!r}; official task prompts '
             f'are "OCR:", "Table Recognition:", "Formula Recognition:", '
             f'"Chart Recognition:")'
    )
    parser.add_argument(
        "--output", "-o",
        help="Output file path (default: stdout)"
    )
    parser.add_argument(
        "--timeout", "-t", type=int, default=DEFAULT_TIMEOUT,
        help=f"Request timeout in seconds (default: {DEFAULT_TIMEOUT})"
    )
    parser.add_argument(
        "--max-tokens", type=int, default=4000,
        help="Max tokens the model may generate (default: 4000)"
    )
    parser.add_argument(
        "--passes", type=int, default=DEFAULT_PASSES,
        help="OCR runs per image; the longest result is returned. Use 2-3 "
             "for formula-dense full pages where the model may stop early "
             f"(default: {DEFAULT_PASSES})"
    )
    parser.add_argument(
        "--fix-latex", action="store_true", default=DEFAULT_FIX_LATEX,
        help="Repair mechanical LaTeX syntax defects in the output (missing "
             "braces on sub/superscripts, unclosed delimiters/environments, "
             "stray backslashes). Text outside math is never touched. "
             "Recommended when the output feeds a LaTeX renderer. "
             "(default: off; env LMSTUDIO_OCR_FIX_LATEX=1 to enable)"
    )
    parser.add_argument(
        "--json", action="store_true",
        help="Output JSON with text/elapsed/usage/attempts (machine-readable)"
    )
    parser.add_argument(
        "--check", action="store_true",
        help="Only check if LM Studio server is reachable and model is loaded"
    )
    args = parser.parse_args()

    # ---- Health check mode ----
    if args.check:
        ok = check_server()
        if ok:
            print(f"[OK] LM Studio reachable, model '{MODEL_ID}' is loaded.")
            return 0
        else:
            print(
                f"[FAIL] Cannot reach {API_URL} or model '{MODEL_ID}' not loaded.",
                file=sys.stderr,
            )
            print(
                "Start LM Studio, load PaddleOCR-VL-1.5, then start Local Server.",
                file=sys.stderr,
            )
            return 2

    # ---- OCR mode (requires --image) ----
    if not args.image:
        parser.error("--image is required (unless --check is used)")

    try:
        text, elapsed, usage, meta = ocr_image(
            args.image, args.prompt, args.timeout, args.max_tokens, args.passes
        )
    except FileNotFoundError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1
    except RuntimeError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    warn = ""
    if meta["degenerate"]:
        warn = (
            f"\n[WARN] Output still shows repetition after {meta['attempts']} "
            f"attempts ({'; '.join(meta['reasons'])}). Result may be unreliable; "
            f"consider cropping the image or using the region-specific prompt."
        )

    latex_meta = None
    if args.fix_latex:
        text, n_lx, lx_details = fix_latex(text)
        latex_meta = {"count": n_lx, "details": lx_details}

    if args.json:
        result = {
            "image": os.path.abspath(args.image),
            "prompt": args.prompt,
            "text": text,
            "elapsed_seconds": round(elapsed, 2),
            "usage": usage,
            "attempts": meta["attempts"],
            "degenerate": meta["degenerate"],
            "reasons": meta["reasons"],
        }
        if latex_meta is not None:
            result["latex_fixes"] = latex_meta
        out = json.dumps(result, ensure_ascii=False, indent=2)
    else:
        out = text

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(out)
        print(
            f"[OK] OCR done in {elapsed:.1f}s "
            f"({meta['attempts']} request(s)), saved to {args.output}",
            file=sys.stderr,
        )
        if latex_meta and latex_meta["count"]:
            print(
                f"[FIX] latex: {latex_meta['count']} repair(s) "
                f"({', '.join(latex_meta['details'])})",
                file=sys.stderr,
            )
        if warn:
            print(warn.strip(), file=sys.stderr)
    else:
        # Plain text mode: print a short timing line to stderr BEFORE the
        # actual content on stdout, so stdout stays clean for piping.
        print(
            f"[OCR] {elapsed:.1f}s, {usage.get('total_tokens', '?')} tokens, "
            f"{meta['attempts']} request(s)",
            file=sys.stderr,
        )
        if latex_meta and latex_meta["count"]:
            print(
                f"[FIX] latex: {latex_meta['count']} repair(s) "
                f"({', '.join(latex_meta['details'])})",
                file=sys.stderr,
            )
        if warn:
            print(warn.strip(), file=sys.stderr)
        print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
