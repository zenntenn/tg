import random

from characters.models.core.ability import Ability
from characters.models.core.archetype import Archetype
from characters.models.core.attribute import Attribute
from characters.models.core.meritflaw import MeritFlaw
from characters.models.core.specialty import Specialty
from characters.models.mage.effect import Effect
from characters.models.mage.faction import MageFaction
from characters.models.mage.focus import Instrument, Paradigm, Practice
from characters.models.mage.resonance import Resonance
from characters.models.mage.sphere import Sphere
from core.models import Language, Noun
from game.models import ObjectType
from items.models.core.material import Material
from items.models.core.medium import Medium


def human_setup():
    human = ObjectType.objects.get_or_create(name="human", type="char", gameline="wod")[
        0
    ]

    Attribute.objects.get_or_create(name="Strength", property_name="strength")[0]
    Attribute.objects.get_or_create(name="Dexterity", property_name="dexterity")[0]
    Attribute.objects.get_or_create(name="Stamina", property_name="stamina")[0]
    Attribute.objects.get_or_create(name="Perception", property_name="perception")[0]
    Attribute.objects.get_or_create(name="Intelligence", property_name="intelligence")[
        0
    ]
    Attribute.objects.get_or_create(name="Wits", property_name="wits")[0]
    Attribute.objects.get_or_create(name="Charisma", property_name="charisma")[0]
    Attribute.objects.get_or_create(name="Manipulation", property_name="manipulation")[
        0
    ]
    Attribute.objects.get_or_create(name="Appearance", property_name="appearance")[0]


def vampire_setup():
    human_setup()


def werewolf_setup():
    human_setup()


