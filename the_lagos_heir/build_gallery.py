#!/usr/bin/env python3
"""
Build storyboard gallery for The Hidden Heir movie project.
Generates HTML gallery showing all AI-generated images organized by act and scene.
"""

import os
from pathlib import Path
from collections import defaultdict

# Project structure
PROJECT_DIR = Path(__file__).parent
IMAGES_DIR = PROJECT_DIR / "images"
OUTPUT_FILE = PROJECT_DIR / "storyboard.html"

# Scene information
SCENES = {
    "S01": {"title": "The Father's Ultimatum", "act": 1},
    "S02": {"title": "Dele's Decision", "act": 1},
    "S03": {"title": "The Mechanic's Shop", "act": 1},
    "S04": {"title": "The First Meeting", "act": 1},
    "S05": {"title": "The Broken Car", "act": 1},
    "S06": {"title": "Coffee at Mama's", "act": 1},
    "S07": {"title": "The Hospital Shift", "act": 2},
    "S08": {"title": "Tunde's Warning", "act": 2},
    "S09": {"title": "Sunset on the Bridge", "act": 2},
    "S10": {"title": "The Confession Almost", "act": 2},
    "S11": {"title": "The Charity Gala", "act": 3},
    "S12": {"title": "Iyeke's Entrance", "act": 3},
    "S13": {"title": "The Truth Unravels", "act": 3},
    "S14": {"title": "Chioma's Heartbreak", "act": 3},
    "S15": {"title": "Tunde's Betrayal", "act": 3},
    "S16": {"title": "The Confrontation with Father", "act": 4},
    "S17": {"title": "Dele's Choice", "act": 4},
    "S18": {"title": "Chioma's Decision", "act": 4},
    "S19": {"title": "The Journey to Ibadan", "act": 4},
    "S20": {"title": "Grandmother's Wisdom", "act": 4},
    "S21": {"title": "Dele's Proof", "act": 5},
    "S22": {"title": "The Apology", "act": 5},
    "S23": {"title": "Mama Nkechi's Blessing", "act": 5},
    "S24": {"title": "The Traditional Engagement", "act": 5},
    "S25": {"title": "The Wedding on the Beach", "act": 5},
}

def get_all_images():
    """Scan images directory and organize by act and scene. Only includes images > 100KB (AI-generated)."""
    images = {
        'refs': [],
        'scenes': defaultdict(list)
    }
    
    # Character references
    refs_dir = IMAGES_DIR / "refs"
    if refs_dir.exists():
        for img in sorted(refs_dir.glob("*.png")):
            if img.stat().st_size > 100000:  # Only AI-generated images
                images['refs'].append(img)
    
    # Scene images
    for act_num in range(1, 6):
        act_dir = IMAGES_DIR / f"act{act_num}"
        if not act_dir.exists():
            continue
            
        for img in sorted(act_dir.glob("*.png")):
            if img.stat().st_size > 100000:  # Only AI-generated images
                # Extract scene ID from filename (e.g., S01_Step01_...)
                scene_id = img.stem.split('_')[0]
                if scene_id in SCENES:
                    images['scenes'][scene_id].append(img)
    
    return images

