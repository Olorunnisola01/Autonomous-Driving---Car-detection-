#!/usr/bin/env python3
"""Create one portable, self-contained storyboard gallery with hierarchy:

Character References → Act header → Scene subsection with voiceover → Step cards.

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

# Voiceover / narration scripts — one per scene, sum tells full story
VOICE_SCRIPTS = {
    "S01": (
        "In Accra, I learned to love things that hum when you fix them. Panels, wires, "
        "a city that never asks who you are, only if the light comes on. I left Afenyo on purpose — "
        "traded its tides for a roof where competence could be a kind of distance. Then Ama's voice note "
        "cut through the heat, four seconds of lagoon wind behind it: 'They are measuring the lagoon again. "
        "Come before they turn our water into a gate.' I told the empty roof I was done coming home for emergencies. "
        "Then I packed my tools anyway. Home is a circuit you never really disconnect."
    ),
    "S02": (
        "The tro-tro left me at red dust and cassava smoke, and Sena was already there — mustard hoodie, headphones too big, "
        "speaking into a dead microphone like it was alive. My cousin by love and argument, sixteen and allergic to edited truths. "
        "\"Grandma said not to tell you she was scared, so I'm telling you,\" she said on air. That is Afenyo watching me: same palms, "
        "same blue water, but thinner somehow, as if the town itself was holding its breath, waiting to see if I would stay long enough to listen."
    ),
    "S03": (
        "Ama had made pepper soup, my favourite, but the courtyard lantern hung dark — blue glass, copper frame, empty. "
        "I hugged her and felt the tremor she tried to hide in her elbow. Sena strung cracked glass in the mango tree like prayers. "
        "'A dark lantern is not only darkness,' Ama said. 'It tells boats they are not expected.' For years I thought she spoke in proverbs to sound wise. "
        "That night I understood: she spoke in warnings, because no one else was keeping watch anymore. The light that had guided us home had been taught to go out."
    ),
    "S04": (
        "Morning market smells of smoke, brine and hot oil. Esi Tetteh — soot-black apron, crescent scar, voice that does not ask permission — slapped a wet survey notice onto silver fish. "
        "Public landing to become 'private access improvement.' Kojo, my childhood pilot, said the water smelled metallic since the drills started. "
        "I traced the diagram with a fish knife: a power line that powered nothing, running straight to our navigation buoy. 'Whose feet are improved by a locked gate?' Esi asked. "
        "In that moment the resort stopped being a building. It became a subtraction. A theft learning to wear a hard hat."
    ),
    "S05": (
        "They call it a hearing, but the chairs are arranged for applause. District Chair Nii Lamptey — charcoal caftan, heron-headed cane, voice like polished wood — speaks of jobs and clean power like blessings. "
        "Beside him, Kwame, my university friend, crisp and uncomfortable to see me, offers safeguards on slides with no map on the wall. 'If the plan is safe, why is the map not on the wall?' I ask. "
        "'Engineer Mensah,' Nii smiles, 'trust is also infrastructure.' Sena hits record without being told. In Afenyo, the only permission you get to speak is the one you take."
    ),
    "S06": (
        "Dusk turns the lagoon to beaten metal. Kojo poles without a motor, silent as prayer. The buoy that should flash green for fishermen is blind. Under it, the solar housing gutted, bypassed by a fresh cable, warm to touch, buried in silt. "
        "A thin oil slick breaks the surface, rainbows, vanishes. Far away, the resort generators burn like a second sunset that never sets. "
        "'The channel has always carried us out,' Kojo whispers. 'Then someone has taught it to carry their dirt in,' I say. I photograph the severed joint, hands shaking — not from fear, but from knowing. This was deliberate. I will not leave tomorrow."
    ),
    "S07": (
        "Night in Ama's workshop smells of solder and dried hibiscus. I try to fix the courtyard lantern and a loose blue pane falls out. Behind it, folded tight, a water-stained ledger page in Ama's hand: 1961 landing rights, public commons in perpetuity, and a line of numbers beside a wave pattern. "
        "I thought it a frequency. Sena sees a code, a rhythm. 'The old people hid papers where officials never looked,' Ama says softly. 'Inside what kept us safe.' Three generations of women, one small square of blue glass, and proof that this shore was never for sale — it was waiting to be remembered."
    ),
    "S08": (
        "Sena's radio shack is plywood, stickers, and hope. The transmitter only works when the sun tells the truth. We hook my spare battery and for the first time Afenyo hears itself breathe. "
        "Esi speaks first — not as leader, but as a woman whose trays are being measured without her. Then a boat boy calls. Then a market auntie. I beg Sena to wait, to protect names until we have proof. She puts the mic between us: 'The proof is that people are afraid to say it.' "
        "That morning I learn a signal is not just physics. It is permission. And once given, it does not go back into the box."
    ),
    "S09": (
        "Chain-link at noon burns. Kwame meets me there, field jacket on, compass-rose lapel pin missing for the first time — a small absence that tells me more than his words. He brings an approved plan with a black bar where the discharge pipe should be. "
        "'I took this job to get a seat at the table,' he says. The table, I think, is sitting on our water. The contractor would not show him, so he could not show me. Compromise has a way of sounding like diplomacy until someone turns on the light. "
        "Before he leaves, he lets my camera see a survey number. Shame, I realize, is also a kind of evidence."
    ),
    "S10": (
        "Kojo knows the mangroves like a man knows his own scars — where water thins, where roots make a doorway. We slip under the canopy, Sena filming with held breath. I lower a sensor on wire; numbers spike, bitter and fast. "
        "By a hidden grey pipe, warm water pulses out like a wound bleeding out of season. A machine coughs and dies in the distance — they heard us. 'If they see us?' Sena mouths. Kojo, steady: 'Then you keep your camera still.' "
        "I seal the sample, glass warm as blood. Proof is heavier when it is wet, because you cannot pretend you did not touch it."
    ),
    "S11": (
        "That night the tide remembered. Ama says water remembers every blocked path, every promise. It came into our courtyard, lifted stools, oil, extension cables. I held live leads above my head while Kojo waded in, canoe on his shoulders. "
        "Ama refused to leave until Sena carried the crate of lanterns — not food, not clothes, but light. We floated our tools out like a strange ark. And in the storm, a single blue lantern woke without battery, without touch, flickering against the flood. "
        "My grandmother says there are no miracles, only things that have been waiting to be seen at the right water level."
    ),
    "S12": (
        "Before dawn, red moon, Ama takes us to the old beacon hut no one under sixty remembers, swallowed by vines and salt. Inside, dust and stories. She tells how colonial surveyors came to claim the landing and the elders, who could not read their papers, taught the surveyors to read theirs — "
        "encoding the archive number of the true deed in a lantern flash: long-short-long-long, a rhythm, a frequency. The number matches the hidden page. 'Memory is not a box,' Ama says. 'It is a signal someone must still answer.' "
        "Sena turns it into her new sign-off, and I hear in it the whole town learning to speak again."
    ),
    "S13": (
        "Esi does not call a protest. She calls a pause. One day, no smoke. Fish trays stacked like a quiet wall across the resort road, children watching from stoops, no ambulance blocked, no elder turned away. "
        "Chairman Nii arrives, suit dry, cane sharp, calling it unlawful spectacle. I offer water data on paper. He will not touch paper he did not approve. Esi stands before buckets of ash and fresh catch: "
        "'We are not stopping work. We are stopping theft from wearing a hard hat.' Sena broadcasts the silence that follows. And for the first time, the resort gate listens, because everyone else is listening too."
    ),
    "S14": (
        "Archives at night smell like damp that learned to keep secrets. Kwame swipes us in, hand shaking on the keycard. We find the hemp-bound 1961 register — 'public commons in perpetuity' — and beside it, a fresh amendment with a digital stamp from an office that was closed for elections that day. "
        "A forgery so lazy it assumed no one would ever check, so arrogant it thought the past had no readers. Sena photographs every page, light trembling. Kwame whispers, 'If I send this, I'm finished here.' I answer, 'If you hide it, so are we.' "
        "He presses the keycard into my palm. Sometimes courage is just passing the key to the next hand."
    ),
    "S15": (
        "The promenade meeting was supposed to have a generator. At dusk the generator dies. Streetlights die. For a breath no one moves — that particular African dark that makes you hear your neighbours breathe. Then Ama, tired, dips to one knee. I catch her. "
        "Around us, one phone lights, then ten, then a hand lantern, then fifty, blue and amber, irregular, human. We did not need their grid to hold a hearing. I look at the old navigation beacon on the point and understand: it can carry Sena's frequency farther than any shack. "
        "'Tomorrow the town does not ask for a hearing,' I say. 'The town gives one.' 'And who will light it?' Esi asks. 'All of us,' I say, and the dark answers with light."
    ),
    "S16": (
        "Morning in Festival Square, usually for drumming. That morning for fixing. Blue glass from broken bottles, jar lids, solar cells from dead garden lights — Afenyo making lanterns like our ancestors made proverbs, from what was left. "
        "I teach children to wire low voltage without fear: red to red, care to care. Esi coordinates rice and patience. Kwame arrives sleeves rolled, without his lapel pin, carrying the master access code like contraband. "
        "Ama places the oldest lantern — great-grandmother's, copper patched three times — into Sena's hands: 'A light means nothing if it only points at itself.' Sena grins, turquoise headphones catching sun: 'Good. Mine points at everybody.'"
    ),
    "S17": (
        "Blue hour. The lagoon holds its breath between day and night. Kojo brings us to the beacon, and behind us a flotilla — thirty canoes, then fifty, then more than we can count, each with a lantern made that morning, each with a child or grandmother holding it steady. "
        "I connect the repaired solar cell, hands steady for the first time in months. Sena plugs the scans into the air: deeds, water tests, the unredacted map Kwame sends before his phone dies. Then the beacon answers — one long steady blue pulse not seen in twenty years. "
        "'Afenyo is speaking,' Sena says on air, voice cracking. 'Please do not call this noise.' The whole coast hears, because light travels further over water when it is carried by many."
    ),
    "S18": (
        "The community hall has never been that full. Lantern light makes everyone honest. On the blank sheet we project the deed, the pipe, the slick — truth with nowhere to hide. Chairman Nii enters last, expecting silence to be his inheritance. "
        "Instead an old fisherman stands and names the exact date the landing was promised to his father. A market woman corrects him by two days, and everyone laughs, because in Afenyo memory is communal, argued over, alive. "
        "'Development requires difficult decisions,' Nii says, voice thinner now. Ama, small and iron in navy kaba, answers: 'Then let the people who carry the difficulty make them.' He lowers his heron cane, and the room exhales twenty years."
    ),
    "S19": (
        "Morning light after rain is forensic. The district hall windows open for the first time I can remember. Under public eyes — phones recording, Sena's mic red, children on the floor — Chairman Nii reads the suspension himself, each word a stone dropped in water. "
        "Resort permit suspended pending independent inquiry. Kwame stands, jacket off, lays down resignation and every file marked PERSONAL. But Esi does not let us stop at a pause. 'A pause is only a door,' I say, 'if we decide what walks through it.' "
        "We vote not just for stoppage, but for a cooperative water board — fisherfolk, boatmen, grandmothers, engineers. Sena catches the sound of hands rising. It is the first time voting sounds like a tide coming in."
    ),
    "S20": (
        "Sunrise on the pier and the pier looks new though it is old. The beacon flashes white now, not just for navigation but to remind. Kojo and I bolt a community battery beneath it, Esi's coop loading nets, Kwame in work gloves learning to mend instead of liaise. "
        "Ama watches Sena start her new program, oldest lantern on the desk, mic live. 'This is Afenyo,' she says, voice finding itself. 'The light is public. The water is public. Good morning.' "
        "I look at Ama. She nods once. The lagoon brightens — not because the sun came up, but because we finally decided to share its first light. The river remembers, yes, but only if someone chooses, every morning, to remember with it."
    ),
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
        except Exception as exc:
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
    if not SCREENPLAY.exists():
        return FALLBACK_ACT_TITLES, FALLBACK_SCENE_TITLES, FALLBACK_ACT_SCENES
    text = SCREENPLAY.read_text(encoding="utf-8")
    act_pat = re.compile(r"^###\s+ACT\s+([IV]+)\s+[—\-]\s+(.+)$", re.IGNORECASE | re.MULTILINE)
    scene_pat = re.compile(r"^##\s+(S\d+)\s+[—\-]\s+(.+)$", re.MULTILINE)
    act_titles: dict[int, str] = {}
    scene_titles: dict[str, str] = {}
    act_scenes: dict[int, list[str]] = defaultdict(list)
    lines = text.splitlines()
    current_act_num: int | None = None
    for line in lines:
        act_m = act_pat.match(line.strip())
        if act_m:
            roman = act_m.group(1).upper()
            name_raw = act_m.group(2).strip()
            act_num = ROMAN_TO_INT.get(roman)
            if act_num is None:
                continue
            name = name_raw.title() if name_raw.isupper() else name_raw
            act_titles[act_num] = f"Act {roman} — {name}"
            current_act_num = act_num
            if current_act_num not in act_scenes:
                act_scenes[current_act_num] = []
            continue
        scene_m = scene_pat.match(line.strip())
        if scene_m:
            sid = scene_m.group(1).upper()
            title_raw = scene_m.group(2).strip()
            scene_titles[sid] = f"{sid} — {title_raw}"
            if current_act_num is not None:
                if sid not in act_scenes[current_act_num]:
                    act_scenes[current_act_num].append(sid)
            continue
    if not act_titles:
        act_titles = FALLBACK_ACT_TITLES.copy()
    else:
        for k, v in FALLBACK_ACT_TITLES.items():
            if k not in act_titles:
                act_titles[k] = v
    if not scene_titles or len(scene_titles) < 20:
        merged = FALLBACK_SCENE_TITLES.copy()
        merged.update(scene_titles)
        scene_titles = merged
    if not act_scenes or sum(len(v) for v in act_scenes.values()) < 20:
        act_scenes = FALLBACK_ACT_SCENES.copy()
    else:
        for k in FALLBACK_ACT_SCENES:
            if k not in act_scenes:
                act_scenes[k] = FALLBACK_ACT_SCENES[k]
    for act_num in act_scenes:
        uniq = list(OrderedDict.fromkeys(act_scenes[act_num]))
        act_scenes[act_num] = sorted(uniq, key=lambda s: int(s[1:]))
    return act_titles, scene_titles, act_scenes


def group_by_scene(files: list[Path]) -> dict[str, list[Path]]:
    grouped: dict[str, list[Path]] = defaultdict(list)
    for p in files:
        stem = p.stem
        if "_" in stem:
            sid = stem.split("_")[0]
            if re.match(r"^S\d+$", sid):
                grouped[sid].append(p)
            else:
                grouped["_other"].append(p)
        else:
            grouped["_other"].append(p)
    for k in grouped:
        grouped[k] = sorted(grouped[k], key=lambda x: x.name)
    return dict(sorted(grouped.items()))


def main() -> None:
    refs = image_files(ROOT / "images" / "refs")
    acts_files = {act: image_files(ROOT / "images" / f"act{act}") for act in (1, 2, 3)}
    total = len(refs) + sum(len(v) for v in acts_files.values())
    act_titles, scene_titles, act_scenes = parse_screenplay()

    body_parts: list[str] = []

    refs_heading = "Character References"
    refs_count = len(refs)
    refs_grid = cards(refs, "Reference sheets are awaiting generation.")
    body_parts.append(
        f'<section class="top-section refs-section">'
        f'<div class="section-heading"><h2>{html.escape(refs_heading)}</h2>'
        f'<span>{refs_count} image{"s" if refs_count != 1 else ""}</span></div>'
        f'<div class="grid">{refs_grid}</div></section>'
    )

    for act_num in (1, 2, 3):
        files = acts_files.get(act_num, [])
        grouped = group_by_scene(files)
        act_title = act_titles.get(act_num, FALLBACK_ACT_TITLES.get(act_num, f"Act {act_num}"))
        act_count = len(files)
        scene_order = act_scenes.get(act_num)
        if not scene_order:
            scene_order = [k for k in grouped.keys() if k.startswith("S")]
            scene_order = sorted(scene_order, key=lambda s: int(s[1:]) if s[1:].isdigit() else 999)

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
                s_title = scene_titles.get(sid, sid)
                voice = VOICE_SCRIPTS.get(sid, "")
                if not s_files:
                    cards_html = f'<p class="empty">No images for {html.escape(s_title)} yet.</p>'
                    count = 0
                else:
                    cards_html = cards(s_files, f"No images for {s_title}")
                    count = len(s_files)
                anchor = sid.lower()
                voice_block = ""
                if voice:
                    voice_block = (
                        f'<div class="voiceover">'
                        f'<div class="voice-label">🎙️ VOICEOVER — {html.escape(sid)} NARRATION</div>'
                        f'<p>{html.escape(voice)}</p>'
                        f'</div>'
                    )
                act_html.append(
                    f'<div class="scene" id="{html.escape(anchor)}">'
                    f'<div class="scene-heading"><h3>{html.escape(s_title)}</h3>'
                    f'<span>{count} step{"s" if count != 1 else ""}</span></div>'
                    f'{voice_block}'
                    f'<div class="grid">{cards_html}</div></div>'
                )

            extra_sids = [k for k in grouped.keys() if k not in scene_order and k.startswith("S")]
            for sid in sorted(extra_sids, key=lambda s: int(s[1:]) if s[1:].isdigit() else 999):
                s_files = grouped[sid]
                s_title = scene_titles.get(sid, sid)
                voice = VOICE_SCRIPTS.get(sid, "")
                cards_html = cards(s_files, "")
                count = len(s_files)
                anchor = sid.lower()
                voice_block = ""
                if voice:
                    voice_block = (
                        f'<div class="voiceover">'
                        f'<div class="voice-label">🎙️ VOICEOVER — {html.escape(sid)} NARRATION</div>'
                        f'<p>{html.escape(voice)}</p>'
                        f'</div>'
                    )
                act_html.append(
                    f'<div class="scene" id="{html.escape(anchor)}">'
                    f'<div class="scene-heading"><h3>{html.escape(s_title)}</h3>'
                    f'<span>{count} step{"s" if count != 1 else ""}</span></div>'
                    f'{voice_block}'
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
:root {{ --ink:#172020; --muted:#617071; --paper:#f7f2e9; --navy:#102c3a; --teal:#19636b; --amber:#d88a28; --card:#fffdf9; --line:#d8d0c1; --line-light:#e8e0d1; --voice-bg:#fdf1d8; --voice-border:#d8a73a; }}
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
.scene-heading {{ display:flex; align-items:baseline; justify-content:space-between; gap:1rem; border-bottom:1px solid var(--line-light); padding-bottom:.5rem; margin-bottom:.8rem; }}
.scene-heading h3 {{ margin:0; font-size:1.18rem; font-family:Georgia,serif; letter-spacing:.01em; }}
.scene-heading span {{ color:var(--muted); font-size:.82rem; white-space:nowrap; }}
.voiceover {{ margin:0 0 1rem 0; padding:1rem 1.1rem; background:var(--voice-bg); border-left:4px solid var(--voice-border); border-radius:8px; line-height:1.7; }}
.voice-label {{ font-size:.72rem; letter-spacing:.12em; font-weight:700; color:var(--teal); margin-bottom:.4rem; text-transform:uppercase; }}
.voiceover p {{ margin:0; font-family:Georgia,serif; font-size:.98rem; color:#2c2a26; }}
footer {{ max-width:1380px; margin:auto; padding:0 1.3rem 3rem; color:var(--muted); font-size:.8rem; }}
@media (max-width:600px) {{ .grid {{ grid-template-columns:1fr 1fr; gap:.7rem; }} .scene {{ padding:.8rem; }} .scene-heading h3 {{ font-size:1rem; }} .voiceover p {{ font-size:.92rem; }} }}
</style>
</head>
<body>
<header><h1>The River Remembers</h1><p>A self-contained visual production gallery. Every thumbnail is JPEG-compressed, base64-inlined and viewable offline; no external image, font, script or network request is used. Hierarchy: Character References → Act → Scene (S01–S20) with voiceover narration → Step cards.</p><span class="badge">{total} visual asset{'s' if total != 1 else ''} in this build — 7 refs + 200 steps + 20 voice scripts</span>
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
<footer>Generated from <code>images/refs/</code> and <code>images/act1–3/</code>. Re-run <code>build_gallery.py</code> after adding a batch. All images are inlined as base64 JPEG thumbnails for offline viewing. Hierarchy: Character References → Act → Scene + Voiceover → Steps. 20 voice scripts form continuous story.</footer>
</body></html>"""
    document = document.replace('class="top-section refs-section"', 'class="top-section refs-section" id="refs"')
    document = document.replace('class="act act-1"', 'class="act act-1" id="act1"')
    document = document.replace('class="act act-2"', 'class="act act-2" id="act2"')
    document = document.replace('class="act act-3"', 'class="act act-3" id="act3"')

    OUT.write_text(document, encoding="utf-8")
    print(f"Wrote {OUT.name} with {len(refs)} refs, {sum(len(v) for v in acts_files.values())} scenes = {total}, plus {len(VOICE_SCRIPTS)} voiceovers.")
    for act_num in (1,2,3):
        print(f"{act_titles.get(act_num)}: {act_scenes.get(act_num)}")


if __name__ == "__main__":
    main()
