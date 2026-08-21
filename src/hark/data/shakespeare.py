"""Shakespeare collection for the saddle MCP server.

Public-domain text from MIT Shakespeare and Project Gutenberg.
Spelling checked against common editions.
"""

QUOTES: dict = {
    "macbeth": {
        "title": "Macbeth",
        "summary": (
            "A Scottish general named Macbeth receives a prophecy from three witches "
            "that he will become king. Driven by ambition and pushed by his wife, he "
            "murders King Duncan and takes the throne. Paranoia and further killings "
            "follow. Lady Macbeth's guilt drives her to madness and suicide. Macduff "
            "leads a revolt, killing Macbeth in combat. Malcolm becomes king."
        ),
        "quotes": [
            {
                "text": "The devil damn thee black, thou cream-faced loon! Where got'st thou that goose look?",
                "speaker": "Macbeth",
                "act": 2,
                "scene": 3,
                "themes": ["insult", "fear", "appearance"],
            },
            {
                "text": "What, you egg!",
                "speaker": "Macduff",
                "act": 4,
                "scene": 2,
                "themes": ["insult", "violence"],
            },
            {
                "text": "Take thy face hence.",
                "speaker": "Macbeth",
                "act": 5,
                "scene": 3,
                "themes": ["insult", "dismissal", "anger"],
            },
            {
                "text": "Thou lily-liver'd boy.",
                "speaker": "Macbeth",
                "act": 5,
                "scene": 3,
                "themes": ["insult", "cowardice"],
            },
            {
                "text": "Out, damned spot! out, I say!",
                "speaker": "Lady Macbeth",
                "act": 5,
                "scene": 1,
                "themes": ["guilt", "madness", "blood"],
            },
            {
                "text": "Is this a dagger which I see before me, the handle toward my hand?",
                "speaker": "Macbeth",
                "act": 2,
                "scene": 1,
                "themes": ["hallucination", "ambition", "violence"],
            },
            {
                "text": "Fair is foul, and foul is fair: Hover through the fog and filthy air.",
                "speaker": "Witches",
                "act": 1,
                "scene": 1,
                "themes": ["deception", "supernatural", "appearance"],
            },
            {
                "text": "Double, double toil and trouble; Fire burn, and caldron bubble.",
                "speaker": "Witches",
                "act": 4,
                "scene": 1,
                "themes": ["supernatural", "prophecy", "incantation"],
            },
            {
                "text": "Life's but a walking shadow, a poor player, That struts and frets his hour upon the stage, And then is heard no more.",
                "speaker": "Macbeth",
                "act": 5,
                "scene": 5,
                "themes": ["despair", "mortality", "meaning"],
            },
            {
                "text": "By the pricking of my thumbs, Something wicked this way comes.",
                "speaker": "Second Witch",
                "act": 4,
                "scene": 1,
                "themes": ["supernatural", "foreshadowing", "evil"],
            },
            {
                "text": "Stars, hide your fires; Let not light see my black and deep desires.",
                "speaker": "Macbeth",
                "act": 1,
                "scene": 4,
                "themes": ["ambition", "secrecy", "desire"],
            },
            {
                "text": "I have no spur To prick the sides of my intent, but only Vaulting ambition, which o'erleaps itself And falls on the other.",
                "speaker": "Macbeth",
                "act": 1,
                "scene": 7,
                "themes": ["ambition", "self-awareness", "hesitation"],
            },
            {
                "text": "Look like the innocent flower, but be the serpent under't.",
                "speaker": "Lady Macbeth",
                "act": 1,
                "scene": 5,
                "themes": ["deception", "appearance", "ambition"],
            },
            {
                "text": "Nothing in his life became him like the leaving it.",
                "speaker": "Malcolm",
                "act": 1,
                "scene": 4,
                "themes": ["death", "dignity", "honor"],
            },
            {
                "text": "All the perfumes of Arabia will not sweeten this little hand.",
                "speaker": "Lady Macbeth",
                "act": 5,
                "scene": 1,
                "themes": ["guilt", "desperation", "blood"],
            },
        ],
    },
    "hamlet": {
        "title": "Hamlet",
        "summary": (
            "Prince Hamlet of Denmark mourns his father's death and resents his mother's "
            "hasty marriage to his uncle Claudius, who has taken the throne. The ghost of "
            "Hamlet's father reveals he was murdered by Claudius. Hamlet feigns madness to "
            "investigate, stages a play to catch the king's conscience, and ultimately kills "
            "Claudius but dies from a poisoned blade in the process."
        ),
        "quotes": [
            {
                "text": "To be, or not to be, that is the question.",
                "speaker": "Hamlet",
                "act": 3,
                "scene": 1,
                "themes": ["mortality", "existential", "suicide"],
            },
            {
                "text": "Brevity is the soul of wit.",
                "speaker": "Polonius",
                "act": 2,
                "scene": 2,
                "themes": ["wit", "brevity", "irony"],
            },
            {
                "text": "Something is rotten in the state of Denmark.",
                "speaker": "Marcellus",
                "act": 1,
                "scene": 4,
                "themes": ["corruption", "foreshadowing", "decay"],
            },
            {
                "text": "The lady doth protest too much, methinks.",
                "speaker": "Gertrude",
                "act": 3,
                "scene": 2,
                "themes": ["deception", "guilt", "appearance"],
            },
            {
                "text": "Though this be madness, yet there is method in't.",
                "speaker": "Polonius",
                "act": 2,
                "scene": 2,
                "themes": ["madness", "strategy", "appearance"],
            },
            {
                "text": "There is nothing either good or bad, but thinking makes it so.",
                "speaker": "Hamlet",
                "act": 2,
                "scene": 2,
                "themes": ["perspective", "perception", "philosophy"],
            },
        ],
    },
    "othello": {
        "title": "Othello",
        "summary": (
            "Othello, a Moorish general in Venice, marries Desdemona. Iago, passed over "
            "for promotion, orchestrates a campaign of jealousy that convinces Othello "
            "his wife is unfaithful. Othello murders Desdemona, learns the truth, and "
            "kills himself. Iago is arrested but never explains his motives."
        ),
        "quotes": [
            {
                "text": "O, beware, my lord, of jealousy; It is the green-eyed monster which doth mock The meat it feeds on.",
                "speaker": "Iago",
                "act": 3,
                "scene": 3,
                "themes": ["jealousy", "manipulation", "warning"],
            },
            {
                "text": "I am not what I am.",
                "speaker": "Iago",
                "act": 1,
                "scene": 1,
                "themes": ["deception", "identity", "honesty"],
            },
        ],
    },
    "tempest": {
        "title": "The Tempest",
        "summary": (
            "Prospero, the rightful Duke of Milan, has been exiled to an island with his "
            "daughter Miranda. Using magic, he conjures a storm to shipwreck his usurping "
            "brother Antonio and the King of Naples. Plotting revenge, Prospero instead "
            "chooses forgiveness, frees the spirit Ariel, and returns to Milan."
        ),
        "quotes": [
            {
                "text": "We are such stuff as dreams are made on, and our little life is rounded with a sleep.",
                "speaker": "Prospero",
                "act": 4,
                "scene": 1,
                "themes": ["mortality", "dreams", "impermanence"],
            },
            {
                "text": "Hell is empty And all the devils are here.",
                "speaker": "Ariel",
                "act": 1,
                "scene": 2,
                "themes": ["chaos", "danger", "supernatural"],
            },
        ],
    },
    "lear": {
        "title": "King Lear",
        "summary": (
            "King Lear divides his kingdom among two daughters who flatter him and "
            "disinherits the one who loves him honestly. He descends into madness on the "
            "heath. A parallel plot involves Gloucester, who is blinded by his own "
            "misjudgment of his sons. Nearly everyone dies by the end."
        ),
        "quotes": [
            {
                "text": "Blow, winds, and crack your cheeks! rage! blow!",
                "speaker": "Lear",
                "act": 3,
                "scene": 2,
                "themes": ["fury", "nature", "madness"],
            },
            {
                "text": "I am a man more sinned against than sinning.",
                "speaker": "Lear",
                "act": 3,
                "scene": 2,
                "themes": ["victimhood", "injustice", "suffering"],
            },
        ],
    },
    "merchant": {
        "title": "The Merchant of Venice",
        "summary": (
            "Antonio borrows money from Shylock to help his friend Bassanio woo Portia. "
            "Shylock demands a pound of Antonio's flesh as collateral. When Antonio "
            "defaults, Portia, disguised as a lawyer, argues in court that Shylock may "
            "take flesh but must not shed blood. Shylock loses. The play mixes comedy "
            "with one of Shakespeare's most debated characters."
        ),
        "quotes": [
            {
                "text": "The quality of mercy is not strained. It droppeth as the gentle rain from heaven Upon the place beneath.",
                "speaker": "Portia",
                "act": 4,
                "scene": 1,
                "themes": ["mercy", "justice", "pleading"],
            },
            {
                "text": "All that glisters is not gold.",
                "speaker": "Prince of Morocco",
                "act": 2,
                "scene": 7,
                "themes": ["deception", "appearance", "value"],
            },
        ],
    },
}