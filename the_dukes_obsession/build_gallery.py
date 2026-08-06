#!/usr/bin/env python3
"""Build storyboard gallery with header, sidebar, and full-resolution lightbox."""
import base64, io, random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "storyboard_gallery.html"
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".webp"}

SCENES = [
    ("S01", "The Debt That Breathes", """[A = Elara Finch (bookbinder's daughter) · B = Thomas Finch (her father) · Z = Narrator]

Z: The bindery smells of old paper and desperation. Every creditor notice on the wall is another winter we might not survive.

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
Z: She says it gently. But the candle is dying, and the walls are papered in notices, and the night is very long.""", "FINCH_BINDERY", 1),
    ("S02", "The Summons Arrives", """[A = Elara Finch · B = Thomas Finch · Z = Narrator]

Z: The letter slides under the door like a thief. Black wax. Black seal. A thorned rose pressed into it like a brand.

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
Z: She folds the letter. It is heavy, like a stone. Like a sentence.""", "FINCH_BINDERY", 1),
    ("S03", "The Road to Blackthorn", """[A = Elara Finch · Z = Narrator]

Z: The road stretches ahead, written in frost. Every hedgerow is skeletal. Every breath a small white ghost.

A: Every story about that house ends the same way. He did it. She vanished. No one agrees on how. They all agreed it happened.

Z: She pulls her cloak tighter. The milestone appears — carved with a thorned rose, ancient and deliberate.

A: I am close.

Z: The wind keens through the hedgerows. Turn back, it seems to say.

A: I cannot turn back. The debt is too great. The ruin too complete.

Z: Her boots crunch on the frozen ground. The village is a grey smudge behind her.

A: I am a bookbinder's daughter. I am a keeper of stories. I am a mender of broken things.

Z: The trees grow thicker. The light grows dimmer. The road becomes a tunnel of black wood.

A: Even if I cannot mend this. Even if I cannot save us. Even if I am walking into the dark.
Z: She keeps walking. One foot. Then the other. The rhythm becomes a kind of prayer.""", "FINCH_BINDERY", 1),
    ("S04", "The Gates of Blackthorn Hall", """[A = Elara Finch · B = Mrs. Varma (the housekeeper) · Z = Narrator]

Z: The gates are taller than a man. Twisted into thorned vines. Black iron against a grey sky that seems to press down on everything.

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
Z: The gravel is pale, almost white. Like crushed bone.""", "WINTER_ROAD", 1),
    ("S05", "The First Glimpse of Him", """[A = Elara Finch · B = Duke Silas Blackthorn · Z = Narrator]

Z: The foyer is a cavern of candelabras and damask. Every shadow is longer than it should be.

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
Z: The clock ticks. Somewhere deep in the house, a door closes.""", "BLACKTHORN_GATES", 1),
    ("S06", "The Library That Remembered", """[A = Elara Finch · B = Mrs. Varma · Z = Narrator]

Z: Two stories of shelves bow under the weight of centuries. Dust motes hang motionless in slanting winter light.

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
Z: She runs her hand along a shelf. Her fingers tingle. Something like recognition.""", "BLACKTHORN_FOYER", 1),
    ("S07", "The Journals with Her Name", """[A = Elara Finch · Z = Narrator]

Z: The journals are leather-bound and cracked with age. Each one a small coffin of secrets.

A: Thirteen years ago. A margin note. Beside a passage on the binding of psalters.

Z: Her fingers tremble. She reads the entry again.

A: Elara Finch. Written in elegant copperplate. The date is ten years before I was born.

Z: The ink is old. The handwriting is deliberate.

A: This was not a coincidence.

Z: She closes the journal. Her breath comes shallow.

A: He knew. Before I existed. He wrote me down.

Z: The library is very quiet. The candles have burned low.

A: Who writes a name into a book that does not yet exist? Who binds a story before the heroine is born?
Z: Somewhere in the house, a door opens. Then closes. Then silence.""", "BLACKTHORN_LIBRARY", 1),
    ("S08", "The Duke Watches", """[A = Elara Finch · B = Duke Silas Blackthorn · Z = Narrator]

Z: Candlelight. Late. She works without knowing he is there.

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
Z: The house settles. A timber creaks. Somewhere deep in Blackthorn, a clock strikes two.""", "BLACKTHORN_LIBRARY", 1),
    ("S09", "The Gallery of Dead Wives", """[A = Elara Finch · B = Lucy (the maid) · Z = Narrator]

Z: The corridor of portraits stretches longer than expected. Each face watches with painted eyes that never blink.

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
Z: The portrait's emerald pendant catches the candlelight. It gleams. It warns.""", "BLACKTHORN_LIBRARY", 1),
    ("S10", "The First Touch", """[A = Elara Finch · B = Duke Silas Blackthorn · Z = Narrator]

Z: She fell asleep at the reading desk. A book open against her cheek.

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
A: He knows my name. He has known my name. And I — I am only now beginning to understand what that means.""", "BLACKTHORN_GALLERY", 1),
    ("S11", "The Contract on the Desk", """[A = Elara Finch · B = Duke Silas Blackthorn · Z = Narrator]

Z: A desk of black oak. A single document.

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
Z: So she stood there. And she did neither.""", "BLACKTHORN_LIBRARY", 1),
    ("S12", "The Fake Engagement", """[A = Elara Finch · B = Duke Silas Blackthorn · C = Mrs. Varma · D = Lucy · Z = Narrator]

Z: A long table set for two, though the house holds twenty.

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
Z: He raised his glass. She did not raise hers. Not yet.""", "BLACKTHORN_STUDY", 1),
    ("S13", "The Jealousy at the Hunt Ball", """[A = Elara Finch · B = Duke Silas Blackthorn · C = Julian Fox (the Duke's cousin) · Z = Narrator]

Z: The ballroom glittered. A thousand candles in crystal chandeliers. The local gentry in jewels and calculated indifference.

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
Z: The music began again. He did not let go.""", "BLACKTHORN_DINING_HALL", 1),
    ("S14", "The Secret of the First Wife", """[A = Elara Finch · B = Duke Silas Blackthorn · Z = Narrator]

Z: The locked drawer. The bone folder. The splintered wood.

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
Z: The candlelight guttered. And she did not know whether to rise and leave or stay and be destroyed.""", "BLACKTHORN_BALLROOM", 1),
    ("S15", "The Agreement", """[A = Elara Finch · B = Duke Silas Blackthorn · Z = Narrator]

Z: Winter light turned the library gold.

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
Z: The winter sun caught the edge of the contract and made it glow. And for the first time, she did not feel like a woman who had come to sell herself. She felt like a woman who had come to be found.""", "BLACKTHORN_STUDY", 1),
    ("S16", "The Betrayal", """[A = Elara Finch · B = Julian Fox · C = Duke Silas Blackthorn · Z = Narrator]

Z: Julian found her in the gallery. He always found her when she was alone.

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
Z: And she was only now, too late, learning its true name.""", "BLACKTHORN_LIBRARY", 1),
    ("S17", "The Fire in the East Wing", """[A = Elara Finch · B = Lucy · C = Mrs. Varma · Z = Narrator]

Z: Smoke. Thin at first. Then thickening. Crawling under the door.

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
A: Until the house was a shape of fire against the winter sky. Until Lady Margaret's portrait was ash. Until she was finally, truly, alone.""", "BLACKTHORN_STUDY", 1),
    ("S18", "She Tries to Flee", """[A = Elara Finch · Z = Narrator]

Z: The snow came up past her ankles. Then her calves. Then her knees.

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
A: There is only one direction left to walk. Back.""", "BLACKTHORN_EAST_WING", 1),
    ("S19", "He Lets Her Go", """[A = Elara Finch · B = Duke Silas Blackthorn · Z = Narrator]

Z: The iron gates stood open. The gravel drive held a single figure.

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
A: I knew I would return. Not because I had nowhere else. Because there was nowhere else I wanted to be.""", "BLACKTHORN_GROUNDS", 1),
    ("S20", "The Distance Between", """[A = Elara Finch · B = Father Benedict (the vicar) · Z = Narrator]

Z: The inn was called the Black Swan. Halfway between the life she had left and the life she was walking toward.

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
A: (sat by the fire, wrapped in a cloak she had not asked for, and chose.)""", "BLACKTHORN_GATES", 1),
    ("S21", "The Return on Her Own Terms", """[A = Elara Finch · B = Duke Silas Blackthorn · C = Mrs. Varma · Z = Narrator]

Z: She returned to the gates. Not in the cloak he gave her. She had returned it.

C: (opened the gate without being asked)

A: (in her own forest-green dress. Clean but worn. Satchel over her shoulder. No contract. Only herself.)

Z: The Duke stood in the gravel drive. Uncovered by hat or hood. Snow catching in his too-long black hair.

B: (had been waiting. Had always been waiting.)

A: I did not come back for the contract.

B: I know.

A: I came back because the alternative was a lifetime of listening for your footsteps and pretending I did not miss them.

Z: The snow fell between them. The manor stood dark and silent behind him.

B: (did not speak. Did not need to.)
A: (stepped through the gate. And the gate closed behind her. And she was home.)""", "VILLAGE_INN", 1),
    ("S22", "The Consummation", """[A = Elara Finch · B = Duke Silas Blackthorn · Z = Narrator]

Z: His private chambers. High windows black with winter night. Fire low and amber.

A: (stood before him. No contract. No audience. No bargain.)

B: (removed his gloves slowly. Finger by finger.)

Z: His bare hands took her face. As if she were a text he had been trying to read for a decade and had only now learned the language.

B: Say my name.

A: Silas.

Z: He closed his eyes.

B: It was the first time he had heard his own name spoken like a prayer.
A: (and the fire crackled, and the winter pressed against the windows, and the house held them in its old dark hands.)""", "BLACKTHORN_GATES", 1),
    ("S23", "The Public Claiming", """[A = Elara Finch · B = Duke Silas Blackthorn · C = Julian Fox · D = Mrs. Varma · E = Lucy · Z = Narrator]

Z: A second ball. This one her choice.

A: (entered on the Duke's arm. Not as contract bride. As chosen Duchess.)

C: (watched from the crowd. Smile sharp enough to cut.)

D: (stood at the door. And for the first time, she smiled.)

E: (caught Elara's eye from behind the refreshment table. Mouthed: finally.)

Z: The Duke led her to the center of the floor.

B: Let them stare. Let them write it down. Julian can tell every version he likes. They will never be able to say I did not ask.

A: You asked every day.

B: —

A: I simply could not hear it until I was ready to answer.
Z: He did not let go. The music began. And the room understood what it was witnessing.""", "BLACKTHORN_CHAMBERS", 1),
    ("S24", "The Marriage", """[A = Elara Finch · B = Duke Silas Blackthorn · C = Father Benedict · D = Thomas Finch · E = Lucy · F = Mrs. Varma · Z = Narrator]

Z: A small village church. Snow on the windowsills. Not a cathedral performance but a true thing.

D: (walked his daughter down the aisle. His hands steadier than they had been in years.)

E: (held the flowers.)

F: (stood as witness for the house.)

C: (spoke the words. His voice cracked on the word join.)

Z: The Duke's signet ring was warm against her finger as he slid it on — beside her brass thimble chain, beside the ink that would never wash out.

B: I do.

A: I always have.
Z: The snow fell outside. The candlelight held. And the house of God, small and old and true, received them.""", "BLACKTHORN_BALLROOM", 1),
    ("S25", "The True Duchess", """[A = Elara Finch · B = Duke Silas Blackthorn · C = Child · Z = Narrator]

Z: Years later. The same library. But alive now. Curtains drawn back. Fire lit. Books opened and scattered.

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
A: (and the library smelled of old paper and beeswax and woodsmoke, and the winter pressed against the windows, and the story — their story — kept itself.)""", "UNKNOWN", 1),
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
    print("THE DUKE'S OBSESSION — Gallery Builder")
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
    html.append('<div class="subtitle">A Gothic Dark Romance</div>')
    html.append('<p class="description">When an impoverished bookbinder\'s daughter is summoned to catalog the library of a reclusive, widowed Duke rumored to have killed his first wife, she discovers her name already written in his journals from ten years before she was born — and a contract offering her family\'s debts cleared in exchange for one winter as his Duchess in name only.</p>')
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
