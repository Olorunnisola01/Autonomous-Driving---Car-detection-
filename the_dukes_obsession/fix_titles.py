"""Fix corrupted scene titles in build_gallery.py."""
import re

TITLES = {
    "S02": "The Summons Arrives",
    "S03": "The Road to Blackthorn",
    "S04": "The Gates of Blackthorn Hall",
    "S05": "The First Glimpse of Him",
    "S06": "The Library That Remembered",
    "S07": "The Journals with Her Name",
    "S08": "The Duke Watches",
    "S09": "The Gallery of Dead Wives",
    "S10": "The First Touch",
    "S11": "The Contract on the Desk",
    "S12": "The Fake Engagement",
    "S13": "The Jealousy at the Hunt Ball",
    "S14": "The Secret of the First Wife",
    "S15": "The Agreement",
    "S16": "The Betrayal",
    "S17": "The Fire in the East Wing",
    "S18": "She Tries to Flee",
    "S19": "He Lets Her Go",
    "S20": "The Distance Between",
    "S21": "The Return on Her Own Terms",
    "S22": "The Consummation",
    "S23": "The Public Claiming",
    "S24": "The Marriage",
}

with open('build_gallery.py', 'r', encoding='utf-8') as f:
    content = f.read()

fixed = 0
for scene_id, correct_title in TITLES.items():
    pattern = rf'\("{scene_id}",\s*"Unknown"'
    replacement = f'("{scene_id}", "{correct_title}"'
    new_content, n = re.subn(pattern, replacement, content)
    if n > 0:
        content = new_content
        fixed += n
        print(f"  Fixed {scene_id}: '{correct_title}'")
    else:
        print(f"  WARNING: Could not find '{scene_id}' with 'Unknown'")

with open('build_gallery.py', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nFixed {fixed} scene titles.")
remaining = content.count('"Unknown"')
print(f"Remaining 'Unknown' titles: {remaining}")
