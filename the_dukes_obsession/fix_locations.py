"""Fix corrupted location fields in build_gallery.py."""
import re

# Map of scene IDs to correct locations
LOCATIONS = {
    "S01": "FINCH_BINDERY",
    "S02": "FINCH_BINDERY",
    "S03": "WINTER_ROAD",
    "S04": "BLACKTHORN_GATES",
    "S05": "BLACKTHORN_FOYER",
    "S06": "BLACKTHORN_LIBRARY",
    "S07": "BLACKTHORN_LIBRARY",
    "S08": "BLACKTHORN_LIBRARY",
    "S09": "BLACKTHORN_GALLERY",
    "S10": "BLACKTHORN_LIBRARY",
    "S11": "BLACKTHORN_STUDY",
    "S12": "BLACKTHORN_DINING_HALL",
    "S13": "BLACKTHORN_BALLROOM",
    "S14": "BLACKTHORN_STUDY",
    "S15": "BLACKTHORN_LIBRARY",
    "S16": "BLACKTHORN_STUDY",
    "S17": "BLACKTHORN_EAST_WING",
    "S18": "BLACKTHORN_GROUNDS",
    "S19": "BLACKTHORN_GATES",
    "S20": "VILLAGE_INN",
    "S21": "BLACKTHORN_GATES",
    "S22": "BLACKTHORN_CHAMBERS",
    "S23": "BLACKTHORN_BALLROOM",
    "S24": "VILLAGE_CHURCH",
    "S25": "BLACKTHORN_LIBRARY",
}

with open('build_gallery.py', 'r', encoding='utf-8') as f:
    content = f.read()

fixed = 0
for scene_id, correct_location in LOCATIONS.items():
    # Pattern: ("SXX", "Title", """...""", "UNKNOWN", ACT),
    pattern = rf'\("{scene_id}",\s*"[^"]*",\s*""".*?""",\s*"UNKNOWN"'
    
    def replacer(match):
        return match.group(0).replace('"UNKNOWN"', f'"{correct_location}"')
    
    new_content, n = re.subn(pattern, replacer, content, flags=re.DOTALL)
    if n > 0:
        content = new_content
        fixed += n
        print(f"  Fixed {scene_id} location: '{correct_location}'")
    else:
        print(f"  WARNING: Could not find {scene_id} with 'UNKNOWN' location")

with open('build_gallery.py', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nFixed {fixed} scene locations.")
remaining = content.count('"UNKNOWN"')
print(f"Remaining 'UNKNOWN' locations: {remaining}")
