#!/usr/bin/env python3
"""Create one portable, self-contained storyboard gallery with hierarchy:

Character References → Act header → individual Scene subsection → Step cards.

All 207 images are inlined as base64 JPEG thumbnails; gallery is fully offline.

Run after every image batch:
    python3 build_gallery.py
(or any env with Pillow installed.)
"""
from __future__ import annotations

import base64
import html
import io
import re
from collections import defaultdict, OrderedDict
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "storyboard_gallery.html"
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
SCREENPLAY = ROOT / "SCREENPLAY.md"

# Fallback metadata if SCREENPLAY.md parsing fails
FALLBACK_ACT_TITLES = {
    1: "Act I — Return",
    2: "Act II — The Signal",
    3: "Act III — Public Light",
}
FALLBACK_SCENE_TITLES = {
    "S01": "S01 — The Roof That Hums",
    "S02": "S02 — Road to Afenyo",
    "S03": "S03 — A Lantern Left Dark",
    "S04": "S04 — Price of the Water",
    "S05": "S05 — The Polite Hearing",
    "S06": "S06 — The Black Buoy",
    "S07": "S07 — The Ledger in the Lantern",
    "S08": "S08 — Open Frequency",
    "S09": "S09 — Map with a Missing Line",
    "S10": "S10 — Under the Roots",
    "S11": "S11 — King Tide",
    "S12": "S12 — Night of the Red Moon",
    "S13": "S13 — The Yard Stands Still",
    "S14": "S14 — Archive of the Unheard",
    "S15": "S15 — When the Power Fails",
    "S16": "S16 — A Thousand Small Lights",
    "S17": "S17 — Signal on the Water",
    "S18": "S18 — The Chair Answers",
    "S19": "S19 — The Water Is Public",
    "S20": "S20 — First Light, Shared",
}
FALLBACK_ACT_SCENES = {
    1: ["S01", "S02", "S03", "S04", "S05", "S06"],
    2: ["S07", "S08", "S09", "S10", "S11", "S12", "S13", "S14", "S15"],
    3: ["S16", "S17", "S18", "S19", "S20"],
}

ROMAN_TO_INT = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5}


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
        except Exception as exc:  # Continue building if one image is corrupt
            fragments.append(
                f'<article class="card error"><h3>{html.escape(path.name)}</h3>'
                f'<p>Could not thumbnail image: {html.escape(str(exc))}</p></article>'
            )
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
    return sorted(
        (p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS),
        key=lambda p: p.name,
    )


def parse_screenplay() -> tuple[dict[int, str], dict[str, str], dict[int, list[str]]]:
    """
    Returns (act_titles, scene_titles, act_scenes)
    act_titles: act_num -> "Act I — Return"
    scene_titles: "S01" -> "S01 — The Roof That Hums"
    act_scenes: act_num -> [S01, S02, ...] in order
    """
    if not SCREENPLAY.exists():
        return FALLBACK_ACT_TITLES, FALLBACK_SCENE_TITLES, FALLBACK_ACT_SCENES

    text = SCREENPLAY.read_text(encoding="utf-8")
    # Accept both em dash — and hyphen -
    act_pat = re.compile(r"^###\s+ACT\s+([IV]+)\s+[—\-]\s+(.+)$", re.IGNORECASE | re.MULTILINE)
    scene_pat = re.compile(r"^##\s+(S\d+)\s+[—\-]\s+(.+)$", re.MULTILINE)

    # Map roman -> int and preserve order by scanning lines
    act_titles: dict[int, str] = {}
    scene_titles: dict[str, str] = {}
    act_scenes: dict[int, list[str]] = defaultdict(list)

    # Build list of events sorted by position
    lines = text.splitlines()
    current_act_num: int | None = None

    # Pre-index act lines for quick lookup
    # Iterate sequentially
    for line in lines:
        act_m = act_pat.match(line.strip())
        if act_m:
            roman = act_m.group(1).upper()
            name_raw = act_m.group(2).strip()
            act_num = ROMAN_TO_INT.get(roman)
            if act_num is None:
                continue
            # Convert RETURN -> Return, THE SIGNAL -> The Signal
            # title() will handle but keep small words: we use title() then fix apostrophes etc.
            # Use str.title() but preserve original if not all caps? Simpler: title()
            name = name_raw.title() if name_raw.isupper() else name_raw
            # Ensure consistent "Act I — Return"
            act_titles[act_num] = f"Act {roman} — {name}"
            current_act_num = act_num
            if current_act_num not in act_scenes:
                act_scenes[current_act_num] = []
            continue

        scene_m = scene_pat.match(line.strip())
        if scene_m:
            sid = scene_m.group(1).upper()  # S01
            title_raw = scene_m.group(2).strip()
            # Full label S01 — Title
            scene_titles[sid] = f"{sid} — {title_raw}"
            if current_act_num is not None:
                if sid not in act_scenes[current_act_num]:
                    act_scenes[current_act_num].append(sid)
            continue

    # If parsing didn't yield expected counts, merge with fallback
    if not act_titles:
        act_titles = FALLBACK_ACT_TITLES.copy()
    else:
        # Ensure all 3 acts present
        for k, v in FALLBACK_ACT_TITLES.items():
            if k not in act_titles:
                act_titles[k] = v

    if not scene_titles or len(scene_titles) < 20:
        # Merge missing from fallback
        merged = FALLBACK_SCENE_TITLES.copy()
        merged.update(scene_titles)
        scene_titles = merged

    if not act_scenes or sum(len(v) for v in act_scenes.values()) < 20:
        act_scenes = FALLBACK_ACT_SCENES.copy()
    else:
        # Ensure sorting by S number within act if needed, but keep original order
        # For any act missing from parsed but in fallback, add fallback
        for k in FALLBACK_ACT_SCENES:
            if k not in act_scenes:
                act_scenes[k] = FALLBACK_ACT_SCENES[k]

    # Sort act_scenes keys and ensure scene order is numeric
    # Keep act order but also sort each list by numeric id to guarantee S01..S20 order
    for act_num in act_scenes:
        # Deduplicate preserving order then sort numerically? We sort numerically for determinism
        uniq = list(OrderedDict.fromkeys(act_scenes[act_num]))
        act_scenes[act_num] = sorted(uniq, key=lambda s: int(s[1:]))

    return act_titles, scene_titles, act_scenes


