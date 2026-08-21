"""Rush studio albums collection for the hark MCP server.

Covers all Rush studio releases 1974-2012, including the Feedback covers EP.
Lyric excerpts are short and used for commentary under fair use.
Biographical and review quotes attributed to their sources.
"""

QUOTES: dict = {
    "rush": {
        "title": "Rush (1974)",
        "summary": (
            "The self-titled debut, recorded with original drummer John Rutsey. "
            "A bluesy hard-rock record in the vein of Led Zeppelin and Cream, "
            "it gave the band a foothold through FM radio play of Working Man. "
            "Neil Peart had not yet joined."
        ),
        "quotes": [
            {
                "text": "I've been working so hard, just working for the man.",
                "speaker": "Geddy Lee",
                "themes": ["labor", "working_class", "blues_rock"],
            },
            {
                "text": "Finding my way to the morning sun, I've got no time for the road I'm on.",
                "speaker": "Geddy Lee",
                "themes": ["restlessness", "debut", "hard_rock"],
            },
            {
                "text": "Rush's debut is a highly promising record that shows a band still finding its own voice.",
                "speaker": "AllMusic",
                "themes": ["debut", "promise", "derivative"],
            },
            {
                "text": "We just wanted to play. We didn't think about a career, we thought about the next gig.",
                "speaker": "Alex Lifeson",
                "themes": ["early_years", "ambition", "live"],
            },
        ],
    },
    "fly_by_night": {
        "title": "Fly by Night (1975)",
        "summary": (
            "First album with Neil Peart on drums and as primary lyricist. "
            "The sound tightens and the lyrics reach toward fantasy and myth. "
            "By-Tor and the Snow Dog and Anthem announce the band's new direction."
        ),
        "quotes": [
            {
                "text": "Live for yourself, there's no one else more worth living for.",
                "speaker": "Neil Peart",
                "themes": ["individualism", "objectivism", "anthem"],
            },
            {
                "text": "Fly by night, away from here, change my life again.",
                "speaker": "Neil Peart",
                "themes": ["departure", "change", "flight"],
            },
            {
                "text": "Anthem was inspired by Ayn Rand. I was young and taken with the idea of self-reliance.",
                "speaker": "Neil Peart",
                "themes": ["objectivism", "rand", "influence"],
            },
            {
                "text": "The addition of Neil Peart transformed Rush from a capable hard rock band into something far more ambitious.",
                "speaker": "Rolling Stone",
                "themes": ["lineup_change", "lyrics", "ambition"],
            },
        ],
    },
    "caress_of_steel": {
        "title": "Caress of Steel (1975)",
        "summary": (
            "A divisive step toward long-form composition. The Fountain of Lamneth "
            "and The Necromancer push the band into sidelong epics and fantasy. "
            "Sales were poor and the label wanted a more commercial follow-up."
        ),
        "quotes": [
            {
                "text": "The Fountain of Lamneth showed we were willing to fail in public trying to do something bigger.",
                "speaker": "Geddy Lee",
                "themes": ["ambition", "epic", "risk"],
            },
            {
                "text": "Caress of Steel was the album that almost killed us. The label lost faith.",
                "speaker": "Alex Lifeson",
                "themes": ["commercial_failure", "label_pressure", "epic"],
            },
            {
                "text": "A flawed but fascinating record that pointed the way to 2112.",
                "speaker": "AllMusic",
                "themes": ["transitional", "flawed", "epic"],
            },
        ],
    },
    "2112": {
        "title": "2112 (1976)",
        "summary": (
            "The breakthrough. The seven-part title suite tells of a dystopian "
            "future where the Priests of Syrinx suppress music and an individual "
            "rediscovers a guitar. Rush dedicated the album to Ayn Rand. It "
            "vindicated the band after Caress of Steel and made their career."
        ),
        "quotes": [
            {
                "text": "We are the Priests of the Temples of Syrinx. Our great computers fill the hallowed halls.",
                "speaker": "Neil Peart",
                "themes": ["dystopia", "totalitarianism", "sci-fi"],
            },
            {
                "text": "I don't think I've ever seen a guitar. I don't think I've ever heard one play.",
                "speaker": "Neil Peart",
                "themes": ["discovery", "music", "individualism"],
            },
            {
                "text": "And the meek shall inherit the earth.",
                "speaker": "Neil Peart",
                "themes": ["collapse", "prophecy", "suite"],
            },
            {
                "text": "With acknowledgement to the genius of Ayn Rand.",
                "speaker": "Rush",
                "themes": ["objectivism", "rand", "dedication"],
            },
            {
                "text": "2112 is where Rush figured out how to be Rush.",
                "speaker": "AllMusic",
                "themes": ["breakthrough", "identity", "suite"],
            },
        ],
    },
    "farewell_to_kings": {
        "title": "A Farewell to Kings (1977)",
        "summary": (
            "Recorded at Rockfield Studios in Wales. The title track and Xanadu "
            "expand the band's range with classical guitar, synth openings, and "
            "an 11-minute Coleridge adaptation. Closer to the Heart became their "
            "first real radio hit."
        ),
        "quotes": [
            {
                "text": "Closer to the heart, closer to the heart.",
                "speaker": "Neil Peart",
                "themes": ["empathy", "idealism", "accessibility"],
            },
            {
                "text": "I will await the sun's rising, and drink the cup of wine.",
                "speaker": "Neil Peart",
                "themes": ["coleridge", "xanadu", "myth"],
            },
            {
                "text": "A Farewell to Kings showed a new maturity, both musically and lyrically.",
                "speaker": "AllMusic",
                "themes": ["maturity", "range", "growth"],
            },
            {
                "text": "We wanted to use the studio as an instrument, not just capture a live performance.",
                "speaker": "Alex Lifeson",
                "themes": ["production", "studio", "ambition"],
            },
        ],
    },
    "hemispheres": {
        "title": "Hemispheres (1978)",
        "summary": (
            "The band's most technically demanding record. The side-long title "
            "track balances Apollo and Dionysus, reason and emotion. La Villa "
            "Strangiato is an nine-part instrumental that became a live centerpiece."
        ),
        "quotes": [
            {
                "text": "La Villa Strangiato took us so many takes we nearly lost our minds.",
                "speaker": "Geddy Lee",
                "themes": ["virtuosity", "instrumental", "difficulty"],
            },
            {
                "text": "The struggle of the left and right hemispheres, of reason and feeling.",
                "speaker": "Neil Peart",
                "themes": ["philosophy", "duality", "balance"],
            },
            {
                "text": "Hemispheres is the peak of Rush's progressive period, a record of staggering complexity.",
                "speaker": "AllMusic",
                "themes": ["progressive", "complexity", "peak"],
            },
            {
                "text": "We were pushing ourselves to the edge of what we could play.",
                "speaker": "Alex Lifeson",
                "themes": ["virtuosity", "challenge", "power_trio"],
            },
        ],
    },
    "permanent_waves": {
        "title": "Permanent Waves (1980)",
        "summary": (
            "The pivot toward shorter songs and radio accessibility without losing "
            "complexity. The Spirit of Radio opens the record with a tribute to "
            "radio itself. Freewill and Natural Science balance philosophy and "
            "tight ensemble work. Their first top-five album in the UK."
        ),
        "quotes": [
            {
                "text": "Begin the day with a friendly voice, a companion half-way through the night.",
                "speaker": "Neil Peart",
                "themes": ["radio", "medium", "tribute"],
            },
            {
                "text": "If you choose not to decide, you still have made a choice.",
                "speaker": "Neil Peart",
                "themes": ["freewill", "choice", "philosophy"],
            },
            {
                "text": "Permanent Waves is where Rush reconciled their complexity with a genuine pop sense.",
                "speaker": "Rolling Stone",
                "themes": ["accessibility", "maturity", "pivot"],
            },
            {
                "text": "We were tired of writing sidelong epics. We wanted songs.",
                "speaker": "Geddy Lee",
                "themes": ["songwriting", "shift", "concision"],
            },
        ],
    },
    "moving_pictures": {
        "title": "Moving Pictures (1981)",
        "summary": (
            "Rush's commercial and artistic peak. Tom Sawyer, Red Barchetta, YYZ, "
            "and Limelight became permanent fixtures of rock radio and the band's "
            "live set. The album hit number three on the US chart and went "
            "multi-platinum. It is the record most listeners know them for."
        ),
        "quotes": [
            {
                "text": "Today's Tom Sawyer, he gets high on you, and the space he invades.",
                "speaker": "Neil Peart",
                "themes": ["individualism", "modern_man", "character"],
            },
            {
                "text": "Though his mind is not for rent, to any god or government.",
                "speaker": "Neil Peart",
                "themes": ["autonomy", "independence", "skepticism"],
            },
            {
                "text": "Living in the limelight, the universal dream for those who wish to seem.",
                "speaker": "Neil Peart",
                "themes": ["fame", "performance", "alienation"],
            },
            {
                "text": "YYZ is named after the IATA code for Toronto Pearson, our home airport.",
                "speaker": "Neil Peart",
                "themes": ["instrumental", "toronto", "identity"],
            },
            {
                "text": "Moving Pictures is Rush's masterpiece, the album where everything came together.",
                "speaker": "AllMusic",
                "themes": ["masterpiece", "peak", "classic"],
            },
        ],
    },
    "signals": {
        "title": "Signals (1982)",
        "summary": (
            "Synths move to the front of the mix. Subdivisions becomes an anthem "
            "for the suburban outsider. New World Man was a surprise hit single. "
            "Some fans resisted the keyboard-heavy direction, but the band "
            "committed to it for the rest of the decade."
        ),
        "quotes": [
            {
                "text": "Subdivisions in the basement bars, in the shadows of the stadiums.",
                "speaker": "Neil Peart",
                "themes": ["suburbia", "alienation", "conformity"],
            },
            {
                "text": "Be cool or be cast out.",
                "speaker": "Neil Peart",
                "themes": ["conformity", "peer_pressure", "youth"],
            },
            {
                "text": "Signals alienated some fans but it's one of Rush's most consistent records.",
                "speaker": "AllMusic",
                "themes": ["synths", "division", "consistency"],
            },
            {
                "text": "The keyboards weren't a gimmick. They were where we wanted to go.",
                "speaker": "Geddy Lee",
                "themes": ["synths", "evolution", "conviction"],
            },
        ],
    },
    "grace_under_pressure": {
        "title": "Grace Under Pressure (1984)",
        "summary": (
            "A cold-war record. Distant Early Warning and Red Sector A engage "
            "nuclear anxiety and Holocaust memory. The synths stay prominent "
            "but the mood is darker and more anxious than Signals."
        ),
        "quotes": [
            {
                "text": "Distant early warning, a future out of control.",
                "speaker": "Neil Peart",
                "themes": ["cold_war", "anxiety", "warning"],
            },
            {
                "text": "Red Sector A was inspired by my parents' experience in the camps.",
                "speaker": "Geddy Lee",
                "themes": ["holocaust", "memory", "family"],
            },
            {
                "text": "Grace Under Pressure is Rush at their most anxious, a record steeped in dread.",
                "speaker": "AllMusic",
                "themes": ["anxiety", "cold_war", "darkness"],
            },
            {
                "text": "The title comes from Hemingway's definition of courage: grace under pressure.",
                "speaker": "Neil Peart",
                "themes": ["hemingway", "courage", "title"],
            },
        ],
    },
    "power_windows": {
        "title": "Power Windows (1985)",
        "summary": (
            "Synths and politics dominate. The Big Money, Manhattan Project, and "
            "Territories examine wealth, the atomic bomb, and imperialism. "
            "Production is dense and bright, the most keyboard-forward Rush album."
        ),
        "quotes": [
            {
                "text": "The big money, the big money, the big money.",
                "speaker": "Neil Peart",
                "themes": ["wealth", "capitalism", "critique"],
            },
            {
                "text": "Manhattan Project recounted the making of the bomb with a kind of awe and horror.",
                "speaker": "AllMusic",
                "themes": ["nuclear", "history", "awe"],
            },
            {
                "text": "Power Windows is the most synthetic Rush album, for better and worse.",
                "speaker": "Rolling Stone",
                "themes": ["synths", "politics", "production"],
            },
            {
                "text": "We were interested in power in all its forms, political and personal.",
                "speaker": "Neil Peart",
                "themes": ["power", "politics", "theme"],
            },
        ],
    },
    "hold_your_fire": {
        "title": "Hold Your Fire (1987)",
        "summary": (
            "The band pushes further into synth-pop texture. Time Stand Still, "
            "featuring Aimee Mann, became a signature late-period song. Lyrics "
            "turn toward time, restraint, and relationships. Commercial results "
            "were softer than Moving Pictures."
        ),
        "quotes": [
            {
                "text": "Time stand still, I'm not looking back but I want to look around me now.",
                "speaker": "Neil Peart",
                "themes": ["time", "mortality", "presence"],
            },
            {
                "text": "Hold Your Fire is Rush's most melodic and least aggressive album.",
                "speaker": "AllMusic",
                "themes": ["melody", "synths", "softening"],
            },
            {
                "text": "I wanted to write about things that weren't just abstract.",
                "speaker": "Neil Peart",
                "themes": ["personal", "maturity", "lyrics"],
            },
            {
                "text": "Aimee Mann's vocal on Time Stand Still gave it exactly the ache it needed.",
                "speaker": "Geddy Lee",
                "themes": ["collaboration", "vocals", "single"],
            },
        ],
    },
    "presto": {
        "title": "Presto (1989)",
        "summary": (
            "A deliberate pullback from synths toward guitar and band performance. "
            "Produced by Rupert Hine. The songs are shorter and more playful, "
            "with Chain Lightning and The Pass among the standouts."
        ),
        "quotes": [
            {
                "text": "We wanted to get back to being a band, not a production.",
                "speaker": "Alex Lifeson",
                "themes": ["return_to_guitar", "band", "pullback"],
            },
            {
                "text": "Presto is a quiet rebound, guitar-forward and warm.",
                "speaker": "AllMusic",
                "themes": ["rebound", "guitar", "warmth"],
            },
            {
                "text": "The Pass is about suicide and the choice to keep going. It's one of Neil's heaviest lyrics.",
                "speaker": "Geddy Lee",
                "themes": ["suicide", "hope", "lyrics"],
            },
            {
                "text": "I'd been writing too many songs about abstractions. I wanted something more human.",
                "speaker": "Neil Peart",
                "themes": ["human", "lyrics", "shift"],
            },
        ],
    },
    "roll_the_bones": {
        "title": "Roll the Bones (1991)",
        "summary": (
            "A loose, groove-oriented record. The title track includes Geddy Lee's "
            "unexpected rap section, a first for the band. Bravado and Dreamline "
            "became live favorites. Production by Paul Northfield and the band."
        ),
        "quotes": [
            {
                "text": "Roll the bones, fate is still the common dominator.",
                "speaker": "Neil Peart",
                "themes": ["chance", "fate", "risk"],
            },
            {
                "text": "Some men live by the luck of the draw, and some men live for the thrill.",
                "speaker": "Neil Peart",
                "themes": ["gambling", "risk", "life"],
            },
            {
                "text": "The rap in Roll the Bones was meant to be funny, not a career pivot.",
                "speaker": "Geddy Lee",
                "themes": ["rap", "humor", "experiment"],
            },
            {
                "text": "Roll the Bones is looser and lighter than anything Rush had done in years.",
                "speaker": "AllMusic",
                "themes": ["loose", "light", "groove"],
            },
        ],
    },
    "counterparts": {
        "title": "Counterparts (1993)",
        "summary": (
            "A return to heavy guitar rock. Produced by Peter Collins. Leave That "
            "Thing Alone and Animate feature some of Lifeson's sharpest riffs of "
            "the decade. The album hit number two in the US, their highest chart "
            "position to that point."
        ),
        "quotes": [
            {
                "text": "We wanted to make a hard rock record again, no apologies.",
                "speaker": "Alex Lifeson",
                "themes": ["heavy", "guitar", "return"],
            },
            {
                "text": "Counterparts is Rush's heaviest album since Moving Pictures.",
                "speaker": "Rolling Stone",
                "themes": ["heavy", "comparison", "guitar"],
            },
            {
                "text": "Animate is about the anima, the Jungian idea of the feminine within.",
                "speaker": "Neil Peart",
                "themes": ["jung", "anima", "psychology"],
            },
            {
                "text": "The record hit number two in the US, our highest chart position yet.",
                "speaker": "Rush",
                "themes": ["chart", "success", "us"],
            },
        ],
    },
    "test_for_echo": {
        "title": "Test for Echo (1996)",
        "summary": (
            "Recorded in the Tennessee woods with engineer Peter Collins. Peart "
            "worked with Freddie Gruber and rebuilt his drumming approach, "
            "introducing a looser, circular technique. The title track and "
            "Driven anchor a denser, more deliberate record."
        ),
        "quotes": [
            {
                "text": "I went back to school on the drums. Freddie Gruber changed how I thought about the instrument.",
                "speaker": "Neil Peart",
                "themes": ["drumming", "gruber", "rebuild"],
            },
            {
                "text": "Test for Echo is dense and deliberate, sometimes to a fault.",
                "speaker": "AllMusic",
                "themes": ["dense", "deliberate", "mixed"],
            },
            {
                "text": "Driven came out of that new drumming approach, that circular motion.",
                "speaker": "Neil Peart",
                "themes": ["drumming", "technique", "song"],
            },
            {
                "text": "We were isolated in Tennessee and it gave the record a particular feel.",
                "speaker": "Alex Lifeson",
                "themes": ["recording", "isolation", "tennessee"],
            },
        ],
    },
    "vapor_trails": {
        "title": "Vapor Trails (2002)",
        "summary": (
            "The comeback after a five-year hiatus. Neil Peart lost his daughter "
            "and wife in the span of ten months and rode across North America to "
            "grieve. The record is raw, dense, and guitar-only, with no solos. "
            "A controversial mix was remixed and reissued in 2013."
        ),
        "quotes": [
            {
                "text": "I was done. I thought I'd never play again.",
                "speaker": "Neil Peart",
                "themes": ["grief", "hiatus", "return"],
            },
            {
                "text": "Ghost Rider is about the motorcycle journey I took to find a reason to live.",
                "speaker": "Neil Peart",
                "themes": ["grief", "motorcycle", "journey"],
            },
            {
                "text": "Vapor Trails is dense and raw, a record made by men grateful to be making music at all.",
                "speaker": "AllMusic",
                "themes": ["raw", "comeback", "grief"],
            },
            {
                "text": "We deliberately left out solos. It didn't feel right for these songs.",
                "speaker": "Alex Lifeson",
                "themes": ["no_solos", "restraint", "choice"],
            },
            {
                "text": "The original mix was cluttered. The 2013 remix let the songs breathe.",
                "speaker": "Geddy Lee",
                "themes": ["mix", "remix", "production"],
            },
        ],
    },
    "feedback": {
        "title": "Feedback (2004)",
        "summary": (
            "An eight-track covers EP celebrating the bands that inspired Rush: "
            "Cream, The Who, Blue Cheer, Buffalo Springfield, and others. "
            "Recorded quickly as a warmup for the R30 tour. A love letter to "
            "the late-1960s rock they grew up on."
        ),
        "quotes": [
            {
                "text": "We wanted to go back to the songs that made us want to play in the first place.",
                "speaker": "Alex Lifeson",
                "themes": ["covers", "roots", "tribute"],
            },
            {
                "text": "Feedback is a loose, affectionate EP with no pretense of originality.",
                "speaker": "AllMusic",
                "themes": ["covers", "loose", "tribute"],
            },
            {
                "text": "Crossroads and Summertime Blues were the songs we played in basements as kids.",
                "speaker": "Geddy Lee",
                "themes": ["roots", "basement", "youth"],
            },
        ],
    },
    "snakes_arrows": {
        "title": "Snakes & Arrows (2007)",
        "summary": (
            "Produced by Nick Raskulinecz. A heavier, guitar-driven record with "
            "Peart's lyrics engaging faith, doubt, and religious conflict. Far "
            "Cry and Armor and Sword anchor the album. Malignant Narcissism is "
            "an instrumental nominated for a Grammy."
        ),
        "quotes": [
            {
                "text": "Snakes & Arrows is a brooding, guitar-heavy record about faith and its absence.",
                "speaker": "Rolling Stone",
                "themes": ["faith", "guitar", "brooding"],
            },
            {
                "text": "The lyrics deal with religion, how it's used and misused.",
                "speaker": "Neil Peart",
                "themes": ["religion", "doubt", "conflict"],
            },
            {
                "text": "Far Cry became one of the strongest late-period Rush songs.",
                "speaker": "AllMusic",
                "themes": ["far_cry", "late_period", "strength"],
            },
            {
                "text": "Nick pushed us hard, harder than anyone in years. It was good for us.",
                "speaker": "Alex Lifeson",
                "themes": ["producer", "push", "energy"],
            },
        ],
    },
    "clockwork_angels": {
        "title": "Clockwork Angels (2012)",
        "summary": (
            "The final Rush studio album, a steampunk concept record with a "
            "novelization by Kevin J. Anderson and Peart. The story follows a "
            "young man across a world ruled by the Watchmaker. Produced again "
            "by Nick Raskulinecz. Caravan and The Wreckers were previewed two "
            "years before the full release."
        ),
        "quotes": [
            {
                "text": "All is for the best, in this best of all possible worlds.",
                "speaker": "Neil Peart",
                "themes": ["voltaire", "optimism", "candide"],
            },
            {
                "text": "I can't stop thinking big.",
                "speaker": "Neil Peart",
                "themes": ["ambition", "dreaming", "individualism"],
            },
            {
                "text": "Clockwork Angels is a fitting capstone, a concept record that sums up everything Rush did well.",
                "speaker": "AllMusic",
                "themes": ["capstone", "concept", "summary"],
            },
            {
                "text": "The steampunk world gave me a frame to write about freedom and order.",
                "speaker": "Neil Peart",
                "themes": ["steampunk", "freedom", "order"],
            },
            {
                "text": "We knew it might be the last one. We put everything into it.",
                "speaker": "Geddy Lee",
                "themes": ["finale", "effort", "closure"],
            },
        ],
    },
}