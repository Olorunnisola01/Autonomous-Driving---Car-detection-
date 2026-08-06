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

The bindery had been our home for as long as I could remember, though 'home' was perhaps too generous a word for a place that smelled perpetually of turpentine and despair. Father's hands, once steady enough to thread a needle in dim light, now shook so badly he could barely hold the awl. The tremor had started three years ago, around the time the last of Mother's jewelry disappeared into the pawnbroker's till. Since then, the shaking had spread from his hands to his voice, from his voice to his spirit, until the man who had once taught me to distinguish between calfskin and goatskin by touch alone could barely meet my eyes.

I worked by the light of a single tallow candle, its flame guttering in the draft that seeped through the cracks in the walls. The Bible I was rebinding belonged to the vicar's wife, who had paid us in stale bread and the promise of prayers. It was honest work, if poorly compensated, and I had learned to find a kind of peace in the rhythm of needle and thread, in the careful folding of signatures, in the patient application of paste to leather. Each book was a small resurrection, a dead thing brought back to life through skill and care.

But no amount of skill could resurrect our fortunes. The creditors came every week now, their notices papering the walls like autumn leaves, each one more urgent than the last. The butcher had stopped extending credit. The baker demanded payment before delivery. Even the chandler now required coin before surrendering his candles. We were drowning, and I was the only one who seemed to notice the water rising.

The Chaucer sat on the highest shelf, its brass clasps gleaming dully in the candlelight. It had been Mother's favorite, a first edition she had purchased with her dowry money, back when such things still mattered. Father had forbidden me to touch it, saying it was the last thing of beauty in our lives. But beauty, I had learned, was a luxury we could no longer afford.

'We can sell it,' I said again, keeping my voice gentle, the way one speaks to a wounded animal. 'The brass alone is worth something. And the pages — they're old, Father. Someone might pay for the paper alone.'

He looked up from his work, his eyes red-rimmed and haunted. 'Your mother loved that book,' he said, as if that settled the matter. As if love were a currency we could spend.

'Then it is worth more alive than dead,' I replied, and we both knew I was lying. The Chaucer would fetch perhaps three pounds at the bookseller's, enough to keep us for a month, perhaps two if we were careful. But then what? There would be another debt, another notice, another winter.

I returned to my stitching, the needle slipping in and out of the leather with practiced ease. My fingers were stained with ink, permanently marked by the trade I had learned at my mother's knee. She had been a bookbinder too, before the cough took her, before the medicine costs bankrupted us, before the slow unraveling of everything we had been. I had her hands, people said. I had her patience. But I also had her stubbornness, her refusal to accept that some things cannot be mended no matter how carefully you stitch them.

The candle guttered lower, casting long shadows that danced on the walls like ghosts. Outside, the wind howled through the bare branches of the elms, and I could hear the distant clang of the church bell marking the hour. Midnight. Another day survived, another day closer to ruin. I tied off the thread, trimmed the excess with my shears, and set the Bible aside. Tomorrow I would deliver it to the vicar's wife and collect my stale bread. Tomorrow I would face the creditors again. Tomorrow I would pretend that we were not drowning.

But tonight, in the flickering candlelight, with my father's trembling hands and the ghost of my mother's Chaucer watching over us, I allowed myself a moment of honesty. We were finished. The bindery was finished. The life we had known was finished. And no amount of careful stitching could mend what was broken beyond repair. Some things, once sold, cannot be bought back. But some things, once lost, cannot be kept either. And I was beginning to understand that love — for a father, for a mother, for a life that no longer existed — was the most expensive thing of all.""", "FINCH_BINDERY", 1),
    ("S02", "Unknown", """The letter came under the door like a thief — black wax, black seal, the thorned rose pressed into it like a brand. I broke it open before I understood what I was opening. The parchment was thick, expensive, the kind of paper that cost more than a week of our bread. They wanted a bookbinder's daughter at Blackthorn Hall. Payment enough to clear every debt, every notice, every whisper of ruin. My father's eyes went wide when I read it aloud. Not with hope. With recognition. He said the Duke knew his name. I said not his name. Someone else's. The question sat between us like a third person in the room.

