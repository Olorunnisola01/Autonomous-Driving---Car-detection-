#!/usr/bin/env python3
"""Create a self-contained storyboard gallery for The Duke's Obsession.

Features:
- Character References section
- 5 Acts with scene headers and Voiceover blocks
- 10 step cards per scene in 16:9 contain tiles
- Click-to-popup lightbox
- Collapsible sidebar with full navigation
- All images base64-inlined for offline viewing
"""

import base64
import html
import io
import random
import struct
import zlib
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "storyboard_gallery.html"
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}

# ── Scene data ──────────────────────────────────────────────────────────
SCENES = [
    ("S01", "The Debt That Breathes",
     "I learned to count debts the way other girls counted stitches — by candlelight, by the tremor in my father's hands, by the silence that grew thicker than the leather we bound. The workshop smelled of old paper and desperation. Every creditor notice on the wall was another winter we might not survive. I told him we could sell the Chaucer. He said Mother loved it. I said it was worth more alive than dead. We both knew I was lying. Some things, once sold, cannot be bought back.",
     "FINCH_BINDERY", 1),
    ("S02", "The Summons Arrives",
     "The letter came under the door like a thief — black wax, black seal, the thorned rose pressed into it like a brand. I broke it open before I understood what I was opening. They wanted a bookbinder's daughter at Blackthorn Hall. Payment enough to clear every debt, every notice, every whisper of ruin. My father's eyes went wide when I read it aloud. Not with hope. With recognition. He said the Duke knew his name. I said not his name. Someone else's. The question sat between us like a third person in the room.",
     "FINCH_BINDERY", 1),
    ("S03", "The Road to Blackthorn",
     "The road stretched ahead of me like a warning written in frost. Every hedgerow was skeletal, every breath a small white ghost that vanished before I could name it. I walked alone with my satchel of binding tools and the weight of a decision I hadn't fully made. The milestone appeared suddenly — carved with a thorned rose, ancient and deliberate. I knew then that every story about that house ended the same way. He did it. She vanished. No one agreed on how. They all agreed it happened. I pulled my cloak tighter and kept walking.",
     "WINTER_ROAD", 1),
    ("S04", "The Gates of Blackthorn Hall",
     "The gates were taller than a man and twisted into thorned vines, black iron against a grey sky that seemed to press down on everything below it. Mrs. Varma waited in the gateway like a sentinel carved from shadow and silk. She did not smile. She did not welcome. She measured me with one look that took in my ink-stained hands and my worn boots and found something acceptable, or at least tolerable. She said I would sleep in the east wing. Not the upper corridor. The Duke does not receive callers. He receives people who answer letters. I asked what the difference was. She did not answer.",
     "BLACKTHORN_GATES", 1),
    ("S05", "The First Glimpse of Him",
     "The foyer was a cavern of candelabras and damask, every shadow longer than it should be. I removed my gloves and tried not to think about the ink still staining my fingertips. Then I looked up. He stood in the upper gallery, half-consumed by darkness, watching me with the patience of a man who had been waiting for a very long time. He did not descend. He did not speak. He simply watched, then turned and disappeared. I whispered to the empty hall that he was not surprised to see me. The echo agreed.",
     "BLACKTHORN_FOYER", 1),
    ("S06", "The Library That Remembered",
     "Two stories of shelves bowed under the weight of centuries. Dust motes hung motionless in slanting winter light. A fireplace large enough to stand in held cold ashes and the memory of warmer years. I set down my satchel and exhaled — the first full breath I had taken since arriving. This room was alive with knowledge. I touched a spine and felt something like recognition. Mrs. Varma said the late Duchess had arranged everything by feeling, not subject. I asked how long that took her to understand. She said ten years. She never did.",
     "BLACKTHORN_LIBRARY", 2),
    ("S07", "The Journals with Her Name",
     "The journals were leather-bound and cracked with age, each one a small coffin of secrets. I opened one dated thirteen years ago and began to catalogue, to organize, to make order from chaos. Then I found it — my own name. Elara Finch. Written in elegant copperplate in a margin note beside a passage on the binding of psalters. The date was ten years before I was born. My fingers trembled. I read the entry again. The ink was old. The handwriting was deliberate. This was not a coincidence. He knew. Before I existed. He wrote me down.",
     "BLACKTHORN_LIBRARY", 2),
    ("S08", "The Duke Watches",
     "Candlelight. Late. I worked without knowing he was there, without knowing I was being watched. He stood in the doorway's shadow, observing as I carefully lifted a page with a bone folder, as if I were performing surgery on something alive. He did not announce himself. I sensed him the way animals sense a storm — in the air pressure, in the sudden stillness that precedes violence or tenderness. When I turned, he was already gone. Only the scent of cold wool and smoke remained. I whispered that he was always there, just behind the edge of seeing.",
     "BLACKTHORN_LIBRARY", 2),
    ("S09", "The Gallery of Dead Wives",
     "The corridor of portraits stretched longer than I expected, each face watching me with painted eyes that never blinked. Lucy showed me the house by stolen candlelight, her breath fogging in the cold. We stopped before a painting of Lady Margaret — white satin gown, pearl choker, emerald pendant at her throat. The eyes were dark and knowing. Lucy said they claimed the Duke locked himself in here for a year after she died. I asked how she died. Lucy said that was the question no one answered twice the same way. I looked at my own reflection in the gilt frame and did not like the comparison.",
     "BLACKTHORN_GALLERY", 2),
    ("S10", "The First Touch",
     "I fell asleep at the reading desk, a book open against my cheek, unaware of the figure who entered silently. He stood over me, his shadow falling across the page. His gloved hand reached down — not to shake me, not to wake me, but to brush a stray auburn curl from my forehead. His finger grazed my temple. I stirred. Our eyes met across the smallest distance. Neither moved. The candle between us guttered. His voice, when it came, was barely audible. You are exactly as I wrote you. I did not know whether to be terrified or flattered. Perhaps both.",
     "BLACKTHORN_LIBRARY", 2),
    ("S11", "The Contract on the Desk",
     "A desk of black oak. A single document. He stood behind it, hands braced on the wood, signet ring catching the firelight. The contract read: all Finch family debts cleared, father's workshop preserved, in exchange for one winter as his Duchess. In name, in public, in residence. No conjugal obligation. No permanent arrangement. I could leave at spring thaw. I asked him why me. He said because I was always the answer. He simply had to wait for the question to arrive. I did not know whether to believe him or run.",
     "BLACKTHORN_STUDY", 3),
    ("S12", "The Fake Engagement",
     "A long table set for two, though the house held twenty. Mrs. Varma stood behind my chair, adjusting my collar with proprietary hands. Lucy peeked from the serving doorway, wide-eyed. The Duke took his seat and did not look at me until I was settled, then held my gaze with an intensity that made the candlelight seem dim. He said I would call him Silas in private. In public, I would call him Your Grace and allow no one to see me smile first. I asked what would happen if I smiled first. He said he would spend the evening making it worth the scandal.",
     "BLACKTHORN_DINING_HALL", 3),
    ("S13", "The Jealousy at the Hunt Ball",
     "The ballroom glittered with candlelight and crystalline pretense, the local gentry dressed in jewels and calculated indifference. Julian appeared in burgundy velvet, claiming me for a dance with the ease of a man who had never been refused. His hand settled at my waist. Across the room, the Duke watched, a glass of brandy untouched in his hand. Julian asked why I was trembling. I said his cousin's moods were not a difficult text. Julian smiled and said, Then why are you trembling? The Duke crossed the room. He did not dance. He took my hand from Julian's waist and placed it on his own coat.",
     "BLACKTHORN_BALLROOM", 3),
    ("S14", "The Secret of the First Wife",
     "I found the locked drawer and forced it open with a bone folder. Inside: letters from Lady Margaret's brother describing his sister's slow poisoning, and a doctor's note that the Duke refused an autopsy. I confronted him. He did not deny the letters. He said they were incomplete. I asked if he killed her. He said she asked him to let her go and he held on too tightly. That was the closest thing to murder he had committed. I asked what about me. A long silence. The fire popped. He said I was the only thing he had ever been afraid to hold.",
     "BLACKTHORN_STUDY", 3),
    ("S15", "The Agreement",
     "Winter light turned the library gold. I stood by the window, the contract in my hands. He waited by the fireplace, still as a portrait. I had read every clause. I had found the escape clause: I could leave at spring, with my father's debts cleared, no conditions. I folded the document slowly. I told him I would stay the winter. Not because of the debt. Because I needed to know if what he wrote in those journals was true, or if I was just the woman who looked enough like a ghost to fill the space. He crossed the room and stopped exactly one arm's length from me. He said I was never a ghost. I was the only living thing he could imagine in this house.",
     "BLACKTHORN_LIBRARY", 3),
    ("S16", "The Betrayal",
     "Julian found me alone and smiled like a man who enjoyed delivering poison. He revealed that the Duke's journals contained entries not about love — but about ownership. He had been watching me since I was a child, arranging circumstances to bring me here. Julian showed me a page: the Duke purchased my father's debt from the original creditor three years ago. I was never summoned — I was harvested. Julian said I was not a bride. I was a collection. The Duke entered. He did not deny it.",
     "BLACKTHORN_STUDY", 4),
    ("S17", "The Fire in the East Wing",
     "My room. I had packed my satchel. The smell of smoke seeped under the door before I understood what it meant. The east wing corridor filled with orange light. Lucy screamed from the stairwell. Mrs. Varma appeared, pressing a key into my hand — a servants' exit. She said go, now, do not look for him. Lucy said the fire started in the gallery, the portraits were burning. I ran through smoke, the key cold in my palm, and did not look at the burning gallery where Lady Margaret's portrait turned to ash.",
     "BLACKTHORN_EAST_WING", 4),
    ("S18", "She Tries to Flee",
     "I stumbled through snow beyond the grounds, my green dress stained with soot, my brass thimble swinging against my collarbone. The frost bit through my boots. I had gone perhaps a mile when I realized I had been walking in a circle — the frost showed my own footprints ahead of me. The grounds of Blackthorn were larger than I understood. Or something was keeping me contained. I stopped. My breath came in white clouds. I was alone. I was lost. I was furious. I whispered that I would not be the ghost, I would not be the collection, I would not be the thing he wrote.",
     "BLACKTHORN_GROUNDS", 4),
    ("S19", "He Lets Her Go",
     "The iron gates. I reached them at first light, exhausted, smoke-stained. The Duke stood on the other side. He had a horse saddled, a traveling cloak folded over its back, a letter of transit in his hand. He had not come to stop me. He had come to arm me. He said he bought the debt because he could not bear the thought of me starving while he did nothing. He said he did not arrange me. He waited for me. There was a difference and he knew it did not excuse anything. He opened the gate. He said go. If I returned, it must be because I chose to. Not because I had nowhere else.",
     "BLACKTHORN_GATES", 4),
    ("S20", "The Distance Between",
     "A village inn. I sat by a fire, wrapped in the traveling cloak the Duke gave me though I had tried to return it. Father Benedict brought me tea and sat without invitation. He had known the Duke for decades. He had known grief. He said the Duke came to him after Margaret died and asked how to stop loving what he could not save. I asked what he chose. Father Benedict said he chose to wait. For ten years, he chose to wait. That was not obsession, child. That was the only patience he had ever seen that deserved to be called love.",
     "VILLAGE_INN", 4),
    ("S21", "The Return on Her Own Terms",
     "I returned to the gates. Not in the cloak he gave me — I had returned it. I wore my own forest-green dress, clean but worn, my satchel over my shoulder. I carried no contract. I carried nothing except myself. Mrs. Varma opened the gate without being asked. The Duke stood in the gravel drive, uncovered by hat or hood, snow catching in his too-long black hair. He had been waiting. He had always been waiting. I told him I did not come back for the contract. He said he knew. I said I came back because the alternative was a lifetime of listening for his footsteps and pretending I did not miss them.",
     "BLACKTHORN_GATES", 5),
    ("S22", "The Consummation",
     "His private chambers. High windows black with winter night, a fire low and amber. I stood before him. No contract between us now. No audience. No bargain. He removed his gloves slowly, finger by finger. His bare hands took my face as if I were a text he had been trying to read for a decade and had only now learned the language. He said say my name. I said Silas. He closed his eyes. It was the first time he had heard his own name spoken like a prayer.",
     "BLACKTHORN_CHAMBERS", 5),
    ("S23", "The Public Claiming",
     "A second ball — this one my choice. I entered on the Duke's arm, not as contract bride but as chosen Duchess. Julian watched from the crowd, his smile sharp enough to cut. Mrs. Varma stood at the door, and for the first time, she smiled. Lucy caught my eye from behind the refreshment table and mouthed: finally. The Duke led me to the center of the floor and did not let go. He whispered that they could stare, they could write it down, Julian could tell every version he liked. They would never be able to say he did not ask. I said he asked every day. I simply could not hear it until I was ready to answer.",
     "BLACKTHORN_BALLROOM", 5),
    ("S24", "The Marriage",
     "A small village church, snow on the windowsills. Not a cathedral performance but a true thing. My father walked me down the aisle, his hands steadier than they had been in years. Lucy held the flowers. Mrs. Varma stood as witness for the house. Father Benedict spoke the words with a voice that cracked on the word join. The Duke's signet ring was warm against my finger as he slid it on — beside my brass thimble chain, beside the ink that would never wash out. I said I do. He said he always had.",
     "VILLAGE_CHURCH", 5),
    ("S25", "The True Duchess",
     "Years later. The same library, but alive now — curtains drawn back, fire lit, books opened and scattered. I sat in the reading chair with a child balanced on my knee, pointing at gold lettering on a page. The Duke stood behind me, his hand on the chair's back, his signet ring catching light that fell through winter glass. The room smelled of old paper and beeswax and woodsmoke. The thorned rose crest was carved into the chair's armrest, but now it looked less like a warning and more like a welcome. I read aloud to the child: And the Duke kept his word. Every word. Every winter. Every one. The Duke said not every word. He told me once that he would survive without me. I said that was the only lie he ever told. The child laughed. The fire crackled.",
     "BLACKTHORN_LIBRARY", 5),
]

