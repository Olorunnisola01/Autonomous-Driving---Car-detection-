#!/usr/bin/env python3
"""Generate AI images for all scenes using OpenAI API.

Reads prompts from prompts.json and generates images in batches.
Falls back to PIL placeholders if API key is missing.

Usage:
    python generate_images.py [--config movie_config.yaml] [--api-key OPENAI_KEY]
"""
import argparse
import json
import os
import random
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

try:
    from openai import OpenAI
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False


def load_config(path="movie_config.yaml"):
    if HAS_YAML and os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    return {}


def generate_placeholder(scene_id, step_num, width=1672, height=940, theme=None):
    """Generate a Gothic-themed placeholder image using PIL."""
    if not HAS_PIL:
        return None

    rng = random.Random(hash(f"{scene_id}_{step_num}"))

    # Gothic palettes based on theme
    if theme:
        palettes = [
            ((50, 10, 15), (100, 25, 30), (20, 5, 8)),
            ((15, 15, 25), (40, 40, 55), (8, 8, 15)),
            ((60, 15, 20), (90, 30, 35), (25, 5, 8)),
            ((30, 15, 35), (60, 35, 65), (15, 8, 18)),
            ((15, 25, 40), (35, 55, 70), (5, 10, 20)),
            ((45, 10, 10), (85, 20, 25), (18, 3, 5)),
        ]
    else:
        palettes = [
            ((40, 40, 40), (80, 80, 80), (20, 20, 20)),
            ((30, 50, 70), (60, 100, 140), (10, 20, 30)),
        ]

    dark, mid, darker = rng.choice(palettes)
    img = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(img)

    # Radial gradient
    cx, cy = width // 2, height // 2
    max_dist = ((width // 2) ** 2 + (height // 2) ** 2) ** 0.5

    for y in range(height):
        dy = (y - cy) / max_dist
        for x in range(0, width, 4):
            dx = (x - cx) / max_dist
            dist = min(1.0, (dx * dx + dy * dy) ** 0.5)
            r = int(mid[0] * (1 - dist) + darker[0] * dist)
            g = int(mid[1] * (1 - dist) + darker[1] * dist)
            b = int(mid[2] * (1 - dist) + darker[2] * dist)
            draw.rectangle([x, y, x + 4, y + 1], fill=(r, g, b))

    # Noise
    for _ in range(width * height // 200):
        x = rng.randint(0, width - 1)
        y = rng.randint(0, height - 1)
        v = rng.randint(0, 40)
        draw.point((x, y), fill=(v + 20, v + 15, v + 10))

    # Label
    label = f"{scene_id} — Step {step_num:02d}"
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
    except Exception:
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), label, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = (width - tw) // 2
    y = (height - th) // 2
    draw.text((x + 2, y + 2), label, fill=(0, 0, 0), font=font)
    draw.text((x, y), label, fill=(200, 180, 150), font=font)

    return img


def generate_with_openai(client, prompt, size="1792x1024", quality="hd", style="vivid"):
    """Generate an image using OpenAI DALL-E API."""
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            n=1,
            size=size,
            quality=quality,
            style=style,
        )
        return response.data[0].url
    except Exception as e:
        print(f"  API error: {e}")
        return None


def build_prompts_from_config(config):
    """Build image prompts from the config for all scenes."""
    theme = config.get("theme", {})
    acts = config.get("acts", [])
    chars = config.get("characters", [])
    visual = theme.get("visual_style", "")
    negative = theme.get("negative_prompt", "")

    prompts = []
    for act_idx, act in enumerate(acts):
        for scene_idx, scene in enumerate(act.get("scenes", []), 1):
            scene_id = f"S{act_idx * 5 + scene_idx:02d}"
            title = scene.get("title", "Untitled")
            location = scene.get("location", "Unknown")

            for step in range(1, 11):
                prompt = f"16:9 widescreen, {theme.get('genre', 'cinematic')}. {title}. Location: {location}. Visual style: {visual}. {negative}."
                prompts.append({
                    "scene_id": scene_id,
                    "step": step,
                    "prompt": prompt,
                    "act": act_idx + 1,
                })

    return prompts


def main():
    parser = argparse.ArgumentParser(description="Generate images for all scenes")
    parser.add_argument("--config", default="movie_config.yaml")
    parser.add_argument("--api-key", default=os.environ.get("OPENAI_API_KEY", ""))
    parser.add_argument("--output-dir", default="output/images")
    parser.add_argument("--placeholder-only", action="store_true", help="Generate placeholders only, no API calls")
    args = parser.parse_args()

    config = load_config(args.config)
    prompts = build_prompts_from_config(config)

    print(f"Total images to generate: {len(prompts)}")
    print(f"API key: {'present' if args.api_key else 'missing'}")
    print(f"Placeholder mode: {args.placeholder_only}")

    # Create output directories
    acts_count = len(config.get("acts", []))
    for act_num in range(1, acts_count + 1):
        act_dir = Path(args.output_dir) / f"act{act_num}"
        act_dir.mkdir(parents=True, exist_ok=True)

    ref_dir = Path(args.output_dir) / "refs"
    ref_dir.mkdir(parents=True, exist_ok=True)

    # Generate client if API key present
    client = None
    if args.api_key and HAS_OPENAI and not args.placeholder_only:
        client = OpenAI(api_key=args.api_key)

    # Generate character reference images
    for char in config.get("characters", []):
        ref_path = ref_dir / f"{char['id']}_ref.png"
        if ref_path.exists():
            continue
        print(f"Generating reference for {char['name']}...")
        img = generate_placeholder("REF", 0, theme=config.get("theme"))
        if img:
            img.save(ref_path)
            print(f"  Saved {ref_path}")

    # Generate scene images
    total = len(prompts)
    for i, p in enumerate(prompts):
        scene_id = p["scene_id"]
        step = p["step"]
        act_num = p["act"]
        filename = f"{scene_id}_Step{step:02d}.png"
        filepath = Path(args.output_dir) / f"act{act_num}" / filename

        if filepath.exists():
            continue

        if client:
            print(f"[{i+1}/{total}] Generating {scene_id} Step {step} via API...")
            url = generate_with_openai(client, p["prompt"])
            if url:
                import urllib.request
                urllib.request.urlretrieve(url, filepath)
                print(f"  Saved {filepath}")
        else:
            print(f"[{i+1}/{total}] Generating placeholder for {scene_id} Step {step}")
            img = generate_placeholder(scene_id, step, theme=config.get("theme"))
            if img:
                img.save(filepath)
                print(f"  Saved {filepath}")

    print(f"\nDone! Images saved to {args.output_dir}")


if __name__ == "__main__":
    main()