The seal was heavy in my hand, the wax cold and dark. The thorned rose was intricate, beautiful in a cruel way, the kind of beauty that suggested power rather than grace. I had heard the name Blackthorn before, of course. Everyone in the village had. The Duke of Blackthorn, the reclusive widower, the man who lived in the manor on the hill and never came down. They said he was mad. They said he was cruel. They said he had killed his wife. But they also said he was rich. And rich men paid their debts.

I read the letter again, my lips moving silently over the elegant, spidery script. 'To Mr. Thomas Finch,' it began, formal and cold. 'It has come to our attention that your daughter, Elara Finch, possesses skills in the art of bookbinding that may be of service to the Duke of Blackthorn. The Duke requires a cataloguer for his library, a task of some magnitude and delicacy. Compensation shall be provided upon completion, sufficient to satisfy all outstanding obligations.'

Outstanding obligations. A polite way of saying debts. A polite way of saying we were ruined.

Father was sitting on his cot, his hands resting on his knees, his eyes fixed on the floor. He had not moved since I read the letter aloud. The silence in the room was absolute, save for the ticking of the clock on the mantel and the distant sound of the wind outside.

'He knows my name,' Father said finally, his voice barely a whisper.

'Who?' I asked, though I knew.

'The Duke. He knows my name.'

I looked at him, really looked at him. His face was pale, his eyes wide and terrified. He looked like a man who had seen a ghost. Or a man who was about to become one.

'How?' I asked.

He shook his head, a small, jerky movement. 'I don't know. I don't know.'

I looked back at the letter. The paper was heavy, the ink black and sharp. It was a summons. A command. A lifeline.

'I'll go,' I said.

Father looked up, his eyes snapping to mine. 'No.'

'I have to.'

'No,' he said again, stronger this time. 'You don't understand. You don't know what you're walking into.'

'I know we're drowning,' I said, my voice steady, hard. 'I know the creditors are coming. I know we have nothing left to sell but the Chaucer, and you won't let me sell that. This is the only way.'

He stared at me, his chest heaving, his hands trembling on his knees. He looked like he wanted to argue, to forbid me, to lock the door and keep me safe. But he was a broken man, and he knew it. He had no power left to forbid me anything.

'It's not safe,' he whispered.

'Neither is starving,' I replied.

I folded the letter carefully, sliding it into my pocket. It felt heavy there, like a stone. Like a sentence. I began to pack my satchel. My tools. My needles. My thread. My paste. My knives. The things that made me a bookbinder. The things that might save us.

Father watched me, his eyes following my every movement. He didn't help. He didn't speak. He just watched, with the look of a man who knew he was sending his daughter to the slaughter. I didn't look at him. I couldn't. If I looked at him, I might change my mind. And if I changed my mind, we would lose everything.

I packed the satchel. I put on my cloak. I picked up my bag. 'I'll be back,' I said, though I didn't know if it was true. 'When the debt is paid, I'll be back.'

Father didn't answer. He just closed his eyes and turned his face to the wall.

I walked to the door. I opened it. The wind howled outside, cold and sharp. The village was dark, the streets empty. The manor on the hill was a black shape against the grey sky. I stepped out into the cold. And I began to walk.""", "UNKNOWN", 1),
    ("S03", "Unknown", """The road stretched ahead of me like a warning written in frost. Every hedgerow was skeletal, every breath a small white ghost that vanished before I could name it. I walked alone with my satchel of binding tools and the weight of a decision I hadn't fully made. The milestone appeared suddenly — carved with a thorned rose, ancient and deliberate. I knew then that every story about that house ended the same way. He did it. She vanished. No one agreed on how. They all agreed it happened. I pulled my cloak tighter and kept walking.

