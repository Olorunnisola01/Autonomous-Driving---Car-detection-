# 🎬 The Duke's Obsession — Storyboard Gallery

> *A Gothic Dark Romance*

##  Live Gallery

**GitHub Pages:** https://olorunnisola01.github.io/Autonomous-Driving---Car-detection-/the_dukes_obsession/

*(URL will update once GitHub Pages is enabled for this repo)*

---

## 📖 Story

When an impoverished bookbinder's daughter is summoned to catalog the library of a reclusive, widowed Duke rumored to have killed his first wife, she discovers her name already written in his journals from ten years before she was born — and a contract offering her family's debts cleared in exchange for one winter as his Duchess in name only.

**Theme:** Love that feels like being claimed by winter — terrifying, consuming, and finally, chosen.

---

## 🎞️ Gallery Stats

| Metric | Value |
|--------|-------|
| **Acts** | 5 |
| **Scenes** | 25 |
| **Images** | 258 (8 character refs + 250 scene steps) |
| **Voiceover** | ~70,000 characters (dialogue format) |
| **Gallery size** | 82.5 MB |
| **Format** | 16:9 widescreen, 1200×675 lightbox |

---

## 🚀 Reusable Movie Pipeline

This project includes a **reusable pipeline** for generating entire storyboard galleries from a single configuration file.

### Quick Start for New Movies

1. **Copy this folder** as your new project:
   ```bash
   cp -r the_dukes_obsession my_new_movie
   cd my_new_movie
   ```

2. **Edit `movie_config.yaml`** with your new movie idea:
   - Change title, genre, setting, mood
   - Add/remove characters
   - Define acts and scenes
   - Set voiceover style

3. **Run the pipeline** (choose one):

   **Option A — GitHub Actions (recommended):**
   - Go to Actions tab → "Movie Pipeline" → "Run workflow"
   - Select mode: `placeholder` (fast) or `api` (AI images)
   - Watch it auto-generate everything and deploy to GitHub Pages

   **Option B — Local Python:**
   ```bash
   pip install PyYAML Pillow openai
   python generate_screenplay.py
   python generate_images.py --placeholder-only
   python build_gallery.py
   ```

4. **View the gallery:**
   - Open `output/storyboard_gallery.html` in your browser
   - Or wait for GitHub Pages auto-deploy (usually 1-2 minutes)

---

## 📁 Project Structure

```
the_dukes_obsession/
├── movie_config.yaml              ← Your movie's configuration
├── SCREENPLAY.md                  ← Generated screenplay (with voiceovers)
├── generate_screenplay.py         ← Generates screenplay from config
├── generate_images.py             ← Generates images (API or placeholders)
├── build_gallery.py               ← Builds the HTML gallery
├── storyboard_gallery.html        ← Final gallery (82.5 MB)
├── S01_Step01_animated.mp4        ← Animated first scene (10s video)
├── animate_s01.py                 ← Animation script
├── .github/
│   └── workflows/
│       └── movie_pipeline.yml     ← GitHub Actions pipeline
└── images/
    ├── refs/                      ← Character reference portraits (8)
    ── act1/...act5/              ← Scene step images (250)
```

---

## 🎨 Voiceover Format

Each scene uses **multi-character dialogue** format:

```
[A = Narrator · B = Elara Finch · C = Duke Silas Blackthorn]

A: The foyer is a cavern of candelabras and damask.
B: He was not surprised to see me.
C: (from the upper gallery, in shadow)
B: He watched me the way one watches a door left ajar.
```

**Legend:**
- `A` = Narrator (always first, handles stage directions)
- `B` = Primary character (usually protagonist)
- `C`, `D`, `E`, `F` = Supporting characters in order of appearance

---

## 🛠️ Technical Details

