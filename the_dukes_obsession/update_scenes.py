import re

# New Voiceover Texts (Target: ~2,800 chars each)

S01_TEXT = """I learned to count debts the way other girls counted stitches — by candlelight, by the tremor in my father's hands, by the silence that grew thicker than the leather we bound. The workshop smelled of old paper and desperation, of glue and grief and the slow decay of things that once mattered. Every creditor notice on the wall was another winter we might not survive, another nail in the coffin of the life we'd once known. I told him we could sell the Chaucer. He said Mother loved it. I said it was worth more alive than dead. We both knew I was lying. Some things, once sold, cannot be bought back.

The bindery had been our home for as long as I could remember, though 'home' was perhaps too generous a word for a place that smelled perpetually of turpentine and despair. Father's hands, once steady enough to thread a needle in dim light, now shook so badly he could barely hold the awl. The tremor had started three years ago, around the time the last of Mother's jewelry disappeared into the pawnbroker's till. Since then, the shaking had spread from his hands to his voice, from his voice to his spirit, until the man who had once taught me to distinguish between calfskin and goatskin by touch alone could barely meet my eyes.

I worked by the light of a single tallow candle, its flame guttering in the draft that seeped through the cracks in the walls. The Bible I was rebinding belonged to the vicar's wife, who had paid us in stale bread and the promise of prayers. It was honest work, if poorly compensated, and I had learned to find a kind of peace in the rhythm of needle and thread, in the careful folding of signatures, in the patient application of paste to leather. Each book was a small resurrection, a dead thing brought back to life through skill and care.

But no amount of skill could resurrect our fortunes. The creditors came every week now, their notices papering the walls like autumn leaves, each one more urgent than the last. The butcher had stopped extending credit. The baker demanded payment before delivery. Even the chandler now required coin before surrendering his candles. We were drowning, and I was the only one who seemed to notice the water rising.

The Chaucer sat on the highest shelf, its brass clasps gleaming dully in the candlelight. It had been Mother's favorite, a first edition she had purchased with her dowry money, back when such things still mattered. Father had forbidden me to touch it, saying it was the last thing of beauty in our lives. But beauty, I had learned, was a luxury we could no longer afford.

'We can sell it,' I said again, keeping my voice gentle, the way one speaks to a wounded animal. 'The brass alone is worth something. And the pages — they're old, Father. Someone might pay for the paper alone.'

He looked up from his work, his eyes red-rimmed and haunted. 'Your mother loved that book,' he said, as if that settled the matter. As if love were a currency we could spend.

'Then it is worth more alive than dead,' I replied, and we both knew I was lying. The Chaucer would fetch perhaps three pounds at the bookseller's, enough to keep us for a month, perhaps two if we were careful. But then what? There would be another debt, another notice, another winter.

I returned to my stitching, the needle slipping in and out of the leather with practiced ease. My fingers were stained with ink, permanently marked by the trade I had learned at my mother's knee. She had been a bookbinder too, before the cough took her, before the medicine costs bankrupted us, before the slow unraveling of everything we had been. I had her hands, people said. I had her patience. But I also had her stubbornness, her refusal to accept that some things cannot be mended no matter how carefully you stitch them.

The candle guttered lower, casting long shadows that danced on the walls like ghosts. Outside, the wind howled through the bare branches of the elms, and I could hear the distant clang of the church bell marking the hour. Midnight. Another day survived, another day closer to ruin. I tied off the thread, trimmed the excess with my shears, and set the Bible aside. Tomorrow I would deliver it to the vicar's wife and collect my stale bread. Tomorrow I would face the creditors again. Tomorrow I would pretend that we were not drowning.

But tonight, in the flickering candlelight, with my father's trembling hands and the ghost of my mother's Chaucer watching over us, I allowed myself a moment of honesty. We were finished. The bindery was finished. The life we had known was finished. And no amount of careful stitching could mend what was broken beyond repair. Some things, once sold, cannot be bought back. But some things, once lost, cannot be kept either. And I was beginning to understand that love — for a father, for a mother, for a life that no longer existed — was the most expensive thing of all."""

S02_TEXT = """The letter came under the door like a thief — black wax, black seal, the thorned rose pressed into it like a brand. I broke it open before I understood what I was opening. The parchment was thick, expensive, the kind of paper that cost more than a week of our bread. They wanted a bookbinder's daughter at Blackthorn Hall. Payment enough to clear every debt, every notice, every whisper of ruin. My father's eyes went wide when I read it aloud. Not with hope. With recognition. He said the Duke knew his name. I said not his name. Someone else's. The question sat between us like a third person in the room.

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

I walked to the door. I opened it. The wind howled outside, cold and sharp. The village was dark, the streets empty. The manor on the hill was a black shape against the grey sky. I stepped out into the cold. And I began to walk."""