def group_by_scene(files: list[Path]) -> dict[str, list[Path]]:
    grouped: dict[str, list[Path]] = defaultdict(list)
    for p in files:
        # S01_Step01_...
        stem = p.stem
        if "_" in stem:
            sid = stem.split("_")[0]
            # Validate S## pattern
            if re.match(r"^S\d+$", sid):
                grouped[sid].append(p)
            else:
                grouped["_other"].append(p)
        else:
            grouped["_other"].append(p)
    # Sort each group by filename (which sorts by Step01..10)
    for k in grouped:
        grouped[k] = sorted(grouped[k], key=lambda x: x.name)
    return dict(sorted(grouped.items()))


def main() -> None:
    refs = image_files(ROOT / "images" / "refs")
    acts_files = {act: image_files(ROOT / "images" / f"act{act}") for act in (1, 2, 3)}
    total = len(refs) + sum(len(v) for v in acts_files.values())

    act_titles, scene_titles, act_scenes = parse_screenplay()

    # Build body HTML
    body_parts: list[str] = []

    # Character References — top level, no act grouping
    refs_heading = "Character References"
    refs_count = len(refs)
    refs_grid = cards(refs, "Reference sheets are awaiting generation.")
    body_parts.append(
        f'<section class="top-section refs-section">'
        f'<div class="section-heading"><h2>{html.escape(refs_heading)}</h2>'
        f'<span>{refs_count} image{"s" if refs_count != 1 else ""}</span></div>'
        f'<div class="grid">{refs_grid}</div></section>'
    )

    # Acts I-III with scene subsections
    for act_num in (1, 2, 3):
        files = acts_files.get(act_num, [])
        grouped = group_by_scene(files)
        act_title = act_titles.get(act_num, FALLBACK_ACT_TITLES.get(act_num, f"Act {act_num}"))
        act_count = len(files)

        # Determine scene order: use act_scenes mapping if available, else sorted grouped keys
        scene_order = act_scenes.get(act_num)
        if not scene_order:
            # fallback to grouped keys that look like S##
            scene_order = [k for k in grouped.keys() if k.startswith("S")]
            scene_order = sorted(scene_order, key=lambda s: int(s[1:]) if s[1:].isdigit() else 999)

        # Begin act section
        act_html = [
            f'<section class="act act-{act_num}">',
            f'<div class="section-heading act-heading">'
            f'<h2>{html.escape(act_title)}</h2>'
            f'<span>{act_count} image{"s" if act_count != 1 else ""}</span></div>',
        ]

        if not files:
            act_html.append(f'<p class="empty">No {html.escape(act_title)} scene images generated yet.</p>')
        else:
            for sid in scene_order:
                s_files = grouped.get(sid, [])
                # Full scene title like "S01 — The Roof That Hums"
                s_title = scene_titles.get(sid, sid)
                # If no files for this scene but we still want to show empty, handle
                if not s_files:
                    cards_html = f'<p class="empty">No images for {html.escape(s_title)} yet.</p>'
                    count = 0
                else:
                    cards_html = cards(s_files, f"No images for {s_title}")
                    count = len(s_files)

                # Anchor id for linking
                anchor = sid.lower()
                act_html.append(
                    f'<div class="scene" id="{html.escape(anchor)}">'
                    f'<div class="scene-heading"><h3>{html.escape(s_title)}</h3>'
                    f'<span>{count} step{"s" if count != 1 else ""}</span></div>'
                    f'<div class="grid">{cards_html}</div></div>'
                )

            # Handle any leftover grouped scenes not in scene_order (e.g., unexpected S ids)
            extra_sids = [k for k in grouped.keys() if k not in scene_order and k.startswith("S")]
            for sid in sorted(extra_sids, key=lambda s: int(s[1:]) if s[1:].isdigit() else 999):
                s_files = grouped[sid]
                s_title = scene_titles.get(sid, sid)
                cards_html = cards(s_files, "")
                count = len(s_files)
                anchor = sid.lower()
                act_html.append(
                    f'<div class="scene" id="{html.escape(anchor)}">'
                    f'<div class="scene-heading"><h3>{html.escape(s_title)}</h3>'
                    f'<span>{count} step{"s" if count != 1 else ""}</span></div>'
                    f'<div class="grid">{cards_html}</div></div>'
                )

        act_html.append("</section>")
        body_parts.append("\n".join(act_html))

    source = "\n".join(body_parts)

    document = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The River Remembers — Storyboard Gallery</title>
