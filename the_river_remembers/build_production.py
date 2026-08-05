#!/usr/bin/env python3
"""Generate the planning documents for THE RIVER REMEMBERS storyboard.

This source-of-truth generator intentionally creates the full 200-shot plan before
any scene imagery is made.  Scene images must only be marked complete after their
actual files exist; reference portraits are handled separately.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TITLE = "THE RIVER REMEMBERS"
SUBTITLE = "A Ghanaian magical-realism family drama"
STYLE = (
    "Grounded cinematic West African magical realism; contemporary Ghanaian coastal life; "
    "human-scale performances; saturated indigo, lagoon teal, clay red and warm amber palette; "
    "natural skin texture; tactile fabric and weathered wood; 2.39:1 widescreen composition; "
    "subtle film grain; expressive realistic lighting. No written words, no logos, no watermark, "
    "no distorted hands, no duplicate people."
)

characters = [
    {
        "tag": "@KOSI_MENSAH", "filename": "KOSI_MENSAH", "name": "Kosi Mensah", "age": 29,
        "role": "A solar-field engineer returning to the lagoon town where she was raised; protagonist.",
        "physical": "A tall, athletic Ghanaian woman with deep brown skin, alert dark eyes, a heart-shaped face and closely cropped natural coils.",
        "wardrobe": "indigo utility jumpsuit with rolled sleeves, sand-coloured work boots and a narrow woven kente belt",
        "object": "small gold Adinkra-disc earrings", "personality": "Methodical, dryly funny and reluctant to depend on anybody.",
        "arc": "She trades self-protective competence for the courage to let a whole town carry the light with her.",
    },
    {
        "tag": "@AMA_ADJOVI", "filename": "AMA_ADJOVI", "name": "Ama Adjovi", "age": 68,
        "role": "Kosi's grandmother, a retired lantern-maker and keeper of the town's oral records.",
        "physical": "A compact elder with rich dark skin, silver hair woven into a low crown braid, knowing eyes and fine scar lines at her temples.",
        "wardrobe": "deep navy kaba blouse, hand-dyed indigo wrapper with tiny white wave motifs and flat leather sandals",
        "object": "three-strand amber bead necklace", "personality": "Precise, playful and unmovable when a promise is at stake.",
        "arc": "She stops guarding the past alone and places its proof in the hands of the next generation.",
    },
    {
        "tag": "@SENA_ADJOVI", "filename": "SENA_ADJOVI", "name": "Sena Adjovi", "age": 16,
        "role": "Ama's sharp-tongued grandniece and an aspiring community-radio reporter.",
        "physical": "A slim Ghanaian teenager with warm umber skin, a round face, bright observant eyes and short copper-tipped twists.",
        "wardrobe": "mustard oversized hoodie, blue-and-white printed ankle skirt and worn white canvas trainers",
        "object": "turquoise over-ear radio headphones", "personality": "Curious, fearless and allergic to adults editing the truth.",
        "arc": "She learns that reporting is not only recording a crisis but inviting people to speak for themselves.",
    },
    {
        "tag": "@KOJO_DANSO", "filename": "KOJO_DANSO", "name": "Kojo Danso", "age": 33,
        "role": "A lagoon-boat captain and Kosi's childhood friend.",
        "physical": "A lean Ghanaian man with mahogany-brown skin, shoulder-length tidy locs, a soft smile and a small notch through his left eyebrow.",
        "wardrobe": "faded forest-green canvas jacket over a blue-and-cream striped shirt, charcoal trousers and rubber deck boots",
        "object": "weathered brass compass on a cord", "personality": "Patient, teasing and quietly brave when water turns dangerous.",
        "arc": "He moves from watching the town endure to steering its resistance into action.",
    },
    {
        "tag": "@ESI_TETTEH", "filename": "ESI_TETTEH", "name": "Esi Tetteh", "age": 45,
        "role": "Leader of the fish-smokers' cooperative and the town's clearest public voice.",
        "physical": "A broad-shouldered Ghanaian woman with dark skin, a powerful stance, close-cropped hair and a crescent scar above one eyebrow.",
        "wardrobe": "brick-red wax-print dress beneath a soot-black oilskin apron, patterned headwrap and sturdy black sandals",
        "object": "smooth charred-wood smoking paddle", "personality": "Blunt, generous and impatient with polite evasion.",
        "arc": "Her righteous anger becomes disciplined collective leadership rather than a solitary fight.",
    },
    {
        "tag": "@KWAME_AGYEMAN", "filename": "KWAME_AGYEMAN", "name": "Kwame Agyeman", "age": 36,
        "role": "The polished local liaison for the resort project and Kosi's former university friend.",
        "physical": "A slender Ghanaian man with medium-brown skin, neat low-cropped hair, a long thoughtful face and rimless spectacles.",
        "wardrobe": "white linen shirt under a caramel lightweight field jacket, dark tailored trousers and brown loafers",
        "object": "antique bronze lapel pin shaped like a compass rose", "personality": "Diplomatic, ambitious and deeply uncomfortable with his own compromises.",
        "arc": "He stops confusing access to power with service and risks his position to release the truth.",
    },
    {
        "tag": "@NII_LAMPTEY", "filename": "NII_LAMPTEY", "name": "Nii Lamptey", "age": 55,
        "role": "District Assembly Chair whose partnership with the resort threatens Afenyo's public lagoon access; antagonist.",
        "physical": "A tall, imposing Ghanaian man with deep espresso skin, a shaved head, heavy-lidded eyes and a neatly trimmed grey goatee.",
        "wardrobe": "tailored charcoal caftan with a subtle black geometric weave, polished black shoes and a silver wristwatch",
        "object": "black ebony walking cane with a carved heron handle", "personality": "Controlled, eloquent and convinced that progress must have winners.",
        "arc": "Public exposure forces him to confront that authority without consent is only a well-dressed form of theft.",
    },
]

locations = {
    "ACCRA_SOLAR_ROOF": "A broad, sun-whitened corrugated-roof solar workshop above a dense Accra neighbourhood: neat blue-black photovoltaic panels, coiled orange cables, water tanks, hazy low-rise buildings and a vast humid sky.",
    "AFENYO_BUS_STOP": "Afenyo's small red-earth bus stop at the lagoon edge: a faded blue shelter, cassava vendors under striped umbrellas, old tro-tro vans, palm trees bent by sea wind and distant silver water.",
    "COMPOUND_COURTYARD": "Ama's lived-in family compound courtyard in Afenyo: ochre plaster walls, a weathered blue wooden door, clay pots of basil, woven stools, a mango tree, laundry lines and a low view toward the lagoon.",
    "AFENYO_MARKET": "Afenyo's open lagoon market: timber stalls, bright wax-print canopies, baskets of smoked fish and tomatoes, colourful basins, sandy paths, bicycles and the blue-green lagoon visible beyond mangroves.",
    "DISTRICT_ASSEMBLY_HALL": "A modest district assembly hall in Afenyo: cream concrete walls, tall louvre windows, stacked plastic chairs, a raised wood dais, ceiling fans and late-afternoon lagoon light.",
    "LAGOON_CHANNEL": "A narrow Afenyo lagoon channel: glassy teal water, low mangrove roots, weathered fishing canoes, stilted homes, a rusted solar navigation buoy and a wide pale sky.",
    "AMA_LANTERN_WORKSHOP": "Ama's lantern workshop off the compound courtyard: clay-red floor, crowded wooden workbench, brass lantern frames, blue glass panes, hand tools, coils of copper wire, indigo cloth and shafts of warm window light.",
    "SENA_RADIO_SHACK": "Sena's tiny community-radio shack beside the market: a patched corrugated roof, foam-lined timber walls, a second-hand mixing board, a battered microphone, tangled cables, a solar battery and one open window to the lagoon.",
    "RESORT_FENCE": "The unfinished resort perimeter at Afenyo's lagoon shore: pale concrete columns, tall corrugated-metal fence panels, orange survey flags, a locked chain gate, scraped sand and mangroves pressed tightly behind it.",
    "MANGROVE_PASSAGE": "A shadowed mangrove passage off Afenyo lagoon: tangled roots in dark water, a slim canoe path, floating leaves, shafts of green-gold light and the distant hum of construction machinery.",
    "FLOODED_COMPOUND": "Ama's family compound courtyard after a king-tide flood: ankle-deep reflective water around ochre walls and woven stools, floating mango leaves, soaked laundry, a blue door and storm-grey sky.",
    "OLD_BEACON_HUT": "A derelict tidal beacon hut on a small lagoon sandbar: cracked whitewash walls, a rusted ladder, broken blue lantern glass, salt-stained timber, reed grass and sweeping water on every side.",
    "FISH_SMOKE_YARD": "Esi's fish-smoking yard by the Afenyo market: low clay smoking ovens, blackened racks, woven fish trays, stacked firewood, haze of fragrant smoke, red earth and a glimpse of lagoon water.",
    "COUNCIL_ARCHIVE": "A dim records room beneath Afenyo's district assembly hall: metal filing shelves, bound land ledgers, dust motes, a scarred wooden table, a green-shaded desk lamp and narrow high windows.",
    "LAGOON_PROMENADE": "Afenyo's public lagoon promenade at dusk: a cracked concrete path, low sea wall, fishing boats, flowering bougainvillea, street vendors, fading coral sky and the resort fence in the far distance.",
    "FESTIVAL_SQUARE": "Afenyo's central festival square at blue hour: packed red-earth ground, a large silk-cotton tree, simple wooden platform, strings of unlit handmade lanterns, market stalls and the compound roofs beyond.",
    "LAGOON_BEACON": "The restored solar beacon on the open Afenyo lagoon: a weathered metal buoy with a blue-glass lantern crown, tether chain, rippling teal water, mangrove horizon and vast cloud-streaked sky.",
    "COMMUNITY_HALL": "Afenyo's community hall at night: open concrete walls, a corrugated roof, rows of plastic chairs, a hand-painted blank projection sheet, standing fans, amber lantern light and rain-darkened red earth outside.",
    "SUNRISE_PIER": "Afenyo's wooden fishing pier at sunrise: worn planks, moored painted canoes, repaired fishing nets, calm gold-and-teal lagoon water, distant mangroves and a low orange sun.",
}

# The script text is deliberately concise screenplay form: every scene has a playable action,
# a turn, and dialogue that carries the narrative into the next scene.
scenes = [
    {
        "id":"S01", "act":1, "title":"The Roof That Hums", "location":"ACCRA_SOLAR_ROOF", "time":"DAY",
        "characters":["@KOSI_MENSAH"], "mood":"restless possibility", "lighting":"hard white midday sun softened by coastal haze",
        "script":"EXT. ACCRA SOLAR ROOF — DAY\n\nKOSI MENSah moves across a roof with a tester in one hand and a socket wrench in the other. A row of panels starts humming after her repair. Her phone vibrates: a voice message from AMa says, \"The lagoon is being measured again. Come before they turn our water into a gate.\" Kosi watches the city shimmer, deletes a work callback, and packs her tools.\n\nKOSI\nI said I was done coming home for emergencies.\n\nShe says it to the empty roof, then pockets the phone anyway."
    },
    {
        "id":"S02", "act":1, "title":"Road to Afenyo", "location":"AFENYO_BUS_STOP", "time":"LATE AFTERNOON",
        "characters":["@KOSI_MENSAH","@SENA_ADJOVI"], "mood":"uneasy homecoming", "lighting":"late gold filtering through bus dust",
        "script":"EXT. AFENYO BUS STOP — LATE AFTERNOON\n\nA tro-tro coughs away, leaving Kosi with her tool case. SENA pushes through cassava sellers wearing headphones and records a cheery arrival report. She announces Kosi's return into a dead microphone, then admits that the transmitter works only when the sun does.\n\nSENA\nGrandma said not to tell you she was scared. So I am telling you.\n\nKOSI\nThat is not how secrets work.\n\nSENA\nThen Afenyo needs better secrets."
    },
    {
        "id":"S03", "act":1, "title":"A Lantern Left Dark", "location":"COMPOUND_COURTYARD", "time":"SUNSET",
        "characters":["@KOSI_MENSAH","@AMA_ADJOVI","@SENA_ADJOVI"], "mood":"warm reunion with a hidden wound", "lighting":"low amber sunset and first cool blue shadows",
        "script":"EXT. COMPOUND COURTYARD — SUNSET\n\nAMA has laid out Kosi's favourite pepper soup but has not lit the courtyard lantern. Kosi hugs her, noticing the tremor in Ama's hands. Sena hangs a string of blue glass scraps in the mango tree. Ama says the town once lit every channel lantern before the first rain; now even the beacon has gone black.\n\nAMA\nA dark lantern is not only darkness. It tells boats they are not expected.\n\nKosi studies the unlit frame. The sentence lands harder than the welcome."
    },
    {
        "id":"S04", "act":1, "title":"Price of the Water", "location":"AFENYO_MARKET", "time":"MORNING",
        "characters":["@KOSI_MENSAH","@SENA_ADJOVI","@ESI_TETTEH","@KOJO_DANSO"], "mood":"busy, simmering anger", "lighting":"bright tropical morning broken by striped canopies",
        "script":"EXT. AFENYO MARKET — MORNING\n\nESI slaps a wet survey notice onto a fish tray: a new resort will fence the public landing. KOJO says the water has smelled like metal since the drilling began. Kosi checks the notice's power diagrams and spots a line running toward the navigation buoy. Sena records every complaint.\n\nESI\nThey call it access improvement. Whose feet are improved by a locked gate?\n\nKOSI\nShow me where they put the cables."
    },
    {
        "id":"S05", "act":1, "title":"The Polite Hearing", "location":"DISTRICT_ASSEMBLY_HALL", "time":"AFTERNOON",
        "characters":["@KOSI_MENSAH","@ESI_TETTEH","@KWAME_AGYEMAN","@NII_LAMPTEY","@SENA_ADJOVI"], "mood":"civil language hiding violence", "lighting":"stale fan-cooled daylight through louvre windows",
        "script":"INT. DISTRICT ASSEMBLY HALL — AFTERNOON\n\nNII introduces the resort as a future of jobs and clean power. KWAME, immaculate and surprised to see Kosi, explains the environmental safeguards. Esi demands a public copy of the lagoon agreement. Nii promises one after the vote. Kosi recognizes the answer as a lock.\n\nKOSI\nIf the plan is safe, why is the map not on the wall?\n\nNII\nEngineer Mensah, trust is also infrastructure.\n\nSena quietly starts recording."
    },
    {
        "id":"S06", "act":1, "title":"The Black Buoy", "location":"LAGOON_CHANNEL", "time":"DUSK",
        "characters":["@KOSI_MENSAH","@KOJO_DANSO"], "mood":"intimate investigation", "lighting":"violet dusk, reflected teal water and a dead lantern silhouette",
        "script":"EXT. LAGOON CHANNEL — DUSK\n\nKojo steers a canoe toward the dark buoy. Kosi tests the housing; its solar battery has been bypassed by a new buried cable. A thin slick shivers through the water. Kojo points to resort lights burning far away.\n\nKOJO\nThe channel has always carried us out.\n\nKOSI\nThen someone has taught it to carry their dirt in.\n\nShe photographs the severed connection and decides not to leave."
    },
    {
        "id":"S07", "act":2, "title":"The Ledger in the Lantern", "location":"AMA_LANTERN_WORKSHOP", "time":"NIGHT",
        "characters":["@KOSI_MENSAH","@AMA_ADJOVI","@SENA_ADJOVI"], "mood":"discovery and inheritance", "lighting":"warm brass lantern light against deep blue night",
        "script":"INT. AMA LANTERN WORKSHOP — NIGHT\n\nKosi repairs a lantern while Ama watches. A loose blue pane reveals a rolled, water-stained ledger page underneath. It lists public landing rights and an old beacon frequency in Ama's handwriting. Sena sees a code in the wave marks.\n\nAMA\nThe old people hid papers where officials never looked: inside what kept us safe.\n\nKOSI\nThis could prove the shore belongs to the town.\n\nAma closes Kosi's hand around the page."
    },
    {
        "id":"S08", "act":2, "title":"Open Frequency", "location":"SENA_RADIO_SHACK", "time":"MORNING",
        "characters":["@SENA_ADJOVI","@KOSI_MENSAH","@ESI_TETTEH"], "mood":"improvised courage", "lighting":"clean morning sun and small red recording lights",
        "script":"INT. SENA RADIO SHACK — MORNING\n\nSena powers the station from Kosi's temporary battery. Esi gives the first on-air testimony about losing the landing. Calls come in from boat crews and market women. Kosi asks Sena not to name anyone until they have proof.\n\nSENA\nThe proof is that people are afraid to say it.\n\nKOSI\nFear is evidence. It is not enough evidence.\n\nSena puts the microphone between them both."
    },
    {
        "id":"S09", "act":2, "title":"Map with a Missing Line", "location":"RESORT_FENCE", "time":"AFTERNOON",
        "characters":["@KOSI_MENSAH","@KWAME_AGYEMAN"], "mood":"charged old friendship", "lighting":"bleached afternoon heat and hard fence shadows",
        "script":"EXT. RESORT FENCE — AFTERNOON\n\nKwame meets Kosi at a chained gate, carrying an approved site plan. A utility route disappears beneath a black redaction bar. He says the contractor will not show him the discharge run either. Kosi calls that a choice.\n\nKWAME\nI took this job to get a seat at the table.\n\nKOSI\nThen stop pretending the table is not sitting on our water.\n\nBefore leaving, he lets her photograph a survey number on the plan."
    },
    {
        "id":"S10", "act":2, "title":"Under the Roots", "location":"MANGROVE_PASSAGE", "time":"LATE AFTERNOON",
        "characters":["@KOSI_MENSAH","@KOJO_DANSO","@SENA_ADJOVI"], "mood":"tense fieldwork", "lighting":"green-gold shafts through dense mangrove canopy",
        "script":"EXT. MANGROVE PASSAGE — LATE AFTERNOON\n\nKojo poles a narrow canoe through roots while Kosi trails a sensor on a wire. Sena films in silence. The meter spikes near a concealed pipe; warm grey water pulses out. A construction engine stops abruptly in the distance.\n\nSENA\nIf they see us?\n\nKOJO\nThen you keep your camera still.\n\nKosi seals a sample and sends Sena ahead with the footage."
    },
    {
        "id":"S11", "act":2, "title":"King Tide", "location":"FLOODED_COMPOUND", "time":"NIGHT",
        "characters":["@KOSI_MENSAH","@AMA_ADJOVI","@SENA_ADJOVI","@KOJO_DANSO"], "mood":"urgent, tender resilience", "lighting":"storm flashes, lantern reflections and dark blue rain",
        "script":"EXT. FLOODED COMPOUND — NIGHT\n\nA king tide pours into Ama's courtyard. Kosi lifts electrical leads above the water as Kojo wades in with a canoe. Ama refuses to abandon the lantern crate until Sena carries it. The family floats their tools to safety.\n\nAMA\nThe water remembers every blocked path.\n\nKOSI\nThen we will make it testify.\n\nA blue lantern flickers to life in the storm."
    },
    {
        "id":"S12", "act":2, "title":"Night of the Red Moon", "location":"OLD_BEACON_HUT", "time":"PRE-DAWN",
        "characters":["@AMA_ADJOVI","@KOSI_MENSAH","@SENA_ADJOVI","@KOJO_DANSO"], "mood":"revelatory and ancestral", "lighting":"thin pre-dawn blue with a red moon fading behind cloud",
        "script":"INT. OLD BEACON HUT — PRE-DAWN\n\nAma leads them to a forgotten beacon hut. She tells how the town's elders saved the landing deed during a colonial survey by encoding its archive number in a lantern rhythm. Kosi recognizes the rhythm as the frequency in the hidden page.\n\nAMA\nMemory is not a box. It is a signal someone must answer.\n\nSena turns the phrase into a radio sign-off."
    },
    {
        "id":"S13", "act":2, "title":"The Yard Stands Still", "location":"FISH_SMOKE_YARD", "time":"DAY",
        "characters":["@ESI_TETTEH","@KOSI_MENSAH","@SENA_ADJOVI","@NII_LAMPTEY"], "mood":"defiant collective action", "lighting":"white daylight softened by smoke haze",
        "script":"EXT. FISH-SMOKE YARD — DAY\n\nEsi calls a one-day work stoppage. Fish trays are stacked across the road to the resort gate, but no one blocks ambulances or families. Nii arrives to call the action unlawful. Kosi offers water-sample results; he refuses to read them.\n\nESI\nWe are not stopping work. We are stopping theft from wearing a hard hat.\n\nNII\nYou are making a spectacle.\n\nSENA\nNo, Chairman. We are broadcasting one."
    },
    {
        "id":"S14", "act":2, "title":"Archive of the Unheard", "location":"COUNCIL_ARCHIVE", "time":"NIGHT",
        "characters":["@KOSI_MENSAH","@KWAME_AGYEMAN","@SENA_ADJOVI"], "mood":"quiet betrayal turning toward alliance", "lighting":"single green desk lamp, dust and darkness",
        "script":"INT. COUNCIL ARCHIVE — NIGHT\n\nKwame opens the archive after hours. They find the original landing record, plus a recent amendment bearing a digital stamp from an office that was closed that day. Sena photographs every page. A sound in the stairwell makes Kwame freeze.\n\nKWAME\nIf I send this out, I am finished here.\n\nKOSI\nIf you hide it, so are we.\n\nHe hands her the keycard."
    },
    {
        "id":"S15", "act":2, "title":"When the Power Fails", "location":"LAGOON_PROMENADE", "time":"DUSK",
        "characters":["@KOSI_MENSAH","@AMA_ADJOVI","@ESI_TETTEH","@KOJO_DANSO","@SENA_ADJOVI"], "mood":"loss becoming a plan", "lighting":"sudden blackout, last coral sunset and handmade lantern glow",
        "script":"EXT. LAGOON PROMENADE — DUSK\n\nThe town's power fails during the promenade meeting. Ama collapses briefly from exhaustion, not injury; Kosi steadies her. Around them, people raise phone lights, then hand lanterns. Kosi realizes the old beacon can transmit the archive frequency farther than the radio shack.\n\nKOSI\nTomorrow the town does not ask for a hearing. The town gives one.\n\nESI\nAnd who will light it?\n\nKOSI\nAll of us."
    },
    {
        "id":"S16", "act":3, "title":"A Thousand Small Lights", "location":"FESTIVAL_SQUARE", "time":"MORNING",
        "characters":["@KOSI_MENSAH","@AMA_ADJOVI","@SENA_ADJOVI","@KOJO_DANSO","@ESI_TETTEH","@KWAME_AGYEMAN"], "mood":"communal preparation", "lighting":"fresh sun, bright fabrics and building anticipation",
        "script":"EXT. FESTIVAL SQUARE — MORNING\n\nAfenyo makes lanterns from blue glass, jars and recycled solar cells. Kosi teaches children to wire safe low-voltage lights. Esi coordinates food. Kwame arrives without his lapel pin and offers the master access code. Ama gives Sena the oldest lantern.\n\nAMA\nA light means nothing if it only points at itself.\n\nSENA\nGood. Mine points at everybody."
    },
    {
        "id":"S17", "act":3, "title":"Signal on the Water", "location":"LAGOON_BEACON", "time":"BLUE HOUR",
        "characters":["@KOSI_MENSAH","@KOJO_DANSO","@SENA_ADJOVI","@KWAME_AGYEMAN"], "mood":"breath-held suspense", "lighting":"blue-hour sky, beacon amber and reflected lantern trail",
        "script":"EXT. LAGOON BEACON — BLUE HOUR\n\nKojo brings Kosi, Sena and Kwame to the beacon as a flotilla of lantern canoes forms behind them. Kosi connects a repaired solar cell. Sena broadcasts the archive scans and water tests. Kwame sends the unredacted map to regional reporters. The beacon answers with a steady blue pulse.\n\nSENA (ON AIR)\nAfenyo is speaking. Please do not call this noise.\n\nThe whole lagoon hears the signal."
    },
    {
        "id":"S18", "act":3, "title":"The Chair Answers", "location":"COMMUNITY_HALL", "time":"NIGHT",
        "characters":["@NII_LAMPTEY","@KOSI_MENSAH","@ESI_TETTEH","@SENA_ADJOVI","@KWAME_AGYEMAN","@AMA_ADJOVI"], "mood":"public reckoning", "lighting":"amber lanterns, projection glow and rain-muted night",
        "script":"INT. COMMUNITY HALL — NIGHT\n\nThe broadcast draws the town into the hall. The scanned deeds and live water readings appear on the blank sheet. Nii enters to reclaim the room, but one fisherman names the date the landing was promised and another woman corrects him. Nii finally sees that the record is no longer his to bury.\n\nNII\nDevelopment requires difficult decisions.\n\nAMA\nThen let the people who carry the difficulty make them.\n\nNii lowers his cane."
    },
    {
        "id":"S19", "act":3, "title":"The Water Is Public", "location":"DISTRICT_ASSEMBLY_HALL", "time":"MORNING",
        "characters":["@KOSI_MENSAH","@ESI_TETTEH","@KWAME_AGYEMAN","@NII_LAMPTEY","@SENA_ADJOVI"], "mood":"earned clarity", "lighting":"clean post-rain daylight through open louvre windows",
        "script":"INT. DISTRICT ASSEMBLY HALL — MORNING\n\nUnder public observation, the assembly suspends the resort permit pending an independent inquiry. Nii reads the order himself. Kwame submits his resignation and the complete project files. Esi insists the victory include a cooperative water board, not merely a pause.\n\nKOSI\nA pause is only a door if we decide what walks through it.\n\nThe room votes for the board. Sena catches the sound on her recorder."
    },
    {
        "id":"S20", "act":3, "title":"First Light, Shared", "location":"SUNRISE_PIER", "time":"SUNRISE",
        "characters":["@KOSI_MENSAH","@AMA_ADJOVI","@SENA_ADJOVI","@KOJO_DANSO","@ESI_TETTEH","@KWAME_AGYEMAN"], "mood":"hopeful, lived-in renewal", "lighting":"soft gold sunrise over calm teal water",
        "script":"EXT. SUNRISE PIER — SUNRISE\n\nThe repaired beacon flashes over the lagoon. Kosi and Kojo secure a community-owned solar battery at the pier while Esi's cooperative prepares boats. Ama watches Sena begin a new radio programme: The Water Remembers. Kwame, now in work gloves over the same clothes, joins the line carrying nets.\n\nSENA (ON AIR)\nThis is Afenyo. The light is public. The water is public. Good morning.\n\nKosi looks at Ama. The elder nods. The lagoon brightens. FADE OUT."
    },
]

# Each of these ten beats becomes one complete planned shot. The varied visual grammar is
# fixed so every row has an explicit size, camera angle, action, mood and lighting.
visual_grammar = [
    ("WIDE", "high establishing angle"),
    ("MEDIUM", "eye-level"),
    ("CLOSE", "three-quarter profile"),
    ("INSERT", "top-down detail"),
    ("TWO-SHOT", "eye-level"),
    ("OVER-SHOULDER", "over the lead character's shoulder"),
    ("EXTREME CLOSE", "intimate frontal angle"),
    ("WIDE", "low observational angle"),
    ("MEDIUM", "handheld eye-level"),
    ("WIDE", "rear closing tableau"),
]

beats = {
"S01": [
 ("accra_roof_arrival", ["@KOSI_MENSAH"], "Kosi crosses the orderly solar roof with her tool case as Accra spreads beneath her."),
 ("panel_diagnosis", ["@KOSI_MENSAH"], "Kosi kneels beside a silent panel string and checks its junction box."),
 ("focused_engineer", ["@KOSI_MENSAH"], "Kosi concentrates on the meter reading, sweat and resolve visible in her face."),
 ("tester_display", ["@KOSI_MENSAH"], "A gloved hand holds a tester against a sunlit cable connection."),
 ("phone_message", ["@KOSI_MENSAH"], "Kosi listens to Ama's voice message, city glare behind her."),
 ("voice_from_home", ["@KOSI_MENSAH"], "Over Kosi's shoulder, the phone waveform plays while she looks toward the horizon."),
 ("decision_in_eyes", ["@KOSI_MENSAH"], "Kosi's eyes harden as she decides to return home."),
 ("panels_awake", ["@KOSI_MENSAH"], "The repaired panels gleam in rows as Kosi stands among them."),
 ("packing_tools", ["@KOSI_MENSAH"], "Kosi packs a wrench, tester and cables into her battered case."),
 ("leaving_roof", ["@KOSI_MENSAH"], "Kosi walks toward the roof exit with her case as the panels hum behind her."),
],
"S02": [
 ("bus_stop_establish", ["@KOSI_MENSAH"], "A tro-tro pulls away from the red-earth stop, leaving Kosi in the sea wind."),
 ("arrival_with_case", ["@KOSI_MENSAH"], "Kosi steadies her tool case beside cassava baskets and looks toward the lagoon."),
 ("sena_spots_kosi", ["@SENA_ADJOVI"], "Sena grins beneath turquoise headphones as she spots Kosi."),
 ("radio_mic", ["@SENA_ADJOVI"], "Sena's small microphone and turquoise headphone cable rest against her mustard hoodie."),
 ("cousins_reunite", ["@KOSI_MENSAH","@SENA_ADJOVI"], "Sena reaches for Kosi's case rather than a hug; Kosi laughs despite herself."),
 ("fear_confession", ["@KOSI_MENSAH","@SENA_ADJOVI"], "Over Sena's shoulder, Kosi hears that Ama is afraid."),
 ("sena_truthful", ["@SENA_ADJOVI"], "Sena's brave face falters for one honest second."),
 ("wind_and_vendors", ["@KOSI_MENSAH","@SENA_ADJOVI"], "Wind lifts striped umbrellas around the two cousins amid the busy stop."),
 ("walk_home", ["@KOSI_MENSAH","@SENA_ADJOVI"], "Kosi and Sena walk along the lagoon road, one carrying tools and one recording sound."),
 ("road_to_compound", ["@KOSI_MENSAH","@SENA_ADJOVI"], "Their small figures head toward Afenyo's palms and blue water."),
],
"S03": [
 ("compound_reveal", ["@AMA_ADJOVI"], "Ama waits beneath the mango tree in the courtyard beside an unlit blue-glass lantern."),
 ("kosi_enters", ["@KOSI_MENSAH"], "Kosi steps through the weathered blue door and scans her childhood courtyard."),
 ("ama_welcome", ["@AMA_ADJOVI"], "Ama hides a tremor with a warm, teasing smile."),
 ("unlit_lantern", ["@AMA_ADJOVI"], "The dusty blue-glass courtyard lantern hangs dark against sunset."),
 ("family_embrace", ["@KOSI_MENSAH","@AMA_ADJOVI"], "Kosi hugs Ama tightly while Sena watches from a woven stool."),
 ("noticed_tremor", ["@KOSI_MENSAH","@AMA_ADJOVI"], "Over Kosi's shoulder, Ama's hand trembles against the indigo jumpsuit."),
 ("ama_warning", ["@AMA_ADJOVI"], "Ama explains the meaning of a dark lantern with quiet gravity."),
 ("glass_garland", ["@SENA_ADJOVI"], "Sena strings blue glass scraps into the mango branches."),
 ("shared_supper", ["@KOSI_MENSAH","@AMA_ADJOVI","@SENA_ADJOVI"], "The three sit near untouched pepper soup as sunset turns the courtyard amber."),
 ("lantern_between_them", ["@KOSI_MENSAH","@AMA_ADJOVI"], "Kosi faces the dark lantern while Ama watches her understand."),
],
"S04": [
 ("market_morning", ["@ESI_TETTEH","@SENA_ADJOVI"], "The market wakes around fish baskets, bright canopies and a restless lagoon."),
 ("esi_notice", ["@ESI_TETTEH"], "Esi slaps a wet survey notice onto a fish tray with her charred paddle."),
 ("kojo_smell", ["@KOJO_DANSO"], "Kojo looks toward the water, naming the metallic smell in the current."),
 ("survey_map", ["@KOSI_MENSAH"], "Kosi's finger tracks an unfamiliar utility line on the crumpled notice."),
 ("four_way_debate", ["@KOSI_MENSAH","@SENA_ADJOVI","@ESI_TETTEH","@KOJO_DANSO"], "Esi, Kojo, Kosi and Sena circle the notice amid the crowded market."),
 ("line_to_buoy", ["@KOSI_MENSAH","@ESI_TETTEH"], "Over Kosi's shoulder, the diagram points toward the navigation buoy."),
 ("esi_anger", ["@ESI_TETTEH"], "Esi refuses the promise of access behind a locked gate."),
 ("market_listens", ["@ESI_TETTEH","@KOSI_MENSAH","@SENA_ADJOVI"], "Nearby sellers pause to listen as Sena records voices."),
 ("kosi_sets_plan", ["@KOSI_MENSAH","@KOJO_DANSO"], "Kosi asks Kojo to show her where the cables entered the shore."),
 ("toward_lagoon", ["@KOSI_MENSAH","@KOJO_DANSO","@SENA_ADJOVI"], "Kosi, Kojo and Sena leave the market toward the blue-green lagoon."),
],
"S05": [
 ("hall_establish", ["@NII_LAMPTEY","@KWAME_AGYEMAN"], "The assembly hall fills slowly beneath ceiling fans while Nii and Kwame wait at the dais."),
 ("nii_presentation", ["@NII_LAMPTEY"], "Nii presents the resort as a polished future of jobs and clean power."),
 ("kwame_recognizes", ["@KWAME_AGYEMAN"], "Kwame catches sight of Kosi among the public and his rehearsed smile slips."),
 ("blank_map_wall", ["@NII_LAMPTEY"], "An empty wall beside the dais makes the missing public map conspicuous."),
 ("esi_demands_copy", ["@ESI_TETTEH","@NII_LAMPTEY"], "Esi stands to demand a public copy of the lagoon agreement."),
 ("kosi_challenges", ["@KOSI_MENSAH","@NII_LAMPTEY"], "Over Kosi's shoulder, Nii answers her question about why no map is displayed."),
 ("sena_records", ["@SENA_ADJOVI"], "Sena silently presses record beneath turquoise headphones."),
 ("room_divides", ["@KOSI_MENSAH","@ESI_TETTEH","@KWAME_AGYEMAN","@NII_LAMPTEY"], "The public hall divides between concerned residents and officials at the dais."),
 ("kwame_discomfort", ["@KWAME_AGYEMAN"], "Kwame adjusts his bronze compass pin, visibly uneasy."),
 ("hearing_ends", ["@KOSI_MENSAH","@SENA_ADJOVI","@ESI_TETTEH"], "Kosi leaves with Sena and Esi as the polite hearing closes behind them."),
],
"S06": [
 ("channel_dusk", ["@KOJO_DANSO"], "Kojo's narrow canoe glides into the violet channel toward the dark navigation buoy."),
 ("kojo_paddles", ["@KOJO_DANSO"], "Kojo rows steadily, brass compass moving against his striped shirt."),
 ("kosi_tests", ["@KOSI_MENSAH"], "Kosi kneels in the canoe and tests the buoy's dead solar housing."),
 ("bypassed_cable", ["@KOSI_MENSAH"], "A severed solar connection and newer buried cable meet beneath the buoy casing."),
 ("two_at_buoy", ["@KOSI_MENSAH","@KOJO_DANSO"], "Kosi and Kojo balance beside the rusted buoy as resort lights glow far away."),
 ("slick_in_water", ["@KOSI_MENSAH"], "Over Kosi's shoulder, a thin oily slick shivers across teal water."),
 ("kojo_warning", ["@KOJO_DANSO"], "Kojo speaks of the channel that has always carried the town outward."),
 ("dead_lantern", ["@KOSI_MENSAH","@KOJO_DANSO"], "The unlit lantern crown silhouettes against the dusk sky."),
 ("photo_evidence", ["@KOSI_MENSAH"], "Kosi photographs the severed connection with steady hands."),
 ("returning_decision", ["@KOSI_MENSAH","@KOJO_DANSO"], "The canoe turns home as Kosi's decision settles over the dark water."),
],
"S07": [
 ("workshop_night", ["@AMA_ADJOVI","@KOSI_MENSAH"], "Ama's workshop glows with brass lanterns while Kosi opens a damaged frame."),
 ("kosi_repairs", ["@KOSI_MENSAH"], "Kosi uses a small tool to reconnect a lantern wire at the workbench."),
 ("ama_watches", ["@AMA_ADJOVI"], "Ama watches Kosi work with pride and guarded concern."),
 ("hidden_page", ["@KOSI_MENSAH"], "A rolled water-stained ledger page slides from behind a loose blue glass pane."),
 ("sena_decodes", ["@SENA_ADJOVI"], "Sena recognizes a repeating code in the page's hand-drawn wave marks."),
 ("legacy_handoff", ["@KOSI_MENSAH","@AMA_ADJOVI"], "Over Kosi's shoulder, Ama closes Kosi's hand around the recovered page."),
 ("ama_memory", ["@AMA_ADJOVI"], "Ama explains that elders hid papers inside what kept people safe."),
 ("lanterns_crowd", ["@KOSI_MENSAH","@AMA_ADJOVI","@SENA_ADJOVI"], "Three generations stand among crowded lantern frames and copper wire."),
 ("frequency_found", ["@SENA_ADJOVI","@KOSI_MENSAH"], "Sena points from the coded waves to an old radio frequency in the ledger."),
 ("workshop_pact", ["@KOSI_MENSAH","@AMA_ADJOVI","@SENA_ADJOVI"], "The group makes a quiet pact beneath warm lantern light."),
],
"S08": [
 ("radio_shack_morning", ["@SENA_ADJOVI"], "Sena unlocks the tiny radio shack while morning brightens the market outside."),
 ("battery_connection", ["@KOSI_MENSAH"], "Kosi connects a temporary solar battery to the old mixing board."),
 ("sena_on_air", ["@SENA_ADJOVI"], "Sena leans into the battered microphone for the station's first clear broadcast."),
 ("level_meters", ["@SENA_ADJOVI"], "Tiny red recording lights and moving level meters glow on the mixing board."),
 ("esi_testimony", ["@ESI_TETTEH","@SENA_ADJOVI"], "Esi gives a fierce testimony into the microphone as Sena listens."),
 ("kosi_caution", ["@KOSI_MENSAH","@SENA_ADJOVI"], "Over Sena's shoulder, Kosi urges caution until they have proof."),
 ("sena_counter", ["@SENA_ADJOVI"], "Sena answers that fear itself has a voice that deserves air."),
 ("calls_arrive", ["@SENA_ADJOVI","@KOSI_MENSAH","@ESI_TETTEH"], "The cramped shack fills with ringing phones and a growing sense of listeners."),
 ("shared_microphone", ["@KOSI_MENSAH","@SENA_ADJOVI"], "Sena places the microphone between herself and Kosi."),
 ("signal_to_lagoon", ["@SENA_ADJOVI"], "The radio antenna points through the open window toward bright lagoon water."),
],
"S09": [
 ("fence_heat", ["@KWAME_AGYEMAN"], "Kwame waits alone at the chained resort gate in punishing afternoon heat."),
 ("kosi_arrives", ["@KOSI_MENSAH"], "Kosi approaches the fence with her tool case and an unblinking stare."),
 ("kwame_plan", ["@KWAME_AGYEMAN"], "Kwame unfolds an approved site plan against a corrugated fence panel."),
 ("redacted_route", ["@KWAME_AGYEMAN"], "A utility route disappears under a stark black redaction on the plan."),
 ("old_friends_distance", ["@KOSI_MENSAH","@KWAME_AGYEMAN"], "Kosi and Kwame face each other with the locked gate between them."),
 ("kosi_accuses", ["@KOSI_MENSAH","@KWAME_AGYEMAN"], "Over Kosi's shoulder, Kwame admits he is excluded from the discharge route."),
 ("kwame_shame", ["@KWAME_AGYEMAN"], "Kwame's eyes drop behind rimless spectacles as Kosi names his compromise."),
 ("fence_imprisons", ["@KOSI_MENSAH","@KWAME_AGYEMAN"], "Hard shadows of the fence divide the two former friends."),
 ("survey_number", ["@KOSI_MENSAH","@KWAME_AGYEMAN"], "Kosi photographs the survey number Kwame leaves visible on the plan."),
 ("kwame_leaves", ["@KOSI_MENSAH","@KWAME_AGYEMAN"], "Kwame walks along the fence while Kosi remains at the locked gate."),
],
"S10": [
 ("mangrove_entry", ["@KOJO_DANSO","@KOSI_MENSAH","@SENA_ADJOVI"], "A slim canoe slips into a shadowed mangrove passage."),
 ("kojo_poles", ["@KOJO_DANSO"], "Kojo poles carefully between tangled roots and dark water."),
 ("kosi_sensor", ["@KOSI_MENSAH"], "Kosi lowers a water sensor on a wire over the canoe's side."),
 ("meter_spike", ["@KOSI_MENSAH"], "The sensor display spikes sharply against Kosi's gloved hand."),
 ("three_in_canoe", ["@KOSI_MENSAH","@KOJO_DANSO","@SENA_ADJOVI"], "Kosi, Kojo and Sena hold their breath in the narrow canoe."),
 ("hidden_pipe", ["@KOSI_MENSAH","@SENA_ADJOVI"], "Over Kosi's shoulder, Sena films a concealed pipe pulsing warm grey water."),
 ("sena_fear", ["@SENA_ADJOVI"], "Sena whispers about being seen but keeps her phone steady."),
 ("engine_hush", ["@KOJO_DANSO","@KOSI_MENSAH","@SENA_ADJOVI"], "The trio freezes as a distant construction engine cuts out."),
 ("sample_sealed", ["@KOSI_MENSAH"], "Kosi seals the water sample with practiced precision."),
 ("escape_passage", ["@KOJO_DANSO","@KOSI_MENSAH","@SENA_ADJOVI"], "Kojo guides the canoe back through green-gold roots toward daylight."),
],
"S11": [
 ("flooded_home", ["@KOSI_MENSAH","@AMA_ADJOVI"], "Storm water fills the compound around the blue door and floating mango leaves."),
 ("kosi_lifts_leads", ["@KOSI_MENSAH"], "Kosi raises electrical leads above ankle-deep flood water."),
 ("ama_crate", ["@AMA_ADJOVI"], "Ama grips a crate of lanterns and refuses to leave it behind."),
 ("water_reflection", ["@AMA_ADJOVI"], "A blue lantern reflection trembles in flood water around Ama's sandals."),
 ("kojo_arrives", ["@KOJO_DANSO","@SENA_ADJOVI"], "Kojo wades in with a canoe as Sena reaches for the lantern crate."),
 ("kosi_reassures", ["@KOSI_MENSAH","@AMA_ADJOVI"], "Over Ama's shoulder, Kosi promises to make the water testify."),
 ("ama_remembers", ["@AMA_ADJOVI"], "Ama speaks of water remembering every blocked path."),
 ("rescue_team", ["@KOSI_MENSAH","@AMA_ADJOVI","@SENA_ADJOVI","@KOJO_DANSO"], "The family floats tools and lanterns toward Kojo's waiting canoe."),
 ("first_flicker", ["@KOSI_MENSAH","@SENA_ADJOVI"], "A blue lantern sputters to life between rain lashes."),
 ("storm_lantern", ["@KOSI_MENSAH","@AMA_ADJOVI","@SENA_ADJOVI","@KOJO_DANSO"], "One small lantern burns over the flooded courtyard as the group works together."),
],
"S12": [
 ("sandbar_hut", ["@AMA_ADJOVI","@KOSI_MENSAH","@SENA_ADJOVI","@KOJO_DANSO"], "The group approaches the derelict beacon hut across a lonely predawn sandbar."),
 ("ama_leads", ["@AMA_ADJOVI"], "Ama steps through the cracked doorway with amber beads catching the blue light."),
 ("kosi_listens", ["@KOSI_MENSAH"], "Kosi listens closely as Ama begins the old story."),
 ("broken_glass", ["@AMA_ADJOVI"], "Broken blue beacon glass lies among salt-stained timber and reed grass."),
 ("told_history", ["@AMA_ADJOVI","@KOSI_MENSAH"], "Ama recounts how elders preserved a public landing deed during a survey."),
 ("frequency_realization", ["@KOSI_MENSAH","@SENA_ADJOVI"], "Over Kosi's shoulder, Sena compares the page's rhythm to the radio frequency."),
 ("ama_signal", ["@AMA_ADJOVI"], "Ama says memory is a signal someone must answer."),
 ("red_moon", ["@AMA_ADJOVI","@KOSI_MENSAH","@SENA_ADJOVI","@KOJO_DANSO"], "The fading red moon frames the group in the beacon hut doorway."),
 ("sena_signoff", ["@SENA_ADJOVI"], "Sena repeats Ama's words into her pocket recorder, finding a new sign-off."),
 ("leaving_hut", ["@AMA_ADJOVI","@KOSI_MENSAH","@SENA_ADJOVI","@KOJO_DANSO"], "They leave the beacon hut carrying an old signal into first light."),
],
"S13": [
 ("smoke_yard", ["@ESI_TETTEH"], "Esi's smoke yard stands still: ovens cold, fish trays stacked, workers watching."),
 ("esi_calls_stop", ["@ESI_TETTEH"], "Esi raises her charred paddle and calls for a careful work stoppage."),
 ("kosi_results", ["@KOSI_MENSAH"], "Kosi holds water-sample results protected in a clear sleeve."),
 ("fish_tray_barrier", ["@ESI_TETTEH"], "Woven fish trays make a nonviolent barrier across the resort road."),
 ("nii_arrives", ["@NII_LAMPTEY","@ESI_TETTEH"], "Nii arrives with his ebony heron cane as Esi meets him in the smoke."),
 ("proof_refused", ["@KOSI_MENSAH","@NII_LAMPTEY"], "Over Kosi's shoulder, Nii refuses even to read the water results."),
 ("esi_defiance", ["@ESI_TETTEH"], "Esi says theft does not become progress by wearing a hard hat."),
 ("yard_united", ["@ESI_TETTEH","@KOSI_MENSAH","@SENA_ADJOVI","@NII_LAMPTEY"], "Fish smokers stand shoulder to shoulder amid luminous smoke."),
 ("sena_broadcasts", ["@SENA_ADJOVI"], "Sena broadcasts Esi's words into her small microphone."),
 ("silent_standoff", ["@ESI_TETTEH","@NII_LAMPTEY"], "The smoke-yard standoff holds as the whole town watches."),
],
"S14": [
 ("archive_dark", ["@KWAME_AGYEMAN"], "Kwame unlocks the dim archive beneath the assembly hall after hours."),
 ("kosi_files", ["@KOSI_MENSAH"], "Kosi searches rows of bound land ledgers with quick, careful hands."),
 ("kwame_guard", ["@KWAME_AGYEMAN"], "Kwame listens toward the stairwell while holding the keycard."),
 ("original_deed", ["@KOSI_MENSAH"], "An original public-landing record opens beneath the green-shaded desk lamp."),
 ("forged_amendment", ["@KOSI_MENSAH","@KWAME_AGYEMAN"], "Kosi and Kwame compare the recent amendment with the record that disproves it."),
 ("sena_photographs", ["@SENA_ADJOVI","@KOSI_MENSAH"], "Over Sena's shoulder, pages are photographed one after another."),
 ("kwame_confesses", ["@KWAME_AGYEMAN"], "Kwame admits that releasing the files will finish him at the council."),
 ("three_in_dust", ["@KOSI_MENSAH","@KWAME_AGYEMAN","@SENA_ADJOVI"], "Dusty shelves close around the three as a sound rises in the stairwell."),
 ("keycard_handoff", ["@KOSI_MENSAH","@KWAME_AGYEMAN"], "Kwame places the archive keycard in Kosi's open palm."),
 ("escape_archive", ["@KOSI_MENSAH","@KWAME_AGYEMAN","@SENA_ADJOVI"], "The trio slips from the dark archive carrying copied proof."),
],
"S15": [
 ("promenade_blackout", ["@KOSI_MENSAH","@ESI_TETTEH","@SENA_ADJOVI"], "The lagoon promenade falls suddenly dark as a meeting gathers at dusk."),
 ("phone_lights", ["@SENA_ADJOVI"], "Phone lights bloom in the crowd beneath a fading coral sky."),
 ("ama_falters", ["@AMA_ADJOVI"], "Ama briefly loses strength beside the cracked sea wall."),
 ("kosi_supports_ama", ["@KOSI_MENSAH","@AMA_ADJOVI"], "Kosi catches Ama and steadies her with quiet concern."),
 ("esi_asks_who", ["@ESI_TETTEH","@KOSI_MENSAH"], "Esi asks who will light the town's hearing."),
 ("kosi_beacon_plan", ["@KOSI_MENSAH","@ESI_TETTEH"], "Over Kosi's shoulder, Kosi points toward the distant beacon and explains the broadcast plan."),
 ("ama_recovers", ["@AMA_ADJOVI"], "Ama regains her breath and looks toward the handmade lights."),
 ("people_lanterns", ["@KOSI_MENSAH","@AMA_ADJOVI","@ESI_TETTEH","@SENA_ADJOVI","@KOJO_DANSO"], "Residents raise lanterns along the dark promenade."),
 ("all_of_us", ["@KOSI_MENSAH"], "Kosi says the town will light itself, resolve clear in her face."),
 ("dusk_commitment", ["@KOSI_MENSAH","@AMA_ADJOVI","@ESI_TETTEH","@SENA_ADJOVI","@KOJO_DANSO"], "Lantern light draws a communal line along the lagoon at dusk."),
],
"S16": [
 ("square_preparation", ["@KOSI_MENSAH","@AMA_ADJOVI","@SENA_ADJOVI","@KOJO_DANSO","@ESI_TETTEH"], "Festival Square fills with people building lanterns beneath the silk-cotton tree."),
 ("kosi_teaches", ["@KOSI_MENSAH"], "Kosi teaches children to connect safe low-voltage solar cells."),
 ("ama_glass", ["@AMA_ADJOVI"], "Ama sorts blue glass panes with her amber beads catching the morning sun."),
 ("lantern_parts", ["@KOSI_MENSAH"], "Hands arrange recycled solar cells, blue glass and copper wire on red earth."),
 ("esi_coordinates", ["@ESI_TETTEH"], "Esi directs food, work tables and volunteers with her smoking paddle."),
 ("kwame_arrives", ["@KWAME_AGYEMAN","@KOSI_MENSAH"], "Over Kosi's shoulder, Kwame arrives without his bronze lapel pin and offers the master code."),
 ("sena_oldest_lantern", ["@SENA_ADJOVI","@AMA_ADJOVI"], "Ama hands Sena the oldest blue-glass lantern in the square."),
 ("growing_lights", ["@KOSI_MENSAH","@AMA_ADJOVI","@SENA_ADJOVI","@KOJO_DANSO","@ESI_TETTEH","@KWAME_AGYEMAN"], "Six allies work amid strings of lanterns that slowly begin to glow."),
 ("sena_points_outward", ["@SENA_ADJOVI"], "Sena says her light points at everybody, smiling beneath turquoise headphones."),
 ("square_ready", ["@KOSI_MENSAH","@AMA_ADJOVI","@SENA_ADJOVI","@KOJO_DANSO","@ESI_TETTEH","@KWAME_AGYEMAN"], "The prepared square gleams with a thousand small, unlit promises."),
],
"S17": [
 ("beacon_blue_hour", ["@KOSI_MENSAH","@KOJO_DANSO","@SENA_ADJOVI","@KWAME_AGYEMAN"], "Kojo's canoe reaches the restored beacon as lantern canoes gather in the distance."),
 ("kojo_moors", ["@KOJO_DANSO"], "Kojo secures the canoe to the buoy with practiced hands."),
 ("kosi_connects", ["@KOSI_MENSAH"], "Kosi connects a repaired solar cell inside the blue-glass lantern crown."),
 ("archive_signal", ["@SENA_ADJOVI"], "Sena's broadcast equipment displays the transmitted archive pages and water readings."),
 ("four_at_beacon", ["@KOSI_MENSAH","@KOJO_DANSO","@SENA_ADJOVI","@KWAME_AGYEMAN"], "The four balance at the beacon as a flotilla of lights forms behind them."),
 ("kwame_sends_files", ["@KWAME_AGYEMAN"], "Over Kwame's shoulder, he sends the unredacted map to regional reporters."),
 ("sena_on_air", ["@SENA_ADJOVI"], "Sena announces that Afenyo is speaking and asks listeners not to call it noise."),
 ("flotilla_glow", ["@KOSI_MENSAH","@KOJO_DANSO","@SENA_ADJOVI","@KWAME_AGYEMAN"], "Lantern canoes glow in a broad arc across the blue lagoon."),
 ("beacon_pulse", ["@KOSI_MENSAH"], "The blue-glass beacon gives its first steady pulse."),
 ("lagoon_hears", ["@KOSI_MENSAH","@KOJO_DANSO","@SENA_ADJOVI","@KWAME_AGYEMAN"], "The beacon and flotilla burn together beneath a vast cloud-streaked sky."),
],
"S18": [
 ("hall_lanterns", ["@ESI_TETTEH","@SENA_ADJOVI","@AMA_ADJOVI"], "Afenyo packs the community hall under amber lantern light and rain-darkened night."),
 ("projected_deed", ["@SENA_ADJOVI"], "The landing deed and water data shine clearly on a blank projection sheet."),
 ("nii_enters", ["@NII_LAMPTEY"], "Nii enters the open hall with his ebony heron cane and confronts the crowd."),
 ("watching_faces", ["@AMA_ADJOVI"], "Ama's calm face reflects the projection glow as neighbours begin to speak."),
 ("public_reckoning", ["@NII_LAMPTEY","@KOSI_MENSAH","@ESI_TETTEH","@SENA_ADJOVI","@KWAME_AGYEMAN","@AMA_ADJOVI"], "The principals face each other while the public owns the room around them."),
 ("kosi_evidence", ["@KOSI_MENSAH","@NII_LAMPTEY"], "Over Kosi's shoulder, live water readings refute the project safeguards."),
 ("ama_reply", ["@AMA_ADJOVI"], "Ama tells Nii that people carrying the difficulty must make the decision."),
 ("hall_answers", ["@ESI_TETTEH","@SENA_ADJOVI","@AMA_ADJOVI"], "Many residents raise their voices beneath rain-muted darkness."),
 ("nii_lowers_cane", ["@NII_LAMPTEY"], "Nii lowers his cane as the truth becomes impossible to re-bury."),
 ("shared_room", ["@NII_LAMPTEY","@KOSI_MENSAH","@ESI_TETTEH","@SENA_ADJOVI","@KWAME_AGYEMAN","@AMA_ADJOVI"], "Lanterns and projection light hold every face in the reclaimed hall."),
],
"S19": [
 ("morning_hall", ["@NII_LAMPTEY","@KWAME_AGYEMAN"], "Post-rain daylight fills the assembly hall before the public decision."),
 ("public_observers", ["@SENA_ADJOVI"], "Sena records rows of residents watching the dais in silence."),
 ("nii_reads_order", ["@NII_LAMPTEY"], "Nii reads the order suspending the resort permit pending inquiry."),
 ("suspension_paper", ["@NII_LAMPTEY"], "The signed suspension order rests beside Nii's silver wristwatch."),
 ("kwame_resigns", ["@KWAME_AGYEMAN","@KOSI_MENSAH"], "Kwame submits his resignation and complete project files to the assembly."),
 ("esi_demands_board", ["@ESI_TETTEH","@NII_LAMPTEY"], "Over Esi's shoulder, she insists that victory include a cooperative water board."),
 ("kosi_door", ["@KOSI_MENSAH"], "Kosi says a pause is only a door if the town decides what walks through it."),
 ("vote_rises", ["@KOSI_MENSAH","@ESI_TETTEH","@SENA_ADJOVI","@KWAME_AGYEMAN","@NII_LAMPTEY"], "Hands rise around the hall in support of the community water board."),
 ("sena_catches_sound", ["@SENA_ADJOVI"], "Sena captures the sound of the vote with a bright, astonished smile."),
 ("open_windows", ["@KOSI_MENSAH","@ESI_TETTEH","@SENA_ADJOVI","@KWAME_AGYEMAN"], "The allies leave through open louvre-lit doors into clean post-rain morning."),
],
"S20": [
 ("pier_sunrise", ["@KOSI_MENSAH","@KOJO_DANSO","@AMA_ADJOVI","@SENA_ADJOVI","@ESI_TETTEH","@KWAME_AGYEMAN"], "Sunrise opens across the fishing pier, repaired nets and calm gold-and-teal water."),
 ("kosi_battery", ["@KOSI_MENSAH"], "Kosi secures the community-owned solar battery at the pier."),
 ("kojo_nets", ["@KOJO_DANSO"], "Kojo lifts repaired fishing nets beneath the distant beacon pulse."),
 ("beacon_in_distance", ["@KOSI_MENSAH"], "The blue beacon flashes across calm water beyond painted canoes."),
 ("ama_and_sena", ["@AMA_ADJOVI","@SENA_ADJOVI"], "Ama watches Sena prepare the first episode of her new radio programme."),
 ("sena_good_morning", ["@SENA_ADJOVI"], "Over Sena's shoulder, she broadcasts that the light and water are public."),
 ("ama_nods", ["@AMA_ADJOVI"], "Ama's knowing smile softens as she nods to Kosi."),
 ("kwame_helps", ["@KWAME_AGYEMAN","@ESI_TETTEH"], "Kwame in work gloves joins Esi's line carrying fishing nets, no longer standing apart."),
 ("kosi_at_home", ["@KOSI_MENSAH","@AMA_ADJOVI"], "Kosi and Ama share a quiet look over the brightening lagoon."),
 ("first_light_shared", ["@KOSI_MENSAH","@AMA_ADJOVI","@SENA_ADJOVI","@KOJO_DANSO","@ESI_TETTEH","@KWAME_AGYEMAN"], "The whole pier works together beneath the first fully shared light."),
],
}

assert len(scenes) == 20
assert all(len(beats[s["id"]]) == 10 for s in scenes)
assert sum(len(x) for x in beats.values()) == 200

char_lookup = {c["tag"]: c for c in characters}


def shot_records():
    records = []
    for scene in scenes:
        for index, (slug, tags, action) in enumerate(beats[scene["id"]], start=1):
            size, angle = visual_grammar[index-1]
            sid = f'{scene["id"]}_Step{index:02d}'
            act_dir = f'images/act{scene["act"]}'
            filename = f'{sid}_{slug}.png'
            wardrobe = [f'{tag}: {char_lookup[tag]["wardrobe"]}; signature object: {char_lookup[tag]["object"]}' for tag in tags]
            location_text = locations[scene["location"]]
            consistency = wardrobe + [f"Environment = Location Registry id '{scene['location']}': {location_text}"]
            character_text = "; ".join(f"{tag} ({char_lookup[tag]['wardrobe']}, {char_lookup[tag]['object']})" for tag in tags)
            prompt = (
                f"{STYLE} Scene {scene['id']} — {scene['title']}. {size} shot, {angle}. "
                f"Characters in frame: {character_text}. {action} "
                f"Mood: {scene['mood']}. Lighting: {scene['lighting']}. "
                f"Environment = Location Registry id '{scene['location']}': {location_text}"
            )
            planned_file = f"{act_dir}/{filename}"
            records.append({
                "shot_id": sid, "scene": f"{scene['id']} — {scene['title']}", "act": scene["act"],
                "location_id": scene["location"], "location": location_text, "characters": tags,
                "shot_size": size, "camera_angle": angle, "action": action,
                "mood": scene["mood"], "lighting": scene["lighting"], "consistency": consistency,
                "prompt": prompt, "status": "✅" if (ROOT / planned_file).is_file() else "⬜", "file": planned_file,
            })
    return records


def write_screenplay():
    lines = [
        f"# {TITLE}", "", f"*{SUBTITLE}*", "",
        "## Production overview", "",
        "**Format:** Feature screenplay / 20-scene storyboard",
        "**Genre & tone:** Contemporary Ghanaian magical-realism drama; an intimate civic mystery that grows into a warm, hopeful community thriller.",
        "**Setting:** Afenyo, a fictional lagoon town on Ghana's coast; contemporary day.",
        "**Logline:** When a guarded solar engineer returns to her Ghanaian lagoon hometown and finds a resort project has darkened its public beacon, she, her lantern-maker grandmother and a teenage radio reporter must turn a hidden civic archive into a town-wide signal before the water is fenced away.",
        "**Theme:** Public things survive when ordinary people decide to remember and care for them together.", "",
        "## Visual style guide", "", STYLE, "",
        "### Continuity rules", "",
        "- Keep each principal in the exact signature wardrobe and signature object specified below in every present-day frame.\n- Reuse each location registry description **verbatim** in image prompts.\n- The magical-realism element is restrained: the lanterns and water carry emotional resonance, not overt supernatural effects.\n- Favour community-scale images, real working hands, tactile blue glass, reed, copper, wood and water.\n- Maintain 2.39:1 compositions and avoid readable text, logos, watermarks or generic tourism imagery.", "",
        "## Character Bible", "",
    ]
    for c in characters:
        lines.extend([
            f"### {c['tag']} — {c['name']}",
            f"- **Age / role:** {c['age']}; {c['role']}",
            f"- **Physical description:** {c['physical']}",
            f"- **Fixed signature wardrobe:** {c['wardrobe']}.",
            f"- **Signature object:** {c['object']}.",
            f"- **Personality:** {c['personality']}",
            f"- **One-line arc:** {c['arc']}", ""
        ])
    lines.extend(["## Screenplay", "", "### ACT I — RETURN", ""])
    for scene in scenes:
        if scene["id"] == "S07": lines.extend(["### ACT II — THE SIGNAL", ""])
        if scene["id"] == "S16": lines.extend(["### ACT III — PUBLIC LIGHT", ""])
        char_names = ", ".join(scene["characters"])
        lines.extend([
            f"## {scene['id']} — {scene['title']}",
            f"**Location:** `{scene['location']}` · **Time:** {scene['time']} · **Speaking characters:** {char_names}", "",
            scene["script"], ""
        ])
    (ROOT / "SCREENPLAY.md").write_text("\n".join(lines), encoding="utf-8")


def write_locations():
    lines = [f"# {TITLE} — Location Registry", "", "These canonical descriptions are locked continuity anchors. The exact description for the stated ID is inserted verbatim into every related JSON prompt.", ""]
    for key, description in locations.items():
        lines.extend([f"## `{key}`", "", f"> {description}", ""])
    (ROOT / "LOCATION_REGISTRY.md").write_text("\n".join(lines), encoding="utf-8")


def generated_reference_count():
    """Count only the locked reference filenames, never arbitrary files in images/refs."""
    return sum((ROOT / "images" / "refs" / f"{character['filename']}_ref.png").is_file() for character in characters)


def write_manifest(records):
    scene_done = sum(record["status"] == "✅" for record in records)
    refs_done = generated_reference_count()
    next_pending = next((record["shot_id"] for record in records if record["status"] == "⬜"), "All scene shots complete")
    lines = [
        f"# {TITLE} — Shot Manifest", "",
        "## Production state", "", f"- **Scene shots complete:** {scene_done} / {len(records)}", f"- **Character reference sheets complete:** {refs_done} / {len(characters)}", f"- **Next scene-image label after reference approval:** `{next_pending}`", "- **Status legend:** `✅` actual image exists and was reviewed in this package; `⬜` planned, not generated. A filename alone never changes status.", "",
        "## Locked visual basis", "", f"- **Style:** {STYLE}", "- **Character references:** generate and approve all seven `images/refs/*_ref.png` portraits before generating any scene shot.", "- **Location continuity:** each row below uses its `location_id` exactly as defined in `LOCATION_REGISTRY.md`.", "",
    ]
    for act in (1, 2, 3):
        act_scenes = [s for s in scenes if s["act"] == act]
        lines.extend([f"# ACT {['I — RETURN','II — THE SIGNAL','III — PUBLIC LIGHT'][act-1]}", ""])
        for scene in act_scenes:
            lines.extend([f"## {scene['id']} — {scene['title']} ({scene['location']})", "", "| Status | Label | Characters in frame | Size / camera | Action / blocking / emotion | Mood + lighting | Planned file |", "|---|---|---|---|---|---|---|"])
            for record in [r for r in records if r["scene"].startswith(scene["id"] + " ")]:
                lines.append(
                    f"| {record['status']} | `{record['shot_id']}` | {' '.join(record['characters'])} | {record['shot_size']} / {record['camera_angle']} | {record['action']} | {record['mood']}; {record['lighting']} | `{record['file']}` |"
                )
            lines.append("")
    (ROOT / "SHOT_MANIFEST.md").write_text("\n".join(lines), encoding="utf-8")


def write_prompts(records):
    scene_done = sum(record["status"] == "✅" for record in records)
    payload = {
        "project": TITLE,
        "subtitle": SUBTITLE,
        "visual_style": STYLE,
        "planned_shot_count": len(records),
        "generation_progress": {"scene_shots_complete": scene_done, "scene_shots_total": len(records), "references_complete": generated_reference_count(), "references_total": len(characters)},
        "shots": records,
    }
    (ROOT / "prompts.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    flat = [f"# {TITLE} — Flat image prompts", "", f"Planned scene images: {len(records)}. Scene generation is pending reference approval.", ""]
    for record in records:
        flat.extend([f"## {record['shot_id']} · {record['file']}", record["prompt"], ""])
    (ROOT / "prompts.txt").write_text("\n".join(flat), encoding="utf-8")


def write_reference_prompts():
    refs = []
    for c in characters:
        refs.append({
            "tag": c["tag"], "file": f"images/refs/{c['filename']}_ref.png",
            "prompt": (
                f"Vertical 2:3, full-body single-character reference portrait of {c['name']}, age {c['age']}; three-quarter standing pose, "
                f"from head to boots fully inside the frame, face and complete outfit clearly visible. {c['physical']} "
                f"Exact fixed wardrobe: {c['wardrobe']}. Exact signature object: {c['object']}, visibly and naturally worn or held. "
                f"Grounded, premium cinematic Ghanaian coastal drama; neutral warm clay studio backdrop; soft daylight; realistic natural skin texture; "
                f"authentic textile detail; clear silhouette; sophisticated editorial costume reference. One person only, no text, no labels, no logo, "
                f"no watermark, no collage, no character turnaround grid, no duplicate person, no cropped feet, no extra limbs."
            )
        })
    (ROOT / "REFERENCE_PROMPTS.json").write_text(json.dumps({"project": TITLE, "references": refs}, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    for folder in ("images/refs", "images/act1", "images/act2", "images/act3"):
        (ROOT / folder).mkdir(parents=True, exist_ok=True)
        keep = ROOT / folder / ".gitkeep"
        keep.touch(exist_ok=True)
    records = shot_records()
    write_screenplay()
    write_locations()
    write_manifest(records)
    write_prompts(records)
    write_reference_prompts()
    print(f"Wrote screenplay, registry, manifest, reference prompts and {len(records)} structured shot prompts in {ROOT}")

if __name__ == "__main__":
    main()
