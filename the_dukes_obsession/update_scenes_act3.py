import re

S11_TEXT = """A desk of black oak. A single document. He stood behind it, hands braced on the wood, signet ring catching the firelight. The contract read: all Finch family debts cleared, father's workshop preserved, in exchange for one winter as his Duchess. In name, in public, in residence. No conjugal obligation. No permanent arrangement. I could leave at spring thaw. I asked him why me. He said because I was always the answer. He simply had to wait for the question to arrive. I did not know whether to believe him or run.

The study was smaller than the library but no less imposing. Dark wood panelling rose to a ceiling lost in shadow, and a fire burned steadily in a marble hearth, casting long orange reflections across the polished floor. I had been summoned here at dawn — a crisp, formal summons delivered by Mrs. Varma in her unreadable voice — and I had come with my satchel over my shoulder and my heart hammering against my ribs.

The Duke stood behind the desk. He was the desk, in some way — they shared the same dark gravity, the same immovable quality. His hands rested flat on the black oak, fingers spread, and on his right hand the signet ring caught the firelight and threw a small, sharp glint across the wall behind him.

Between us, on the desk, lay a single document.

It was thick parchment, the kind used for legal agreements, and it had been written in the same precise copperplate I had seen in the journals. I didn't need to read it to know what it said. The letter had promised compensation. This was the shape that promise had taken.

He didn't push it toward me. He didn't ask me to sit. He simply stood there and waited, his dark eyes fixed on mine with an intensity that made the fire behind him seem almost cold by comparison.

I read it.

The terms were exact. Every debt my father owed — to Hemsworth, to Gable, to the chandler, to the physician, to every merchant and tradesman whose name was papered to our walls — would be settled in full. The bindery would be preserved, its tools maintained, its lease secured for a further ten years. In exchange, I would take the title of Duchess of Blackthorn for one winter. I would reside in the house. I would appear in public at his side. I would wear the clothes he provided, speak the words he required, play the part his world expected of him.

There would be no conjugal obligation. No permanent arrangement. I could leave at spring thaw with my father's debts cleared and my name no longer whispered in the village as a ruin's daughter.

I read it twice. The words were clean, legal, final. There was no ambiguity, no hidden clause, no trapdoor I could see. And yet the weight of it pressed against me like something physical.

'Why me?' I asked, because it was the only question that mattered.

He was quiet for a long moment. The fire popped. The clock on the mantel ticked.

'Because you were always the answer,' he said, and his voice was lower than I expected, rougher at the edges. 'I simply had to wait for the question to arrive.'

I stared at him. I wanted to believe he was speaking in riddles, in the elaborate metaphors of a man who had lived too long alone. I wanted to believe it was a line, a performance, a piece of the role he had cast me in. But his eyes were too steady, too unguarded, and I did not know whether to believe him or run.

So I stood there, with the contract between us and the fire at our backs, and I did neither."""

S12_TEXT = """A long table set for two, though the house held twenty. Mrs. Varma stood behind my chair, adjusting my collar with proprietary hands. Lucy peeked from the serving doorway, wide-eyed. The Duke took his seat and did not look at me until I was settled, then held my gaze with an intensity that made the candlelight seem dim. He said I would call him Silas in private. In public, I would call him Your Grace and allow no one to see me smile first. I asked what would happen if I smiled first. He said he would spend the evening making it worth the scandal.

The dining hall was long enough to be a chapel. A single table ran its length, polished to a dark shine, set with silver and crystal and candles that burned in tall brass holders. At one end, two places were set — close together, almost uncomfortably so — while the rest of the table stretched away into shadow, empty and echoing.

I had been dressed for the occasion. A gown of dark green velvet, the colour of the forest I had walked through to reach this house, had been laid out in my room by a maid I hadn't met. Mrs. Varma had appeared at my door as the clock struck eight and stood in silence until I was ready, then led me here with her usual gliding grace.

She stood behind my chair as I sat. Her hands, cool and dry, adjusted the collar of my gown with the proprietary care of a woman who had spent a lifetime dressing other people's bodies. I wanted to flinch. I didn't.

'He has rules,' she murmured, so quietly I almost didn't hear it. 'You will learn them.'

Then she stepped back, and the Duke entered.

He took his seat at the head of the table without looking at me. I watched his hands — bare now, the gloves gone — as they settled on the arm of his chair, the signet ring catching the candlelight. The servants appeared with the first course, silent as ghosts, and only when the plates were set and the wine poured and the servants had withdrawn did he finally raise his eyes.

He looked at me.

It was not the polite, considering look of a host assessing a guest. It was the look of a man who had been waiting, and who was now, at last, looking at what he had waited for. The candlelight between us flickered, and for a moment the rest of the hall — the empty places, the long shadows, the silent portraits — seemed to fall away.

'There are rules,' he said. His voice was quiet, formal, but not unkind. 'In private, you will call me Silas.'

I blinked. I had expected 'Your Grace' in all circumstances. I had expected distance.

'In public,' he continued, 'you will call me Your Grace. You will allow no one to see you smile first. You will look at me when I speak to you, and you will look away only when I permit it. You will not speak to Julian Fox without my knowledge. And you will not, under any circumstances, leave the house without my company.'

The list was specific, almost clinical. A contract within a contract. I absorbed it the way I absorbed the structure of a new binding — each rule a stitch, each condition a fold, all of it building toward something that would hold.

'And if I smile first?' I asked, because something in me — the stubbornness Mother had given me, the defiance that had kept me stitching through the worst of our ruin — would not let the moment pass unchallenged.

He was quiet for a long moment. The fire behind him burned low and amber, and in its light his eyes were darker than I had ever seen them.

'Then I will spend the evening making it worth the scandal,' he said.

And for the first time since I had entered this house, I did not know whether he was threatening me or promising me something. Perhaps both."""

