#!/usr/bin/env python3
"""Generate SCREENPLAY.md from movie_config.yaml.

This script reads the YAML config and produces a complete screenplay
with character bible, scene breakdowns, and multi-character dialogue
voiceovers for every scene.

Usage:
    python generate_screenplay.py [--config movie_config.yaml]
"""
import argparse
import os
import re
import yaml
from pathlib import Path


def load_config(path="movie_config.yaml"):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def build_character_bible(config):
    """Generate the Character Bible section."""
    lines = []
    for char in config.get("characters", []):
        lines.append(f"### @{char['id']} — {char['name']}")
        lines.append(f"Age {char.get('age', '?')}; {char.get('role', 'character')}.")
        lines.append(char.get("description", ""))
        lines.append(f"**Wardrobe:** {char.get('wardrobe', '')}")
        lines.append(f"**Object:** {char.get('object', '')}")
        lines.append(f"**Personality:** {char.get('personality', '')}")
        lines.append("")
    return "\n".join(lines)


def build_dialogue_for_scene(scene_title, location, characters, vo_config):
    """Generate a multi-character dialogue voiceover for a scene.

    Returns a string formatted with character codes (A=Narrator, B=Elara, etc.)
    """
    narrator_letter = vo_config.get("narrator_letter", "A")
    pov = vo_config.get("pov_character", "Elara")

    # Map first non-narrator character to B, second to C, etc.
    actor_letters = {}
    letter_idx = 1  # Start at B
    for char in characters:
        char_id = char["id"]
        actor_letters[char_id] = chr(ord("B") + letter_idx - 1)
        letter_idx += 1

    return narrator_letter, actor_letters


