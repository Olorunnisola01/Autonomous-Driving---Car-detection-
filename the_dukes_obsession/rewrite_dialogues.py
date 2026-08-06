#!/usr/bin/env python3
"""Rewrite all 25 scenes as multi-character dialogue with legend headers."""
import re

DIALOGUES = {
"S01": {
    "legend": "A = Elara Finch (bookbinder's daughter) · B = Thomas Finch (her father) · Z = Narrator",
    "text": """Z: The bindery smells of old paper and desperation. Every creditor notice on the wall is another winter we might not survive.
A: We can sell the Chaucer, Father. It has the brass clasps.
B: Your mother loved that one.
A: Then it is worth more alive than dead.
Z: He sets down his needle. His hands are worse than yesterday.
B: They will not wait forever, Elara.
A: Who will not?
B: The men whose names are on those walls. Hemsworth. Gable. The chandler.
A: I know their names. I count them every morning.
B: And what do they count, when they look at us?
A: Debts. They count debts.
Z: The candle gutters. Outside, the wind howls through the bare elms.
B: I was a bookbinder once. Before the cough took your mother. Before the medicine.
A: I know, Father.
B: Now I am a man who cannot hold a needle.
A: You can still teach me. Your hands remember what your fingers no longer can.
Z: He looks at her — the auburn hair, the ink-stained fingertips, the face of a girl who has aged ten years in three.
B: You have her hands. Your mother's hands.
A: I know.
B: Do you know what that means?
A: It means I can finish the vicar's Bible. It means we eat tomorrow.
B: It means you will have to decide, sooner than either of us would like, what we keep and what we let go.
A: I have already decided, Father. We keep the Chaucer.
Z: She says it gently. But the candle is dying, and the walls are papered in notices, and the night is very long."""
},
"S02": {
    "legend": "A = Elara Finch · B = Thomas Finch · Z = Narrator",
    "text": """Z: The letter slides under the door like a thief. Black wax. Black seal. A thorned rose pressed into it like a brand.
A: Father — a letter.
B: From whom?
Z: She breaks the seal. The parchment is thick, expensive.
A: It is from Blackthorn Hall.
Z: His face changes. Not hope. Something older.
B: Read it.
A: "To Mr. Thomas Finch. It has come to our attention that your daughter, Elara Finch, possesses skills in the art of bookbinding that may be of service to the Duke of Blackthorn. The Duke requires a cataloguer for his library. Compensation shall be provided upon completion, sufficient to satisfy all outstanding obligations."
Z: Silence. The clock ticks.
B: He knows my name.
A: Whose name?
B: The Duke. He knows my name.
A: How is that possible?
B: I do not know. I do not know.
A: I will go.
B: No.
A: I have to.
B: You do not understand what you are walking into.
A: I understand we are drowning.
B: It is not safe.
A: Neither is starving.
Z: She folds the letter. It is heavy, like a stone. Like a sentence."""
},
"S03": {
    "legend": "A = Elara Finch · Z = Narrator",
    "text": """Z: The road stretches ahead, written in frost. Every hedgerow is skeletal. Every breath a small white ghost.
A: Every story about that house ends the same way. He did it. She vanished. No one agrees on how. They all agreed it happened.
Z: She pulls her cloak tighter. The milestone appears — carved with a thorned rose, ancient and deliberate.
A: I am close.
Z: The wind keens through the hedgerows. Turn back, it seems to say.
A: I cannot turn back. The debt is too great. The ruin too complete.
Z: Her boots crunch on the frozen ground. The village is a grey smudge behind her.
A: I am a bookbinder's daughter. I am a keeper of stories. I am a mender of broken things.
Z: The trees grow thicker. The light grows dimmer. The road becomes a tunnel of black wood.
A: Even if I cannot mend this. Even if I cannot save us. Even if I am walking into the dark.
Z: She keeps walking. One foot. Then the other. The rhythm becomes a kind of prayer."""
},
"S04": {
    "legend": "A = Elara Finch · B = Mrs. Varma (the housekeeper) · Z = Narrator",
    "text": """Z: The gates are taller than a man. Twisted into thorned vines. Black iron against a grey sky that seems to press down on everything.
B: You will sleep in the east wing.
A: And the upper corridor?
B: Do not use it.
A: Why not?
Z: She does not answer. She measures Elara with one look — ink-stained hands, worn boots, the nervous set of the shoulders.
B: The Duke does not receive callers. He receives people who answer letters.
A: What is the difference?
Z: The gates groan open. The sound is iron grinding against iron.
B: You will find your room at the end of the east corridor. Dinner is at eight. Do not be late.
A: When do I begin the library?
B: The Duke will summon you when he is ready. Until then, you stay in your room.
A: May I ask —
B: You may ask nothing. Not yet.
Z: She turns. Her black silk dress whispers against the stone path. The house looms ahead, dark stone, windows like empty eyes.
A: I have walked into a mouth.
Z: The gravel is pale, almost white. Like crushed bone."""
},
"S05": {
    "legend": "A = Elara Finch · B = Duke Silas Blackthorn · Z = Narrator",
    "text": """Z: The foyer is a cavern of candelabras and damask. Every shadow is longer than it should be.
A: He was not surprised to see me.
Z: She whispers it to the empty hall. The echo agrees.
B: (from the upper gallery, in shadow)
Z: He stands half-consumed by darkness. He has been waiting a very long time.
A: Your Grace?
Z: He does not descend. He does not speak.
B: (still silent)
A: I know you are there.
Z: The candle between them gutters. Then he turns. Then he disappears.
A: He watched me the way one watches a door left ajar. Patient. Intent. As if he had been waiting for a very long time.
Z: The hall is empty now. But the air still holds the weight of him — cold wool, smoke, something metallic and sharp.
A: He knew I was coming.
Z: The clock ticks. Somewhere deep in the house, a door closes."""
},
"S06": {
    "legend": "A = Elara Finch · B = Mrs. Varma · Z = Narrator",
    "text": """Z: Two stories of shelves bow under the weight of centuries. Dust motes hang motionless in slanting winter light.
A: I set down my satchel and exhale. The first full breath since arriving.
B: She arranged it by feeling, not subject. The late Duchess.
A: How long did that take you to understand?
B: Ten years. I never did.
A: She touched the spines. Leather. Vellum. Gold leaf. Each book a small resurrection.
B: You will disturb nothing until you understand her order.
A: And if I cannot understand it?
B: Then you will leave it as it is. Some things are not meant to be catalogued.
Z: The fireplace is large enough to stand in. It holds cold ashes.
A: This room is alive.
B: It is waiting. There is a difference.
Z: She runs her hand along a shelf. Her fingers tingle. Something like recognition."""
},
"S07": {
    "legend": "A = Elara Finch · Z = Narrator",
    "text": """Z: The journals are leather-bound and cracked with age. Each one a small coffin of secrets.
A: Thirteen years ago. A margin note. Beside a passage on the binding of psalters.
Z: Her fingers tremble. She reads the entry again.
A: Elara Finch. Written in elegant copperplate. The date is ten years before I was born.
Z: The ink is old. The handwriting is deliberate.
A: This was not a coincidence.
Z: She closes the journal. Her breath comes shallow.
A: He knew. Before I existed. He wrote me down.
Z: The library is very quiet. The candles have burned low.
A: Who writes a name into a book that does not yet exist? Who binds a story before the heroine is born?
Z: Somewhere in the house, a door opens. Then closes. Then silence."""
},
"S08": {
    "legend": "A = Elara Finch · B = Duke Silas Blackthorn · Z = Narrator",
    "text": """Z: Candlelight. Late. She works without knowing he is there.
A: The air has changed. The pressure. The stillness.
Z: He stands in the doorway's shadow. Observing.
A: He was watching me lift the page. As if I were performing surgery on something alive.
Z: She turns.
B: (already gone)
A: Only the scent of cold wool and smoke remains.
Z: The candle between them has guttered. The page she was reading lies open.
A: He is always there. Just behind the edge of seeing.
Z: She touches the spot on the desk where his shadow fell. The leather is warm.
A: He was here. He was standing here. And then he was not.
Z: The house settles. A timber creaks. Somewhere deep in Blackthorn, a clock strikes two."""
},
"S09": {
    "legend": "A = Elara Finch · B = Lucy (the maid) · Z = Narrator",
    "text": """Z: The corridor of portraits stretches longer than expected. Each face watches with painted eyes that never blink.
B: They say he locked himself in here for a year after she died.
A: How did she die?
B: That is the question no one answers twice the same way.
Z: Lucy's candle flickers. They stop before a painting — white satin, pearl choker, emerald pendant.
A: Lady Margaret.
B: She was beautiful. In a cold way.
A: Her eyes — they look right through me.
Z: Elara sees her own reflection in the gilt frame, superimposed over the painted face. The auburn hair. The pale skin. The wide eyes.
B: You look like her.
A: I know.
B: That is why you should not be here.
A: Then why am I here?
B: That is the question you should be asking.
Z: The portrait's emerald pendant catches the candlelight. It gleams. It warns."""
},
"S10": {
    "legend": "A = Elara Finch · B = Duke Silas Blackthorn · Z = Narrator",
    "text": """Z: She fell asleep at the reading desk. A book open against her cheek.
B: (enters silently)
Z: His gloved hand reaches down. Not to shake her. Not to wake her.
B: (brushes a stray auburn curl from her forehead. His finger grazes her temple.)
Z: She stirs. Their eyes meet across the smallest distance. Neither moves.
B: You are exactly as I wrote you.
Z: His voice is barely audible. The candle between them gutters.
A: I did not know whether to be terrified or flattered.
B: Perhaps both.
Z: He steps back. The shadows reclaim him.
A: He touched me as if I were a text he had been trying to read for a decade.
Z: The library is silent again. But the air is different now. Warmer. Charged.
A: He knows my name. He has known my name. And I — I am only now beginning to understand what that means."""
},
"S11": {
    "legend": "A = Elara Finch · B = Duke Silas Blackthorn · Z = Narrator",
    "text": """Z: A desk of black oak. A single document.
B: (hands braced on the wood, signet ring catching the firelight)
A: All Finch family debts cleared. Father's workshop preserved. In exchange for one winter as your Duchess.
B: In name. In public. In residence. No conjugal obligation. No permanent arrangement.
A: I may leave at spring thaw.
B: You may.
A: Why me?
B: Because you were always the answer.
A: Always?
B: I simply had to wait for the question to arrive.
Z: She reads the contract again. The words are clean. Legal. Final.
A: There is no trapdoor here.
B: There is no trapdoor. Only a door. And it opens in one direction.
A: And if I do not sign?
B: Then the door closes. And the creditors come. And the bindery is lost.
Z: She looks at him. His dark charcoal eyes are steady. Patient.
A: I did not know whether to believe him or run.
Z: So she stood there. And she did neither."""
},
"S12": {
    "legend": "A = Elara Finch · B = Duke Silas Blackthorn · C = Mrs. Varma · D = Lucy · Z = Narrator",
    "text": """Z: A long table set for two, though the house holds twenty.
C: (adjusts Elara's collar with proprietary hands)
D: (peeks from the serving doorway, wide-eyed)
B: (takes his seat. Does not look at her until she is settled. Then holds her gaze.)
B: You will call me Silas in private.
A: And in public?
B: Your Grace. Allow no one to see you smile first.
A: And if I smile first?
B: Then I will spend the evening making it worth the scandal.
Z: The candlelight between them makes the rest of the hall seem to fall away.
C: (steps back, satisfied)
D: (disappears into the shadows)
A: You have rules for everything.
B: I have rules for the things that matter.
A: And what matters?
B: That no one sees you smile first. That you look at me when I speak. That you do not speak to Julian Fox without my knowledge.
A: Julian Fox?
B: My cousin. You will meet him. You will not like him. That is as it should be.
Z: The servants bring the first course. The wine is poured. The silence is a third presence at the table.
A: I did not know whether he was threatening me or promising me something.
B: Perhaps both.
Z: He raised his glass. She did not raise hers. Not yet."""
},
"S13": {
    "legend": "A = Elara Finch · B = Duke Silas Blackthorn · C = Julian Fox (the Duke's cousin) · Z = Narrator",
    "text": """Z: The ballroom glittered. A thousand candles in crystal chandeliers. The local gentry in jewels and calculated indifference.
C: My dear Duchess. May I claim the first dance?
A: Before I could answer, his hand was at my waist.
C: You are trembling.
A: Your cousin's moods are not a difficult text.
C: Then why are you trembling, Elara?
Z: He used my name the way a man uses a blade he has tested.
B: (across the room. A glass of brandy untouched. Knuckles white.)
A: He was not dancing. He was performing for someone else.
Z: The Duke crossed the room. The crowd parted for him the way water parts for something heavier than itself.
C: Ah. The master of the house.
B: (does not speak to Julian. Simply takes Elara's hand from his waist and places it against his own coat, over his heart.)
Z: The room understood. And Elara understood. And Julian understood.
B: I did not ask you to dance.
A: I know.
B: I simply did not let go.
Z: The music began again. He did not let go."""
},
"S14": {
    "legend": "A = Elara Finch · B = Duke Silas Blackthorn · Z = Narrator",
    "text": """Z: The locked drawer. The bone folder. The splintered wood.
A: Letters from Lady Margaret's brother. Describing his sister's slow poisoning.
Z: She read them all. Twice. Then she sat in the Duke's chair and waited.
B: (enters at midnight)
A: You found them.
B: I found them.
A: Did you kill her?
Z: Long silence. The fire popped.
B: The letters are incomplete.
A: Are they?
B: She asked me to let her go.
A: Let her go?
B: She was ill. Not the illness they described. That was the medicine, the laudanum, the physician's incompetence. She was ill in a way that had no name.
A: And you —
B: I held on too tightly. That is the closest thing to murder I have ever committed.
A: And me? What about me?
Z: The silence was long enough that she heard the house settling.
B: I am afraid of you.
A: Afraid?
B: You are the only thing I have ever been afraid to hold.
Z: The candlelight guttered. And she did not know whether to rise and leave or stay and be destroyed."""
},
"S15": {
    "legend": "A = Elara Finch · B = Duke Silas Blackthorn · Z = Narrator",
    "text": """Z: Winter light turned the library gold.
A: I stood by the window. The contract in my hands.
B: (by the fireplace. Still as a portrait.)
A: I found the escape clause. I can leave at spring. The debts are cleared. No conditions.
B: I wrote it that way.
A: I will stay the winter.
B: —
A: Not because of the debt. Not because of the contract. Because I need to know if what you wrote in those journals was true.
B: And if it was not?
A: Then I am just the woman who looked enough like a ghost to fill the space she left behind.
Z: He crossed the room. Stopped exactly one arm's length from her.
B: You were never a ghost.
A: Then what was I?
B: The only living thing I could imagine in this house.
Z: The winter sun caught the edge of the contract and made it glow. And for the first time, she did not feel like a woman who had come to sell herself. She felt like a woman who had come to be found."""
},
"S16": {
    "legend": "A = Elara Finch · B = Julian Fox · C = Duke Silas Blackthorn · Z = Narrator",
    "text": """Z: Julian found her in the gallery. He always found her when she was alone.
B: You look lost, cousin.
A: I am looking at your family.
B: Our family. Or it will be, if my cousin has his way. Have you read the rest of the journals? Not the ones with your name in the margin. The others.
A: The ones he wrote about me before he knew I existed.
B: That winter — 1844 — three creditors called on your father in a single week. Do you remember?
A: I remember the winter of the blue hands.
B: Your father's debts were purchased. All of them. By a single buyer. The same buyer who, three years later, sent the letter summoning you here.
A: I was never summoned.
B: You were harvested. My cousin does not collect books. He collects people.
Z: Footsteps. The Duke stood in the doorway.
C: (does not deny it)
A: It was not a marriage. It was not a bargain. It was a possession that had begun before I was born.
Z: And she was only now, too late, learning its true name."""
},
"S17": {
    "legend": "A = Elara Finch · B = Lucy · C = Mrs. Varma · Z = Narrator",
    "text": """Z: Smoke. Thin at first. Then thickening. Crawling under the door.
A: (packed satchel at her feet)
Z: The corridor outside lit with flickering orange. Wallpaper curling. Blackening.
B: (from the stairwell, a short sharp scream)
A: (ran)
Z: Mrs. Varma met her on the landing. Not panicked. Not hurried. But her face — open, in a way Elara had never seen.
C: (pressed a key into her hand. Heavy. Cold. Iron.)
C: The servants' door. Through the kitchens. Down the back stairs. Do not stop. Do not look back.
A: What about —
C: Do not look for him.
Z: Lucy appeared behind her, coughing, face streaked with soot.
B: The gallery. The fire started in the gallery. The portraits — they're all —
Z: She did not finish. She did not need to.
A: (did not look at the gallery. Did not look at the room where the Duke had stood and not denied it.)
Z: She ran through the kitchens, through the servants' door, into the cold.
A: Until the house was a shape of fire against the winter sky. Until Lady Margaret's portrait was ash. Until she was finally, truly, alone."""
},
"S18": {
    "legend": "A = Elara Finch · Z = Narrator",
    "text": """Z: The snow came up past her ankles. Then her calves. Then her knees.
A: (brass thimble swinging against her collarbone with each stride)
Z: She walked for what felt like an hour. Then she saw them.
A: Footprints. My own footprints. Ahead of me.
Z: She turned slowly. The house was behind her again. The same orange glow. The same distance.
A: I had walked for an hour and I had not moved at all.
Z: The grounds of Blackthorn were larger than she understood. Or something was keeping her contained.
A: I will not be the ghost.
Z: Her voice sounded strange. Thin. Like something that belonged to someone else.
A: I will not be the collection. I will not be the thing he wrote.
Z: The snow fell. The house burned. And she stood in the circle of her own footprints.
A: There is only one direction left to walk. Back."""
},
"S19": {
    "legend": "A = Elara Finch · B = Duke Silas Blackthorn · Z = Narrator",
    "text": """Z: The iron gates stood open. The gravel drive held a single figure.
B: (on the outside. A saddled horse behind him. A folded travelling cloak on its back. A letter of transit in his gloved hand.)
B: You came back.
A: I had nowhere else to go.
B: I know.
Z: He stepped aside. The gate stood open.
B: I bought your father's debt because I could not bear the thought of you starving while I did nothing.
A: —
B: I did not arrange you. I waited for you. There is a difference, and I know it does not excuse anything.
A: (looked at him. He looked at her.)
B: Go.
Z: He stepped back. He did not follow. He did not call after her.
B: If you return, it must be because you chose to. Not because you had nowhere else.
A: (took the cloak. Took the letter. Did not take the horse.)
Z: She walked through the gate. The gravel crunched. The road opened ahead.
A: I knew I would return. Not because I had nowhere else. Because there was nowhere else I wanted to be."""
},
"S20": {
    "legend": "A = Elara Finch · B = Father Benedict (the vicar) · Z = Narrator",
    "text": """Z: The inn was called the Black Swan. Halfway between the life she had left and the life she was walking toward.
B: (did not ask permission to sit. Placed his leather-bound prayer book on the table between them.)
B: I have known Silas Blackthorn for thirty years. I married him to Margaret. I buried her.
A: —
B: He came to me the night she died. He stood in my study and said, "Tell me how to stop loving what I could not save."
A: What did you tell him?
B: I told him there is no stopping. Only choosing.
A: What did he choose?
B: He chose to wait. For ten years, he chose to wait.
A: And that is not obsession?
B: That is the only patience I have ever seen that deserved to be called love.
Z: Father Benedict closed his prayer book.
B: You choose. As he chose. As she chose. As every person in this story has chosen, rightly or wrongly, for as long as it has been telling itself.
Z: He stood. He left the prayer book on the table. He walked out into the night.
A: (sat by the fire, wrapped in a cloak she had not asked for, and chose.)"""
},
"S21": {
    "legend": "A = Elara Finch · B = Duke Silas Blackthorn · C = Mrs. Varma · Z = Narrator",
    "text": """Z: She returned to the gates. Not in the cloak he gave her. She had returned it.
C: (opened the gate without being asked)
A: (in her own forest-green dress. Clean but worn. Satchel over her shoulder. No contract. Only herself.)
Z: The Duke stood in the gravel drive. Uncovered by hat or hood. Snow catching in his too-long black hair.
B: (had been waiting. Had always been waiting.)
A: I did not come back for the contract.
B: I know.
A: I came back because the alternative was a lifetime of listening for your footsteps and pretending I did not miss them.
Z: The snow fell between them. The manor stood dark and silent behind him.
B: (did not speak. Did not need to.)
A: (stepped through the gate. And the gate closed behind her. And she was home.)"""
},
"S22": {
    "legend": "A = Elara Finch · B = Duke Silas Blackthorn · Z = Narrator",
    "text": """Z: His private chambers. High windows black with winter night. Fire low and amber.
A: (stood before him. No contract. No audience. No bargain.)
B: (removed his gloves slowly. Finger by finger.)
Z: His bare hands took her face. As if she were a text he had been trying to read for a decade and had only now learned the language.
B: Say my name.
A: Silas.
Z: He closed his eyes.
B: It was the first time he had heard his own name spoken like a prayer.
A: (and the fire crackled, and the winter pressed against the windows, and the house held them in its old dark hands.)"""
},
"S23": {
    "legend": "A = Elara Finch · B = Duke Silas Blackthorn · C = Julian Fox · D = Mrs. Varma · E = Lucy · Z = Narrator",
    "text": """Z: A second ball. This one her choice.
A: (entered on the Duke's arm. Not as contract bride. As chosen Duchess.)
C: (watched from the crowd. Smile sharp enough to cut.)
D: (stood at the door. And for the first time, she smiled.)
E: (caught Elara's eye from behind the refreshment table. Mouthed: finally.)
Z: The Duke led her to the center of the floor.
B: Let them stare. Let them write it down. Julian can tell every version he likes. They will never be able to say I did not ask.
A: You asked every day.
B: —
A: I simply could not hear it until I was ready to answer.
Z: He did not let go. The music began. And the room understood what it was witnessing."""
},
"S24": {
    "legend": "A = Elara Finch · B = Duke Silas Blackthorn · C = Father Benedict · D = Thomas Finch · E = Lucy · F = Mrs. Varma · Z = Narrator",
    "text": """Z: A small village church. Snow on the windowsills. Not a cathedral performance but a true thing.
D: (walked his daughter down the aisle. His hands steadier than they had been in years.)
E: (held the flowers.)
F: (stood as witness for the house.)
C: (spoke the words. His voice cracked on the word join.)
Z: The Duke's signet ring was warm against her finger as he slid it on — beside her brass thimble chain, beside the ink that would never wash out.
B: I do.
A: I always have.
Z: The snow fell outside. The candlelight held. And the house of God, small and old and true, received them."""
},
"S25": {
    "legend": "A = Elara Finch · B = Duke Silas Blackthorn · C = Child · Z = Narrator",
    "text": """Z: Years later. The same library. But alive now. Curtains drawn back. Fire lit. Books opened and scattered.
A: (sat in the reading chair. A child balanced on her knee. Pointing at gold lettering on a page.)
C: Read it again, Mama.
A: And the Duke kept his word. Every word. Every winter. Every one.
Z: The Duke stood behind her. His hand on the chair's back. His signet ring catching light through winter glass.
B: Not every word.
A: What do you mean?
B: I told you once that I would survive without you.
A: That was the only lie you ever told.
Z: The thorned rose crest was carved into the chair's armrest. But now it looked less like a warning and more like a welcome.
C: (laughed)
Z: The child laughed. The fire crackled.
A: (and the library smelled of old paper and beeswax and woodsmoke, and the winter pressed against the windows, and the story — their story — kept itself.)"""
}
}

