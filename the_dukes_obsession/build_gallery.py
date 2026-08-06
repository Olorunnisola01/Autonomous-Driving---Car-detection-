#!/usr/bin/env python3
"""Build storyboard gallery with header, sidebar, and full-resolution lightbox."""
import base64, io, random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "storyboard_gallery.html"
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".webp"}

SCENES = [
    ("S01", "The Debt That Breathes", """I learned to count debts the way other girls counted stitches — by candlelight, by the tremor in my father's hands, by the silence that grew thicker than the leather we bound. The workshop smelled of old paper and desperation, of glue and grief and the slow decay of things that once mattered. Every creditor notice on the wall was another winter we might not survive, another nail in the coffin of the life we'd once known. I told him we could sell the Chaucer. He said Mother loved it. I said it was worth more alive than dead. We both knew I was lying. Some things, once sold, cannot be bought back.

The bindery had been our home for as long as I could remember, though "home" was perhaps too generous a word for a place that smelled perpetually of turpentine and despair. Father's hands, once steady enough to thread a needle in dim light, now shook so badly he could barely hold the awl. The tremor had started three years ago, around the time the last of Mother's jewelry disappeared into the pawnbroker's till. Since then, the shaking had spread from his hands to his voice, from his voice to his spirit, until the man who had once taught me to distinguish between calfskin and goatskin by touch alone could barely meet my eyes.

I worked by the light of a single tallow candle, its flame guttering in the draft that seeped through the cracks in the walls. The Bible I was rebinding belonged to the vicar's wife, who had paid us in stale bread and the promise of prayers. It was honest work, if poorly compensated, and I had learned to find a kind of peace in the rhythm of needle and thread, in the careful folding of signatures, in the patient application of paste to leather. Each book was a small resurrection, a dead thing brought back to life through skill and care.

But no amount of skill could resurrect our fortunes. The creditors came every week now, their notices papering the walls like autumn leaves, each one more urgent than the last. Mr. Hemsworth the butcher had stopped extending credit. Mrs. Gable the baker demanded payment before delivery. Even the chandler, who had once been a friend of Father's, now required coin before surrendering his candles. We were drowning, and I was the only one who seemed to notice the water rising.

The Chaucer sat on the highest shelf, its brass clasps gleaming dully in the candlelight. It had been Mother's favorite, a first edition she had purchased with her dowry money, back when such things still mattered. Father had forbidden me to touch it, saying it was the last thing of beauty in our lives. But beauty, I had learned, was a luxury we could no longer afford.

"We can sell it," I said again, keeping my voice gentle, the way one speaks to a wounded animal. "The brass alone is worth something. And the pages — they're old, Father. Someone might pay for the paper alone."

He looked up from his work, his eyes red-rimmed and haunted. "Your mother loved that book," he said, as if that settled the matter. As if love were a currency we could spend.

"Then it is worth more alive than dead," I replied, and we both knew I was lying. The Chaucer would fetch perhaps three pounds at the bookseller's, enough to keep us for a month, perhaps two if we were careful. But then what? There would be another debt, another notice, another winter.

I returned to my stitching, the needle slipping in and out of the leather with practiced ease. My fingers were stained with ink, permanently marked by the trade I had learned at my mother's knee. She had been a bookbinder too, before the cough took her, before the medicine costs bankrupted us, before the slow unraveling of everything we had been. I had her hands, people said. I had her patience. But I also had her stubbornness, her refusal to accept that some things cannot be mended no matter how carefully you stitch them.

The candle guttered lower, casting long shadows that danced on the walls like ghosts. Outside, the wind howled through the bare branches of the elms, and I could hear the distant clang of the church bell marking the hour. Midnight. Another day survived, another day closer to ruin. I tied off the thread, trimmed the excess with my shears, and set the Bible aside. Tomorrow I would deliver it to the vicar's wife and collect my stale bread. Tomorrow I would face the creditors again. Tomorrow I would pretend that we were not drowning.

But tonight, in the flickering candlelight, with my father's trembling hands and the ghost of my mother's Chaucer watching over us, I allowed myself a moment of honesty. We were finished. The bindery was finished. The life we had known was finished. And no amount of careful stitching could mend what was broken beyond repair.

Some things, once sold, cannot be bought back. But some things, once lost, cannot be kept either. And I was beginning to understand that love — for a father, for a mother, for a life that no longer existed — was the most expensive thing of all.

I remember when the bindery was different. When it smelled of possibility rather than despair. Mother would sit at her workbench, her hands moving with the confidence of someone who knew exactly what she was doing. She would sing as she worked, old folk songs that I can still hear in my head when the wind is right. Father would watch her with an expression I can only describe now as worship, his eyes following her every movement as if she were performing magic rather than craftsmanship.

The books we bound in those days were different too. Not the desperate repairs of water-damaged Bibles and moth-eaten prayer books that now constituted our income, but fine editions, leather-bound volumes with gold leaf tooling and silk endpapers. We had clients then — real clients, not just the vicar's wife paying in bread. The squire's library, the doctor's collection, even a few commissions from London. We were respected. We were artists.

Now we were scavengers, picking through the remnants of our former life, trying to extract whatever value we could from the ruins.

The creditor notices on the wall told the story of our decline in stark black ink. Hemsworth & Sons, Butchers — 2 pounds, 7 shillings. Gable's Bakery — 1 pound, 3 shillings. The Chandlery — 15 shillings. Each one a small death, a small failure, a small acknowledgment that we were no longer the people we had once been. The notices were arranged chronologically, though I don't know why. Perhaps Father found some comfort in seeing the progression, in watching our ruin unfold in neat rows of numbers. Or perhaps he simply didn't have the energy to take them down.

I had taken to reading them in the morning, when Father was still asleep. I would stand before the wall and trace the amounts with my finger, calculating how long we could survive on what we had. The answer was always the same: not long enough.

The Chaucer. Mother's Chaucer. I had never opened it, though I knew I should have. It seemed sacrilegious somehow, to read the words that had given her so much pleasure when she was no longer here to enjoy them. But now, with the creditors circling and Father's hands shaking worse each day, I wondered if the book held any secrets that might save us. Some hidden value, some forgotten inscription that might make it worth more than three pounds.

I reached for it, my fingers closing around the brass clasp. It was cold, colder than I expected. The leather was soft with age, worn smooth by Mother's hands. I could almost feel her presence in the binding, in the careful stitching, in the way the pages lay flat and true. She had loved this book. She had read it every evening, by the light of the fire, while Father and I worked at our benches. She would read aloud sometimes, her voice filling the bindery with Chaucer's Middle English, making the old words sound like music.

"Whan that Aprill with his shoures soote, The droghte of March hath perced to the roote..."

I could hear her voice now, clear as if she were standing beside me. And for a moment, just a moment, I could pretend that she was. That this was any other evening, that the bindery was warm and bright, that we were a family intact rather than a family in ruins.

But the candle guttered, and the moment passed, and I was alone with the Chaucer and the creditor notices and the sound of Father's ragged breathing from the cot in the corner.

I opened the book.

The pages were yellowed but intact, the black ink still sharp against the cream paper. I turned to the first page, expecting to find the famous opening of the Canterbury Tales. Instead, I found an inscription, written in Mother's careful hand:

"For Thomas, with all my love. May this book bring you as much joy as it has brought me. — Eleanor, 1847"

1847. The year before I was born. The year before everything started to go wrong. I ran my finger over the words, feeling the slight indentation where Mother's pen had pressed into the paper. She had been happy then. We had all been happy then.

I turned another page and found a pressed flower, a violet, its color faded to brown but its shape still perfect. Mother's favorite flower. She used to press them in books, said it was a way of preserving beauty, of keeping a moment alive forever.

Forever. The word felt like a mockery now. Nothing lasted forever. Not beauty, not love, not even books. Especially not books, which were the first things to go when the creditors came calling.

I closed the Chaucer gently, carefully, as if it might break. As if I might break. I placed it back on its shelf, high up where Father's trembling hands couldn't reach it, where the creditors couldn't see it, where the world couldn't take it away from us.

Not yet. Not tonight.

Tomorrow I would make my decision. Tomorrow I would choose between the Chaucer and our survival, between Mother's memory and Father's future, between the past and whatever scraps of the future we might still claw back from the jaws of ruin.

But tonight, I would stitch. Tonight, I would bind. Tonight, I would do the only thing I knew how to do, the only thing that made sense in a world that had lost all meaning.

I picked up my needle and thread and returned to the vicar's Bible. The leather was cheap, the paper thin, but the stitching was mine. The care was mine. The love I put into every stitch was mine, and no creditor could take that away.

The candle burned lower. The night grew deeper. And I stitched, and I stitched, and I stitched, as if I could stitch our lives back together, as if I could bind our broken family as carefully as I bound this book.

But some things cannot be bound. Some things cannot be mended. Some debts cannot be paid.

And some loves, once lost, can never be recovered.

Not even by the most skilled bookbinder in all of England.

I worked through the night, the needle slipping in and out of the leather with a rhythm that was older than thought, older than words. My mother had taught me this rhythm, and her mother had taught her, and so on back through the generations of women who had bound books and bound families and bound the fragile threads of their lives together with nothing but skill and determination.

The vicar's Bible was nearly finished now. The spine was tight, the covers secure, the gold lettering on the front still legible despite the wear. It was good work. Honest work. The kind of work that would have made Mother proud.

But pride was another luxury we could not afford.

Dawn was approaching. I could see the first grey light seeping through the cracks in the shutters, and I knew that soon Father would wake, and the day would begin, and the creditors would come again, and we would face another day of pretending that we were not drowning.

I tied off the final stitch, trimmed the thread, and set the Bible aside. It was done. Another book bound, another small resurrection complete. But no amount of resurrections could bring our life back. No amount of careful stitching could mend what was broken.

I stood and stretched, my back aching from hours at the workbench. The bindery was cold, the fire having died to embers in the small grate. I should bank it, add more coal, but we were low on coal too. Everything was low. Everything was running out.

I moved to the window and looked out at the street. The village was quiet, the houses dark, the world asleep. In a few hours, the baker would light his ovens, the butcher would open his shop, the chandler would trim his wicks. In a few hours, the creditors would come.

But for now, in this moment between night and day, there was peace. For now, in this moment between what was and what would be, there was stillness.

I pressed my forehead against the cold glass and closed my eyes. I could smell the leather and the glue and the old paper. I could hear Father's breathing from the corner. I could feel the weight of the Chaucer on the shelf behind me, heavy with memory and loss and the impossible choice that awaited me.

Tomorrow. Tomorrow I would decide.

But tonight, I was still a bookbinder's daughter. Tonight, I was still a keeper of stories. Tonight, I was still a mender of broken things.

Even if some things, I was learning, could not be mended.

Even if some debts could not be paid.

Even if some loves could not be saved.

The candle finally guttered and died, leaving me in darkness. But I did not move. I stood at the window and watched the night give way to dawn, and I thought about my mother, and my father, and the Chaucer, and the creditors, and the impossible arithmetic of our survival.

And I understood, with a clarity that was almost peaceful, that we were already lost. That the bindery was already gone. That the life we had known was already over.

All that remained was to choose how we would face the end.

With dignity, I thought. With skill. With love.

With the careful stitching of a bookbinder's daughter who knew that some things, once sold, cannot be bought back, but who would try anyway.

Because that was what love was. That was what family was. That was what survival was.

Trying anyway.

Even when you knew you would fail.

Even when you knew the debt could not be paid.

Even when you knew the book could not be saved.

Trying anyway.

The dawn came. The village woke. The creditors came.

And I made my choice.

I chose the Chaucer.

I chose my mother's memory.

I chose love over survival.

And in that choice, in that impossible, irrational, beautiful choice, I found the strength to face whatever came next.

Even if what came next was the end.""", "FINCH_BINDERY", 1),
    ("S02", "The Summons Arrives", "The letter came under the door like a thief — black wax, black seal, the thorned rose pressed into it like a brand. I broke it open before I understood what I was opening. They wanted a bookbinder's daughter at Blackthorn Hall. Payment enough to clear every debt, every notice, every whisper of ruin. My father's eyes went wide when I read it aloud. Not with hope. With recognition. He said the Duke knew his name. I said not his name. Someone else's. The question sat between us like a third person in the room.", "FINCH_BINDERY", 1),
    ("S03", "The Road to Blackthorn", "The road stretched ahead of me like a warning written in frost. Every hedgerow was skeletal, every breath a small white ghost that vanished before I could name it. I walked alone with my satchel of binding tools and the weight of a decision I hadn't fully made. The milestone appeared suddenly — carved with a thorned rose, ancient and deliberate. I knew then that every story about that house ended the same way. He did it. She vanished. No one agreed on how. They all agreed it happened. I pulled my cloak tighter and kept walking.", "WINTER_ROAD", 1),
    ("S04", "The Gates of Blackthorn Hall", "The gates were taller than a man and twisted into thorned vines, black iron against a grey sky that seemed to press down on everything below it. Mrs. Varma waited in the gateway like a sentinel carved from shadow and silk. She did not smile. She did not welcome. She measured me with one look that took in my ink-stained hands and my worn boots and found something acceptable, or at least tolerable. She said I would sleep in the east wing. Not the upper corridor. The Duke does not receive callers. He receives people who answer letters. I asked what the difference was. She did not answer.", "BLACKTHORN_GATES", 1),
    ("S05", "The First Glimpse of Him", "The foyer was a cavern of candelabras and damask, every shadow longer than it should be. I removed my gloves and tried not to think about the ink still staining my fingertips. Then I looked up. He stood in the upper gallery, half-consumed by darkness, watching me with the patience of a man who had been waiting for a very long time. He did not descend. He did not speak. He simply watched, then turned and disappeared. I whispered to the empty hall that he was not surprised to see me. The echo agreed.", "BLACKTHORN_FOYER", 1),
    ("S06", "The Library That Remembered", "Two stories of shelves bowed under the weight of centuries. Dust motes hung motionless in slanting winter light. A fireplace large enough to stand in held cold ashes and the memory of warmer years. I set down my satchel and exhaled — the first full breath I had taken since arriving. This room was alive with knowledge. I touched a spine and felt something like recognition. Mrs. Varma said the late Duchess had arranged everything by feeling, not subject. I asked how long that took her to understand. She said ten years. She never did.", "BLACKTHORN_LIBRARY", 2),
    ("S07", "The Journals with Her Name", "The journals were leather-bound and cracked with age, each one a small coffin of secrets. I opened one dated thirteen years ago and began to catalogue, to organize, to make order from chaos. Then I found it — my own name. Elara Finch. Written in elegant copperplate in a margin note beside a passage on the binding of psalters. The date was ten years before I was born. My fingers trembled. I read the entry again. The ink was old. The handwriting was deliberate. This was not a coincidence. He knew. Before I existed. He wrote me down.", "BLACKTHORN_LIBRARY", 2),
    ("S08", "The Duke Watches", "Candlelight. Late. I worked without knowing he was there, without knowing I was being watched. He stood in the doorway's shadow, observing as I carefully lifted a page with a bone folder, as if I were performing surgery on something alive. He did not announce himself. I sensed him the way animals sense a storm — in the air pressure, in the sudden stillness that precedes violence or tenderness. When I turned, he was already gone. Only the scent of cold wool and smoke remained. I whispered that he was always there, just behind the edge of seeing.", "BLACKTHORN_LIBRARY", 2),
    ("S09", "The Gallery of Dead Wives", "The corridor of portraits stretched longer than I expected, each face watching me with painted eyes that never blinked. Lucy showed me the house by stolen candlelight, her breath fogging in the cold. We stopped before a painting of Lady Margaret — white satin gown, pearl choker, emerald pendant at her throat. The eyes were dark and knowing. Lucy said they claimed the Duke locked himself in here for a year after she died. I asked how she died. Lucy said that was the question no one answered twice the same way. I looked at my own reflection in the gilt frame and did not like the comparison.", "BLACKTHORN_GALLERY", 2),
    ("S10", "The First Touch", "I fell asleep at the reading desk, a book open against my cheek, unaware of the figure who entered silently. He stood over me, his shadow falling across the page. His gloved hand reached down — not to shake me, not to wake me, but to brush a stray auburn curl from my forehead. His finger grazed my temple. I stirred. Our eyes met across the smallest distance. Neither moved. The candle between us guttered. His voice, when it came, was barely audible. You are exactly as I wrote you. I did not know whether to be terrified or flattered. Perhaps both.", "BLACKTHORN_LIBRARY", 2),
    ("S11", "The Contract on the Desk", "A desk of black oak. A single document. He stood behind it, hands braced on the wood, signet ring catching the firelight. The contract read: all Finch family debts cleared, father's workshop preserved, in exchange for one winter as his Duchess. In name, in public, in residence. No conjugal obligation. No permanent arrangement. I could leave at spring thaw. I asked him why me. He said because I was always the answer. He simply had to wait for the question to arrive. I did not know whether to believe him or run.", "BLACKTHORN_STUDY", 3),
    ("S12", "The Fake Engagement", "A long table set for two, though the house held twenty. Mrs. Varma stood behind my chair, adjusting my collar with proprietary hands. Lucy peeked from the serving doorway, wide-eyed. The Duke took his seat and did not look at me until I was settled, then held my gaze with an intensity that made the candlelight seem dim. He said I would call him Silas in private. In public, I would call him Your Grace and allow no one to see me smile first. I asked what would happen if I smiled first. He said he would spend the evening making it worth the scandal.", "BLACKTHORN_DINING_HALL", 3),
    ("S13", "The Jealousy at the Hunt Ball", "The ballroom glittered with candlelight and crystalline pretense, the local gentry dressed in jewels and calculated indifference. Julian appeared in burgundy velvet, claiming me for a dance with the ease of a man who had never been refused. His hand settled at my waist. Across the room, the Duke watched, a glass of brandy untouched in his hand. Julian asked why I was trembling. I said his cousin's moods were not a difficult text. Julian smiled and said, Then why are you trembling? The Duke crossed the room. He did not dance. He took my hand from Julian's waist and placed it on his own coat.", "BLACKTHORN_BALLROOM", 3),
    ("S14", "The Secret of the First Wife", "I found the locked drawer and forced it open with a bone folder. Inside: letters from Lady Margaret's brother describing his sister's slow poisoning, and a doctor's note that the Duke refused an autopsy. I confronted him. He did not deny the letters. He said they were incomplete. I asked if he killed her. He said she asked him to let her go and he held on too tightly. That was the closest thing to murder he had committed. I asked what about me. A long silence. The fire popped. He said I was the only thing he had ever been afraid to hold.", "BLACKTHORN_STUDY", 3),
    ("S15", "The Agreement", "Winter light turned the library gold. I stood by the window, the contract in my hands. He waited by the fireplace, still as a portrait. I had read every clause. I had found the escape clause: I could leave at spring, with my father's debts cleared, no conditions. I folded the document slowly. I told him I would stay the winter. Not because of the debt. Because I needed to know if what he wrote in those journals was true, or if I was just the woman who looked enough like a ghost to fill the space. He crossed the room and stopped exactly one arm's length from me. He said I was never a ghost. I was the only living thing he could imagine in this house.", "BLACKTHORN_LIBRARY", 3),
    ("S16", "The Betrayal", "Julian found me alone and smiled like a man who enjoyed delivering poison. He revealed that the Duke's journals contained entries not about love — but about ownership. He had been watching me since I was a child, arranging circumstances to bring me here. Julian showed me a page: the Duke purchased my father's debt from the original creditor three years ago. I was never summoned — I was harvested. Julian said I was not a bride. I was a collection. The Duke entered. He did not deny it.", "BLACKTHORN_STUDY", 4),
    ("S17", "The Fire in the East Wing", "My room. I had packed my satchel. The smell of smoke seeped under the door before I understood what it meant. The east wing corridor filled with orange light. Lucy screamed from the stairwell. Mrs. Varma appeared, pressing a key into my hand — a servants' exit. She said go, now, do not look for him. Lucy said the fire started in the gallery, the portraits were burning. I ran through smoke, the key cold in my palm, and did not look at the burning gallery where Lady Margaret's portrait turned to ash.", "BLACKTHORN_EAST_WING", 4),
    ("S18", "She Tries to Flee", "I stumbled through snow beyond the grounds, my green dress stained with soot, my brass thimble swinging against my collarbone. The frost bit through my boots. I had gone perhaps a mile when I realized I had been walking in a circle — the frost showed my own footprints ahead of me. The grounds of Blackthorn were larger than I understood. Or something was keeping me contained. I stopped. My breath came in white clouds. I was alone. I was lost. I was furious. I whispered that I would not be the ghost, I would not be the collection, I would not be the thing he wrote.", "BLACKTHORN_GROUNDS", 4),
    ("S19", "He Lets Her Go", "The iron gates. I reached them at first light, exhausted, smoke-stained. The Duke stood on the other side. He had a horse saddled, a traveling cloak folded over its back, a letter of transit in his hand. He had not come to stop me. He had come to arm me. He said he bought the debt because he could not bear the thought of me starving while he did nothing. He said he did not arrange me. He waited for me. There was a difference and he knew it did not excuse anything. He opened the gate. He said go. If I returned, it must be because I chose to. Not because I had nowhere else.", "BLACKTHORN_GATES", 4),
    ("S20", "The Distance Between", "A village inn. I sat by a fire, wrapped in the traveling cloak the Duke gave me though I had tried to return it. Father Benedict brought me tea and sat without invitation. He had known the Duke for decades. He had known grief. He said the Duke came to him after Margaret died and asked how to stop loving what he could not save. I asked what he chose. Father Benedict said he chose to wait. For ten years, he chose to wait. That was not obsession, child. That was the only patience he had ever seen that deserved to be called love.", "VILLAGE_INN", 4),
    ("S21", "The Return on Her Own Terms", "I returned to the gates. Not in the cloak he gave me — I had returned it. I wore my own forest-green dress, clean but worn, my satchel over my shoulder. I carried no contract. I carried nothing except myself. Mrs. Varma opened the gate without being asked. The Duke stood in the gravel drive, uncovered by hat or hood, snow catching in his too-long black hair. He had been waiting. He had always been waiting. I told him I did not come back for the contract. He said he knew. I said I came back because the alternative was a lifetime of listening for his footsteps and pretending I did not miss them.", "BLACKTHORN_GATES", 5),
    ("S22", "The Consummation", "His private chambers. High windows black with winter night, a fire low and amber. I stood before him. No contract between us now. No audience. No bargain. He removed his gloves slowly, finger by finger. His bare hands took my face as if I were a text he had been trying to read for a decade and had only now learned the language. He said say my name. I said Silas. He closed his eyes. It was the first time he had heard his own name spoken like a prayer.", "BLACKTHORN_CHAMBERS", 5),
    ("S23", "The Public Claiming", "A second ball — this one my choice. I entered on the Duke's arm, not as contract bride but as chosen Duchess. Julian watched from the crowd, his smile sharp enough to cut. Mrs. Varma stood at the door, and for the first time, she smiled. Lucy caught my eye from behind the refreshment table and mouthed: finally. The Duke led me to the center of the floor and did not let go. He whispered that they could stare, they could write it down, Julian could tell every version he liked. They would never be able to say he did not ask. I said he asked every day. I simply could not hear it until I was ready to answer.", "BLACKTHORN_BALLROOM", 5),
    ("S24", "The Marriage", "A small village church, snow on the windowsills. Not a cathedral performance but a true thing. My father walked me down the aisle, his hands steadier than they had been in years. Lucy held the flowers. Mrs. Varma stood as witness for the house. Father Benedict spoke the words with a voice that cracked on the word join. The Duke's signet ring was warm against my finger as he slid it on — beside my brass thimble chain, beside the ink that would never wash out. I said I do. He said he always had.", "VILLAGE_CHURCH", 5),
    ("S25", "The True Duchess", "Years later. The same library, but alive now — curtains drawn back, fire lit, books opened and scattered. I sat in the reading chair with a child balanced on my knee, pointing at gold lettering on a page. The Duke stood behind me, his hand on the chair's back, his signet ring catching light that fell through winter glass. The room smelled of old paper and beeswax and woodsmoke. The thorned rose crest was carved into the chair's armrest, but now it looked less like a warning and more like a welcome. I read aloud to the child: And the Duke kept his word. Every word. Every winter. Every one. The Duke said not every word. He told me once that he would survive without me. I said that was the only lie he ever told. The child laughed. The fire crackled.", "BLACKTHORN_LIBRARY", 5),
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
            html.append(f'<div class="voiceover">{info["voiceover"]}</div>')
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