def generate_scene_voiceover(scene, config, act_index):
    """Generate dialogue-style voiceover for a single scene."""
    chars = config.get("characters", [])
    vo = config.get("voiceover", {})
    narrator = vo.get("narrator_letter", "A")

    # Determine which characters appear in this scene
    # Simple heuristic: early acts use first few characters, later acts use more
    num_chars = min(len(chars), 3 + act_index // 2)
    active_chars = chars[:num_chars]

    # Build legend
    legend_parts = [f"{narrator} = Narrator"]
    letter_map = {}
    idx = 1
    for char in active_chars[1:] if active_chars[0].get("role") == "protagonist" else active_chars:
        letter = chr(ord("B") + idx - 1)
        letter_map[char["id"]] = letter
        legend_parts.append(f"{letter} = {char['name']}")
        idx += 1

    # If protagonist not mapped yet, assign B
    if "ELARA_FINCH" not in letter_map and active_chars:
        for char in active_chars:
            if char.get("role") == "protagonist":
                letter_map[char["id"]] = "B"
                legend_parts.append(f"B = {char['name']}")
                break

    legend = " · ".join(legend_parts)

    # Generate dialogue based on scene position in act
    scene_num = scene.get("_num", 1)
    title = scene["title"]

    # Simple templated dialogue based on scene archetype
    dialogues = {
        "opening": f"""{narrator}: The scene opens on {scene.get('location', 'the setting')}. {title} begins here.

B: I've been expecting this moment.

C: Then you know what must be done.

{narrator}: The weight of the moment settles between them like dust in still air.

B: I know.

{narrator}: And yet neither of them moves. The silence says what words cannot.""",

        "confrontation": f"""{narrator}: The confrontation arrives like a storm that has been building for weeks.

B: You knew. You knew all along.

C: I knew enough.

B: That's not the same thing and you know it.

{narrator}: The space between them crackles with unspoken accusation.

C: What do you want me to say?

B: The truth. Just once. The truth.""",

        "revelation": f"""{narrator}: The truth arrives not with drama, but with the quiet finality of a door closing.

B: All this time — you never told me.

C: There was nothing to tell.

B: There was everything to tell.

{narrator}: The revelation hangs in the air between them, fragile as glass.

C: And now that you know?

B: Now I understand why you kept it from me.

{narrator}: But understanding and forgiveness are different rooms, and she has not yet found the door.""",

        "resolution": f"""{narrator}: In the end, it is not the grand gesture but the small one that matters.

B: I came back.

C: I know.

B: Not because I had to.

C: I know that too.

{narrator}: The space between them has changed. Something has shifted that cannot be unshifted.

B: Then what now?

C: Now we begin.""",

        "default": f"""{narrator}: The scene unfolds in {scene.get('location', 'the setting')}.

{narrator}: {title}. The weight of what has come before presses on this moment.

B: I didn't expect to find you here.

C: I didn't expect you to come.

{narrator}: A pause. The kind that contains more than words.

B: We need to talk.

C: I know.

{narrator}: And so they begin."""
    }

    # Choose dialogue template based on scene number
    if scene_num == 1:
        dialogue = dialogues["opening"]
    elif scene_num == 3:
        dialogue = dialogues["revelation"]
    elif scene_num == 5:
        dialogue = dialogues["resolution"]
    elif "betrayal" in title.lower() or "secret" in title.lower():
        dialogue = dialogues["confrontation"]
    else:
        dialogue = dialogues["default"]

    return f"[{legend}]\n\n{dialogue}"


def generate_screenplay(config):
    """Generate the complete SCREENPLAY.md from config."""
    project = config.get("project", {})
    theme = config.get("theme", {})
    story = config.get("story", {})
    acts = config.get("acts", [])
    chars = config.get("characters", [])
    vo = config.get("voiceover", {})

    # Header
    md = []
    md.append(f"# {project.get('title', 'Untitled')}")
    md.append("")
    md.append(f"*{project.get('tagline', '')}*")
    md.append("")
    md.append("## Logline")
    md.append("")
    md.append("*(Auto-generated — customize in movie_config.yaml)*")
    md.append("")
    md.append("## Character Bible")
    md.append("")
    md.append(build_character_bible(config))
    md.append("## Screenplay")
    md.append("")

    # Generate each act
    for act_idx, act in enumerate(acts):
        act_name = act.get("name", f"ACT {act_idx + 1}")
        md.append(f"### ACT {act_idx + 1} — {act_name}")
        md.append("")

        for scene_idx, scene in enumerate(act.get("scenes", []), 1):
            scene_id = f"S{act_idx * 5 + scene_idx:02d}"
            scene["_num"] = scene_idx
            title = scene.get("title", f"Scene {scene_idx}")
            location = scene.get("location", "UNKNOWN")

            md.append(f"## {scene_id} — {title}")
            md.append("")
            md.append(f"**Location:** `{location}`")
            md.append("")

            # Generate dialogue voiceover
            vo_text = generate_scene_voiceover(scene, config, act_idx)
            md.append(f"**VOICEOVER:**")
            md.append("")
            md.append(vo_text)
            md.append("")

    return "\n".join(md)


def main():
    parser = argparse.ArgumentParser(description="Generate screenplay from config")
    parser.add_argument("--config", default="movie_config.yaml", help="Path to YAML config")
    parser.add_argument("--output", default="SCREENPLAY.md", help="Output file")
    args = parser.parse_args()

    if not os.path.exists(args.config):
        print(f"Config file not found: {args.config}")
        print("Create movie_config.yaml based on the template in the_dukes_obsession/")
        return

    print(f"Loading config from {args.config}...")
    config = load_config(args.config)

    print(f"Generating screenplay: {config['project']['title']}")
    screenplay = generate_screenplay(config)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(screenplay)

    print(f"✓ Wrote {args.output}")
    print(f"  Acts: {len(config.get('acts', []))}")
    total_scenes = sum(len(a.get("scenes", [])) for a in config.get("acts", []))
    print(f"  Scenes: {total_scenes}")
    print(f"  Characters: {len(config.get('characters', []))}")


if __name__ == "__main__":
    main()