S03_TEXT = """The road stretched ahead of me like a warning written in frost. Every hedgerow was skeletal, every breath a small white ghost that vanished before I could name it. I walked alone with my satchel of binding tools and the weight of a decision I hadn't fully made. The milestone appeared suddenly — carved with a thorned rose, ancient and deliberate. I knew then that every story about that house ended the same way. He did it. She vanished. No one agreed on how. They all agreed it happened. I pulled my cloak tighter and kept walking.

The cold was a physical thing, a weight that pressed against my chest and made it hard to breathe. The wind cut through my wool dress, through my cloak, through the layers of petticoats I wore against the chill. It felt like the cold was trying to find the heat in my body and extinguish it, just as the creditors were trying to find the last remnants of our life and extinguish them.

My boots crunched on the frozen ground, a rhythmic sound that was the only company I had. The village was far behind me now, a cluster of grey roofs and smoking chimneys that looked small and fragile from this distance. I didn't look back. Looking back was a luxury for people who had something to return to. I had nothing.

The landscape was bleak, stripped of color by the winter. The trees were black bones against the grey sky, their branches reaching out like skeletal fingers trying to grab me, to pull me back, to warn me away. I ignored them. I had made my choice. I had chosen the Chaucer. I had chosen my father's pride. I had chosen the unknown over the slow, certain death of our life in the village.

The milestone was old, the stone pitted and worn by years of wind and rain. The thorned rose was carved deep, the petals sharp and dangerous. It was a warning, I realized. A marker. Here begins the territory of the Duke. I ran my gloved hand over the carving, feeling the rough stone, the sharp edges of the thorns. It felt like touching a weapon.

I pulled my cloak tighter, wrapping it around my shoulders, pulling the hood up over my head. The wind howled through the hedgerows, a high, keening sound that sounded almost like a voice. Turn back, it seemed to say. Turn back while you can.

I didn't turn back. I couldn't. The debt was too great. The ruin too complete. The only way forward was through the gate, into the house, to the Duke. To the man who knew my father's name. To the man who had sent the letter.

The road wound upward now, climbing the hill toward the manor. The trees grew thicker, closer together, their branches interlacing overhead to form a tunnel of black wood. The light grew dimmer, the shadows longer. I felt like I was walking into a mouth. Into a throat. Into a stomach that would digest me and leave nothing behind.

But I kept walking. One foot in front of the other. One step after another. The rhythm of my boots on the frozen ground became a kind of mantra. I am a bookbinder's daughter. I am a keeper of stories. I am a mender of broken things.

Even if I couldn't mend this. Even if I couldn't save us. Even if I was walking into the dark.

I kept walking."""

S04_TEXT = """The gates were taller than a man and twisted into thorned vines, black iron against a grey sky that seemed to press down on everything below it. Mrs. Varma waited in the gateway like a sentinel carved from shadow and silk. She did not smile. She did not welcome. She measured me with one look that took in my ink-stained hands and my worn boots and found something acceptable, or at least tolerable. She said I would sleep in the east wing. Not the upper corridor. The Duke does not receive callers. He receives people who answer letters. I asked what the difference was. She did not answer.

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

I picked up my satchel and began to look for the east corridor."""

S05_TEXT = """The foyer was a cavern of candelabras and damask, every shadow longer than it should be. I removed my gloves and tried not to think about the ink still staining my fingertips. Then I looked up. He stood in the upper gallery, half-consumed by darkness, watching me with the patience of a man who had been waiting for a very long time. He did not descend. He did not speak. He simply watched, then turned and disappeared. I whispered to the empty hall that he was not surprised to see me. The echo agreed.

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

I turned and walked quickly toward the east corridor, my boots loud on the stone floor. I didn't look back. I didn't want to see if he was watching me again. But I knew he was. I knew he would be watching me for a long time to come."""

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

    content = replace_scene("S01", S01_TEXT, content)
    content = replace_scene("S02", S02_TEXT, content)
    content = replace_scene("S03", S03_TEXT, content)
    content = replace_scene("S04", S04_TEXT, content)
    content = replace_scene("S05", S05_TEXT, content)
    
    with open('build_gallery.py', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Updated S01-S05 voiceovers.")

if __name__ == "__main__":
    update_scenes()