### Gallery Features
- ✅ Professional white theme with purple/blue gradient header
- ✅ Collapsible sidebar navigation (☰ button)
- ✅ Thumbnail grid (520px, 16:9 contain)
- ✅ Full-resolution lightbox (1200×675)
- ✅ All images base64-inlined (works offline)
- ✅ Responsive design (mobile/tablet/desktop)
- ✅ 259 images total (8 character refs + 250 scene steps)

### Animation
- `animate_s01.py` creates cinematic videos with:
  - Candlelight flicker (multi-frequency oscillation)
  - Warm color pulse
  - Drifting dust mote particles
- Output: 1672×940 @ 24fps, H.264, ~19 MB

### GitHub Pages Deployment
The `.github/workflows/movie_pipeline.yml` workflow:
1. Reads `movie_config.yaml`
2. Generates screenplay with dialogue voiceovers
3. Generates all images (API or placeholders)
4. Builds HTML gallery
5. Deploys to GitHub Pages automatically

---

## 🎬 Creating New Movies

### Example: Nigerian Yoruba Drama

Edit `movie_config.yaml`:

```yaml
project:
  title: "The Royal Succession"
  tagline: "A Yoruba Family Drama"
  slug: "royal_succession"

theme:
  genre: "Nigerian Family Drama"
  setting: "Lagos mansion and village compound"
  mood: "political intrigue, family loyalty, tradition vs modernity"
  color_palette: "rich earth tones, gold, deep red, forest green"
  visual_style: "natural light, vibrant fabrics, bustling markets, ceremonial dress"

characters:
  - id: "ADEBAYO"
    name: "Chief Adebayo"
    role: "patriarch"
    age: 65
    description: "Distinguished Yoruba chief with silver-streaked beard, commanding presence"
    wardrobe: "traditional agbada in deep indigo, coral beads, ceremonial cap"
    object: "ivory staff of office"
  
  # ... add more characters

acts:
  - name: "THE SUMMONS"
    scenes:
      - title: "The Chief's Call"
        location: "LAGOS_MANSION"
      # ... more scenes
```

Then run the pipeline — it generates everything automatically.

---

## 💰 API Costs (Optional)

If you use OpenAI DALL-E for AI image generation:
- **DALL-E 3 HD (1792×1024):** ~$0.08 per image
- **250 images:** ~$20 total
- **Alternative:** Use placeholders (free, instant)

To use API:
1. Get API key from https://platform.openai.com/api-keys
2. Add as GitHub Secret: `OPENAI_API_KEY`
3. Run workflow with mode: `api`

---

## 📝 License

This project is a creative demonstration. Character names, dialogue, and story are fictional.

---

## 🙏 Credits

Built with:
- **Pillow** — Image generation and processing
- **imageio + ffmpeg** — Video animation
- **PyYAML** — Configuration parsing
- **OpenAI DALL-E** — AI image generation (optional)
- **GitHub Actions** — Automated pipeline
- **GitHub Pages** — Live deployment

---

## 🔧 Troubleshooting

### Gallery not loading?
- Check browser console for errors
- File is 82.5 MB — may take a moment to load on slow connections
- Try opening directly (not through GitHub viewer)

### GitHub Pages not deploying?
- Go to Settings → Pages → ensure source is "GitHub Actions"
- Check Actions tab for workflow errors
- First deploy may take 2-3 minutes

### Want to customize the theme?
- Edit CSS in `build_gallery.py` (search for `html.append('<style>')`)
- Change colors in the `:root` variables

---

## 📊 Project Timeline

| Phase | What Happened |
|-------|---------------|
| **Initial build** | 8 AI character refs + 250 scene images generated |
| **Voiceover expansion** | 70,000 characters of dialogue across 25 scenes |
| **Format conversion** | Monologue → multi-character dialogue (A/B/C format) |
| **Theme redesign** | Dark Gothic → professional white theme |
| **Animation** | S01 scene animated as 10s video with candlelight effects |
| **Pipeline automation** | GitHub Actions workflow for auto-generation |
| **Reusable config** | YAML-based system for creating new movies |

---

**Enjoy the gallery! 🎭**