def update_scenes():
    with open('build_gallery.py', 'r', encoding='utf-8') as f:
        content = f.read()

    for scene_id, data in DIALOGUES.items():
        legend = data["legend"]
        text = data["text"]
        new_vo = f"[{legend}]\n\n{text}"
        
        start_idx = content.find(f'("{scene_id}", ')
        if start_idx == -1:
            print(f"Warning: Start not found for {scene_id}")
            continue
            
        next_scene_num = int(scene_id[1:]) + 1
        if next_scene_num <= 25:
            next_scene_id = f"S{next_scene_num:02d}"
            end_idx = content.find(f'("{next_scene_id}", ')
        else:
            end_idx = content.find(']\n\nACTS', start_idx)
            if end_idx == -1:
                end_idx = content.find(']\nACTS', start_idx)
        if end_idx == -1:
            print(f"Warning: End not found for {scene_id}")
            continue
        
        old_block = content[start_idx:end_idx]
        title_match = re.search(r'"([^"]+)",\s*"""', old_block)
        title = title_match.group(1) if title_match else "Unknown"
        
        end_match = re.search(r'""",\s*"([^"]+)",\s*(\d+)\),', old_block)
        location = end_match.group(1) if end_match else "UNKNOWN"
        act = end_match.group(2) if end_match else "1"
        
        safe_text = new_vo.replace('"""', "'''")
        new_block = f'("{scene_id}", "{title}", """{safe_text}""", "{location}", {act}),\n    '
        content = content[:start_idx] + new_block + content[end_idx:]
        print(f"  Updated {scene_id}: {title}")

    with open('build_gallery.py', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\nUpdated {len(DIALOGUES)} scenes with dialogue format.")

if __name__ == "__main__":
    update_scenes()
