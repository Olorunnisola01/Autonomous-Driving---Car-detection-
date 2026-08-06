import re

# New Voiceover Texts for Act II (Target: ~2,500-2,800 chars each)

S06_TEXT = """Two stories of shelves bowed under the weight of centuries. Dust motes hung motionless in slanting winter light. A fireplace large enough to stand in held cold ashes and the memory of warmer years. I set down my satchel and exhaled — the first full breath I had taken since arriving. This room was alive with knowledge. I touched a spine and felt something like recognition. Mrs. Varma said the late Duchess had arranged everything by feeling, not subject. I asked how long that took her to understand. She said ten years. She never did.

The library was vast. That was the first thing that struck me — not the beauty, not the age, but the sheer, overwhelming scale of it. The shelves rose two stories high, connected by a wrought-iron gallery that ran along the upper level like a balcony in a cathedral. The books were everywhere, floor to ceiling, their spines a patchwork of faded leather and tarnished gold. Some were chained to the shelves. Some were stacked horizontally, as if they had been placed there in haste and never moved.

The air smelled of old paper and beeswax, with an undertone of something sharper — damp stone, perhaps, or the ghost of woodsmoke from the great fireplace that dominated the far wall. The fire was dead, the hearth cold, but I could imagine it blazing, could imagine someone sitting in one of the leather chairs with a book and a glass of something amber, reading while the flames danced.

Dust motes drifted through the shafts of winter light that fell from the tall windows. They moved slowly, almost languidly, as if time itself was thicker here, more viscous. I stood in the center of the room and turned slowly, taking it all in. This was what I had come for. This was the task that would save us.

I walked to the nearest shelf and ran my hand along the spines. The leather was cool, soft with age. I could feel the texture of the binding, the slight irregularities that told me these were hand-bound volumes, crafted by someone who understood their art. My fingers tingled. I wanted to open them, to read them, to lose myself in their pages.

But that wasn't why I was here. I was here to catalog, to organize, to make order from chaos. I pulled my satchel closer and set it on a reading desk near the window. I took out my notebooks, my pens, my measuring tape. I was ready to work.

Mrs. Varma appeared in the doorway, silent as always. 'The late Duchess arranged everything by feeling, not subject,' she said, her voice flat. 'You will find no logic to it. No system.'

'How long did it take you to understand?' I asked.

She looked at me, and for a moment, something flickered in her dark eyes. 'Ten years,' she said. 'I never did.'

Then she was gone, leaving me alone with the books and the dust and the silence. I opened my notebook and began."""

S07_TEXT = """The journals were leather-bound and cracked with age, each one a small coffin of secrets. I opened one dated thirteen years ago and began to catalogue, to organize, to make order from chaos. Then I found it — my own name. Elara Finch. Written in elegant copperplate in a margin note beside a passage on the binding of psalters. The date was ten years before I was born. My fingers trembled. I read the entry again. The ink was old. The handwriting was deliberate. This was not a coincidence. He knew. Before I existed. He wrote me down.

I had been working for three days now, and the library was beginning to yield its secrets. Not the secrets I had expected — the hidden compartments, the coded messages, the scandalous letters — but the quieter secrets of a life lived among books. The Duchess had been a reader, a collector, a woman who understood that books were more than objects. They were companions.

The journals were different. They were the Duke's, I realized, though they bore no name. The handwriting was sharp, precise, the copperplate so perfect it looked almost printed. He had written them over the course of decades, one for each year, recording his thoughts, his observations, his... what? Not quite a diary. More like a ledger of the mind.

I opened the journal dated thirteen years ago, expecting to find accounts of the Duchess, of their life together, of the events that had led to her death. Instead, I found pages of meticulous notes on bookbinding techniques. The Duke was studying the craft, learning it, mastering it. Why? I turned the pages, reading entries about leather types, stitching methods, the chemistry of adhesives. It was obsessive in its detail.

And then I saw it. My name. Elara Finch. Written in the margin beside a passage about the binding of psalters. The date in the header was 1837. I was born in 1847. Ten years after this was written.

My breath caught. I stared at the name, at the elegant curves of the letters, at the ink that had dried more than a decade before I drew my first breath. This was impossible. And yet, here it was. My name, in his hand, in a journal written before I existed.

I read the entry again. And again. The handwriting was deliberate, careful, as if he had known this would be found. As if he had wanted it to be found.

I closed the journal slowly, my hands shaking. I looked around the library, at the shelves of books, at the dust motes drifting in the winter light. The room felt different now. Heavier. Watched.

He knew. Before I existed. He wrote me down.

And I didn't know what that meant."""

