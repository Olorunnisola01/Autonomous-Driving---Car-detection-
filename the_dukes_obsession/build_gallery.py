#!/usr/bin/env python3
"""Build storyboard gallery for The Duke's Obsession.

Parses SCREENPLAY.md, collects images, generates placeholders for missing ones,
and creates a self-contained storyboard_gallery.html with all 258 images inlined.
"""
import base64
import io
import random
import re
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "storyboard_gallery.html"
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".webp"}

SCENES = [
    ("S01", "The Debt That Breathes", "I learned to count debts the way other girls counted stitches — by candlelight, by the tremor in my father's hands, by the silence that grew thicker than the leather we bound. The workshop smelled of old paper and desperation. Every creditor notice on the wall was another winter we might not survive. I told him we could sell the Chaucer. He said Mother loved it. I said it was worth more alive than dead. We both knew I was lying. Some things, once sold, cannot be bought back.", "FINCH_BINDERY", 1),
    ("S02", "The Summons Arrives", "The letter came under the door like a thief — black wax, black seal, the thorned rose pressed into it like a brand. I broke it open before I understood what I was opening. They wanted a bookbinder's daughter at Blackthorn Hall. Payment enough to clear every debt, every notice, every whisper of ruin. My father's eyes went wide when I read it aloud. Not with hope. With recognition. He said the Duke knew his name. I said not his name. Someone else's. The question sat between us like a third person in the room.", "FINCH_BINDERY", 1),
    ("S03", "The Road to Blackthorn", "The road stretched ahead of me like a warning written in frost. Every hedgerow was skeletal, every breath a small white ghost that vanished before I could name it. I walked alone with my satchel of binding tools and the weight of a decision I hadn't fully made. The milestone appeared suddenly — carved with a thorned rose, ancient and deliberate. I knew then that every story about that house ended the same way. He did it. She vanished. No one agreed on how. They all agreed it happened. I pulled my cloak tighter and kept walking.", "WINTER_ROAD", 1),
    ("S04", "The Gates of Blackthorn Hall", "The gates were taller than a man and twisted into thorned vines, black iron against a grey sky that seemed to press down on everything below it. Mrs. Varma waited in the gateway like a sentinel carved from shadow and silk. She did not smile. She did not welcome. She measured me with one look that took in my ink-stained hands and my worn boots and found something acceptable, or at least tolerable. She said I would sleep in the east wing. Not the upper corridor. The Duke does not receive callers. He receives people who answer letters. I asked what the difference was. She did not answer.", "BLACKTHORN_GATES", 1),
    ("S05", "The First Glimpse of Him", "The foyer was a cavern of candelabras and damask, every shadow longer than it should be. I removed my gloves and tried not to think about the ink still staining my fingertips. Then I looked up. He stood in the upper gallery, half-consumed by darkness, watching me with the patience of a man who had been waiting for a very long time. He did not descend. He did not speak. He simply watched, then turned and disappeared. I whispered to the empty hall that he was not surprised to see me. The echo agreed.", "BLACKTHORN_FOYER", 1),
    ("S06", "The Library That Remembered", "Two stories of shelves bowed under the weight of centuries. Dust motes hung motionless in slanting winter light. A fireplace large enough to stand in held cold ashes and the memory of warmer years. I set down my satchel and exhaled — the first full breath I had taken since arriving. This room was alive with knowledge. I touched a spine and felt something like recognition. Mrs. Varma said the late Duchess had arranged everything by feeling, not subject. I asked how long that took her to understand. She said ten years. She never did.", "BLACKTHORN_LIBRARY", 2),
    ("S07", "The Journals with Her Name", "The journals were leather-bound and cracked with age, each one a small coffin of secrets. I opened one dated thirteen years ago and began to catalogue, to organize, to make order from chaos. Then I found it — my own name. Elara Finch. Written in elegant copperplate in a margin note beside a passage on the binding of psalters. The date was ten years before I was born. My fingers trembled. I read the entry again. The ink was old. The handwriting was deliberate. This was not a coincidence. He knew. Before I existed. He wrote me down.", "BLACKTHORN_LIBRARY", 2),
    ("S08", "The Duke Watches", "Candlelight. Late. I worked without knowing he was there, without knowing I was being watched. He stood in the doorway's shadow, observing as I carefully lifted a page with a bone folder, as if I were performing surgery on something alive. He did not announce himself. I sensed him the way animals sense a storm — in the air pressure, in the sudden stillness that precedes violence or tenderness. When I turned, he was already gone. Only the scent of cold wool and smoke remained. I whispered that he was always there, just behind the edge of seeing.", "BLACKTHORN_LIBRARY", 2),
    ("S09", "The Gallery of Dead Wives", "The corridor of portraits stretched longer than I expected, each face watching me with painted eyes that never blinked. Lucy showed me the house by stolen candlelight, her breath fogging in the cold. We stopped before a painting of Lady Margaret — white satin gown, pearl choker, emerald pendant at her throat. The eyes were dark and knowing. Lucy said they claimed the Duke locked himself in here for a year after she died. I asked how she died. Lucy said that was the question no one answered twice the same way. I looked at my own reflection in the gilt frame and did not like the comparison.", "BLACKTHORN_GALLERY", 2),
    ("S10", "The First Touch", "I fell asleep at the reading desk, a book open against my cheek, unaware of the figure who entered silently. He stood over me, his shadow falling across the page. His gloved hand reached down — not to shake me, not to wake me, but to brush a stray auburn curl from my forehead. His finger grazed my temple. I stirred. Our eyes met across the smallest distance. Neither moved. The candle between us guttered. His voice, when it came, was barely audible. You are exactly as I wrote you. I did not know whether to be terrified or flattered. Perhaps both.", "BLACKTHORN_LIBRARY", 2),
    ("S11", "The Contract on the Desk", "A desk of black oak. A single document. He stood behind it, hands braced on the wood, signet ring catching the firelight. The contract read: all Finch family debts cleared, father's workshop preserved, in exchange for one winter as his Duchess. In name, in public, in residence. No conjugal obligation. No permanent arrangement. I could leave at spring thaw. I asked him why me. He said because I was always the answer. He simply had to wait for the question to arrive. I did not know whether to believe him or run.", "BLACKTHORN_STUDY", 3),
    ("S12", "The Fake Engagement", "A long table set for two, though the house held twenty. Mrs. Varma stood behind my chair, adjusting my collar with proprietary hands. Lucy peeked from the serving doorway, wide-eyed. The Duke took his seat and did not look at me until I was settled, then held my gaze with an intensity that made the candlelight seem dim. He said I would call him Silas in private. In public, I would call him Your Grace and allow no one to see me smile first. I asked what would happen if I smiled first. He said he would spend the evening making it worth the scandal.", "BLACKTHORN_DINING_HALL", 3),
    ("S13", "The Jealousy at the Hunt Ball", "The ballroom glittered with candlelight and crystalline pretense, the local gentry dressed in jewels and calculated indifference. Julian appeared in burgundy velvet, claiming me for a dance with the ease of a man who had never been refused. His hand settled at my waist. Across the room, the Duke watched, a glass of brandy untouched in his hand. Julian asked why I was trembling. I said his cousin's moods were not a difficult text. Julian smiled and said, Then why are you trembling? The Duke crossed the room. He did not dance. He took my hand from Julian's waist and placed it on his own coat.", "BLACKTHORN_BALLROOM", 3),
    ("S14", "The Secret of the First Wife", "I found the locked drawer and forced it open with a bone folder. Inside: letters from Lady Margaret's brother describing his sister's slow poisoning, and a doctor's note that the Duke refused an autopsy. I confronted him. He did not deny the letters. He said they were incomplete. I asked if he killed her. He said she asked him to let her go and he held on too tightly. That was the closest thing to murder he had committed. I asked what about me. A long silence. The fire popped. He said I was the only thing he had ever been afraid to hold.", "BLACKTHORN_STUDY", 3),
    ("S15", "The Agreement", "Winter light turned the library gold. I stood by the window, the contract in my hands. He waited by the fireplace, still as a portrait. I had read every clause. I had found the escape clause: I could leave at spring, with my father's debts cleared, no conditions. I folded the document slowly. I told him I would stay the winter. Not because of the debt. Because I needed to know if what he wrote in those journals was true, or if I was just the woman who looked enough like a ghost to fill the space. He crossed the room and stopped exactly one arm's length from me. He said I was never a ghost. I was the only living thing he could imagine in this house.", "BLACKTHORN_LIBRARY", 3),
    ("S16", "The Betrayal", "Julian found me alone and smiled like a man who enjoyed delivering poison. He revealed that the Duke's journals contained entries not about love — but about ownership. He had been watching me since I was a child, arranging circumstances to bring me here. Julian showed me a page: the Duke purchased my father's debt from the original creditor three years ago. I was never summoned — I was harvested. Julian said I was not a bride. I was a collection. The Duke entered. He did not deny it.", "BLACKTHORN_STUDY", 4),
    ("S17", "The Fire in the East Wing", "My room. I had packed my satchel. The smell of smoke seeped under the door before I understood what it meant. The east wing corridor filled with orange light. Lucy screamed from the stairwell. Mrs. Varma appeared, pressing a key into my hand — a servants' exit. She said go, now, do not look for him. Lucy said the fire started in the gallery, the portraits were burning. I ran through smoke, the key cold in my palm, and did not look at the burning gallery where Lady Margaret's portrait turned to ash.", "BLACKTHORN_EAST_WING", 4),
    ("S18", "She Tries to Flee", "I stumbled through snow beyond the grounds, my green dress stained with soot, my brass thimble swinging against my collarbone. The frost bit through my boots. I had gone perhaps a mile when I realized I had been walking in a circle — the frost showed my own footprints ahead of me. The grounds of Blackthorn were larger than I understood. Or something was keeping me contained. I stopped. My breath came in white clouds. I was alone. I was lost. I was furious. I whispered that I would not be the ghost, I would not be the collection, I would not be the thing he wrote.", "BLACKTHORN_GROUNDS", 4),
    ("S19", "He Lets Her Go", "The iron gates. I reached them at first light, exhausted, smoke-stained. The Duke stood on the other side. He had a horse saddled, a traveling cloak folded over its back, a letter of transit in his hand. He had not come to stop me. He had come to arm me. He said he bought the debt because he could not bear the thought of me starving while he did nothing. He said he did not arrange me. He waited for me. There was a difference and he knew it did not excuse anything. He opened the gate. He said go. If I returned, it must be because I chose to. Not because I had nowhere else.", "BLACKTHORN_GATES", 4),
    ("S20", "The Distance Between", "A village inn. I sat by a fire, wrapped in the traveling cloak the Duke gave me though I had tried to return it. Father Benedict brought me tea and sat without invitation. He had known the Duke for decades. He had known grief. He said the Duke came to him after Margaret died and asked how to stop loving what he could not save. I asked what he chose. Father Benedict said he chose to wait. For ten years, he chose to wait. That was not obsession, child. That was the only patience he had ever seen that deserved to be called love.", "VILLAGE_INN", 4),
    ("S21", "The Return on Her Own Terms", "I returned to the gates. Not in the cloak he gave me — I had returned it. I wore my own forest-green dress, clean but worn, my satchel over my shoulder. I carried no contract. I carried nothing except myself. Mrs. Varma opened the gate without being asked. The Duke stood in the gravel drive, uncovered by hat or hood, snow catching in his too-long black hair. He had been waiting. He had always been waiting. I told him I did not come back for the contract. He said he knew. I said I came back because the alternative was a lifetime of listening for his footsteps and pretending I did not miss them.", "BLACKTHORN_GATES", 5),
    ("S22", "The Consummation", "His private chambers. High windows black with winter night, a fire low and amber. I stood before him. No contract between us now. No audience. No bargain. He removed his gloves slowly, finger by finger. His bare hands took my face as if I were a text he had been trying to read for a decade and had only now learned the language. He said say my name. I said Silas. He closed his eyes. It was the first time he had heard his own name spoken like a prayer.", "BLACKTHORN_CHAMBERS", 5),
    ("S23", "The Public Claiming", "A second ball — this one my choice. I entered on the Duke's arm, not as contract bride but as chosen Duchess. Julian watched from the crowd, his smile sharp enough to cut. Mrs. Varma stood at the door, and for the first time, she smiled. Lucy caught my eye from behind the refreshment table and mouthed: finally. The Duke led me to the center of the floor and did not let go. He whispered that they could stare, they could write it down, Julian could tell every version he liked. They would never be able to say he did not ask. I said he asked every day. I simply could not hear it until I was ready to answer.", "BLACKTHORN_BALLROOM", 5),
    ("S24", "The Marriage", "A small village church, snow on the windowsills. Not a cathedral performance but a true thing. My father walked me down the aisle, his hands steadier than they had been in years. Lucy held the flowers. Mrs. Varma stood as witness for the house. Father Benedict spoke the words with a voice that cracked on the word join. The Duke's signet ring was warm against my finger as he slid it on — beside my brass thimble chain, beside the ink that would never wash out. I said I do. He said he always had.", "VILLAGE_CHURCH", 5),
    ("S25", "The True Duchess", "Years later. The same library, but alive now — curtains drawn back, fire lit, books opened and scattered. I sat in the reading chair with a child balanced on my knee, pointing at gold lettering on a page. The Duke stood behind me, his hand on the chair's back, his signet ring catching light that fell through winter glass. The room smelled of old paper and beeswax and woodsmoke. The thorned rose crest was carved into the chair's armrest, but now it looked less like a warning and more like a welcome. I read aloud to the child: And the Duke kept his word. Every word. Every winter. Every one. The Duke said not every word. He told me once that he would survive without me. I said that was the only lie he ever told. The child laughed. The fire crackled.", "BLACKTHORN_LIBRARY", 5),
]

