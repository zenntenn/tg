from core.models import HouseRule

HouseRule.objects.get_or_create(
    name="Weekly XP",
    description="""Weekly XP is awarded as follows: 1 XP for finishing a scene (scenes are only considered complete if marked as such.), 1 XP if your character learned something significant, 1 XP for quality Role-Playing (nomination only), 1 XP for portraying Focus, and 1 XP for standing out in a scene involving NPCs (May be awarded multiple times per week)""",
    chronicle=None,
    gameline="wod",
)[0]
HouseRule.objects.get_or_create(
    name="Story XP",
    description="""At the end of a Story, XP is Awarded at ST discretion, but will take into account success, danger, character growth/wisdom, and interesting drama, as well as how long the story has gone.""",
    chronicle=None,
    gameline="wod",
)[0]
HouseRule.objects.get_or_create(
    name="Additional XP",
    description="""In addition to Story and Weekly XP, players who assist the Storyteller, such as by writing summaries of scenes, may receive additional XP for this work, to be given to a character of their choice.""",
    chronicle=None,
    gameline="wod",
)[0]
HouseRule.objects.get_or_create(
    name="Freebies",
    description="""Characters start with 15 Freebie points, however, it is possible to start with as many as 45. You may receieve 15 additional Freebies for a backstory that includes plot hooks for the ST, at the ST's discretion. Additionally, 15 freebies will be awarded to each character in a Coterie, Pack, Cabal, Motley, or Circle at creation consisting of at least 3 PCs submitted together. Characters who receive both bonuses may be eligible for character creation restrictions being loosened, again, at ST discretion.""",
    chronicle=None,
    gameline="wod",
)[0]
HouseRule.objects.get_or_create(
    name="Well-Skilled Craftsman",
    description="""Some abilties have traditionally had to be bought multiple times for each specialty. With this rule, instead you buy them with a single specialty at character creation (even if you only have a single dot) and may buy additional specialties for 4 XP each at rank 4.""",
    chronicle=None,
    gameline="wod",
)[0].add_source("Mage: the Ascension 20th Anniversary Edition", 279)

HouseRule.objects.get_or_create(
    name="Abilities",
    description="""Several abilities have been removed. Martial Arts has been merged into Brawl and Esoterica into Occult. Their slots have been filled by Larceny and Finance. Additionally, Hypertech is no longer a Skill.""",
    chronicle=None,
    gameline="mta",
)[0]
HouseRule.objects.get_or_create(
    name="Nodes",
    description="""Nodes are created as per the rules in Sources of Magick, which add Resonance, Merits and Flaws, and other relevant traits. If you want to create a Node and don't have access to Sources of Magick, contact your Storyteller.""",
    chronicle=None,
    gameline="mta",
)[0].add_source("Sources of Magick", 19)
HouseRule.objects.get_or_create(
    name="Focus",
    description="""Focus is reworked via Prism of Focus. It now consists of three Tenets describing statements the mage believes along with Practices that include ratings.  Effects must mention which Practice is being used and to use a Practice for an effect the Spheres involved must be less than or equal to the Practice rating. See Prism of Focus for more details.""",
    chronicle=None,
    gameline="mta",
)[0].add_source("Prism of Focus", 10)
HouseRule.objects.get_or_create(
    name="Resonance",
    description="""We use a simplified version of the Resonance rules from Fallen Tower. Resonance is a set of adjectives describing the characters magick rated from 1-5. Magick that aligns with the Resonance subtracts it from difficulty, that opposes it adds it to difficulty. Mages start with one dot in a Resonance trait. Characters with Awareness may roll Perception + Awareness at difficulty 9 - highest resonance trait to sense a character's resonance as a reflexive action. Additional rolls and successes may reveal additional traits, and the collection of traits and ratings of a character is often considered identifying. Resonance dots may be added or removed for 3 XP or Freebies.""",
    chronicle=None,
    gameline="mta",
)[0].add_source("Fallen Tower: Las Vegas", 122)
HouseRule.objects.get_or_create(
    name="Rotes",
    description="""Characters begin with 6 rote points, and rotes cost their total number of sphere dots in points to learn. Learning from a mentor or grimoire halves this. The primary benefit is that rotes roll Attribute + Ability based on Practice instead of Arete. Rote points may be purchased at 4 per Freebie or 3 per XP.""",
    chronicle=None,
    gameline="mta",
)[0].add_source("Prism of Focus", 32)
HouseRule.objects.get_or_create(
    name="Reality Zones",
    description="""Reality Zones are as in Prism of Focus: they have ratings in several Practices, ranging from -5 to 5. Positive ratings make Spheres lower than that using the Practice automatically coincidental. Negative ratings instead make high rankings of Spheres vulgar, ie, Hypertech -1 would cause Rank 5 Hypertech effects to be vulgar, -2 would include Rank 4, etc.""",
    chronicle=None,
    gameline="mta",
)[0].add_source("Prism of Focus", 31)
HouseRule.objects.get_or_create(
    name="Alternate Spheres",
    description="""At this time, Data and Dimensional Science will be handled as different difficulty/target number charts for Correspondence and Spirit. Primal Utility is sufficiently different to be taken as a wholly distinct Sphere. In the future, this may change, in which case characters will be allowed to respec in small ways to accomodate a rules change.""",
    chronicle=None,
    gameline="mta",
)[0]
HouseRule.objects.get_or_create(
    name="Divided Success Rule",
    description="""This game uses the divided success rule.""",
    chronicle=None,
    gameline="mta",
)[0]
HouseRule.objects.get_or_create(
    name="Vulgarity and Permissiveness",
    description="""When in doubt, assume that magick the mage is certain was their action is vulgar. Also assume that things are possible, though anything unusual requires the presence of a Storyteller to adjudicate.""",
    chronicle=None,
    gameline="mta",
)[0]