S08_TEXT = """Candlelight. Late. I worked without knowing he was there, without knowing I was being watched. He stood in the doorway's shadow, observing as I carefully lifted a page with a bone folder, as if I were performing surgery on something alive. He did not announce himself. I sensed him the way animals sense a storm — in the air pressure, in the sudden stillness that precedes violence or tenderness. When I turned, he was already gone. Only the scent of cold wool and smoke remained. I whispered that he was always there, just behind the edge of seeing.

The library at night was a different place. The winter light faded early, and by four o'clock the room was dark save for the candles I had lit on the reading desk. The flames cast long, dancing shadows on the shelves, making the books seem to move, to breathe. I worked by their light, cataloguing, measuring, recording. The silence of the house was absolute, save for the scratch of my pen and the occasional creak of the old building settling.

I was so absorbed in my work that I didn't notice him at first. Not his presence, not his weight in the room. But something changed. The air grew heavier, thicker, as if the pressure had dropped. The candles flickered, though there was no draft. The hair on the back of my neck prickled.

I turned slowly, my bone folder still in my hand, and saw him. He stood in the doorway, half-consumed by shadow, one hand resting on the doorframe. He was perfectly still, perfectly silent. His dark coat blended with the darkness, but his face was visible, pale and sharp in the candlelight. His eyes were fixed on me.

He had been watching me work. For how long, I didn't know. Minutes? Hours? The thought sent a shiver down my spine. He had been standing there, silent and still, observing me as I touched his books, as I turned the pages of his journals, as I wrote his secrets in my notebooks.

He didn't speak. He didn't move. He just watched.

I stood, my chair scraping against the stone floor, the sound loud in the silence. 'Your Grace,' I said, my voice steadier than I felt.

He tilted his head slightly, as if considering my words. Then, slowly, deliberately, he stepped back into the shadows of the corridor and was gone.

I walked to the doorway and looked out. The corridor was empty, dark. But the scent of him lingered — cold wool, woodsmoke, something metallic and sharp. He had been here. He had watched me. And then he had vanished.

I returned to my desk and sat down, my hands shaking slightly. I picked up my pen and tried to continue my work. But the words wouldn't come. All I could think was: he was always there. Just behind the edge of seeing.

And I didn't know whether to be terrified or flattered."""

S09_TEXT = """The corridor of portraits stretched longer than I expected, each face watching me with painted eyes that never blinked. Lucy showed me the house by stolen candlelight, her breath fogging in the cold. We stopped before a painting of Lady Margaret — white satin gown, pearl choker, emerald pendant at her throat. The eyes were dark and knowing. Lucy said they claimed the Duke locked himself in here for a year after she died. I asked how she died. Lucy said that was the question no one answered twice the same way. I looked at my own reflection in the gilt frame and did not like the comparison.

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

And I didn't know what she wanted."""

S10_TEXT = """I fell asleep at the reading desk, a book open against my cheek, unaware of the figure who entered silently. He stood over me, his shadow falling across the page. His gloved hand reached down — not to shake me, not to wake me, but to brush a stray auburn curl from my forehead. His finger grazed my temple. I stirred. Our eyes met across the smallest distance. Neither moved. The candle between us guttered. His voice, when it came, was barely audible. You are exactly as I wrote you. I did not know whether to be terrified or flattered. Perhaps both.

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

I sat there for a long time, my hand touching the spot on my temple where his finger had grazed my skin. And I didn't know whether to be terrified or flattered. Perhaps both. Perhaps that was the point."""

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

    content = replace_scene("S06", S06_TEXT, content)
    content = replace_scene("S07", S07_TEXT, content)
    content = replace_scene("S08", S08_TEXT, content)
    content = replace_scene("S09", S09_TEXT, content)
    content = replace_scene("S10", S10_TEXT, content)
    
    with open('build_gallery.py', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Updated S06-S10 voiceovers.")

if __name__ == "__main__":
    update_scenes()