def generate_html(images):
    """Generate HTML gallery."""
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Hidden Heir - Storyboard Gallery</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
            padding: 20px;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
        }
        
        header {
            text-align: center;
            color: white;
            margin-bottom: 40px;
        }
        
        h1 {
            font-size: 3em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .subtitle {
            font-size: 1.3em;
            font-style: italic;
            opacity: 0.9;
        }
        
        .stats {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin-top: 20px;
            flex-wrap: wrap;
        }
        
        .stat-box {
            background: rgba(255,255,255,0.2);
            padding: 15px 25px;
            border-radius: 10px;
            backdrop-filter: blur(10px);
        }
        
        .stat-number {
            font-size: 2em;
            font-weight: bold;
        }
        
        .stat-label {
            font-size: 0.9em;
            opacity: 0.9;
        }
        
        .section {
            background: white;
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        
        h2 {
            color: #667eea;
            margin-bottom: 20px;
            font-size: 2em;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
        }
        
        h3 {
            color: #764ba2;
            margin: 20px 0 15px 0;
            font-size: 1.5em;
        }
        
        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
        }
        
        .image-card {
            background: #f8f9fa;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .image-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        }
        
        .image-card img {
            width: 100%;
            height: auto;
            display: block;
        }
        
        .image-caption {
            padding: 15px;
            font-size: 0.9em;
            color: #555;
        }
        
        .progress-bar {
            background: #e0e0e0;
            border-radius: 10px;
            overflow: hidden;
            margin: 20px 0;
        }
        
        .progress-fill {
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            height: 30px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: bold;
            transition: width 0.5s ease;
        }
        
        footer {
            text-align: center;
            color: white;
            margin-top: 40px;
            padding: 20px;
            opacity: 0.9;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🎬 The Hidden Heir</h1>
            <p class="subtitle">He hid his wealth to find her heart</p>
            <div class="stats">
"""
    
    # Calculate stats
    total_images = len(images['refs']) + sum(len(imgs) for imgs in images['scenes'].values())
    total_scenes = len(SCENES)
    completed_scenes = sum(1 for scene_imgs in images['scenes'].values() if len(scene_imgs) >= 10)
    
    html += f"""
                <div class="stat-box">
                    <div class="stat-number">{total_images}</div>
                    <div class="stat-label">Images Generated</div>
                </div>
                <div class="stat-box">
                    <div class="stat-number">{completed_scenes}/{total_scenes}</div>
                    <div class="stat-label">Scenes Complete</div>
                </div>
                <div class="stat-box">
                    <div class="stat-number">{len(images['refs'])}</div>
                    <div class="stat-label">Character Refs</div>
                </div>
            </div>
        </header>
        
        <div class="section">
            <h2>📊 Progress</h2>
            <div class="progress-bar">
                <div class="progress-fill" style="width: {completed_scenes/total_scenes*100:.0f}%">
                    {completed_scenes/total_scenes*100:.0f}% Complete
                </div>
            </div>
        </div>
        
        <div class="section">
            <h2>👥 Character References</h2>
            <div class="gallery">
"""
    
    # Character references
    for img in images['refs']:
        char_name = img.stem.replace('_ref', '').replace('_', ' ').title()
        html += f"""
                <div class="image-card">
                    <img src="{img.relative_to(PROJECT_DIR)}" alt="{char_name}">
                    <div class="image-caption">{char_name}</div>
                </div>
"""
    
    html += """
            </div>
        </div>
"""
    
    # Scene images by act
    for act_num in range(1, 6):
        act_scenes = {k: v for k, v in images['scenes'].items() if SCENES[k]['act'] == act_num}
        
        if act_scenes:
            html += f"""
        <div class="section">
            <h2>🎭 Act {act_num}</h2>
"""
            
            for scene_id in sorted(act_scenes.keys()):
                scene_info = SCENES[scene_id]
                scene_images = act_scenes[scene_id]
                
                html += f"""
            <h3>{scene_id}: {scene_info['title']}</h3>
            <div class="gallery">
"""
                
                for img in scene_images:
                    step_num = img.stem.split('_')[1]  # Step01, Step02, etc.
                    step_title = img.stem.split('_', 2)[2] if len(img.stem.split('_')) > 2 else ''
                    caption = f"{step_num.replace('Step', 'Step ')}{(' - ' + step_title) if step_title else ''}"
                    
                    html += f"""
                <div class="image-card">
                    <img src="{img.relative_to(PROJECT_DIR)}" alt="{scene_id} {step_num}">
                    <div class="image-caption">{caption}</div>
                </div>
"""
                
                html += """
            </div>
"""
            
            html += """
        </div>
"""
    
    html += """
        <footer>
            <p>🎬 The Hidden Heir - Storyboard Gallery</p>
            <p>Generated automatically as images are created</p>
        </footer>
    </div>
</body>
</html>
"""
    
    return html

def main():
    print("🎬 Building storyboard gallery...")
    
    # Scan images
    images = get_all_images()
    
    # Generate HTML
    html = generate_html(images)
    
    # Write to file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ Gallery built successfully: {OUTPUT_FILE}")
    print(f" Total images: {len(images['refs']) + sum(len(imgs) for imgs in images['scenes'].values())}")
    print(f"👥 Character refs: {len(images['refs'])}")
    print(f"🎬 Scenes with images: {len(images['scenes'])}")

if __name__ == "__main__":
    main()
