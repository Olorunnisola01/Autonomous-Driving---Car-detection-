#!/usr/bin/env python3
"""Build storyboard gallery with header, sidebar, and full-resolution lightbox."""
import base64, io, random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "storyboard_gallery.html"
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".webp"}

SCENES = [
    ("S01", "The Father's Ultimatum", "The scene opens in the grand Adebayo mansion in Victoria Island, Lagos. Chief Adebayo sits behind his massive mahogany desk, his carved walking stick resting against his knee. His son Dele stands before him in faded mechanic's clothes. The weight of expectation fills the luxurious study.", "ADEBAYO_MANSION_VI", 1),
    ("S02", "Dele's Decision", "Dele drives across the Third Mainland Bridge at sunset. The Lagos skyline glitters behind him. He has made his choice — to leave his father's wealth behind and discover if any woman could love him for himself, not for the Adebayo fortune.", "THIRD_MAINLAND_BRIDGE", 1),
    ("S03", "The Mechanic's Shop", "A humble workshop in Surulere. Oil stains, old car parts, the smell of petrol and hard work. Dele's new home. He ties his mechanic's apron and picks up a wrench. For the first time in his life, he will work with his own hands.", "SURULERE_WORKSHOP", 1),
    ("S04", "The First Meeting", "Balogun Market at noon — a sea of color and noise. Ankara fabrics, shouting traders, the smell of suya. Chioma rushes through the crowd with her nurse's bag. She bumps into a stranger. Their eyes meet for the first time.", "BALOGUN_MARKET", 1),
    ("S05", "The Broken Car", "An expensive car has broken down on an Ikoyi street. Dele the mechanic is called to fix it. Chioma happens to be passing by. She watches this handsome stranger work with grease on his hands and kindness in his eyes.", "IKOYI_STREET", 1),
    ("S06", "Coffee at Mama's", "Chioma's small but warm house in Surulere. Mama Nkechi serves coffee and akara. Dele sits awkwardly on a plastic chair. The mother's wise eyes study him. She sees something in him that even he doesn't see yet.", "CHIIOMA_HOUSE_SURULERE", 1),
    ("S07", "The Hospital Shift", "Lagos University Teaching Hospital. Chioma in her nurse's uniform moves between patients with grace and compassion. Dele watches from the corridor, having come to bring her lunch. He sees her in her element — saving lives.", "LAGOS_UNIVERSITY_TEACHING_HOSPITAL", 1),
    ("S08", "Tunde's Warning", "A slick Victoria Island club. Tunde sips expensive whiskey and delivers his warning to Dele: Chioma will discover the truth, and when she does, she will never forgive the lie. Tunde's silver lighter flicks open and closed.", "Victoria_ISLAND_CLUB", 1),
    ("S09", "Sunset on the Bridge", "Third Mainland Bridge at golden hour. The lagoon stretches to the horizon. Dele and Chioma stand side by side, the city glittering below. He almost tells her the truth. Almost.", "THIRD_MAINLAND_BRIDGE_EVENING", 1),
    ("S10", "The Confession Almost", "Lekki Conservation Centre. Walking through the canopy walkway, surrounded by nature. Chioma laughs freely. Dele's heart is full. The words are on his lips — but fear stops him. Not yet.", "LEKKI_CONSERVATION_CENTRE", 1),
    ("S11", "The Charity Gala", "Eko Hotel ballroom glittering with Lagos high society. Dele has been summoned by his father. He must wear his true clothes — tailored agbada, gold embroidery, coral beads. He sees Chioma across the room. She sees him too.", "EKO_HOTEL_BALLROOM", 1),
    ("S12", "Iyeke's Entrance", "The ballroom doors open. Iyeke enters in a designer cream gown, diamond ring flashing. She is everything Dele's father wants for him — wealthy, polished, suitable. She walks toward him with a possessive smile.", "EKO_HOTEL_ENTRANCE", 1),
    ("S13", "The Truth Unravels", "Chioma confronts Dele in a quiet corner of the ballroom. The truth pours out — the mansion, the wealth, the disguise. Her face crumbles. The man she loved was real, but the lie was real too.", "EKO_HOTEL_BALLROOM", 1),
    ("S14", "Chioma's Heartbreak", "Surulere streets at night. Chioma walks alone, tears streaming. The mechanic she fell for was a billionaire's son. Everything she believed was built on deception. The Lagos night swallows her grief.", "SURULERE_STREET_NIGHT", 1),
    ("S15", "Tunde's Betrayal", "A Victoria Island restaurant. Tunde sits with Iyeke, plotting. He will help Iyeke win Dele, and in return, he will take a cut of the Adebayo fortune. Two vultures circling one heart.", "VICTORIA_ISLAND_RESTAURANT", 1),
    ("S16", "The Confrontation with Father", "The Adebayo mansion study. Dele stands before his father, no longer in disguise but in truth. Chief Adebayo's walking stick strikes the floor. 'You chose a common girl over your family name?' The words cut deeper than any blade.", "ADEBAYO_MANSION_STUDY", 1),
    ("S17", "Dele's Choice", "Pastor Emmanuel's small church in Surulere. Morning light through stained glass. Dele kneels in the empty pews. He prays for guidance. The answer comes not from heaven but from his own heart. He knows what he must do.", "PASTOR_EMMANUELS_CHURCH", 1),
    ("S18", "Chioma's Decision", "Chioma's house at dawn. Mama Nkechi watches her daughter pack a small bag. 'Where will you go, my child?' 'I need to think, Mama. I need to know what my heart truly wants.' The door closes softly.", "CHIIOMA_HOUSE_MORNING", 1),
    ("S19", "The Journey to Ibadan", "The Lagos-Ibadan expressway stretches ahead. Chioma in a commercial bus watches the city fade behind her. She is going to her grandmother's compound in Ibadan. She needs the wisdom of elders.", "LAGOS_IBADAN_EXPRESSWAY", 1),
    ("S20", "Grandmother's Wisdom", "An Ibadan compound with ancient walls and a mango tree. Chioma's grandmother grinds peppers and listens. 'A man who hides his wealth to find love is either a fool or a king. Which one is he, my child?'", "IBADAN_COMPOUND", 1),
    ("S21", "Dele's Proof", "The Surulere workshop rebuilt with Dele's own hands. No mansion, no agbada, no coral beads. Just a man, his tools, and honest work. He has sold his luxury cars. He has given away his watches. He has nothing but his truth.", "SURULERE_WORKSHOP_REBUILT", 1),
    ("S22", "The Apology", "Hospital gate at evening. Dele waits with a single flower. Chioma emerges from her shift, tired and wary. He doesn't speak of wealth. He speaks of regret. 'I was afraid you would love my money, not me. I was wrong.'", "HOSPITAL_GATE", 1),
    ("S23", "Mama Nkechi's Blessing", "Chioma's house evening. Mama Nkechi sits Dele down and pours palm wine. She studies him for a long time. Then she smiles. 'You have suffered enough for your lie. Now suffer for your love. Marry my daughter.'", "CHIIOMA_HOUSE_EVENING", 1),
    ("S24", "The Traditional Engagement", "The Adebayo compound transformed for ceremony. Ankara fabrics, talking drums, jollof rice in massive pots. Chief Adebayo in full regalia. Chioma's family in their finest. Two families becoming one. Coral beads exchanged.", "ADEBAYO_COMPOUND_CEREMONY", 1),
    ("S25", "The Wedding on the Beach", "Elegushi Beach at sunset. White lace and gold embroidery. Chioma radiant in her wedding gown. Dele in his finest agbada. The Atlantic ocean as witness. Lagos high society and Surulere neighbors side by side. Love wins.", "ELEGUSHI_BEACH_SUNSET", 1),
]