S13_TEXT = """The ballroom glittered with candlelight and crystalline pretense, the local gentry dressed in jewels and calculated indifference. Julian appeared in burgundy velvet, claiming me for a dance with the ease of a man who had never been refused. His hand settled at my waist. Across the room, the Duke watched, a glass of brandy untouched in his hand. Julian asked why I was trembling. I said his cousin's moods were not a difficult text. Julian smiled and said, Then why are you trembling? The Duke crossed the room. He did not dance. He took my hand from Julian's waist and placed it on his own coat.

The ballroom had been transformed. Where I had seen only shadow and silence before, there was now light — a thousand candles reflected in crystal chandeliers, in gilt mirrors, in the jewels at the throats and wrists of the women who filled the room. The local gentry had come in their hundreds, it seemed, every family of consequence within twenty miles gathered beneath the Blackthorn roof to see the new Duchess.

I stood at the edge of the floor in my dark green velvet, and I felt their eyes like a weight. Some were curious. Some were cruel. All of them were measuring me the way I had learned to measure leather — by weight, by grain, by the flaws that would eventually show.

He had not yet appeared. I knew he would. He never did anything without timing it perfectly.

Julian Fox found me first.

He moved through the crowd with the easy grace of a man who had never been refused anything, his burgundy velvet coat catching the candlelight like something alive. He was beautiful in the way dangerous things are beautiful — sandy hair, ice-blue eyes, a smile that never quite reached them. The Duke's cousin. The Duke's opposite.

'My dear Duchess,' he said, bowing with elaborate precision. 'May I claim the first dance?'

Before I could answer, his hand was at my waist, his other hand lifting mine, and we were on the floor. The music began — strings and something lower, something almost mournful — and Julian led me into the dance with a skill that suggested he had spent a great deal of his life leading women who did not entirely wish to be led.

His hand was too low on my waist. I could feel the heat of it through the velvet, and I stiffened, but he only smiled down at me with those cold blue eyes.

'You're trembling,' he said. It was not a question.

'Your cousin's moods are not a difficult text,' I replied, because it was the only defence I had.

Julian's smile sharpened. 'Then why are you trembling, Elara?'

He used my name the way a man uses a blade he has tested. And for one terrible, clarifying moment, I understood that he was not dancing with me. He was performing for someone else.

I looked across the room.

The Duke stood at the far end of the ballroom, a glass of brandy in his hand that he had not raised to his lips. His expression was perfectly composed, perfectly still, and I could see, with a clarity that frightened me, the precise moment at which the glass in his hand began to betray him. His knuckles whitened. The brandy trembled.

Julian followed my gaze and laughed — a low, pleasant sound that was somehow worse than a sneer.

Then the Duke crossed the room.

He did not hurry. He did not push through the crowd. The crowd simply parted for him, the way water parts for something heavier than itself, and by the time he reached us the music had stopped and the entire room was watching.

He did not dance. He did not speak to Julian. He simply took my hand from where it rested against Julian's waist and placed it, deliberately, against his own coat, over his heart.

And the room understood. And I understood. And Julian understood.

The Duke did not ask me to dance. He simply did not let go."""

