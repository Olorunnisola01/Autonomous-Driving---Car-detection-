import re

S21_TEXT = """I returned to the gates. Not in the cloak he gave me — I had returned it. I wore my own forest-green dress, clean but worn, my satchel over my shoulder. I carried no contract. I carried nothing except myself. Mrs. Varma opened the gate without being asked. The Duke stood in the gravel drive, uncovered by hat or hood, snow catching in his too-long black hair. He had been waiting. He had always been waiting. I told him I did not come back for the contract. He said he knew. I said I came back because the alternative was a lifetime of listening for his footsteps and pretending I did not miss them."""

S22_TEXT = """His private chambers. High windows black with winter night, a fire low and amber. I stood before him. No contract between us now. No audience. No bargain. He removed his gloves slowly, finger by finger. His bare hands took my face as if I were a text he had been trying to read for a decade and had only now learned the language. He said say my name. I said Silas. He closed his eyes. It was the first time he had heard his own name spoken like a prayer."""

S23_TEXT = """A second ball — this one my choice. I entered on the Duke's arm, not as contract bride but as chosen Duchess. Julian watched from the crowd, his smile sharp enough to cut. Mrs. Varma stood at the door, and for the first time, she smiled. Lucy caught my eye from behind the refreshment table and mouthed: finally. The Duke led me to the center of the floor and did not let go. He whispered that they could stare, they could write it down, Julian could tell every version he liked. They would never be able to say he did not ask. I said he asked every day. I simply could not hear it until I was ready to answer."""

S24_TEXT = """A small village church, snow on the windowsills. Not a cathedral performance but a true thing. My father walked me down the aisle, his hands steadier than they had been in years. Lucy held the flowers. Mrs. Varma stood as witness for the house. Father Benedict spoke the words with a voice that cracked on the word join. The Duke's signet ring was warm against my finger as he slid it on — beside my brass thimble chain, beside the ink that would never wash out. I said I do. He said he always had."""

S25_TEXT = """Years later. The same library, but alive now — curtains drawn back, fire lit, books opened and scattered. I sat in the reading chair with a child balanced on my knee, pointing at gold lettering on a page. The Duke stood behind me, his hand on the chair's back, his signet ring catching light that fell through winter glass. The room smelled of old paper and beeswax and woodsmoke. The thorned rose crest was carved into the chair's armrest, but now it looked less like a warning and more like a welcome. I read aloud to the child: And the Duke kept his word. Every word. Every winter. Every one. The Duke said not every word. He told me once that he would survive without me. I said that was the only lie you ever told. The child laughed. The fire crackled."""

def update_scenes():
    with open('build_gallery.py', 'r', encoding='utf-8') as f:
        content = f.read()

    def replace_scene(scene_id, new_text, file_content):
        start_idx = file_content.find(f'("{scene_id}", ')
        if start_idx == -1:
            print(f"Warning: Start not found for {scene_id}")
            return file_content
            
        next_scene_num = int(scene_id[1:]) + 1
        next_scene_id = f"S{next_scene_num:02d}"
        end_idx = file_content.find(f'("{next_scene_id}", ')
        if end_idx == -1:
            print(f"Warning: End not found for {scene_id}")
            return file_content
            
        old_block = file_content[start_idx:end_idx]
        
        title_match = re.search(r'"([^"]+)",\s*"""', old_block)
        title = title_match.group(1) if title_match else "Unknown"
        
        end_match = re.search(r'""",\s*"([^"]+)",\s*(\d+)\),', old_block)
        location = end_match.group(1) if end_match else "UNKNOWN"
        act = end_match.group(2) if end_match else "1"
        
        new_block = f'("{scene_id}", "{title}", """{new_text}""", "{location}", {act}),\n    '
        
        return file_content[:start_idx] + new_block + file_content[end_idx:]

    content = replace_scene("S21", S21_TEXT, content)
    content = replace_scene("S22", S22_TEXT, content)
    content = replace_scene("S23", S23_TEXT, content)
    content = replace_scene("S24", S24_TEXT, content)
    content = replace_scene("S25", S25_TEXT, content)
    
    with open('build_gallery.py', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Updated S21-S25 voiceovers.")

if __name__ == "__main__":
    update_scenes()