The cold was a physical thing, a weight that pressed against my chest and made it hard to breathe. The wind cut through my wool dress, through my cloak, through the layers of petticoats I wore against the chill. It felt like the cold was trying to find the heat in my body and extinguish it, just as the creditors were trying to find the last remnants of our life and extinguish them.

My boots crunched on the frozen ground, a rhythmic sound that was the only company I had. The village was far behind me now, a cluster of grey roofs and smoking chimneys that looked small and fragile from this distance. I didn't look back. Looking back was a luxury for people who had something to return to. I had nothing.

The landscape was bleak, stripped of color by the winter. The trees were black bones against the grey sky, their branches reaching out like skeletal fingers trying to grab me, to pull me back, to warn me away. I ignored them. I had made my choice. I had chosen the Chaucer. I had chosen my father's pride. I had chosen the unknown over the slow, certain death of our life in the village.

The milestone was old, the stone pitted and worn by years of wind and rain. The thorned rose was carved deep, the petals sharp and dangerous. It was a warning, I realized. A marker. Here begins the territory of the Duke. I ran my gloved hand over the carving, feeling the rough stone, the sharp edges of the thorns. It felt like touching a weapon.

I pulled my cloak tighter, wrapping it around my shoulders, pulling the hood up over my head. The wind howled through the hedgerows, a high, keening sound that sounded almost like a voice. Turn back, it seemed to say. Turn back while you can.

I didn't turn back. I couldn't. The debt was too great. The ruin too complete. The only way forward was through the gate, into the house, to the Duke. To the man who knew my father's name. To the man who had sent the letter.

The road wound upward now, climbing the hill toward the manor. The trees grew thicker, closer together, their branches interlacing overhead to form a tunnel of black wood. The light grew dimmer, the shadows longer. I felt like I was walking into a mouth. Into a throat. Into a stomach that would digest me and leave nothing behind.

But I kept walking. One foot in front of the other. One step after another. The rhythm of my boots on the frozen ground became a kind of mantra. I am a bookbinder's daughter. I am a keeper of stories. I am a mender of broken things.

Even if I couldn't mend this. Even if I couldn't save us. Even if I was walking into the dark.

I kept walking.""", "UNKNOWN", 1),
    ("S04", "Unknown", """The gates were taller than a man and twisted into thorned vines, black iron against a grey sky that seemed to press down on everything below it. Mrs. Varma waited in the gateway like a sentinel carved from shadow and silk. She did not smile. She did not welcome. She measured me with one look that took in my ink-stained hands and my worn boots and found something acceptable, or at least tolerable. She said I would sleep in the east wing. Not the upper corridor. The Duke does not receive callers. He receives people who answer letters. I asked what the difference was. She did not answer.

The gates groaned as she pushed one open, a sound like a dying animal, iron grinding against iron. The sound set my teeth on edge. I stepped through the gap, my boots crunching on the gravel drive. The gravel was pale, almost white, like crushed bone. I tried not to think about that. I tried not to think about anything except the task ahead. The cataloguing. The payment. The survival.

Mrs. Varma turned and walked toward the house. She moved with a strange, gliding grace, her black silk dress whispering against the stone path. I followed her, my satchel heavy on my shoulder. The house loomed ahead, a massive structure of dark stone, its windows like empty eyes staring down at me. It looked less like a home and more like a fortress. A tomb.

The air around the house was different. Colder. Still. The wind that had howled through the trees seemed to die here, as if the house itself absorbed the sound, the movement, the life. It was a place of silence. Of waiting.

We reached the front door. It was enormous, dark wood with iron studs, the thorned rose carved into the center. Mrs. Varma produced a key from the ring at her waist — there were so many keys, I realized, dozens of them, clinking together like chains — and unlocked the door. It swung open without a sound.

The foyer beyond was vast. I stepped inside and felt the size of the place press against me, a physical weight. The ceiling was lost in shadow, the walls lined with dark wood and heavy tapestries. Candelabras stood on tables and sconces, their candles unlit, waiting. The smell of the house was old. Dust and wax and something else, something metallic and sharp.