S14_TEXT = """I found the locked drawer and forced it open with a bone folder. Inside: letters from Lady Margaret's brother describing his sister's slow poisoning, and a doctor's note that the Duke refused an autopsy. I confronted him. He did not deny the letters. He said they were incomplete. I asked if he killed her. He said she asked him to let her go and he held on too tightly. That was the closest thing to murder he had committed. I asked what about me. A long silence. The fire popped. He said I was the only thing he had ever been afraid to hold.

I told myself I would not look. I told myself it was not my business. I told myself that the locked drawer in the Duke's study was locked for a reason, and that a cataloguer's duties did not extend to the private griefs of a widower.

I told myself all of these things, and then I forced the drawer open with my bone folder.

The wood splintered. The lock gave. And inside, arranged with the same meticulous care I had come to associate with the Duke's mind, were letters. Dozens of them. I read the first one standing up, the candlelight flickering over the spidery hand of a man I did not know, and by the third paragraph my hands were shaking.

Lady Margaret's brother. Writing to the Duke. Describing, in careful, legalistic prose, his sister's decline — the wasting, the fevers, the slow dimming of a woman who had entered this house healthy and left it in a coffin. Accusing, without quite accusing. Suggesting, without quite suggesting. And beneath the letters, a doctor's note, signed and sealed, confirming that the Duke had refused an autopsy. Refused an inquiry. Refused the one thing that might have cleared his name or damned it forever.

I read them all. I read them twice. And then I closed the drawer and sat in the Duke's chair and waited for him to come.

He came at midnight, as I had known he would. He stopped in the doorway and saw the splintered wood and the open drawer and my face, and he did not move.

'You found them,' he said.

'I found them.'

He crossed the room and stood on the other side of the desk, between me and the fire. In the candlelight his face was half-shadow, half-light, and I could not read it.

'Did you kill her?' I asked. The question hung in the air between us like something living.

He did not deny it. He did not confirm it. He simply said, 'The letters are incomplete.'

'Are they?'

'Yes.'

'What isn't in them?'

He was quiet for a long time. The fire popped and threw a shower of sparks up the chimney, and for a moment I thought he would not answer at all.

'She asked me to let her go,' he said finally, and his voice was lower than I had ever heard it, almost gentle. 'She was ill. Not the illness they described — that was the medicine, the laudanum, the physician's incompetence. She was ill in a way that had no name, and she asked me to release her from it. I held on too tightly. That is the closest thing to murder I have ever committed.'

I stared at him. The man who had written my name in a journal ten years before I was born. The man who had watched me from the doorway in the library. The man who had taken my hand from his cousin's waist and placed it over his heart.

'And me?' I asked. 'What about me?'

The silence that followed was long enough that I heard the house settling around us, the old timbers creaking, the wind outside pressing against the windows.

'I am afraid of you,' he said, and the words were so quiet I almost did not catch them. 'You are the only thing I have ever been afraid to hold.'

The fire popped again. The candlelight guttered. And I sat in his chair with his secrets scattered on the desk between us, and I did not know whether to rise and leave or stay and be destroyed."""

S15_TEXT = """Winter light turned the library gold. I stood by the window, the contract in my hands. He waited by the fireplace, still as a portrait. I had read every clause. I had found the escape clause: I could leave at spring, with my father's debts cleared, no conditions. I folded the document slowly. I told him I would stay the winter. Not because of the debt. Because I needed to know if what he wrote in those journals was true, or if I was just the woman who looked enough like a ghost to fill the space. He crossed the room and stopped exactly one arm's length from me. He said I was never a ghost. I was the only living thing he could imagine in this house.

The library at dawn was a different place from the library at night. The winter sun rose late and low, and when it finally broke through the tall windows it poured across the shelves like honey, turning the dust motes to gold and the leather spines to something almost alive. I had not slept. I had stood at the window since the sky began to grey, the contract folded in my hands, and I had watched the night become morning without once looking away.

He was waiting for me. I had known he would be. He stood by the fireplace, where the ashes of last night's fire had been swept clean, and he was perfectly, unnaturally still — the same stillness I had seen in the upper gallery on my first night, the stillness of a man who has learned, over many years, that motion betrays intention.

I did not turn to face him immediately. I watched the light move across the shelves. I watched it touch the place where I had found his journal, where my name was written in ink older than I was.

'I read every clause,' I said.

'I know.'

'I found the escape clause. I can leave at spring. The debts are cleared regardless. No conditions.'

'I wrote it that way.'

I turned then. The winter sun was behind me, and I knew he would be looking into the light, that I would be a silhouette to him, a shape outlined in gold. I wondered if that was how he had always seen me — not as a person, but as a shape his mind had drawn before I arrived.

'I will stay the winter,' I said.

He did not move.

'Not because of the debt,' I continued, and my voice was steadier than I had any right for it to be. 'Not because of the contract. Not because my father's bindery depends on it. I will stay because I need to know if what you wrote in those journals was true.'

I let the pause between us fill with the sound of the house — the distant creak of timbers, the whisper of the wind against the glass, the small, intimate noises of a building that had stood for centuries and would stand for centuries more.

'Or if I am just the woman who looked enough like a ghost to fill the space she left behind.'

He crossed the room.

He did it slowly, the way he did everything — with the deliberation of a man who understood that speed was a kind of violence — and he stopped exactly one arm's length from me. Close enough that I could see the grey at his temples, which I had not noticed before. Close enough that I could smell the cold wool and woodsmoke that always clung to him. Close enough that I could see, in his dark eyes, something that was not patience and was not obsession and was not anything I had a name for.

'You were never a ghost,' he said.

The words were simple. They were also, I understood in the same instant, the truest thing he had ever said to me.

'You are the only living thing I could imagine in this house.'

I folded the contract slowly, deliberately, and placed it on the reading desk between us. The winter sun caught the edge of the paper and made it glow, and for the first time since I had entered Blackthorn Hall, I did not feel like a woman who had come to sell herself.

I felt like a woman who had come to be found."""

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

    content = replace_scene("S11", S11_TEXT, content)
    content = replace_scene("S12", S12_TEXT, content)
    content = replace_scene("S13", S13_TEXT, content)
    content = replace_scene("S14", S14_TEXT, content)
    content = replace_scene("S15", S15_TEXT, content)
    
    with open('build_gallery.py', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Updated S11-S15 voiceovers.")

if __name__ == "__main__":
    update_scenes()