<style>
:root {{ --ink:#172020; --muted:#617071; --paper:#f7f2e9; --navy:#102c3a; --teal:#19636b; --amber:#d88a28; --card:#fffdf9; --line:#d8d0c1; --line-light:#e8e0d1; }}
* {{ box-sizing:border-box; }}
body {{ margin:0; color:var(--ink); background:var(--paper); font-family:ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; line-height:1.5; }}
header {{ padding:3.2rem max(1.3rem,calc((100vw - 1380px)/2)); color:#fff; background:linear-gradient(120deg,var(--navy),var(--teal)); }}
header p {{ max-width:56rem; margin:.7rem 0 0; color:#d9eef0; line-height:1.6; }}
h1 {{ font-family:Georgia,serif; margin:0; letter-spacing:.03em; font-size:clamp(2rem,5vw,4.25rem); }}
.badge {{ display:inline-block; margin-top:1.15rem; padding:.4rem .7rem; border:1px solid #b7dddf; border-radius:99px; font-size:.82rem; }}
.toc {{ margin-top:1.4rem; display:flex; flex-wrap:wrap; gap:.5rem; }}
.toc a {{ color:#cdeef0; text-decoration:none; border:1px solid rgba(255,255,255,.35); padding:.25rem .6rem; border-radius:99px; font-size:.8rem; }}
.toc a:hover {{ background:rgba(255,255,255,.12); }}
main {{ max-width:1380px; margin:auto; padding:2rem 1.3rem 4rem; }}
section {{ margin:2.8rem 0; }}
.top-section {{ margin-top:0; }}
.section-heading {{ display:flex; align-items:baseline; justify-content:space-between; gap:1rem; border-bottom:2px solid var(--line); padding-bottom:.35rem; }}
.act-heading {{ border-bottom:3px solid var(--navy); }}
.act-heading h2 {{ font-size:1.6rem; }}
.section-heading h2 {{ margin:0 0 .7rem; font-size:1.5rem; font-family:Georgia,serif; }}
.section-heading span {{ color:var(--muted); font-size:.9rem; white-space:nowrap; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(240px,1fr)); gap:1rem; padding-top:1rem; }}
.card {{ overflow:hidden; border:1px solid #ded6ca; border-radius:12px; background:var(--card); box-shadow:0 3px 12px rgba(21,40,40,.08); display:flex; flex-direction:column; }}
.card img {{ display:block; width:100%; aspect-ratio:16/9; object-fit:cover; background:#e6e1d7; }}
.meta {{ padding:.75rem .8rem .9rem; }}
.meta h3 {{ margin:0; font-size:.88rem; line-height:1.35; }}
.meta p,.empty,.error p {{ margin:.35rem 0 0; color:var(--muted); font-size:.76rem; line-height:1.45; }}
.empty {{ grid-column:1/-1; margin:0; padding:1.1rem; border:1px dashed #b9b1a5; border-radius:9px; background:rgba(255,255,255,.6); }}
.error {{ padding:1rem; border-color:#bd7467; }}
.act {{ padding-top:.8rem; border-top:4px solid var(--navy); margin-top:3.5rem; }}
.act:first-of-type {{ border-top:none; }}
.scene {{ margin:1.8rem 0 2.2rem; padding:1.1rem 1.1rem 1.2rem; background:rgba(255,253,249,.78); border:1px solid var(--line-light); border-radius:14px; box-shadow:0 2px 10px rgba(16,44,58,.06); }}
.scene-heading {{ display:flex; align-items:baseline; justify-content:space-between; gap:1rem; border-bottom:1px solid var(--line-light); padding-bottom:.5rem; margin-bottom:.2rem; }}
.scene-heading h3 {{ margin:0; font-size:1.18rem; font-family:Georgia,serif; letter-spacing:.01em; }}
.scene-heading span {{ color:var(--muted); font-size:.82rem; white-space:nowrap; }}
footer {{ max-width:1380px; margin:auto; padding:0 1.3rem 3rem; color:var(--muted); font-size:.8rem; }}
@media (max-width:600px) {{ .grid {{ grid-template-columns:1fr 1fr; gap:.7rem; }} .scene {{ padding:.8rem; }} .scene-heading h3 {{ font-size:1rem; }} }}
</style>
</head>
<body>
<header><h1>The River Remembers</h1><p>A self-contained visual production gallery. Every thumbnail is JPEG-compressed, base64-inlined and viewable offline; no external image, font, script or network request is used. Hierarchy: Character References → Act → Scene (S01–S20) → Step cards.</p><span class="badge">{total} visual asset{'s' if total != 1 else ''} in this build — 7 refs + 200 steps</span>
<nav class="toc">
<a href="#refs">Character References</a>
<a href="#act1">Act I — Return</a>
<a href="#act2">Act II — The Signal</a>
<a href="#act3">Act III — Public Light</a>
<a href="#s01">S01</a><a href="#s02">S02</a><a href="#s03">S03</a><a href="#s04">S04</a><a href="#s05">S05</a><a href="#s06">S06</a><a href="#s07">S07</a><a href="#s08">S08</a><a href="#s09">S09</a><a href="#s10">S10</a>
<a href="#s11">S11</a><a href="#s12">S12</a><a href="#s13">S13</a><a href="#s14">S14</a><a href="#s15">S15</a><a href="#s16">S16</a><a href="#s17">S17</a><a href="#s18">S18</a><a href="#s19">S19</a><a href="#s20">S20</a>
</nav>
</header>
<main>{source}</main>
<footer>Generated from <code>images/refs/</code> and <code>images/act1–3/</code>. Re-run <code>build_gallery.py</code> after adding a batch. All images are inlined as base64 JPEG thumbnails for offline viewing. Hierarchy: Character References → Act → Scene → Steps.</footer>
</body></html>"""
    # Insert anchors for top sections: we have act sections, but refs anchor
    # Patch the refs section to have id
    document = document.replace('class="top-section refs-section"', 'class="top-section refs-section" id="refs"')
    # Add act anchors
    document = document.replace('class="act act-1"', 'class="act act-1" id="act1"')
    document = document.replace('class="act act-2"', 'class="act act-2" id="act2"')
    document = document.replace('class="act act-3"', 'class="act act-3" id="act3"')

    OUT.write_text(document, encoding="utf-8")
    print(f"Wrote {OUT.name} with {len(refs)} reference(s) and {sum(len(v) for v in acts_files.values())} scene image(s) = {total} total.")
    # Verify counts
    grouped_counts = sum(len(image_files(ROOT / 'images' / f'act{a}')) for a in (1,2,3))
    print(f"Act breakdown: act1={len(acts_files[1])}, act2={len(acts_files[2])}, act3={len(acts_files[3])}, refs={len(refs)}, total={total} (expected 207).")
    # Quick sanity for scenes
    act_titles, scene_titles, act_scenes = parse_screenplay()
    for act_num in (1,2,3):
        print(f"{act_titles.get(act_num)}: {act_scenes.get(act_num)}")


if __name__ == "__main__":
    main()