Mrs. Varma turned to face me. Her eyes were dark, unreadable. 'Your room is at the end of the east corridor,' she said, her voice flat, devoid of inflection. 'You will find everything you need. Dinner is at eight. Do not be late.'

'And the library?' I asked. 'When do I begin?'

She looked at me, and for a moment, something flickered in her eyes. Pity? Warning? I couldn't tell. 'The Duke will summon you when he is ready,' she said. 'Until then, you stay in your room. You do not wander. You do not explore. You do not go to the upper corridor.'

'Why?' I asked.

She didn't answer. She simply turned and walked away, her footsteps silent on the stone floor. I was left alone in the vast, dark foyer, the door closed behind me, the silence pressing in.

I looked up at the staircase. It curved upward into the shadows, the banister dark and polished. I had the distinct, unsettling feeling that I was being watched. I scanned the upper gallery, the shadows, the corners. Nothing. No one.

But the feeling remained. The sense of eyes on me. Of a presence in the dark.

I picked up my satchel and began to look for the east corridor.""", "UNKNOWN", 1),
    ("S05", "Unknown", """The foyer was a cavern of candelabras and damask, every shadow longer than it should be. I removed my gloves and tried not to think about the ink still staining my fingertips. Then I looked up. He stood in the upper gallery, half-consumed by darkness, watching me with the patience of a man who had been waiting for a very long time. He did not descend. He did not speak. He simply watched, then turned and disappeared. I whispered to the empty hall that he was not surprised to see me. The echo agreed.

I had been standing at the foot of the staircase for perhaps ten minutes, debating whether to explore or obey Mrs. Varma's strict instructions to stay in my room. The silence of the house was absolute, save for the ticking of a grandfather clock somewhere in the distance. It was a loud, rhythmic sound, like a heartbeat. Or a countdown.

Then I felt it. The shift in the air. The prickle on the back of my neck. The instinct that told me I was not alone.

I looked up.

He was there. Standing in the shadows of the upper gallery, one hand resting on the dark wood of the banister. He was tall, broader than I had expected, his silhouette sharp against the dim light from the windows. He wore a dark coat, the silver buttons catching the faint light. His hair was black, slightly too long, falling across his forehead.

But it was his eyes that held me. Even from this distance, even in the shadows, I could feel the weight of his gaze. It was a physical thing, heavy and intense. It wasn't the look of a stranger. It was the look of a man who knew me. Who had known me for a long time.

My breath caught in my throat. I wanted to speak, to ask who he was, though I knew. I wanted to run, to retreat to the safety of the east wing. But my feet were rooted to the spot. I was pinned by his gaze, held in place by the sheer force of his attention.

He didn't move. He didn't blink. He just watched me, his expression unreadable, his face a mask of aristocratic stillness. The seconds stretched, becoming minutes, becoming an eternity. The silence of the house grew heavier, thicker, until I thought I might suffocate.

Then, slowly, deliberately, he turned. He stepped back into the shadows of the gallery and was gone.

I let out a breath I didn't know I was holding. My hands were shaking. My heart was hammering against my ribs. I looked up at the empty gallery, the dark wood, the shadows.

'You were not surprised to see me,' I whispered to the empty hall.

The echo of my own voice came back to me, faint and distorted, bouncing off the stone walls, the dark wood, the high ceiling. It sounded like agreement.

I turned and walked quickly toward the east corridor, my boots loud on the stone floor. I didn't look back. I didn't want to see if he was watching me again. But I knew he was. I knew he would be watching me for a long time to come.""", "UNKNOWN", 1),
    ("S06", "Unknown", """Two stories of shelves bowed under the weight of centuries. Dust motes hung motionless in slanting winter light. A fireplace large enough to stand in held cold ashes and the memory of warmer years. I set down my satchel and exhaled — the first full breath I had taken since arriving. This room was alive with knowledge. I touched a spine and felt something like recognition. Mrs. Varma said the late Duchess had arranged everything by feeling, not subject. I asked how long that took her to understand. She said ten years. She never did.