def mage_setup():
    human_setup()
    human = ObjectType.objects.get_or_create(name="human", type="char", gameline="wod")[
        0
    ]

    mtahuman = ObjectType.objects.get_or_create(
        name="mtahuman", type="char", gameline="mta"
    )[0]
    mage = ObjectType.objects.get_or_create(name="mage", type="char", gameline="mta")[0]
    node = ObjectType.objects.get_or_create(name="node", type="loc", gameline="mta")[0]
    awareness = Ability.objects.get_or_create(
        name="Awareness", property_name="awareness"
    )[0]
    art = Ability.objects.get_or_create(name="Art", property_name="art")[0]
    leadership = Ability.objects.get_or_create(
        name="Leadership", property_name="leadership"
    )[0]
    animal_kinship = Ability.objects.get_or_create(
        name="Animal Kinship", property_name="animal_kinship"
    )[0]
    blatancy = Ability.objects.get_or_create(name="Blatancy", property_name="blatancy")[
        0
    ]
    carousing = Ability.objects.get_or_create(
        name="Carousing", property_name="carousing"
    )[0]
    do = Ability.objects.get_or_create(name="Do", property_name="do")[0]
    flying = Ability.objects.get_or_create(name="Flying", property_name="flying")[0]
    high_ritual = Ability.objects.get_or_create(
        name="High Ritual", property_name="high_ritual"
    )[0]
    lucid_dreaming = Ability.objects.get_or_create(
        name="Lucid Dreaming", property_name="lucid_dreaming"
    )[0]
    search = Ability.objects.get_or_create(name="Search", property_name="search")[0]
    seduction = Ability.objects.get_or_create(
        name="Seduction", property_name="seduction"
    )[0]
    martial_arts = Ability.objects.get_or_create(
        name="Martial Arts", property_name="martial_arts"
    )[0]
    meditation = Ability.objects.get_or_create(
        name="Meditation", property_name="meditation"
    )[0]
    research = Ability.objects.get_or_create(name="Research", property_name="research")[
        0
    ]
    survival = Ability.objects.get_or_create(name="Survival", property_name="survival")[
        0
    ]
    technology = Ability.objects.get_or_create(
        name="Technology", property_name="technology"
    )[0]
    acrobatics = Ability.objects.get_or_create(
        name="Acrobatics", property_name="acrobatics"
    )[0]
    archery = Ability.objects.get_or_create(name="Archery", property_name="archery")[0]
    biotech = Ability.objects.get_or_create(name="Biotech", property_name="biotech")[0]
    energy_weapons = Ability.objects.get_or_create(
        name="Energy Weapons", property_name="energy_weapons"
    )[0]
    hypertech = Ability.objects.get_or_create(
        name="Hypertech", property_name="hypertech"
    )[0]
    jetpack = Ability.objects.get_or_create(name="Jetpack", property_name="jetpack")[0]
    riding = Ability.objects.get_or_create(name="Riding", property_name="riding")[0]
    torture = Ability.objects.get_or_create(name="Torture", property_name="torture")[0]
    cosmology = Ability.objects.get_or_create(
        name="Cosmology", property_name="cosmology"
    )[0]
    enigmas = Ability.objects.get_or_create(name="Enigmas", property_name="enigmas")[0]
    esoterica = Ability.objects.get_or_create(
        name="Esoterica", property_name="esoterica"
    )[0]
    law = Ability.objects.get_or_create(name="Law", property_name="law")[0]
    occult = Ability.objects.get_or_create(name="Occult", property_name="occult")[0]
    politics = Ability.objects.get_or_create(name="Politics", property_name="politics")[
        0
    ]
    area_knowledge = Ability.objects.get_or_create(
        name="Area Knowledge", property_name="area_knowledge"
    )[0]
    belief_systems = Ability.objects.get_or_create(
        name="Belief Systems", property_name="belief_systems"
    )[0]
    cryptography = Ability.objects.get_or_create(
        name="Cryptography", property_name="cryptography"
    )[0]
    demolitions = Ability.objects.get_or_create(
        name="Demolitions", property_name="demolitions"
    )[0]
    finance = Ability.objects.get_or_create(name="Finance", property_name="finance")[0]
    lore = Ability.objects.get_or_create(name="Lore", property_name="lore")[0]
    media = Ability.objects.get_or_create(name="Media", property_name="media")[0]
    pharmacopeia = Ability.objects.get_or_create(
        name="Pharmacopeia", property_name="pharmacopeia"
    )[0]
    alertness = Ability.objects.get_or_create(
        name="Alertness", property_name="alertness"
    )[0]
    athletics = Ability.objects.get_or_create(
        name="Athletics", property_name="athletics"
    )[0]
    brawl = Ability.objects.get_or_create(name="Brawl", property_name="brawl")[0]
    empathy = Ability.objects.get_or_create(name="Empathy", property_name="empathy")[0]
    expression = Ability.objects.get_or_create(
        name="Expression", property_name="expression"
    )[0]
    intimidation = Ability.objects.get_or_create(
        name="Intimidation", property_name="intimidation"
    )[0]
    streetwise = Ability.objects.get_or_create(
        name="Streetwise", property_name="streetwise"
    )[0]
    subterfuge = Ability.objects.get_or_create(
        name="Subterfuge", property_name="subterfuge"
    )[0]
    crafts = Ability.objects.get_or_create(name="Crafts", property_name="crafts")[0]
    drive = Ability.objects.get_or_create(name="Drive", property_name="drive")[0]
    etiquette = Ability.objects.get_or_create(
        name="Etiquette", property_name="etiquette"
    )[0]
    firearms = Ability.objects.get_or_create(name="Firearms", property_name="firearms")[
        0
    ]
    melee = Ability.objects.get_or_create(name="Melee", property_name="melee")[0]
    stealth = Ability.objects.get_or_create(name="Stealth", property_name="stealth")[0]
    academics = Ability.objects.get_or_create(
        name="Academics", property_name="academics"
    )[0]
    computer = Ability.objects.get_or_create(name="Computer", property_name="computer")[
        0
    ]
    investigation = Ability.objects.get_or_create(
        name="Investigation", property_name="investigation"
    )[0]
    medicine = Ability.objects.get_or_create(name="Medicine", property_name="medicine")[
        0
    ]
    science = Ability.objects.get_or_create(name="Science", property_name="science")[0]
    cooking = Ability.objects.get_or_create(name="Cooking", property_name="cooking")[0]
    diplomacy = Ability.objects.get_or_create(
        name="Diplomacy", property_name="diplomacy"
    )[0]
    instruction = Ability.objects.get_or_create(
        name="Instruction", property_name="instruction"
    )[0]
    intrigue = Ability.objects.get_or_create(name="Intrigue", property_name="intrigue")[
        0
    ]
    intuition = Ability.objects.get_or_create(
        name="Intuition", property_name="intuition"
    )[0]
    mimicry = Ability.objects.get_or_create(name="Mimicry", property_name="mimicry")[0]
    negotiation = Ability.objects.get_or_create(
        name="Negotiation", property_name="negotiation"
    )[0]
    newspeak = Ability.objects.get_or_create(name="Newspeak", property_name="newspeak")[
        0
    ]
    scan = Ability.objects.get_or_create(name="Scan", property_name="scan")[0]
    scrounging = Ability.objects.get_or_create(
        name="Scrounging", property_name="scrounging"
    )[0]
    style = Ability.objects.get_or_create(name="Style", property_name="style")[0]
    blind_fighting = Ability.objects.get_or_create(
        name="Blind Fighting", property_name="blind_fighting"
    )[0]
    climbing = Ability.objects.get_or_create(name="Climbing", property_name="climbing")[
        0
    ]
    disguise = Ability.objects.get_or_create(name="Disguise", property_name="disguise")[
        0
    ]
    elusion = Ability.objects.get_or_create(name="Elusion", property_name="elusion")[0]
    escapology = Ability.objects.get_or_create(
        name="Escapology", property_name="escapology"
    )[0]
    fast_draw = Ability.objects.get_or_create(
        name="Fast Draw", property_name="fast_draw"
    )[0]
    fast_talk = Ability.objects.get_or_create(
        name="Fast Talk", property_name="fast_talk"
    )[0]
    fencing = Ability.objects.get_or_create(name="Fencing", property_name="fencing")[0]
    fortune_telling = Ability.objects.get_or_create(
        name="Fortune Telling", property_name="fortune_telling"
    )[0]
    gambling = Ability.objects.get_or_create(name="Gambling", property_name="gambling")[
        0
    ]
    gunsmith = Ability.objects.get_or_create(name="Gunsmith", property_name="gunsmith")[
        0
    ]
    heavy_weapons = Ability.objects.get_or_create(
        name="Heavy Weapons", property_name="heavy_weapons"
    )[0]
    hunting = Ability.objects.get_or_create(name="Hunting", property_name="hunting")[0]
    hypnotism = Ability.objects.get_or_create(
        name="Hypnotism", property_name="hypnotism"
    )[0]
    jury_rigging = Ability.objects.get_or_create(
        name="Jury Rigging", property_name="jury_rigging"
    )[0]
    microgravity_operations = Ability.objects.get_or_create(
        name="Microgravity Operations", property_name="microgravity_operations"
    )[0]
    misdirection = Ability.objects.get_or_create(
        name="Misdirection", property_name="misdirection"
    )[0]
    networking = Ability.objects.get_or_create(
        name="Networking", property_name="networking"
    )[0]
    pilot = Ability.objects.get_or_create(name="Pilot", property_name="pilot")[0]
    psychology = Ability.objects.get_or_create(
        name="Psychology", property_name="psychology"
    )[0]
    security = Ability.objects.get_or_create(name="Security", property_name="security")[
        0
    ]
    speed_reading = Ability.objects.get_or_create(
        name="Speed Reading", property_name="speed_reading"
    )[0]
    swimming = Ability.objects.get_or_create(name="Swimming", property_name="swimming")[
        0
    ]
    conspiracy_theory = Ability.objects.get_or_create(
        name="Conspiracy Theory", property_name="conspiracy_theory"
    )[0]
    chantry_politics = Ability.objects.get_or_create(
        name="Chantry Politics", property_name="chantry_politics"
    )[0]
    covert_culture = Ability.objects.get_or_create(
        name="Covert Culture", property_name="covert_culture"
    )[0]
    cultural_savvy = Ability.objects.get_or_create(
        name="Cultural Savvy", property_name="cultural_savvy"
    )[0]
    helmsman = Ability.objects.get_or_create(name="Helmsman", property_name="helmsman")[
        0
    ]
    history_knowledge = Ability.objects.get_or_create(
        name="History Knowledge", property_name="history_knowledge"
    )[0]
    power_brokering = Ability.objects.get_or_create(
        name="Power Brokering", property_name="power_brokering"
    )[0]
    propaganda = Ability.objects.get_or_create(
        name="Propaganda", property_name="propaganda"
    )[0]
    theology = Ability.objects.get_or_create(name="Theology", property_name="theology")[
        0
    ]
    unconventional_warface = Ability.objects.get_or_create(
        name="Unconventional Warface", property_name="unconventional_warface"
    )[0]
    vice = Ability.objects.get_or_create(name="Vice", property_name="vice")[0]

    correspondence = Sphere.objects.get_or_create(
        name="Correspondence", property_name="correspondence"
    )[0]
    spirit = Sphere.objects.get_or_create(name="Spirit", property_name="spirit")[0]
    time = Sphere.objects.get_or_create(name="Time", property_name="time")[0]
    forces = Sphere.objects.get_or_create(name="Forces", property_name="forces")[0]
    matter = Sphere.objects.get_or_create(name="Matter", property_name="matter")[0]
    life = Sphere.objects.get_or_create(name="Life", property_name="life")[0]
    entropy = Sphere.objects.get_or_create(name="Entropy", property_name="entropy")[0]
    prime = Sphere.objects.get_or_create(name="Prime", property_name="prime")[0]
    mind = Sphere.objects.get_or_create(name="Mind", property_name="mind")[0]

    abilities = list(Ability.objects.all())

    for i in range(40):
        Instrument.objects.create(name=f"Test Instrument {i}")
    for i in range(20):
        p = Practice.objects.create(name=f"Test Practice {i}")
        p.add_abilities(abilities[i : i + 7])
        p.instruments.add(Instrument.objects.get(name=f"Test Instrument {i}"))
        p.instruments.add(Instrument.objects.get(name=f"Test Instrument {20+i}"))
        p.save()

    for i in range(3):
        paradigm = Paradigm.objects.create(name=f"Paradigm {i}")

    for i in range(1, 6):
        mf = MeritFlaw.objects.create(name=f"Merit {i}")
        mf.add_rating(i)
        mf.allowed_types.add(human)
        mf.allowed_types.add(mtahuman)
        mf.allowed_types.add(mage)
        mf = MeritFlaw.objects.create(name=f"Flaw {i}")
        mf.add_rating(-i)
        mf.allowed_types.add(human)
        mf.allowed_types.add(mtahuman)
        mf.allowed_types.add(mage)
        mf = MeritFlaw.objects.create(name=f"Merit2 {i}")
        mf.add_rating(i)
        mf.allowed_types.add(human)
        mf.allowed_types.add(mtahuman)
        mf.allowed_types.add(mage)
        mf = MeritFlaw.objects.create(name=f"Flaw2 {i}")
        mf.add_rating(-i)
        mf.allowed_types.add(human)
        mf.allowed_types.add(mtahuman)
        mf.allowed_types.add(mage)
        mf = MeritFlaw.objects.create(name=f"Merit3 {i}")
        mf.add_rating(i)
        mf.allowed_types.add(human)
        mf.allowed_types.add(mtahuman)
        mf.allowed_types.add(mage)
        mf = MeritFlaw.objects.create(name=f"Flaw3 {i}")
        mf.add_rating(-i)
        mf.allowed_types.add(human)
        mf.allowed_types.add(mtahuman)
        mf.allowed_types.add(mage)
        mf = MeritFlaw.objects.create(name=f"Node Merit {i}")
        mf.add_rating(i)
        mf.allowed_types.add(node)
        mf = MeritFlaw.objects.create(name=f"Node Flaw {i}")
        mf.add_rating(-i)
        mf.allowed_types.add(node)

    for i in range(1, 11):
        Resonance.objects.create(name=f"Resonance {i}")

    for i in range(10):
        Noun.objects.create(name=f"Node Noun {i}")

    for i in range(1, 6):
        Effect.objects.create(name=f"Correspondence {i}", correspondence=i)
        Effect.objects.create(name=f"Time {i}", time=i)
        Effect.objects.create(name=f"Spirit {i}", spirit=i)
        Effect.objects.create(name=f"Forces {i}", forces=i)
        Effect.objects.create(name=f"Matter {i}", matter=i)
        Effect.objects.create(name=f"Life {i}", life=i)
        Effect.objects.create(name=f"Entropy {i}", entropy=i)
        Effect.objects.create(name=f"Prime {i}", prime=i)
        Effect.objects.create(name=f"Mind {i}", mind=i)

    spheres = list(Sphere.objects.all())
    for sphere_1 in spheres:
        for sphere_2 in spheres:
            if sphere_1 != sphere_2:
                for i in range(6):
                    for j in range(6):
                        d = {sphere_1.property_name: i, sphere_2.property_name: j}
                        Effect.objects.create(
                            name=f"{sphere_1.name}/{sphere_2.name} Test Effect {5*i+j}",
                            **d,
                        )
        for i in range(5):
            Resonance.objects.get_or_create(
                name=f"{sphere_1.name} Resonance {i}",
                **{sphere_1.property_name: True},
            )
    for i in range(10):
        Resonance.objects.create(name=f"Resonance {i}")

    for i in range(10):
        Material.objects.create(name=f"Test Material {i}")
        Material.objects.create(name=f"Test Soft Material {i}", is_hard=False)
        Language.objects.create(name=f"Test Language {i}", frequency=i)

    for i in range(10):
        for trait in Attribute.objects.all():
            Specialty.objects.create(name=f"{trait.name} {i}", stat=trait.property_name)
        for trait in Ability.objects.all():
            Specialty.objects.create(name=f"{trait.name} {i}", stat=trait.property_name)
        for trait in Sphere.objects.all():
            Specialty.objects.create(name=f"{trait.name} {i}", stat=trait.property_name)
    for i in range(20):
        Archetype.objects.create(name=f"Archetype {i}")

    trad = MageFaction.objects.create(name="Traditions")
    MageFaction.objects.create(name="Akashayana", parent=trad)

    for i in range(5):
        m = MageFaction.objects.create(
            name=f"Test Faction {i}",
        )
        for sphere in spheres[i : i + 4]:
            m.affinities.add(sphere)
        for j in range(i, i + 3):
            m.practices.add(Practice.objects.get(name=f"Test Practice {j}"))
        for j in range(3):
            m1 = MageFaction.objects.create(
                name=f"Test SubFaction {i}, {j}",
                parent=m,
            )
            for sphere in spheres[i : i + 4]:
                m.affinities.add(sphere)
            m1.languages.add(Language.objects.get(name=f"Test Language {i}"))
            m1.languages.add(Language.objects.get(name=f"Test Language {5+i}"))
            m1.save()
        m.languages.add(Language.objects.get(name=f"Test Language {i}"))
        m.languages.add(Language.objects.get(name=f"Test Language {5+i}"))
        m.save()
        for modifier_type in ["+", "-", "*", "/"]:
            for modifier in [1, 20]:
                med = Medium.objects.create(
                    name=f"Test {modifier_type} Medium {i, modifier}",
                    length_modifier_type=modifier_type,
                    length_modifier=modifier,
                )
                m.media.add(med)
                m.save()

    for faction in MageFaction.objects.exclude(parent=None):
        faction.paradigms.set(Paradigm.objects.all())
        faction.practices.set(Practice.objects.all())
        faction.save()
        MageFaction.objects.create(name=f"sub-{faction.name}", parent=faction)


def wraith_setup():
    human_setup()


def changeling_setup():
    human_setup()