STEP_DESCRIPTIONS = {
    "S01": ["candlelit_bindery_wide", "thomas_at_press", "elara_stitching", "creditor_notices", "trembling_hands", "elara_concern", "chaucer_on_shelf", "elara_deciding", "father_protests", "candle_gutters"],
    "S02": ["black_sealed_letter", "elara_picks_up_letter", "breaking_wax_seal", "blackthorn_crest_closeup", "elara_reading", "father_tries_to_rise", "recognition_and_terror", "elara_speaks", "father_responds", "letter_on_table"],
    "S03": ["frost_road_wide", "elara_walking_alone", "skeletal_hedgerows", "breath_fog", "milestone_carving", "boots_on_frozen_ground", "grey_sky_landscape", "elara_pulls_cloak", "distant_manor_silhouette", "approaching_gates"],
    "S04": ["iron_gates_establishing", "thorned_vine_ironwork", "gravel_drive_to_manor", "mrs_varma_at_gateway", "mrs_varma_measures_elara", "elara_nervous", "mrs_varma_leads_inside", "elara_follows_through_gates", "gates_beginning_to_close", "gates_fully_closed"],
    "S05": ["cavernous_foyer", "candelabras_on_walls", "elara_removes_gloves", "staircase_into_shadow", "duke_in_upper_gallery", "duke_watching_from_dark", "elara_looks_up", "duke_turns_away", "duke_disappears", "elara_alone_whispering"],
    "S06": ["library_establishing", "dust_motes_in_light", "elara_sets_down_satchel", "fireplace_cold_ashes", "elara_touches_spine", "shelves_ancient_books", "mrs_varma_explains", "elara_breathes_freely", "library_atmosphere", "elara_begins_work"],
    "S07": ["journals_on_desk", "elara_cataloguing", "opening_leather_journal", "margin_note_closeup", "elara_discovers_name", "hands_trembling", "elara_reads_again", "ink_old_deliberate", "shock_on_face", "alone_with_discovery"],
    "S08": ["elara_works_late", "candlelight_library", "duke_in_doorway_shadow", "elara_senses_presence", "air_pressure_change", "elara_turns", "duke_already_gone", "scent_cold_wool_smoke", "elara_whispers", "empty_doorway"],
    "S09": ["portrait_corridor", "lucy_with_candle", "lady_margaret_portrait", "pearl_choker_emerald", "dark_knowing_eyes", "elara_in_frame_reflection", "lucy_explains", "elara_asks_how_died", "no_one_answers_same", "uncomfortable_comparison"],
    "S10": ["elara_asleep_at_desk", "book_against_cheek", "duke_enters_silently", "shadow_falls_on_page", "gloved_hand_reaches", "brushes_curl_forehead", "finger_grazes_temple", "eyes_meet_smallest_distance", "candle_gutters", "duke_speaks_softly"],
    "S11": ["black_oak_desk", "single_document", "duke_behind_desk", "signet_ring_firelight", "contract_details", "elara_reads", "why_me_question", "duke_responds", "always_the_answer", "waited_for_question"],
    "S12": ["long_table_for_two", "mrs_varma_adjusts_collar", "lucy_peeks_doorway", "duke_takes_seat", "intense_gaze", "call_me_silas", "your_grace_in_public", "smile_first_question", "worth_the_scandal", "dinner_begins"],
    "S13": ["ballroom_glittering", "crystalline_pretense", "julian_in_burgundy", "claims_dance", "hand_at_waist", "duke_watches_distance", "brandy_untouched", "knuckles_whiten", "why_trembling", "duke_crosses_room"],
    "S14": ["locked_drawer_forced", "letters_inside", "poisoning_described", "doctor_note", "elara_confronts", "duke_does_not_deny", "closest_to_murder", "held_on_too_tightly", "what_about_me", "afraid_to_hold"],
    "S15": ["winter_light_gold", "elara_by_window", "contract_in_hands", "duke_by_fireplace", "escape_clause", "folds_document_slowly", "stay_the_winter", "not_for_the_debt", "need_to_know_truth", "one_arms_length"],
    "S16": ["julian_finds_elara_alone", "poison_smile", "journals_reveal_ownership", "watching_since_childhood", "arranging_circumstances", "purchased_debt_page", "never_summoned_harvested", "not_a_bride", "a_collection", "duke_enters_not_deny"],
    "S17": ["room_packed_satchel", "smoke_under_door", "orange_light_corridor", "lucy_screams", "mrs_varma_appears", "key_pressed_in_hand", "servants_exit", "go_now", "fire_in_gallery", "portraits_burning"],
    "S18": ["stumbles_through_snow", "dress_stained_soot", "brass_thimble_swinging", "frost_bites_boots", "walking_in_circle", "own_footprints_ahead", "grounds_larger_than_known", "breath_white_clouds", "alone_lost_furious", "will_not_be_ghost"],
    "S19": ["iron_gates_first_light", "exhausted_smoke_stained", "duke_other_side", "horse_saddled", "traveling_cloak_folded", "letter_of_transit", "not_come_to_stop", "come_to_arm", "bought_debt_not_bear", "opened_the_gate"],
    "S20": ["village_inn_fire", "wrapped_in_cloak", "father_benedict_tea", "known_duke_decades", "known_grief", "asked_how_stop_loving", "what_did_he_choose", "chose_to_wait", "ten_years_patience", "deserved_called_love"],
    "S21": ["returns_to_gates", "not_in_his_cloak", "own_forest_green_dress", "satchel_over_shoulder", "no_contract_carried", "only_herself", "mrs_varma_opens_gate", "duke_in_gravel_drive", "always_been_waiting", "listen_for_footsteps"],
    "S22": ["private_chambers", "high_windows_winter_night", "fire_low_amber", "no_contract_between", "gloves_removed_slowly", "bare_hands_take_face", "text_learned_language", "say_my_name", "silas_spoken_prayer", "eyes_closed"],
    "S23": ["second_ball_her_choice", "enters_on_dukes_arm", "chosen_duchess", "julian_watches_sharp", "mrs_varma_smiles", "lucy_mouths_finally", "center_of_floor", "does_not_let_go", "let_them_stare", "ready_to_answer"],
    "S24": ["small_village_church", "snow_on_windowsills", "father_walks_daughter", "hands_steadier", "lucy_holds_flowers", "mrs_varma_witness", "father_benedict_speaks", "voice_cracks", "signet_ring_warm", "always_had"],
    "S25": ["library_alive_now", "curtains_drawn_back", "fire_lit_books_scattered", "reading_chair_child", "gold_lettering_page", "duke_hand_on_chair", "signet_ring_catching_light", "thorned_rose_welcome", "read_aloud_to_child", "only_lie_ever_told"],
}