The library was vast. That was the first thing that struck me — not the beauty, not the age, but the sheer, overwhelming scale of it. The shelves rose two stories high, connected by a wrought-iron gallery that ran along the upper level like a balcony in a cathedral. The books were everywhere, floor to ceiling, their spines a patchwork of faded leather and tarnished gold. Some were chained to the shelves. Some were stacked horizontally, as if they had been placed there in haste and never moved.

The air smelled of old paper and beeswax, with an undertone of something sharper — damp stone, perhaps, or the ghost of woodsmoke from the great fireplace that dominated the far wall. The fire was dead, the hearth cold, but I could imagine it blazing, could imagine someone sitting in one of the leather chairs with a book and a glass of something amber, reading while the flames danced.

Dust motes drifted through the shafts of winter light that fell from the tall windows. They moved slowly, almost languidly, as if time itself was thicker here, more viscous. I stood in the center of the room and turned slowly, taking it all in. This was what I had come for. This was the task that would save us.

I walked to the nearest shelf and ran my hand along the spines. The leather was cool, soft with age. I could feel the texture of the binding, the slight irregularities that told me these were hand-bound volumes, crafted by someone who understood their art. My fingers tingled. I wanted to open them, to read them, to lose myself in their pages.

But that wasn't why I was here. I was here to catalog, to organize, to make order from chaos. I pulled my satchel closer and set it on a reading desk near the window. I took out my notebooks, my pens, my measuring tape. I was ready to work.

Mrs. Varma appeared in the doorway, silent as always. 'The late Duchess arranged everything by feeling, not subject,' she said, her voice flat. 'You will find no logic to it. No system.'

'How long did it take you to understand?' I asked.

She looked at me, and for a moment, something flickered in her dark eyes. 'Ten years,' she said. 'I never did.'

Then she was gone, leaving me alone with the books and the dust and the silence. I opened my notebook and began.""", "UNKNOWN", 1),
    ("S07", "Unknown", """The journals were leather-bound and cracked with age, each one a small coffin of secrets. I opened one dated thirteen years ago and began to catalogue, to organize, to make order from chaos. Then I found it — my own name. Elara Finch. Written in elegant copperplate in a margin note beside a passage on the binding of psalters. The date was ten years before I was born. My fingers trembled. I read the entry again. The ink was old. The handwriting was deliberate. This was not a coincidence. He knew. Before I existed. He wrote me down.

I had been working for three days now, and the library was beginning to yield its secrets. Not the secrets I had expected — the hidden compartments, the coded messages, the scandalous letters — but the quieter secrets of a life lived among books. The Duchess had been a reader, a collector, a woman who understood that books were more than objects. They were companions.

The journals were different. They were the Duke's, I realized, though they bore no name. The handwriting was sharp, precise, the copperplate so perfect it looked almost printed. He had written them over the course of decades, one for each year, recording his thoughts, his observations, his... what? Not quite a diary. More like a ledger of the mind.

I opened the journal dated thirteen years ago, expecting to find accounts of the Duchess, of their life together, of the events that had led to her death. Instead, I found pages of meticulous notes on bookbinding techniques. The Duke was studying the craft, learning it, mastering it. Why? I turned the pages, reading entries about leather types, stitching methods, the chemistry of adhesives. It was obsessive in its detail.

And then I saw it. My name. Elara Finch. Written in the margin beside a passage about the binding of psalters. The date in the header was 1837. I was born in 1847. Ten years after this was written.

My breath caught. I stared at the name, at the elegant curves of the letters, at the ink that had dried more than a decade before I drew my first breath. This was impossible. And yet, here it was. My name, in his hand, in a journal written before I existed.

I read the entry again. And again. The handwriting was deliberate, careful, as if he had known this would be found. As if he had wanted it to be found.

I closed the journal slowly, my hands shaking. I looked around the library, at the shelves of books, at the dust motes drifting in the winter light. The room felt different now. Heavier. Watched.