ACTS = {
    1: ("INHERITANCE", ["S01", "S02", "S03", "S04", "S05"]),
    2: ("OBSESSION", ["S06", "S07", "S08", "S09", "S10"]),
    3: ("THE BARGAIN", ["S11", "S12", "S13", "S14", "S15"]),
    4: ("RUIN", ["S16", "S17", "S18", "S19", "S20"]),
    5: ("DEVOTION", ["S21", "S22", "S23", "S24", "S25"]),
}

def inline_images(path, thumb_size=520, full_size=1200):
    with Image.open(path) as raw:
        image = ImageOps.exif_transpose(raw).convert("RGB")
        orig_w, orig_h = image.size
        
        thumb_h = int(thumb_size * 9 / 16)
        thumb_img = image.copy()
        thumb_img.thumbnail((thumb_size, thumb_h), Image.Resampling.LANCZOS)
        thumb_canvas = Image.new('RGB', (thumb_size, thumb_h), (17, 29, 36))
        thumb_canvas.paste(thumb_img, ((thumb_size-thumb_img.width)//2, (thumb_h-thumb_img.height)//2))
        thumb_buffer = io.BytesIO()
        thumb_canvas.save(thumb_buffer, format="JPEG", quality=75, optimize=True)
        thumb_b64 = base64.b64encode(thumb_buffer.getvalue()).decode("ascii")
        
        full_h = int(full_size * 9 / 16)
        full_img = image.copy()
        full_img.thumbnail((full_size, full_h), Image.Resampling.LANCZOS)
        full_canvas = Image.new('RGB', (full_size, full_h), (17, 29, 36))
        full_canvas.paste(full_img, ((full_size-full_img.width)//2, (full_h-full_img.height)//2))
        full_buffer = io.BytesIO()
        full_canvas.save(full_buffer, format="JPEG", quality=95, optimize=True)
        full_b64 = base64.b64encode(full_buffer.getvalue()).decode("ascii")
        
        return thumb_b64, full_b64, orig_w, orig_h

def image_files(folder):
    if not folder.exists(): return []
    return sorted((p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_EXT), key=lambda p: p.name)

def label_for(path):
    stem = path.stem
    if stem.endswith("_ref"):
        return stem[:-4].replace("_", " ").title() + " — CHARACTER REFERENCE"
    parts = stem.split("_")
    if len(parts) >= 2 and parts[0].startswith("S") and parts[1].startswith("Step"):
        return f"{parts[0]} — " + " ".join(parts[2:]).replace("_", " ").title()
    return stem.replace("_", " ").title()

def build_gallery():
    print("="*60)
    print("THE HIDDEN HEIR — Gallery Builder")
    print("="*60)
    
    scene_map = {s[0]: {"title": s[1], "voiceover": s[2], "location": s[3], "act": s[4]} for s in SCENES}
    refs = image_files(ROOT / "images" / "refs")
    acts = {a: image_files(ROOT / "images" / f"act{a}") for a in (1,2,3,4,5)}
    total = len(refs) + sum(len(f) for f in acts.values())
    print(f"\nImages: {total} total, {len(refs)} refs")
    
    print("Building HTML with professional white theme...")
    
    html = ['<!doctype html><html><head><meta charset="utf-8">']
    html.append('<title>The Duke\'s Obsession — Storyboard Gallery</title>')
    html.append('<style>')
    html.append('*{margin:0;padding:0;box-sizing:border-box;}')
    html.append('body{font-family:"Segoe UI",Tahoma,Geneva,Verdana,sans-serif;background:#f5f5f5;color:#333;line-height:1.6;}')
    html.append('header{background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);color:#fff;padding:3rem 2rem;text-align:center;box-shadow:0 2px 10px rgba(0,0,0,0.1);}')
    html.append('h1{font-size:2.5rem;margin-bottom:0.5rem;font-weight:300;letter-spacing:1px;}')
    html.append('.subtitle{font-size:1.1rem;opacity:0.9;margin-bottom:1rem;font-weight:300;}')
    html.append('.description{max-width:800px;margin:1rem auto;font-size:1rem;opacity:0.95;line-height:1.6;}')
    html.append('.badge{display:inline-block;padding:0.5rem 1.5rem;background:rgba(255,255,255,0.2);border:1px solid rgba(255,255,255,0.3);border-radius:20px;margin-top:1rem;font-size:0.9rem;}')
    html.append('.sidebar-toggle{position:fixed;top:1.5rem;left:1.5rem;z-index:9999;background:#fff;color:#667eea;border:none;padding:0.75rem 1.25rem;font-size:1rem;cursor:pointer;border-radius:25px;box-shadow:0 2px 10px rgba(0,0,0,0.1);font-family:inherit;transition:all 0.3s;}')
    html.append('.sidebar-toggle:hover{background:#667eea;color:#fff;transform:translateY(-2px);box-shadow:0 4px 15px rgba(102,126,234,0.4);}')
    html.append('.sidebar{position:fixed;top:0;left:-380px;width:380px;height:100vh;background:#fff;border-right:1px solid #e0e0e0;z-index:9998;transition:left 0.3s ease;overflow-y:auto;padding:5rem 1.5rem 2rem;box-shadow:2px 0 10px rgba(0,0,0,0.1);}')
    html.append('.sidebar.open{left:0;}')
    html.append('.sidebar-overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,0.5);z-index:9997;}')
    html.append('.sidebar-overlay.active{display:block;}')
    html.append('.sidebar-close{position:absolute;top:1rem;right:1rem;font-size:1.5rem;color:#666;background:none;border:none;cursor:pointer;width:32px;height:32px;border-radius:50%;transition:background 0.2s;}')
    html.append('.sidebar-close:hover{background:#f0f0f0;}')
    html.append('.sidebar nav{display:flex;flex-direction:column;gap:0.25rem;}')
    html.append('.sidebar nav a{color:#555;text-decoration:none;padding:0.6rem 0.75rem;border-radius:6px;transition:all 0.2s;font-size:0.95rem;}')
    html.append('.sidebar nav a:hover{background:#f0f0f0;color:#667eea;}')
    html.append('.sidebar nav a.act-link{font-weight:600;color:#667eea;margin-top:0.75rem;padding:0.75rem;background:#f8f9ff;border-radius:8px;}')
    html.append('.sidebar nav a.act-link:hover{background:#667eea;color:#fff;}')
    html.append('.sidebar nav a.scene-link{padding-left:1.75rem;font-size:0.9rem;color:#777;}')
    html.append('.sidebar nav a.scene-link:hover{color:#667eea;background:#f0f0f0;}')
    html.append('.container{max-width:1400px;margin:0 auto;padding:2rem;}')
    html.append('.act{margin:3rem 0;}')
    html.append('.act h2{color:#667eea;font-size:2rem;margin-bottom:1.5rem;padding-bottom:0.75rem;border-bottom:2px solid #667eea;font-weight:300;}')
    html.append('.scene{margin:2rem 0;padding:2rem;background:#fff;border-radius:12px;box-shadow:0 2px 10px rgba(0,0,0,0.05);border-left:4px solid #667eea;}')
    html.append('.scene h3{color:#333;font-size:1.5rem;margin-bottom:0.5rem;font-weight:500;}')
    html.append('.scene .location{color:#888;font-size:0.9rem;margin-bottom:1rem;text-transform:uppercase;letter-spacing:1px;}')
    html.append('.voiceover{font-style:italic;color:#555;margin:1.5rem 0;padding:1.5rem;background:#f8f9ff;border-left:3px solid #667eea;border-radius:4px;line-height:1.8;font-size:1.05rem;}')
    html.append('.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:1.5rem;margin-top:1.5rem;}')
    html.append('.card{cursor:pointer;transition:all 0.3s;background:#fff;border-radius:8px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,0.1);}')
    html.append('.card:hover{transform:translateY(-5px);box-shadow:0 8px 25px rgba(0,0,0,0.15);}')
    html.append('.card img{width:100%;height:auto;display:block;}')
    html.append('.card .label{padding:1rem;text-align:center;font-size:0.9rem;color:#555;font-weight:500;}')
    html.append('.lightbox{display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.9);z-index:1000;justify-content:center;align-items:center;}')
    html.append('.lightbox.active{display:flex;}')
    html.append('.lightbox img{max-width:95%;max-height:95%;object-fit:contain;border-radius:4px;}')
    html.append('.lightbox-close{position:absolute;top:20px;right:30px;font-size:2.5rem;color:#fff;cursor:pointer;background:rgba(255,255,255,0.1);border:none;width:50px;height:50px;border-radius:50%;transition:background 0.2s;}')
    html.append('.lightbox-close:hover{background:rgba(255,255,255,0.2);}')
    html.append('@media (max-width:768px){.container{padding:1rem;}.act{margin:2rem 0;}.scene{padding:1rem;}.grid{grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:1rem;}}')
    html.append('</style></head><body>')
    
    html.append('<button class="sidebar-toggle" onclick="toggleSidebar()">☰ Navigate</button>')
    html.append('<div class="sidebar-overlay" id="sidebar-overlay" onclick="toggleSidebar()"></div>')
    html.append('<aside class="sidebar" id="sidebar">')
    html.append('<button class="sidebar-close" onclick="toggleSidebar()">✕</button>')
    html.append('<nav>')
    html.append('<a href="#character-refs" style="font-weight:600;color:#667eea;">Character References</a>')
    for act_num in range(1, 6):
        act_name, scene_ids = ACTS[act_num]
        html.append(f'<a href="#act-{act_num}" class="act-link">Act {act_num} — {act_name}</a>')
        for scene_id in scene_ids:
            info = scene_map[scene_id]
            html.append(f'<a href="#{scene_id}" class="scene-link">{scene_id} — {info["title"]}</a>')
    html.append('</nav></aside>')
    
    html.append('<header>')
    html.append('<h1>The Duke\'s Obsession</h1>')
    html.append('<div class="subtitle">He hid his wealth to find her heart</div>')
    html.append('<p class="description">When an impoverished bookbinder\'s daughter is summoned to find a woman who loved him for his heart, not his money rumored to have killed his first wife, she discovers her name already written in his journals from ten years before she was born — and a contract offering her family\'s debts cleared in exchange for one winter as his Duchess in name only.</p>')
    html.append(f'<div class="badge">{total} images • Click thumbnails for full resolution</div>')
    html.append('</header>')
    
    html.append('<div class="container">')
    html.append('<div class="act" id="character-refs"><h2>Character References</h2><div class="grid">')
    for img_path in refs:
        thumb_b64, full_b64, orig_w, orig_h = inline_images(img_path)
        label = label_for(img_path)
        html.append(f'<div class="card" onclick="openLightbox(\'data:image/jpeg;base64,{full_b64}\')">')
        html.append(f'<img src="data:image/jpeg;base64,{thumb_b64}" alt="{label}">')
        html.append(f'<div class="label">{label}</div>')
        html.append('</div>')
    html.append('</div></div>')
    
    for act_num in range(1, 6):
        act_name, scene_ids = ACTS[act_num]
        html.append(f'<div class="act" id="act-{act_num}"><h2>Act {act_num} — {act_name}</h2>')
        
        for scene_id in scene_ids:
            info = scene_map[scene_id]
            html.append(f'<div class="scene" id="{scene_id}">')
            html.append(f'<h3>{scene_id} — {info["title"]}</h3>')
            html.append(f'<div class="location">{info["location"]}</div>')
            vo_html = info["voiceover"].replace('\n\n', '\n').replace('\n', '<br>')
            html.append(f'<div class="voiceover">{vo_html}</div>')
            html.append('<div class="grid">')
            
            scene_imgs = [p for p in acts[act_num] if p.name.startswith(f"{scene_id}_")]
            for img_path in scene_imgs:
                thumb_b64, full_b64, orig_w, orig_h = inline_images(img_path)
                label = label_for(img_path)
                html.append(f'<div class="card" onclick="openLightbox(\'data:image/jpeg;base64,{full_b64}\')">')
                html.append(f'<img src="data:image/jpeg;base64,{thumb_b64}" alt="{label}">')
                html.append(f'<div class="label">{label}</div>')
                html.append('</div>')
            
            html.append('</div></div>')
        
        html.append('</div>')
    
    html.append('</div>')  # close container
    
    html.append('<div class="lightbox" id="lightbox" onclick="closeLightbox()">')
    html.append('<button class="lightbox-close" onclick="closeLightbox()">&times;</button>')
    html.append('<img id="lightbox-img" src="" alt="Full resolution">')
    html.append('</div>')
    
    html.append('<script>')
    html.append('function openLightbox(src){document.getElementById("lightbox-img").src=src;document.getElementById("lightbox").classList.add("active");}')
    html.append('function closeLightbox(){document.getElementById("lightbox").classList.remove("active");}')
    html.append('function toggleSidebar(){document.getElementById("sidebar").classList.toggle("open");document.getElementById("sidebar-overlay").classList.toggle("active");}')
    html.append('document.addEventListener("keydown",function(e){if(e.key==="Escape"){closeLightbox();if(document.getElementById("sidebar").classList.contains("open"))toggleSidebar();}});')
    html.append('</script>')
    
    html.append('</body></html>')
    
    OUT.write_text('\n'.join(html))
    size_mb = OUT.stat().st_size / (1024*1024)
    print(f"\n✓ Wrote {OUT.name}")
    print(f"  Total images: {total}")
    print(f"  File size: {size_mb:.1f} MB")
    print(f"  Features: Header + Sidebar + Thumbnail grid (520px) + Full-resolution lightbox (1200×675)")
    print("="*60)

if __name__ == "__main__":
    build_gallery()