ACTS = {
    1: ("INHERITANCE", ["S01", "S02", "S03", "S04", "S05"]),
    2: ("OBSESSION", ["S06", "S07", "S08", "S09", "S10"]),
    3: ("THE BARGAIN", ["S11", "S12", "S13", "S14", "S15"]),
    4: ("RUIN", ["S16", "S17", "S18", "S19", "S20"]),
    5: ("DEVOTION", ["S21", "S22", "S23", "S24", "S25"]),
}


def create_placeholder(scene_id: str, step_num: int, w: int = 960, h: int = 540) -> Image.Image:
    """Fast Gothic placeholder with radial gradient."""
    rng = random.Random(hash(f"{scene_id}_{step_num}"))
    palettes = [
        ((50, 10, 15), (100, 25, 30), (20, 5, 8)),
        ((15, 15, 25), (40, 40, 55), (8, 8, 15)),
        ((60, 15, 20), (90, 30, 35), (25, 5, 8)),
        ((30, 15, 35), (60, 35, 65), (15, 8, 18)),
        ((15, 25, 40), (35, 55, 70), (5, 10, 20)),
        ((45, 10, 10), (85, 20, 25), (18, 3, 5)),
    ]
    dark, mid, darker = rng.choice(palettes)
    img = Image.new('RGB', (w, h))
    draw = ImageDraw.Draw(img)
    cx, cy = w // 2, h // 2
    max_dist = ((w // 2) ** 2 + (h // 2) ** 2) ** 0.5
    for y in range(h):
        dy = (y - cy) / max_dist if max_dist > 0 else 0
        for x in range(0, w, 4):
            dx = (x - cx) / max_dist if max_dist > 0 else 0
            dist = min(1.0, (dx * dx + dy * dy) ** 0.5)
            r = int(mid[0] * (1 - dist) + darker[0] * dist)
            g = int(mid[1] * (1 - dist) + darker[1] * dist)
            b = int(mid[2] * (1 - dist) + darker[2] * dist)
            draw.rectangle([x, y, x + 4, y + 1], fill=(r, g, b))
    for _ in range(w * h // 200):
        x = rng.randint(0, w - 1)
        y = rng.randint(0, h - 1)
        v = rng.randint(0, 40)
        draw.point((x, y), fill=(v + 20, v + 15, v + 10))
    step_desc = STEP_DESCRIPTIONS.get(scene_id, [f"step_{i}" for i in range(10)])[step_num - 1]
    label = f"{scene_id} — Step {step_num:02d}"
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    except Exception:
        font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), label, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = (w - tw) // 2
    y = (h - th) // 2
    draw.text((x + 2, y + 2), label, fill=(0, 0, 0), font=font)
    draw.text((x, y), label, fill=(200, 180, 150), font=font)
    return img


def generate_missing():
    """Generate placeholders for missing scene step images."""
    count = 0
    for scene_id, _, _, _, act_num in SCENES:
        act_dir = ROOT / "images" / f"act{act_num}"
        act_dir.mkdir(parents=True, exist_ok=True)
        existing = [p for p in act_dir.iterdir()
                    if p.is_file() and p.suffix.lower() in IMAGE_EXT and p.name.startswith(f"{scene_id}_")]
        existing_stems = {p.stem for p in existing}
        for step_num, step_desc in enumerate(STEP_DESCRIPTIONS[scene_id], 1):
            filename = f"{scene_id}_Step{step_num:02d}_{step_desc}.png"
            stem = filename[:-4]
            if stem not in existing_stems:
                filepath = act_dir / filename
                if not filepath.exists():
                    img = create_placeholder(scene_id, step_num)
                    img.save(filepath, format='PNG', optimize=True)
                    count += 1
                    if count % 20 == 0:
                        print(f"  Generated {count} placeholders...")
    print(f"  Done. Generated {count} placeholder images.")


def label_for(path: Path) -> str:
    stem = path.stem
    if stem.endswith("_ref"):
        return stem[:-4].replace("_", " ").title() + " — CHARACTER REFERENCE"
    parts = stem.split("_")
    if len(parts) >= 2 and parts[0].startswith("S") and parts[1].startswith("Step"):
        return f"{parts[0]} — " + " ".join(parts[2:]).replace("_", " ").title()
    return stem.replace("_", " ").title()


def inline_thumb(path: Path, max_size: int = 520) -> tuple:
    with Image.open(path) as raw:
        image = ImageOps.exif_transpose(raw).convert("RGB")
        orig_w, orig_h = image.size
        target_w = max_size
        target_h = int(max_size * 9 / 16)
        image.thumbnail((target_w, target_h), Image.Resampling.LANCZOS)
        canvas = Image.new('RGB', (target_w, target_h), (17, 29, 36))
        canvas.paste(image, ((target_w - image.width) // 2, (target_h - image.height) // 2))
        buffer = io.BytesIO()
        canvas.save(buffer, format="JPEG", quality=75, optimize=True)
    return base64.b64encode(buffer.getvalue()).decode("ascii"), orig_w, orig_h


def image_files(folder: Path) -> list:
    if not folder.exists():
        return []
    return sorted((p for p in folder.iterdir()
                   if p.is_file() and p.suffix.lower() in IMAGE_EXT),
                  key=lambda p: p.name)


import html as html_mod


def build_card(path: Path) -> str:
    try:
        data, orig_w, orig_h = inline_thumb(path)
        label = label_for(path)
        return (
            f'<article class="card">'
            f'<img loading="lazy" src="data:image/jpeg;base64,{data}" alt="{html_mod.escape(label)}">'
            f'<div class="meta"><h3>{html_mod.escape(label)}</h3>'
            f'<p>{orig_w}×{orig_h}</p></div></article>'
        )
    except Exception as e:
        return f'<article class="card error"><p>Could not load: {html_mod.escape(str(e))}</p></article>'


def build_ref_section(refs):
    cards = "".join(build_card(p) for p in refs)
    return f'''<section id="character-refs">
        <div class="section-heading"><h2>Character References</h2><span>{len(refs)} characters</span></div>
        <div class="grid">{cards}</div>
    </section>'''


def build_scene(sid, title, voiceover, location, images):
    cards = "".join(build_card(p) for p in images)
    if not cards:
        cards = '<p class="empty">No images yet.</p>'
    return f'''<section class="scene-section" id="{sid}">
        <div class="scene-header">
            <h3>{sid} — {html_mod.escape(title)}</h3>
            <div class="scene-location">Location: {html_mod.escape(location)}</div>
            <div class="voiceover">{html_mod.escape(voiceover)}</div>
        </div>
        <div class="grid grid-4">{cards}</div>
    </section>'''


def build_act(act_num, act_name, scene_ids, act_images, scene_map):
    parts = [f'<div class="act-header" id="act-{act_num}"><h2>Act {act_num} — {act_name}</h2>'
             f'<div class="act-subtitle">Scenes {scene_ids[0]}–{scene_ids[-1]}</div></div>']
    for sid in scene_ids:
        info = scene_map[sid]
        scene_imgs = [p for p in act_images if p.name.startswith(f"{sid}_")]
        parts.append(build_scene(sid, info["title"], info["voiceover"], info["location"], scene_imgs))
    return "\n".join(parts)


def build_gallery():
    print("=" * 60)
    print("THE DUKE'S OBSESSION — Gallery Builder")
    print("=" * 60)
    print("\n1. Generating missing placeholders...")
    generate_missing()
    
    scene_map = {s[0]: {"title": s[1], "voiceover": s[2], "location": s[3], "act": s[4]} for s in SCENES}
    refs = image_files(ROOT / "images" / "refs")
    acts = {a: image_files(ROOT / "images" / f"act{a}") for a in (1, 2, 3, 4, 5)}
    total = len(refs) + sum(len(f) for f in acts.values())
    print(f"\n2. Images: {total} total, {len(refs)} refs")
    for a in range(1, 6):
        print(f"   Act {a}: {len(acts[a])}")
    
    print("\n3. Building HTML...")
    sections = [build_ref_section(refs)]
    for a in range(1, 6):
        name, sids = ACTS[a]
        sections.append(build_act(a, name, sids, acts[a], scene_map))
    body = "\n".join(sections)
    
    nav = ['<a href="#character-refs">Character References</a>']
    for a in range(1, 6):
        name, sids = ACTS[a]
        nav.append(f'<a href="#act-{a}" class="act-link">Act {a} — {name}</a>')
        for sid in sids:
            nav.append(f'<a href="#{sid}" class="scene-link">{sid} — {scene_map[sid]["title"]}</a>')
    nav_html = "\n        ".join(nav)
    
    document = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Duke's Obsession — Storyboard Gallery</title>
<style>
:root {{ --bg-dark: #0a0a0f; --bg-card: #111d24; --crimson: #8b1a1a; --crimson-light: #a62020;
    --gold: #c9a961; --gold-dim: #8a7540; --text: #e8e0d5; --muted: #8a8078; --charcoal: #2a2a2f; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ color: var(--text); background: var(--bg-dark); font-family: Georgia, 'Times New Roman', serif; line-height: 1.6; }}
header {{ padding: 4rem 2rem 3rem; text-align: center; background: linear-gradient(180deg, #1a0a0f 0%, #0a0a0f 100%); border-bottom: 2px solid var(--crimson); }}
header h1 {{ font-size: clamp(2.5rem, 6vw, 4.5rem); color: var(--gold); letter-spacing: 0.06em; margin-bottom: 1rem; text-shadow: 0 2px 30px rgba(201,169,97,0.2); }}
header .subtitle {{ font-size: 1.1rem; color: var(--crimson-light); letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 1.5rem; }}
header .logline {{ max-width: 55rem; margin: 0 auto 1.5rem; color: var(--text); font-style: italic; font-size: 1rem; line-height: 1.8; opacity: 0.9; }}
.badge {{ display: inline-block; margin-top: 0.5rem; padding: 0.4rem 1.2rem; border: 1px solid var(--gold-dim); color: var(--gold); font-size: 0.85rem; letter-spacing: 0.1em; }}
main {{ max-width: 1400px; margin: 0 auto; padding: 2rem 1.5rem 4rem; }}
.section-heading {{ display: flex; align-items: baseline; justify-content: space-between; border-bottom: 2px solid var(--crimson); padding-bottom: 0.75rem; margin-bottom: 1.5rem; }}
.section-heading h2 {{ font-size: 1.8rem; color: var(--gold); letter-spacing: 0.03em; }}
.section-heading span {{ color: var(--muted); font-size: 0.9rem; }}
.act-header {{ text-align: center; margin: 5rem 0 2rem; padding: 2.5rem 2rem; border-top: 1px solid var(--gold-dim); border-bottom: 1px solid var(--gold-dim); }}
.act-header h2 {{ font-size: 2.5rem; color: var(--gold); letter-spacing: 0.05em; margin-bottom: 0.5rem; }}
.act-subtitle {{ color: var(--muted); font-style: italic; font-size: 1.1rem; }}
.scene-header {{ margin: 3rem 0 1.5rem; padding: 1.5rem 2rem; background: linear-gradient(135deg, rgba(139,26,26,0.08) 0%, rgba(10,10,15,0.9) 100%); border-left: 4px solid var(--crimson); }}
.scene-header h3 {{ font-size: 1.5rem; color: var(--gold); margin-bottom: 0.3rem; }}
.scene-location {{ color: var(--muted); font-size: 0.85rem; margin-bottom: 1rem; letter-spacing: 0.05em; }}
.voiceover {{ padding: 1.5rem 2rem; background: rgba(42,42,47,0.3); border-left: 3px solid var(--gold); font-style: italic; line-height: 1.9; color: var(--text); position: relative; margin-top: 1rem; }}
.voiceover::before {{ content: '\\201C'; font-size: 4rem; color: var(--gold-dim); position: absolute; top: -0.2rem; left: 0.5rem; line-height: 1; opacity: 0.5; }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 1.2rem; margin-top: 1rem; }}
.grid-4 {{ grid-template-columns: repeat(4, 1fr); }}
.card {{ overflow: hidden; border: 1px solid rgba(201,169,97,0.15); border-radius: 4px; background: var(--bg-card); cursor: pointer; transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s; }}
.card:hover {{ transform: translateY(-3px); border-color: var(--gold); box-shadow: 0 8px 25px rgba(139,26,26,0.25); }}
.card img {{ display: block; width: 100%; aspect-ratio: 16/9; object-fit: contain; background: var(--bg-card); }}
.card .meta {{ padding: 0.6rem 0.8rem 0.8rem; }}
.card h3 {{ font-size: 0.85rem; color: var(--text); line-height: 1.3; }}
.card p {{ color: var(--muted); font-size: 0.72rem; margin-top: 0.2rem; }}
.lightbox {{ display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.95); z-index: 10000; justify-content: center; align-items: center; padding: 2rem; cursor: pointer; }}
.lightbox.active {{ display: flex; }}
.lightbox img {{ max-width: 92vw; max-height: 92vh; object-fit: contain; border: 2px solid var(--gold-dim); cursor: default; }}
.lightbox-close {{ position: fixed; top: 1.5rem; right: 2rem; font-size: 2.5rem; color: var(--gold); background: none; border: none; cursor: pointer; z-index: 10001; line-height: 1; }}
.sidebar-toggle {{ position: fixed; top: 1.5rem; left: 1.5rem; z-index: 9999; background: var(--crimson); color: var(--gold); border: 1px solid var(--gold-dim); padding: 0.6rem 1rem; font-size: 1rem; cursor: pointer; border-radius: 3px; font-family: Georgia, serif; transition: background 0.2s; }}
.sidebar-toggle:hover {{ background: var(--crimson-light); }}
.sidebar {{ position: fixed; top: 0; left: -360px; width: 360px; height: 100vh; background: var(--bg-dark); border-right: 2px solid var(--crimson); z-index: 9998; transition: left 0.3s ease; overflow-y: auto; padding: 4rem 1.5rem 2rem; }}
.sidebar.open {{ left: 0; }}
.sidebar-overlay {{ display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.6); z-index: 9997; }}
.sidebar-overlay.active {{ display: block; }}
.sidebar-close {{ position: absolute; top: 0.8rem; right: 1rem; font-size: 2rem; color: var(--gold); background: none; border: none; cursor: pointer; }}
.sidebar nav {{ display: flex; flex-direction: column; gap: 0.3rem; }}
.sidebar nav a {{ color: var(--text); text-decoration: none; padding: 0.4rem 0.5rem; border-bottom: 1px solid rgba(201,169,97,0.08); transition: color 0.2s, background 0.2s; font-size: 0.95rem; }}
.sidebar nav a:hover {{ color: var(--gold); background: rgba(139,26,26,0.15); }}
.sidebar nav a.act-link {{ font-weight: bold; color: var(--gold); margin-top: 0.5rem; padding-top: 0.6rem; border-bottom: 1px solid var(--gold-dim); }}
.sidebar nav a.scene-link {{ padding-left: 1.5rem; font-size: 0.85rem; color: var(--muted); }}
.sidebar nav a.scene-link:hover {{ color: var(--gold); }}
footer {{ max-width: 1400px; margin: 0 auto; padding: 2rem 1.5rem; color: var(--muted); font-size: 0.8rem; text-align: center; border-top: 1px solid var(--charcoal); }}
@media (max-width: 1100px) {{ .grid-4 {{ grid-template-columns: repeat(3, 1fr); }} }}
@media (max-width: 768px) {{ .grid-4 {{ grid-template-columns: repeat(2, 1fr); }} header {{ padding: 2.5rem 1rem 2rem; }} .scene-header {{ padding: 1rem; }} .sidebar {{ width: 300px; left: -300px; }} }}
@media (max-width: 480px) {{ .grid-4 {{ grid-template-columns: 1fr; }} }}
</style>
</head>
<body>
<button class="sidebar-toggle" id="sidebarToggle">☰ Navigate</button>
<div class="sidebar-overlay" id="sidebarOverlay"></div>
<aside class="sidebar" id="sidebar">
    <button class="sidebar-close" id="sidebarClose">×</button>
    <nav>{nav_html}</nav>
</aside>
<div class="lightbox" id="lightbox">
    <button class="lightbox-close" id="lightboxClose">×</button>
    <img id="lightboxImg" src="" alt="">
</div>
<header>
    <h1>The Duke's Obsession</h1>
    <div class="subtitle">A Gothic Dark Romance</div>
    <p class="logline">When an impoverished bookbinder's daughter is summoned to catalog the library of a reclusive, widowed Duke rumored to have killed his first wife, she discovers her name already written in his journals from ten years before she was born — and a contract offering her family's debts cleared in exchange for one winter as his Duchess in name only.</p>
    <span class="badge">{total} VISUAL ASSETS IN THIS BUILD</span>
</header>
<main>{body}</main>
<footer>
    <p>Generated from <code>images/refs/</code> and <code>images/act1–5/</code>. Re-run <code>build_gallery.py</code> after adding a batch.</p>
    <p><em>Theme: Love that feels like being claimed by winter — terrifying, consuming, and finally, chosen.</em></p>
</footer>
<script>
(function() {{
    var lightbox = document.getElementById('lightbox');
    var lbImg = document.getElementById('lightboxImg');
    document.querySelectorAll('.card img').forEach(function(img) {{
        img.style.cursor = 'pointer';
        img.addEventListener('click', function(e) {{
            e.stopPropagation();
            lbImg.src = this.src;
            lightbox.classList.add('active');
        }});
    }});
    document.getElementById('lightboxClose').addEventListener('click', function(e) {{
        e.stopPropagation();
        lightbox.classList.remove('active');
    }});
    lightbox.addEventListener('click', function() {{ lightbox.classList.remove('active'); }});
    lbImg.addEventListener('click', function(e) {{ e.stopPropagation(); }});
    var sidebar = document.getElementById('sidebar');
    var overlay = document.getElementById('sidebarOverlay');
    function openSidebar() {{ sidebar.classList.add('open'); overlay.classList.add('active'); }}
    function closeSidebar() {{ sidebar.classList.remove('open'); overlay.classList.remove('active'); }}
    document.getElementById('sidebarToggle').addEventListener('click', openSidebar);
    document.getElementById('sidebarClose').addEventListener('click', closeSidebar);
    overlay.addEventListener('click', closeSidebar);
    sidebar.querySelectorAll('a').forEach(function(link) {{ link.addEventListener('click', closeSidebar); }});
    document.addEventListener('keydown', function(e) {{
        if (e.key === 'Escape') {{ lightbox.classList.remove('active'); closeSidebar(); }}
    }});
}})();
</script>
</body>
</html>"""
    
    OUT.write_text(document, encoding="utf-8")
    size_mb = OUT.stat().st_size / (1024 * 1024)
    print(f"\n{'=' * 60}")
    print(f"✓ Wrote {OUT.name} ({size_mb:.1f} MB)")
    print(f"  Total images: {total}")
    print(f"  Character refs: {len(refs)}")
    for a in range(1, 6):
        print(f"  Act {a}: {len(acts[a])} images")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    build_gallery()
