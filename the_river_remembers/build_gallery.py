#!/usr/bin/env python3
"""Create one portable, self-contained storyboard gallery.

Run after every image batch:
    ../.venv/bin/python build_gallery.py
(or use any Python environment with Pillow installed.)
"""
from __future__ import annotations

import base64
import html
import io
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "storyboard_gallery.html"
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}


def label_for(path: Path) -> str:
    stem = path.stem
    if stem.endswith("_ref"):
        return stem[:-4].replace("_", " ") + " — CHARACTER REFERENCE"
    parts = stem.split("_")
    if len(parts) >= 2 and parts[0].startswith("S") and parts[1].startswith("Step"):
        return f"{parts[0]}_{parts[1]} — " + " ".join(parts[2:]).replace("_", " ")
    return stem.replace("_", " ")


def inline_thumbnail(path: Path) -> tuple[str, int, int]:
    with Image.open(path) as raw:
        image = ImageOps.exif_transpose(raw).convert("RGB")
        original_w, original_h = image.size
        image.thumbnail((420, 420), Image.Resampling.LANCZOS)
        buffer = io.BytesIO()
        image.save(buffer, format="JPEG", quality=70, optimize=True)
    return base64.b64encode(buffer.getvalue()).decode("ascii"), original_w, original_h


def cards(paths: list[Path], empty_text: str) -> str:
    if not paths:
        return f'<p class="empty">{html.escape(empty_text)}</p>'
    fragments = []
    for path in paths:
        try:
            data, original_w, original_h = inline_thumbnail(path)
        except Exception as exc:  # Continue building if one user-provided image is corrupt.
            fragments.append(f'<article class="card error"><h3>{html.escape(path.name)}</h3><p>Could not thumbnail image: {html.escape(str(exc))}</p></article>')
            continue
        label = label_for(path)
        fragments.append(
            '<article class="card">'
            f'<img loading="lazy" src="data:image/jpeg;base64,{data}" alt="{html.escape(label)}">'
            '<div class="meta">'
            f'<h3>{html.escape(label)}</h3>'
            f'<p>{html.escape(path.relative_to(ROOT).as_posix())} · original {original_w}×{original_h}</p>'
            '</div></article>'
        )
    return "\n".join(fragments)


def image_files(folder: Path) -> list[Path]:
    if not folder.exists():
        return []
    return sorted((path for path in folder.iterdir() if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS), key=lambda p: p.name)


def main() -> None:
    refs = image_files(ROOT / "images" / "refs")
    acts = {act: image_files(ROOT / "images" / f"act{act}") for act in (1, 2, 3)}
    total = len(refs) + sum(len(files) for files in acts.values())
    sections = [
        ("Character reference sheets", refs, "Reference sheets are awaiting generation."),
        ("Act I — Return", acts[1], "No Act I scene images generated yet."),
        ("Act II — The Signal", acts[2], "No Act II scene images generated yet."),
        ("Act III — Public Light", acts[3], "No Act III scene images generated yet."),
    ]
    body = []
    for heading, files, empty in sections:
        body.append(f'<section><div class="section-heading"><h2>{heading}</h2><span>{len(files)} image{"s" if len(files) != 1 else ""}</span></div><div class="grid">{cards(files, empty)}</div></section>')
    source = "\n".join(body)
    document = f"""<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\">
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
<title>The River Remembers — Storyboard Gallery</title>
<style>
:root {{ --ink:#172020; --muted:#617071; --paper:#f7f2e9; --navy:#102c3a; --teal:#19636b; --amber:#d88a28; --card:#fffdf9; }}
* {{ box-sizing:border-box; }} body {{ margin:0; color:var(--ink); background:var(--paper); font-family:ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; }}
header {{ padding:3.2rem max(1.3rem,calc((100vw - 1380px)/2)); color:#fff; background:linear-gradient(120deg,var(--navy),var(--teal)); }}
header p {{ max-width:55rem; margin:.6rem 0 0; color:#d9eef0; line-height:1.55; }} h1 {{ font-family:Georgia,serif; margin:0; letter-spacing:.03em; font-size:clamp(2rem,5vw,4.25rem); }} .badge {{ display:inline-block; margin-top:1.15rem; padding:.35rem .65rem; border:1px solid #b7dddf; border-radius:99px; font-size:.82rem; }}
main {{ max-width:1380px; margin:auto; padding:2rem 1.3rem 4rem; }} section {{ margin:2.6rem 0; }} .section-heading {{ display:flex; align-items:baseline; justify-content:space-between; gap:1rem; border-bottom:2px solid #d8d0c1; }} h2 {{ margin:0 0 .7rem; font-size:1.5rem; }} .section-heading span {{ color:var(--muted); font-size:.9rem; }} .grid {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(250px,1fr)); gap:1rem; padding-top:1rem; }}
.card {{ overflow:hidden; border:1px solid #ded6ca; border-radius:12px; background:var(--card); box-shadow:0 3px 12px rgba(21,40,40,.08); }} .card img {{ display:block; width:100%; aspect-ratio:1.4/1; object-fit:cover; background:#e6e1d7; }} .meta {{ padding:.75rem .8rem .9rem; }} h3 {{ margin:0; font-size:.9rem; line-height:1.35; }} .meta p,.empty,.error p {{ margin:.35rem 0 0; color:var(--muted); font-size:.76rem; line-height:1.45; }} .empty {{ grid-column:1/-1; margin:0; padding:1.1rem; border:1px dashed #b9b1a5; border-radius:9px; }} .error {{ padding:1rem; border-color:#bd7467; }} footer {{ max-width:1380px; margin:auto; padding:0 1.3rem 3rem; color:var(--muted); font-size:.8rem; }}
</style>
</head>
<body>
<header><h1>The River Remembers</h1><p>A self-contained visual production gallery. Every thumbnail is JPEG-compressed, base64-inlined and viewable offline; no external image, font, script or network request is used.</p><span class=\"badge\">{total} visual asset{'s' if total != 1 else ''} in this build</span></header>
<main>{source}</main>
<footer>Generated from <code>images/refs/</code> and <code>images/act1–3/</code>. Re-run <code>build_gallery.py</code> after adding a batch.</footer>
</body></html>"""
    OUT.write_text(document, encoding="utf-8")
    print(f"Wrote {OUT.name} with {len(refs)} reference(s) and {sum(len(files) for files in acts.values())} scene image(s).")

if __name__ == "__main__":
    main()