He knew. Before I existed. He wrote me down.

And I didn't know what that meant.""", "UNKNOWN", 1),
    ("S08", "Unknown", """Candlelight. Late. I worked without knowing he was there, without knowing I was being watched. He stood in the doorway's shadow, observing as I carefully lifted a page with a bone folder, as if I were performing surgery on something alive. He did not announce himself. I sensed him the way animals sense a storm — in the air pressure, in the sudden stillness that precedes violence or tenderness. When I turned, he was already gone. Only the scent of cold wool and smoke remained. I whispered that he was always there, just behind the edge of seeing.

The library at night was a different place. The winter light faded early, and by four o'clock the room was dark save for the candles I had lit on the reading desk. The flames cast long, dancing shadows on the shelves, making the books seem to move, to breathe. I worked by their light, cataloguing, measuring, recording. The silence of the house was absolute, save for the scratch of my pen and the occasional creak of the old building settling.

I was so absorbed in my work that I didn't notice him at first. Not his presence, not his weight in the room. But something changed. The air grew heavier, thicker, as if the pressure had dropped. The candles flickered, though there was no draft. The hair on the back of my neck prickled.

I turned slowly, my bone folder still in my hand, and saw him. He stood in the doorway, half-consumed by shadow, one hand resting on the doorframe. He was perfectly still, perfectly silent. His dark coat blended with the darkness, but his face was visible, pale and sharp in the candlelight. His eyes were fixed on me.

He had been watching me work. For how long, I didn't know. Minutes? Hours? The thought sent a shiver down my spine. He had been standing there, silent and still, observing me as I touched his books, as I turned the pages of his journals, as I wrote his secrets in my notebooks.

He didn't speak. He didn't move. He just watched.

I stood, my chair scraping against the stone floor, the sound loud in the silence. 'Your Grace,' I said, my voice steadier than I felt.

He tilted his head slightly, as if considering my words. Then, slowly, deliberately, he stepped back into the shadows of the corridor and was gone.

I walked to the doorway and looked out. The corridor was empty, dark. But the scent of him lingered — cold wool, woodsmoke, something metallic and sharp. He had been here. He had watched me. And then he had vanished.

I returned to my desk and sat down, my hands shaking slightly. I picked up my pen and tried to continue my work. But the words wouldn't come. All I could think was: he was always there. Just behind the edge of seeing.

And I didn't know whether to be terrified or flattered.""", "UNKNOWN", 1),
    ("S09", "Unknown", """The corridor of portraits stretched longer than I expected, each face watching me with painted eyes that never blinked. Lucy showed me the house by stolen candlelight, her breath fogging in the cold. We stopped before a painting of Lady Margaret — white satin gown, pearl choker, emerald pendant at her throat. The eyes were dark and knowing. Lucy said they claimed the Duke locked himself in here for a year after she died. I asked how she died. Lucy said that was the question no one answered twice the same way. I looked at my own reflection in the gilt frame and did not like the comparison.

Lucy found me in the library after dinner, her candle flickering in the draft. 'You shouldn't be working so late,' she said, her voice low. 'Not in this house. Not after dark.'

I looked up from my notebooks. 'Why?'

She hesitated, glancing over her shoulder as if someone might be listening. 'The house is different at night. The Duke... he walks. You don't want to encounter him in the corridors.'

I set down my pen. 'Show me the house,' I said. 'Show me what I'm living in.'

She led me out of the library and down the east corridor, her candle casting long shadows on the walls. We passed closed doors, dark staircases, rooms I hadn't yet explored. The house was vast, labyrinthine, and in the candlelight it felt like a place that had been abandoned, left to decay.

Then we reached the portrait gallery. It was a long corridor, the walls lined with paintings from floor to ceiling. The faces stared down at me — stern men in dark coats, severe women in high collars, children with solemn eyes. The Blackthorn lineage, I realized. Generations of Dukes and Duchesses, all watching, all judging.

Lucy stopped before one painting. 'This is her,' she said quietly. 'Lady Margaret. The first Duchess.'

I looked at the portrait. She was beautiful, in a cold, distant way. Raven-black hair, porcelain skin, eyes that seemed to look right through me. She wore a white satin gown, a pearl choker at her throat, and a dark emerald pendant that caught the candlelight. She looked like a ghost. Like a warning.

'They say he locked himself in here for a year after she died,' Lucy said. 'A whole year. No one saw him. No one spoke to him. He just... existed.'

'How did she die?' I asked.

Lucy was quiet for a long moment. 'That's the question no one answers twice the same way,' she said finally. 'Some say illness. Some say accident. Some say...' She stopped, shook her head. 'It doesn't matter. She's gone.'

I looked at the portrait again, at the dark eyes that seemed to follow me. And then I saw it — my own reflection in the gilt frame, superimposed over Lady Margaret's face. The auburn hair, the pale skin, the wide eyes. We looked alike. Too alike.

I stepped back from the painting, my heart hammering. 'We should go,' I said.

Lucy nodded, and we hurried back down the corridor, the portraits watching us go. But I couldn't shake the feeling that one of them — the one with the emerald pendant — was still watching me. Still waiting.

And I didn't know what she wanted.""", "UNKNOWN", 1),
    ("S10", "Unknown", """I fell asleep at the reading desk, a book open against my cheek, unaware of the figure who entered silently. He stood over me, his shadow falling across the page. His gloved hand reached down — not to shake me, not to wake me, but to brush a stray auburn curl from my forehead. His finger grazed my temple. I stirred. Our eyes met across the smallest distance. Neither moved. The candle between us guttered. His voice, when it came, was barely audible. You are exactly as I wrote you. I did not know whether to be terrified or flattered. Perhaps both.

I had been working for fourteen hours straight. The journal with my name in it lay open on the desk, and I had been staring at it for so long that the words had begun to blur, to swim before my eyes. I tried to focus, to make sense of what I had found, but my mind was exhausted, my body aching. The candle had burned low, the flame flickering weakly.

I rested my head on my arms, just for a moment, just to close my eyes. The leather of the journal was cool against my cheek. The smell of old paper filled my nostrils. And I fell asleep.

I don't know how long I slept. Minutes, perhaps. Maybe an hour. But when I stirred, when I became aware of my surroundings again, something was different. The air was heavier. The silence was deeper. And there was a shadow falling across the page, blocking the candlelight.

I opened my eyes slowly, and he was there. Standing over me, so close that I could feel the warmth of his body, could smell the cold wool of his coat, the woodsmoke in his hair. His shadow fell across the open journal, across my name written in his hand.

He was looking down at me, his dark eyes intent, unreadable. His gloved hand was raised, hovering above my face. I froze, my breath caught in my throat. I thought he was going to wake me, to speak, to demand to know what I was doing in his library, in his journals, in his life.

But he didn't. Instead, slowly, carefully, his gloved finger reached down and brushed a stray curl of auburn hair from my forehead. The touch was feather-light, almost reverent. His finger grazed my temple, and I shivered.

I stirred, opening my eyes fully, and we looked at each other across the smallest distance. His face was inches from mine, his dark eyes searching mine, reading me the way I had been reading his journals. Neither of us moved. Neither of us breathed. The candle between us guttered, the flame dancing in the silence.

Then he spoke, his voice barely audible, a whisper that seemed to come from the shadows themselves. 'You are exactly as I wrote you.'

The words hung in the air between us, heavy with meaning, with implication, with something I couldn't name. He stepped back, slowly, deliberately, and turned away. I watched him go, watched him disappear into the shadows of the library, leaving me alone with the guttering candle and the open journal and the echo of his words.

You are exactly as I wrote you.

I sat there for a long time, my hand touching the spot on my temple where his finger had grazed my skin. And I didn't know whether to be terrified or flattered. Perhaps both. Perhaps that was the point.""", "UNKNOWN", 1),
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