# Step descriptions (underscores for filenames)
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
    "S12": ["long_table_for_two", "mrs_varma_adjusts_collar", "lucy_peeks_doorway", "duke_takes_seat", "intense_gaze", "candlelight_dim", "call_me_silas", "your_grace_in_public", "smile_first_question", "worth_the_scandal"],
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

# ── Placeholder image generation ──────────────────────────────────────
def create_placeholder_image(scene_id: str, step_num: int, width: int = 960, height: int = 540) -> Image.Image:
    """Create a Gothic-themed placeholder image with gradient and label."""
    rng = random.Random(hash(f"{scene_id}_{step_num}"))
    
    # Gothic palettes
    palettes = [
        ((50, 10, 15), (100, 25, 30), (20, 5, 8)),
        ((15, 15, 25), (40, 40, 55), (8, 8, 15)),
        ((60, 15, 20), (90, 30, 35), (25, 5, 8)),
        ((30, 15, 35), (60, 35, 65), (15, 8, 18)),
        ((15, 25, 40), (35, 55, 70), (5, 10, 20)),
        ((45, 10, 10), (85, 20, 25), (18, 3, 5)),
    ]
    palette = rng.choice(palettes)
    dark, mid, darker = palette
    
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    
    # Horizontal line-based gradient (fast)
    cx, cy = width // 2, height // 2
    max_dist = ((width // 2) ** 2 + (height // 2) ** 2) ** 0.5
    
    for y in range(height):
        dy = (y - cy) / max_dist if max_dist > 0 else 0
        for x in range(0, width, 4):
            dx = (x - cx) / max_dist if max_dist > 0 else 0
            dist = min(1.0, (dx * dx + dy * dy) ** 0.5)
            r = int(mid[0] * (1 - dist) + darker[0] * dist)
            g = int(mid[1] * (1 - dist) + darker[1] * dist)
            b = int(mid[2] * (1 - dist) + darker[2] * dist)
            draw.rectangle([x, y, x + 4, y + 1], fill=(r, g, b))
    
    # Subtle noise
    for _ in range(width * height // 200):
        x = rng.randint(0, width - 1)
        y = rng.randint(0, height - 1)
        v = rng.randint(0, 40)
        draw.point((x, y), fill=(v + 20, v + 15, v + 10))
    
    # Vignette overlay
    for y in range(0, height, 2):
        for x in range(0, width, 4):
            dx = (x - cx) / (width / 2)
            dy = (y - cy) / (height / 2)
            vignette = max(0, min(1, (dx * dx + dy * dy) ** 0.5 * 0.7))
            if vignette > 0.4:
                alpha = int(min(255, (vignette - 0.4) * 200))
                r, g, b = img.getpixel((x, y))
                r = max(0, r - alpha // 3)
                g = max(0, g - alpha // 3)
                b = max(0, b - alpha // 3)
                draw.rectangle([x, y, x + 4, y + 2], fill=(r, g, b))
    
    # Label
    step_desc = STEP_DESCRIPTIONS.get(scene_id, [f"step_{i}" for i in range(10)])[step_num - 1]
    label = f"{scene_id} — Step {step_num:02d}"
    
