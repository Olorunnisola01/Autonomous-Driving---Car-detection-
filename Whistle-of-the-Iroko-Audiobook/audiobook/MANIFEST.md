# 🎧 AUDIOBOOK MANIFEST — *The Whistle of the Iroko*

**Status:** IN PROGRESS · assembled so far: **Chapter 1 + trailer + 4 character reels**
**Story:** `../The-Whistle-of-the-Iroko.md` (~16,000 words · 10 chapters + epilogue)

---

## 1. VOICE MAP (kept identical across every turn for consistency)

| Role | Voice identity | Files |
|---|---|---|
| **Narrator / Chidinma** (26, journalist, 1st person) | feminine · narration · index 0 | `parts/Chapter-NN/narr-XX.mp3` |
| **Mama Nnenna** (78, grandmother) | feminine · characters · index 0 | `voices/mama-nnenna.mp3` ✅ |
| **Woman in Lace / Aunty Ifeoma** (50s, recruiter) | feminine · characters · index 1 | `voices/woman-in-lace.mp3` ✅ |
| **Chief Odogwu** (60s, villain) | masculine · characters · index 0 | `voices/odogwu.mp3` ⏳ *blocked once — retry next turn* |
| **Uncle Emeka** (father, troubled) | masculine · characters · index 1 | `voices/uncle-emeka.mp3` ✅ |
| **Nnamdi** (22, cousin) | masculine · characters · index 2 | ⏳ future |
| **Inspector Musa Adebayo** (40s, NAPTIP, scarred) | masculine · characters · index 3 | ⏳ future |
| **Ozo Igweoke** (elder, red cap) | masculine · characters · index 4 | ⏳ future |
| **Blessing / the girl from the bus** (17) | feminine · characters · index 2 | ⏳ future |
| **Ifeoma's confession** (graveside) | feminine · characters · index 1 | ⏳ future |

**Rule:** voice = (language `en`, gender, use_case, index). Never change these for a role.

---

## 2. CHAPTER STATUS

| # | Chapter | Narration clips | Assembled file | Time |
|---|---|---|---|---|
| 1 | The Call at 3:47 A.M. | 5/5 ✅ | `Chapter-01-The-Call-at-347-AM.mp3` | 5:20 |
| 2 | The Night Bus | ⏳ | — | — |
| 3 | The Compound | ⏳ | — | — |
| 4 | The Coffin That Would Not Stay Closed | ⏳ | — | — |
| 5 | The Diary | ⏳ | — | — |
| 6 | Whispers and Whistles | ⏳ | — | — |
| 7 | The Man With the Scar | ⏳ | — | — |
| 8 | The Mission House | ⏳ | — | — |
| 9 | The Funeral | ⏳ | — | — |
| 10 | The Keeper's Eulogy | ⏳ | — | — |
| E | Epilogue: Dawn | ⏳ | — | — |

## 3. EXTRAS

| Item | File | Time |
|---|---|---|
| Movie trailer (narrator VO) | `../Whistle-of-the-Iroko-Trailer.mp3` | 0:32 |
| Cover art | `../The-Whistle-of-the-Iroko-Cover.png` | — |
| Movie adaptation pack | `../Movie-Adaptation-Pack.md` | — |

## 4. PIPELINE (per chapter)

1. Split chapter text into ≤1400-char sentence chunks (Python).
2. Generate each chunk as `parts/Chapter-NN/narr-XX.mp3` — narrator voice.
3. Generate 1–2 character reels per turn (voices map above).
4. Assemble: `python3 assemble.py "Chapter-NN-....mp3" 0.7 parts/Chapter-NN/narr-*.mp3`
   (concats with 0.7 s pauses, loudness-normalized to -16 LUFS, mono 44.1 kHz MP3).

## 5. TURN LOG

- **Turn 1 (2026-08-05):** 10/10 speech slots used → Ch.1 narration (5 clips) + Mama Nnenna, Woman in Lace, Uncle Emeka reels + trailer. Odogwu reel **blocked by moderation** (graphic threats) → softened rewrite ready, **retry first slot next turn**. ffmpeg installed via `imageio-ffmpeg` (apt had no candidate).

## 6. NEXT TURN TODO

1. Retry `voices/odogwu.mp3` (softened text) — feminine/masculine slots free.
2. Chapter 2 — The Night Bus (~2,400 words → ~7 narration clips + woman-in-lace scene + scarred-man teaser).
3. Continue chapter-by-chapter until Epilogue. ~7 more narration turns expected (45–55 min total runtime).

---

## 7. LOCKED PRODUCTION PLAN (2026-08-05, user-approved)

**Narrator voice:** feminine · educational · index 3 (= audition "Option 7", the slowest natural voice in the pool)
**Speed:** atempo **0.70** (maximum slow) — applied at assembly time to every narration chunk
**Pauses:** narration recorded in **short ~450-char sentence-aligned chunks** (`split_chapter.py`), assembled with **1.8 s gaps** between chunks for a heavy, cinematic read
**Pipeline:** `split_chapter.py N` → generate `parts/Chapter-NN/narr-XX.mp3` (narrator voice) → assemble with atempo 0.70 + 1.8 s gaps
**Chapter 1 must be RE-RECORDED** with the new voice (15 chunks) and re-assembled to replace the old 5:20 version.
**Auditions:** `auditions/` — reels 1–4 (options 1–20). Option 7 = `opt-G-edu3.mp3`.

## 8. TURN LOG UPDATE

- **Turn 3:** Auditioned 20 narrator options across use_cases (narration/educational/entertainment/conversational, indices 0–9). Slowest natural = Option 7 (edu idx 3, 19.20 s for the demo passage). User chose **maximum slow: Option 7 @ 70% + pauses**. Built `split_chapter.py`; Ch1 = 15 chunks, Ch2 = 24, Epilogue = 15.
