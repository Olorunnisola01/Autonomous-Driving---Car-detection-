#!/usr/bin/env python3
"""Build storyboard gallery with header, sidebar, and full-resolution lightbox."""
import base64, io, random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "storyboard_gallery.html"
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".webp"}

SCENES = [
    ("S01", "The Debt That Breathes", """[A = Narrator · B = Elara Finch (bookbinder's daughter) · C = Thomas Finch (her father)]

A: The bindery smells of old paper and desperation. Every creditor notice on the wall is another winter we might not survive.

B: We can sell the Chaucer, Father. It has the brass clasps.

C: Your mother loved that one.

B: Then it is worth more alive than dead.

A: He sets down his needle. His hands are worse than yesterday.

C: They will not wait forever, Elara.

B: Who will not?

C: The men whose names are on those walls. Hemsworth. Gable. The chandler.

B: I know their names. I count them every morning.

C: And what do they count, when they look at us?

B: Debts. They count debts.

A: The candle gutters. Outside, the wind howls through the bare elms.

C: I was a bookbinder once. Before the cough took your mother. Before the medicine.

B: I know, Father.

C: Now I am a man who cannot hold a needle.

B: You can still teach me. Your hands remember what your fingers no longer can.

A: He looks at her — the auburn hair, the ink-stained fingertips, the face of a girl who has aged ten years in three.

C: You have her hands. Your mother's hands.

B: I know.

C: Do you know what that means?

B: It means I can finish the vicar's Bible. It means we eat tomorrow.

C: It means you will have to decide, sooner than either of us would like, what we keep and what we let go.

B: I have already decided, Father. We keep the Chaucer.
A: She says it gently. But the candle is dying, and the walls are papered in notices, and the night is very long.''', "FINCH_BINDERY", 1),""", "FINCH_BINDERY", 1),
    ("S02", "The Summons Arrives", """[A = Narrator · B = Elara Finch · C = Thomas Finch]

A: The letter slides under the door like a thief. Black wax. Black seal. A thorned rose pressed into it like a brand.

B: Father — a letter.

C: From whom?

A: She breaks the seal. The parchment is thick, expensive.

B: It is from Blackthorn Hall.

A: His face changes. Not hope. Something older.

C: Read it.

B: "To Mr. Thomas Finch. It has come to our attention that your daughter, Elara Finch, possesses skills in the art of bookbinding that may be of service to the Duke of Blackthorn. The Duke requires a cataloguer for his library. Compensation shall be provided upon completion, sufficient to satisfy all outstanding obligations."

A: Silence. The clock ticks.

C: He knows my name.

B: Whose name?

C: The Duke. He knows my name.

B: How is that possible?

C: I do not know. I do not know.

B: I will go.

C: No.

B: I have to.

C: You do not understand what you are walking into.

B: I understand we are drowning.

C: It is not safe.

B: Neither is starving.
A: She folds the letter. It is heavy, like a stone. Like a sentence.''', "FINCH_BINDERY", 1),""", "FINCH_BINDERY", 1),
    ("S03", "The Road to Blackthorn", """[A = Narrator · B = Elara Finch]

A: The road stretches ahead, written in frost. Every hedgerow is skeletal. Every breath a small white ghost.

B: Every story about that house ends the same way. He did it. She vanished. No one agrees on how. They all agreed it happened.

A: She pulls her cloak tighter. The milestone appears — carved with a thorned rose, ancient and deliberate.

B: I am close.

A: The wind keens through the hedgerows. Turn back, it seems to say.

B: I cannot turn back. The debt is too great. The ruin too complete.

A: Her boots crunch on the frozen ground. The village is a grey smudge behind her.

B: I am a bookbinder's daughter. I am a keeper of stories. I am a mender of broken things.

A: The trees grow thicker. The light grows dimmer. The road becomes a tunnel of black wood.

B: Even if I cannot mend this. Even if I cannot save us. Even if I am walking into the dark.
A: She keeps walking. One foot. Then the other. The rhythm becomes a kind of prayer.''', "FINCH_BINDERY", 1),""", "FINCH_BINDERY", 1),
    ("S04", "The Gates of Blackthorn Hall", """[A = Narrator · B = Elara Finch · C = Mrs. Varma (the housekeeper)]

A: The gates are taller than a man. Twisted into thorned vines. Black iron against a grey sky that seems to press down on everything.

C: You will sleep in the east wing.

B: And the upper corridor?

C: Do not use it.

B: Why not?

A: She does not answer. She measures Elara with one look — ink-stained hands, worn boots, the nervous set of the shoulders.

C: The Duke does not receive callers. He receives people who answer letters.

B: What is the difference?

A: The gates groan open. The sound is iron grinding against iron.

C: You will find your room at the end of the east corridor. Dinner is at eight. Do not be late.

B: When do I begin the library?

C: The Duke will summon you when he is ready. Until then, you stay in your room.

B: May I ask —

C: You may ask nothing. Not yet.

A: She turns. Her black silk dress whispers against the stone path. The house looms ahead, dark stone, windows like empty eyes.

B: I have walked into a mouth.
A: The gravel is pale, almost white. Like crushed bone.''', "WINTER_ROAD", 1),""", "WINTER_ROAD", 1),
    ("S05", "The First Glimpse of Him", """[A = Narrator · B = Elara Finch · C = Duke Silas Blackthorn]

A: The foyer is a cavern of candelabras and damask. Every shadow is longer than it should be.

B: He was not surprised to see me.

A: She whispers it to the empty hall. The echo agrees.

C: (from the upper gallery, in shadow)

A: He stands half-consumed by darkness. He has been waiting a very long time.

B: Your Grace?

A: He does not descend. He does not speak.

C: (still silent)

B: I know you are there.

A: The candle between them gutters. Then he turns. Then he disappears.

B: He watched me the way one watches a door left ajar. Patient. Intent. As if he had been waiting for a very long time.

A: The hall is empty now. But the air still holds the weight of him — cold wool, smoke, something metallic and sharp.

B: He knew I was coming.
A: The clock ticks. Somewhere deep in the house, a door closes.''', "BLACKTHORN_GATES", 1),""", "BLACKTHORN_GATES", 1),
    ("S06", "The Library That Remembered", """[A = Narrator · B = Elara Finch · C = Mrs. Varma]

A: Two stories of shelves bow under the weight of centuries. Dust motes hang motionless in slanting winter light.

B: I set down my satchel and exhale. The first full breath since arriving.

C: She arranged it by feeling, not subject. The late Duchess.

B: How long did that take you to understand?

C: Ten years. I never did.

B: She touched the spines. Leather. Vellum. Gold leaf. Each book a small resurrection.

C: You will disturb nothing until you understand her order.

B: And if I cannot understand it?

C: Then you will leave it as it is. Some things are not meant to be catalogued.

A: The fireplace is large enough to stand in. It holds cold ashes.

B: This room is alive.

C: It is waiting. There is a difference.
A: She runs her hand along a shelf. Her fingers tingle. Something like recognition.''', "BLACKTHORN_FOYER", 1),""", "BLACKTHORN_FOYER", 1),
    ("S07", "The Journals with Her Name", """[A = Narrator · B = Elara Finch]

A: The journals are leather-bound and cracked with age. Each one a small coffin of secrets.

B: Thirteen years ago. A margin note. Beside a passage on the binding of psalters.

A: Her fingers tremble. She reads the entry again.

B: Elara Finch. Written in elegant copperplate. The date is ten years before I was born.

A: The ink is old. The handwriting is deliberate.

B: This was not a coincidence.

A: She closes the journal. Her breath comes shallow.

B: He knew. Before I existed. He wrote me down.

A: The library is very quiet. The candles have burned low.

B: Who writes a name into a book that does not yet exist? Who binds a story before the heroine is born?
A: Somewhere in the house, a door opens. Then closes. Then silence.''', "BLACKTHORN_LIBRARY", 1),""", "BLACKTHORN_LIBRARY", 1),
    ("S08", "The Duke Watches", """[A = Narrator · B = Elara Finch · C = Duke Silas Blackthorn]

A: Candlelight. Late. She works without knowing he is there.

B: The air has changed. The pressure. The stillness.

A: He stands in the doorway's shadow. Observing.

B: He was watching me lift the page. As if I were performing surgery on something alive.

A: She turns.

C: (already gone)

B: Only the scent of cold wool and smoke remains.

A: The candle between them has guttered. The page she was reading lies open.

B: He is always there. Just behind the edge of seeing.

A: She touches the spot on the desk where his shadow fell. The leather is warm.

B: He was here. He was standing here. And then he was not.
A: The house settles. A timber creaks. Somewhere deep in Blackthorn, a clock strikes two.''', "BLACKTHORN_LIBRARY", 1),""", "BLACKTHORN_LIBRARY", 1),
    ("S09", "The Gallery of Dead Wives", """[A = Narrator · B = Elara Finch · C = Lucy (the maid)]

A: The corridor of portraits stretches longer than expected. Each face watches with painted eyes that never blink.

C: They say he locked himself in here for a year after she died.

B: How did she die?

C: That is the question no one answers twice the same way.

A: Lucy's candle flickers. They stop before a painting — white satin, pearl choker, emerald pendant.

B: Lady Margaret.

C: She was beautiful. In a cold way.

B: Her eyes — they look right through me.

A: Elara sees her own reflection in the gilt frame, superimposed over the painted face. The auburn hair. The pale skin. The wide eyes.

C: You look like her.

B: I know.

C: That is why you should not be here.

B: Then why am I here?

C: That is the question you should be asking.
A: The portrait's emerald pendant catches the candlelight. It gleams. It warns.''', "BLACKTHORN_LIBRARY", 1),""", "BLACKTHORN_LIBRARY", 1),
    ("S10", "The First Touch", """[A = Narrator · B = Elara Finch · C = Duke Silas Blackthorn]

A: She fell asleep at the reading desk. A book open against her cheek.

C: (enters silently)

A: His gloved hand reaches down. Not to shake her. Not to wake her.

C: (brushes a stray auburn curl from her forehead. His finger grazes her temple.)

A: She stirs. Their eyes meet across the smallest distance. Neither moves.

C: You are exactly as I wrote you.

A: His voice is barely audible. The candle between them gutters.

B: I did not know whether to be terrified or flattered.

C: Perhaps both.

A: He steps back. The shadows reclaim him.

B: He touched me as if I were a text he had been trying to read for a decade.

A: The library is silent again. But the air is different now. Warmer. Charged.
B: He knows my name. He has known my name. And I — I am only now beginning to understand what that means.''', "BLACKTHORN_GALLERY", 1),""", "BLACKTHORN_GALLERY", 1),
    ("S11", "The Contract on the Desk", """[A = Narrator · B = Elara Finch · C = Duke Silas Blackthorn]

A: A desk of black oak. A single document.

C: (hands braced on the wood, signet ring catching the firelight)

B: All Finch family debts cleared. Father's workshop preserved. In exchange for one winter as your Duchess.

C: In name. In public. In residence. No conjugal obligation. No permanent arrangement.

B: I may leave at spring thaw.

C: You may.

B: Why me?

C: Because you were always the answer.

B: Always?

C: I simply had to wait for the question to arrive.

A: She reads the contract again. The words are clean. Legal. Final.

B: There is no trapdoor here.

C: There is no trapdoor. Only a door. And it opens in one direction.

B: And if I do not sign?

C: Then the door closes. And the creditors come. And the bindery is lost.

A: She looks at him. His dark charcoal eyes are steady. Patient.

B: I did not know whether to believe him or run.
A: So she stood there. And she did neither.''', "BLACKTHORN_LIBRARY", 1),""", "BLACKTHORN_LIBRARY", 1),
    ("S12", "The Fake Engagement", """[A = Narrator · B = Elara Finch · C = Duke Silas Blackthorn · D = Mrs. Varma · E = Lucy]

A: A long table set for two, though the house holds twenty.

D: (adjusts Elara's collar with proprietary hands)

E: (peeks from the serving doorway, wide-eyed)

C: (takes his seat. Does not look at her until she is settled. Then holds her gaze.)

C: You will call me Silas in private.

B: And in public?

C: Your Grace. Allow no one to see you smile first.

B: And if I smile first?

C: Then I will spend the evening making it worth the scandal.

A: The candlelight between them makes the rest of the hall seem to fall away.

D: (steps back, satisfied)

E: (disappears into the shadows)

B: You have rules for everything.

C: I have rules for the things that matter.

B: And what matters?

C: That no one sees you smile first. That you look at me when I speak. That you do not speak to Julian Fox without my knowledge.

B: Julian Fox?

C: My cousin. You will meet him. You will not like him. That is as it should be.

A: The servants bring the first course. The wine is poured. The silence is a third presence at the table.

B: I did not know whether he was threatening me or promising me something.

C: Perhaps both.
A: He raised his glass. She did not raise hers. Not yet.''', "BLACKTHORN_STUDY", 1),""", "BLACKTHORN_STUDY", 1),
    ("S13", "The Jealousy at the Hunt Ball", """[A = Narrator · B = Elara Finch · C = Duke Silas Blackthorn · D = Julian Fox (the Duke's cousin)]

A: The ballroom glittered. A thousand candles in crystal chandeliers. The local gentry in jewels and calculated indifference.

D: My dear Duchess. May I claim the first dance?

B: Before I could answer, his hand was at my waist.

D: You are trembling.

B: Your cousin's moods are not a difficult text.

D: Then why are you trembling, Elara?

A: He used my name the way a man uses a blade he has tested.

C: (across the room. A glass of brandy untouched. Knuckles white.)

B: He was not dancing. He was performing for someone else.

A: The Duke crossed the room. The crowd parted for him the way water parts for something heavier than itself.

D: Ah. The master of the house.

C: (does not speak to Julian. Simply takes Elara's hand from his waist and places it against his own coat, over his heart.)

A: The room understood. And Elara understood. And Julian understood.

C: I did not ask you to dance.

B: I know.

C: I simply did not let go.
A: The music began again. He did not let go.''', "BLACKTHORN_DINING_HALL", 1),""", "BLACKTHORN_DINING_HALL", 1),
    ("S14", "The Secret of the First Wife", """[A = Narrator · B = Elara Finch · C = Duke Silas Blackthorn]

A: The locked drawer. The bone folder. The splintered wood.

B: Letters from Lady Margaret's brother. Describing his sister's slow poisoning.

A: She read them all. Twice. Then she sat in the Duke's chair and waited.

C: (enters at midnight)

B: You found them.

C: I found them.

B: Did you kill her?

A: Long silence. The fire popped.

C: The letters are incomplete.

B: Are they?

C: She asked me to let her go.

B: Let her go?

C: She was ill. Not the illness they described. That was the medicine, the laudanum, the physician's incompetence. She was ill in a way that had no name.

B: And you —

C: I held on too tightly. That is the closest thing to murder I have ever committed.

B: And me? What about me?

A: The silence was long enough that she heard the house settling.

C: I am afraid of you.

B: Afraid?

C: You are the only thing I have ever been afraid to hold.
A: The candlelight guttered. And she did not know whether to rise and leave or stay and be destroyed.''', "BLACKTHORN_BALLROOM", 1),""", "BLACKTHORN_BALLROOM", 1),
    ("S15", "The Agreement", """[A = Narrator · B = Elara Finch · C = Duke Silas Blackthorn]

A: Winter light turned the library gold.

B: I stood by the window. The contract in my hands.

C: (by the fireplace. Still as a portrait.)

B: I found the escape clause. I can leave at spring. The debts are cleared. No conditions.

C: I wrote it that way.

B: I will stay the winter.

C: —

B: Not because of the debt. Not because of the contract. Because I need to know if what you wrote in those journals was true.

C: And if it was not?

B: Then I am just the woman who looked enough like a ghost to fill the space she left behind.

A: He crossed the room. Stopped exactly one arm's length from her.

C: You were never a ghost.

B: Then what was I?

C: The only living thing I could imagine in this house.
A: The winter sun caught the edge of the contract and made it glow. And for the first time, she did not feel like a woman who had come to sell herself. She felt like a woman who had come to be found.''', "BLACKTHORN_STUDY", 1),""", "BLACKTHORN_STUDY", 1),
    ("S16", "The Betrayal", """[A = Narrator · B = Elara Finch · C = Julian Fox · D = Duke Silas Blackthorn]

A: Julian found her in the gallery. He always found her when she was alone.

C: You look lost, cousin.

B: I am looking at your family.

C: Our family. Or it will be, if my cousin has his way. Have you read the rest of the journals? Not the ones with your name in the margin. The others.

B: The ones he wrote about me before he knew I existed.

C: That winter — 1844 — three creditors called on your father in a single week. Do you remember?

B: I remember the winter of the blue hands.

C: Your father's debts were purchased. All of them. By a single buyer. The same buyer who, three years later, sent the letter summoning you here.

B: I was never summoned.

C: You were harvested. My cousin does not collect books. He collects people.

A: Footsteps. The Duke stood in the doorway.

D: (does not deny it)

B: It was not a marriage. It was not a bargain. It was a possession that had begun before I was born.
A: And she was only now, too late, learning its true name.''', "BLACKTHORN_LIBRARY", 1),""", "BLACKTHORN_LIBRARY", 1),
    ("S17", "The Fire in the East Wing", """[A = Narrator · B = Elara Finch · C = Lucy · D = Mrs. Varma]

A: Smoke. Thin at first. Then thickening. Crawling under the door.

B: (packed satchel at her feet)

A: The corridor outside lit with flickering orange. Wallpaper curling. Blackening.

C: (from the stairwell, a short sharp scream)

B: (ran)

A: Mrs. Varma met her on the landing. Not panicked. Not hurried. But her face — open, in a way Elara had never seen.

D: (pressed a key into her hand. Heavy. Cold. Iron.)

D: The servants' door. Through the kitchens. Down the back stairs. Do not stop. Do not look back.

B: What about —

D: Do not look for him.

A: Lucy appeared behind her, coughing, face streaked with soot.

C: The gallery. The fire started in the gallery. The portraits — they're all —

A: She did not finish. She did not need to.

B: (did not look at the gallery. Did not look at the room where the Duke had stood and not denied it.)

A: She ran through the kitchens, through the servants' door, into the cold.
B: Until the house was a shape of fire against the winter sky. Until Lady Margaret's portrait was ash. Until she was finally, truly, alone.''', "BLACKTHORN_STUDY", 1),""", "BLACKTHORN_STUDY", 1),
    ("S18", "She Tries to Flee", """[A = Narrator · B = Elara Finch]

A: The snow came up past her ankles. Then her calves. Then her knees.

B: (brass thimble swinging against her collarbone with each stride)

A: She walked for what felt like an hour. Then she saw them.

B: Footprints. My own footprints. Ahead of me.

A: She turned slowly. The house was behind her again. The same orange glow. The same distance.

B: I had walked for an hour and I had not moved at all.

A: The grounds of Blackthorn were larger than she understood. Or something was keeping her contained.

B: I will not be the ghost.

A: Her voice sounded strange. Thin. Like something that belonged to someone else.

B: I will not be the collection. I will not be the thing he wrote.

A: The snow fell. The house burned. And she stood in the circle of her own footprints.
B: There is only one direction left to walk. Back.''', "BLACKTHORN_EAST_WING", 1),""", "BLACKTHORN_EAST_WING", 1),
    ("S19", "He Lets Her Go", """[A = Narrator · B = Elara Finch · C = Duke Silas Blackthorn]

A: The iron gates stood open. The gravel drive held a single figure.

C: (on the outside. A saddled horse behind him. A folded travelling cloak on its back. A letter of transit in his gloved hand.)

C: You came back.

B: I had nowhere else to go.

C: I know.

A: He stepped aside. The gate stood open.

C: I bought your father's debt because I could not bear the thought of you starving while I did nothing.

B: —

C: I did not arrange you. I waited for you. There is a difference, and I know it does not excuse anything.

B: (looked at him. He looked at her.)

C: Go.

A: He stepped back. He did not follow. He did not call after her.

C: If you return, it must be because you chose to. Not because you had nowhere else.

B: (took the cloak. Took the letter. Did not take the horse.)

A: She walked through the gate. The gravel crunched. The road opened ahead.
B: I knew I would return. Not because I had nowhere else. Because there was nowhere else I wanted to be.''', "BLACKTHORN_GROUNDS", 1),""", "BLACKTHORN_GROUNDS", 1),
    ("S20", "The Distance Between", """[A = Narrator · B = Elara Finch · C = Father Benedict (the vicar)]

A: The inn was called the Black Swan. Halfway between the life she had left and the life she was walking toward.

C: (did not ask permission to sit. Placed his leather-bound prayer book on the table between them.)

C: I have known Silas Blackthorn for thirty years. I married him to Margaret. I buried her.

B: —

C: He came to me the night she died. He stood in my study and said, "Tell me how to stop loving what I could not save."

B: What did you tell him?

C: I told him there is no stopping. Only choosing.

B: What did he choose?

C: He chose to wait. For ten years, he chose to wait.

B: And that is not obsession?

C: That is the only patience I have ever seen that deserved to be called love.

A: Father Benedict closed his prayer book.

C: You choose. As he chose. As she chose. As every person in this story has chosen, rightly or wrongly, for as long as it has been telling itself.

A: He stood. He left the prayer book on the table. He walked out into the night.
B: (sat by the fire, wrapped in a cloak she had not asked for, and chose.)''', "BLACKTHORN_GATES", 1),""", "BLACKTHORN_GATES", 1),
    ("S21", "The Return on Her Own Terms", """[A = Narrator · B = Elara Finch · C = Duke Silas Blackthorn · D = Mrs. Varma]

A: She returned to the gates. Not in the cloak he gave her. She had returned it.

D: (opened the gate without being asked)

B: (in her own forest-green dress. Clean but worn. Satchel over her shoulder. No contract. Only herself.)

A: The Duke stood in the gravel drive. Uncovered by hat or hood. Snow catching in his too-long black hair.

C: (had been waiting. Had always been waiting.)

B: I did not come back for the contract.

C: I know.

B: I came back because the alternative was a lifetime of listening for your footsteps and pretending I did not miss them.

A: The snow fell between them. The manor stood dark and silent behind him.

C: (did not speak. Did not need to.)
B: (stepped through the gate. And the gate closed behind her. And she was home.)''', "VILLAGE_INN", 1),""", "VILLAGE_INN", 1),
    ("S22", "The Consummation", """[A = Narrator · B = Elara Finch · C = Duke Silas Blackthorn]

A: His private chambers. High windows black with winter night. Fire low and amber.

B: (stood before him. No contract. No audience. No bargain.)

C: (removed his gloves slowly. Finger by finger.)

A: His bare hands took her face. As if she were a text he had been trying to read for a decade and had only now learned the language.

C: Say my name.

B: Silas.

A: He closed his eyes.

C: It was the first time he had heard his own name spoken like a prayer.
B: (and the fire crackled, and the winter pressed against the windows, and the house held them in its old dark hands.)''', "BLACKTHORN_GATES", 1),""", "BLACKTHORN_GATES", 1),
    ("S23", "The Public Claiming", """[A = Narrator · B = Elara Finch · C = Duke Silas Blackthorn · D = Julian Fox · E = Mrs. Varma · F = Lucy]

A: A second ball. This one her choice.

B: (entered on the Duke's arm. Not as contract bride. As chosen Duchess.)

D: (watched from the crowd. Smile sharp enough to cut.)

E: (stood at the door. And for the first time, she smiled.)

F: (caught Elara's eye from behind the refreshment table. Mouthed: finally.)

A: The Duke led her to the center of the floor.

C: Let them stare. Let them write it down. Julian can tell every version he likes. They will never be able to say I did not ask.

B: You asked every day.

C: —

B: I simply could not hear it until I was ready to answer.
A: He did not let go. The music began. And the room understood what it was witnessing.''', "BLACKTHORN_CHAMBERS", 1),""", "BLACKTHORN_CHAMBERS", 1),
    ("S24", "The Marriage", """[A = Narrator · B = Elara Finch · C = Duke Silas Blackthorn · D = Father Benedict · E = Thomas Finch · F = Lucy · G = Mrs. Varma]

A: A small village church. Snow on the windowsills. Not a cathedral performance but a true thing.

E: (walked his daughter down the aisle. His hands steadier than they had been in years.)

F: (held the flowers.)

G: (stood as witness for the house.)

D: (spoke the words. His voice cracked on the word join.)

A: The Duke's signet ring was warm against her finger as he slid it on — beside her brass thimble chain, beside the ink that would never wash out.

C: I do.

B: I always have.
A: The snow fell outside. The candlelight held. And the house of God, small and old and true, received them.''', "BLACKTHORN_BALLROOM", 1),""", "BLACKTHORN_BALLROOM", 1),
    ("S25", "The True Duchess", """[A = Narrator · B = Elara Finch · C = Duke Silas Blackthorn · D = Child]

A: Years later. The same library. But alive now. Curtains drawn back. Fire lit. Books opened and scattered.

B: (sat in the reading chair. A child balanced on her knee. Pointing at gold lettering on a page.)

D: Read it again, Mama.

B: And the Duke kept his word. Every word. Every winter. Every one.

A: The Duke stood behind her. His hand on the chair's back. His signet ring catching light through winter glass.

C: Not every word.

B: What do you mean?

C: I told you once that I would survive without you.

B: That was the only lie you ever told.

A: The thorned rose crest was carved into the chair's armrest. But now it looked less like a warning and more like a welcome.

D: (laughed)

A: The child laughed. The fire crackled.
B: (and the library smelled of old paper and beeswax and woodsmoke, and the winter pressed against the windows, and the story — their story — kept itself.)''', "UNKNOWN", 1),""", "UNKNOWN", 1),
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
