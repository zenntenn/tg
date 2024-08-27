import random

from characters.models.core.ability import Ability
from characters.models.core.archetype import Archetype
from characters.models.core.human import Human
from characters.models.core.meritflaw import MeritFlaw
from characters.models.core.specialty import Specialty
from characters.models.mage.cabal import Cabal
from characters.models.mage.effect import Effect
from characters.models.mage.faction import MageFaction
from characters.models.mage.focus import Instrument, Paradigm, Practice
from characters.models.mage.mage import Mage
from characters.models.mage.resonance import Resonance
from characters.models.mage.sphere import Sphere
from core.models import Language, Noun
from django.contrib.auth.models import User
from django.test import TestCase
from game.models import ObjectType
from items.models.core.material import Material
from items.models.core.medium import Medium
from items.models.mage.grimoire import Grimoire
from locations.models.mage.chantry import Chantry
from locations.models.mage.library import Library
from locations.models.mage.node import Node


class TestChantry(TestCase):
    def setUp(self) -> None:
        self.chantry = Chantry.objects.create(name="")
        self.library = Library.objects.create(rank=3)
        self.grimoire1 = Grimoire.objects.create()
        self.grimoire2 = Grimoire.objects.create()
        self.grimoire3 = Grimoire.objects.create()
        self.library.add_book(self.grimoire1)
        self.library.add_book(self.grimoire2)
        self.library.add_book(self.grimoire3)
        self.node1 = Node.objects.create(name="node1", rank=1)
        self.node2 = Node.objects.create(name="node2", rank=1)
        self.human = Human.objects.create(name="human")
        self.cabal = Cabal.objects.create(name="cabal")
        self.faction = MageFaction.objects.create(name="faction")
        self.player = User.objects.create_user(username="Test")
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
        blatancy = Ability.objects.get_or_create(
            name="Blatancy", property_name="blatancy"
        )[0]
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
        research = Ability.objects.get_or_create(
            name="Research", property_name="research"
        )[0]
        survival = Ability.objects.get_or_create(
            name="Survival", property_name="survival"
        )[0]
        technology = Ability.objects.get_or_create(
            name="Technology", property_name="technology"
        )[0]
        acrobatics = Ability.objects.get_or_create(
            name="Acrobatics", property_name="acrobatics"
        )[0]
        archery = Ability.objects.get_or_create(
            name="Archery", property_name="archery"
        )[0]
        biotech = Ability.objects.get_or_create(
            name="Biotech", property_name="biotech"
        )[0]
        energy_weapons = Ability.objects.get_or_create(
            name="Energy Weapons", property_name="energy_weapons"
        )[0]
        hypertech = Ability.objects.get_or_create(
            name="Hypertech", property_name="hypertech"
        )[0]
        jetpack = Ability.objects.get_or_create(
            name="Jetpack", property_name="jetpack"
        )[0]
        riding = Ability.objects.get_or_create(name="Riding", property_name="riding")[0]
        torture = Ability.objects.get_or_create(
            name="Torture", property_name="torture"
        )[0]
        cosmology = Ability.objects.get_or_create(
            name="Cosmology", property_name="cosmology"
        )[0]
        enigmas = Ability.objects.get_or_create(
            name="Enigmas", property_name="enigmas"
        )[0]
        esoterica = Ability.objects.get_or_create(
            name="Esoterica", property_name="esoterica"
        )[0]
        law = Ability.objects.get_or_create(name="Law", property_name="law")[0]
        occult = Ability.objects.get_or_create(name="Occult", property_name="occult")[0]
        politics = Ability.objects.get_or_create(
            name="Politics", property_name="politics"
        )[0]
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
        finance = Ability.objects.get_or_create(
            name="Finance", property_name="finance"
        )[0]
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
        empathy = Ability.objects.get_or_create(
            name="Empathy", property_name="empathy"
        )[0]
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
        firearms = Ability.objects.get_or_create(
            name="Firearms", property_name="firearms"
        )[0]
        melee = Ability.objects.get_or_create(name="Melee", property_name="melee")[0]
        stealth = Ability.objects.get_or_create(
            name="Stealth", property_name="stealth"
        )[0]
        academics = Ability.objects.get_or_create(
            name="Academics", property_name="academics"
        )[0]
        computer = Ability.objects.get_or_create(
            name="Computer", property_name="computer"
        )[0]
        investigation = Ability.objects.get_or_create(
            name="Investigation", property_name="investigation"
        )[0]
        medicine = Ability.objects.get_or_create(
            name="Medicine", property_name="medicine"
        )[0]
        science = Ability.objects.get_or_create(
            name="Science", property_name="science"
        )[0]
        cooking = Ability.objects.get_or_create(
            name="Cooking", property_name="cooking"
        )[0]
        diplomacy = Ability.objects.get_or_create(
            name="Diplomacy", property_name="diplomacy"
        )[0]
        instruction = Ability.objects.get_or_create(
            name="Instruction", property_name="instruction"
        )[0]
        intrigue = Ability.objects.get_or_create(
            name="Intrigue", property_name="intrigue"
        )[0]
        intuition = Ability.objects.get_or_create(
            name="Intuition", property_name="intuition"
        )[0]
        mimicry = Ability.objects.get_or_create(
            name="Mimicry", property_name="mimicry"
        )[0]
        negotiation = Ability.objects.get_or_create(
            name="Negotiation", property_name="negotiation"
        )[0]
        newspeak = Ability.objects.get_or_create(
            name="Newspeak", property_name="newspeak"
        )[0]
        scan = Ability.objects.get_or_create(name="Scan", property_name="scan")[0]
        scrounging = Ability.objects.get_or_create(
            name="Scrounging", property_name="scrounging"
        )[0]
        style = Ability.objects.get_or_create(name="Style", property_name="style")[0]
        blind_fighting = Ability.objects.get_or_create(
            name="Blind Fighting", property_name="blind_fighting"
        )[0]
        climbing = Ability.objects.get_or_create(
            name="Climbing", property_name="climbing"
        )[0]
        disguise = Ability.objects.get_or_create(
            name="Disguise", property_name="disguise"
        )[0]
        elusion = Ability.objects.get_or_create(
            name="Elusion", property_name="elusion"
        )[0]
        escapology = Ability.objects.get_or_create(
            name="Escapology", property_name="escapology"
        )[0]
        fast_draw = Ability.objects.get_or_create(
            name="Fast Draw", property_name="fast_draw"
        )[0]
        fast_talk = Ability.objects.get_or_create(
            name="Fast Talk", property_name="fast_talk"
        )[0]
        fencing = Ability.objects.get_or_create(
            name="Fencing", property_name="fencing"
        )[0]
        fortune_telling = Ability.objects.get_or_create(
            name="Fortune Telling", property_name="fortune_telling"
        )[0]
        gambling = Ability.objects.get_or_create(
            name="Gambling", property_name="gambling"
        )[0]
        gunsmith = Ability.objects.get_or_create(
            name="Gunsmith", property_name="gunsmith"
        )[0]
        heavy_weapons = Ability.objects.get_or_create(
            name="Heavy Weapons", property_name="heavy_weapons"
        )[0]
        hunting = Ability.objects.get_or_create(
            name="Hunting", property_name="hunting"
        )[0]
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
        security = Ability.objects.get_or_create(
            name="Security", property_name="security"
        )[0]
        speed_reading = Ability.objects.get_or_create(
            name="Speed Reading", property_name="speed_reading"
        )[0]
        swimming = Ability.objects.get_or_create(
            name="Swimming", property_name="swimming"
        )[0]
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
        helmsman = Ability.objects.get_or_create(
            name="Helmsman", property_name="helmsman"
        )[0]
        history_knowledge = Ability.objects.get_or_create(
            name="History Knowledge", property_name="history_knowledge"
        )[0]
        power_brokering = Ability.objects.get_or_create(
            name="Power Brokering", property_name="power_brokering"
        )[0]
        propaganda = Ability.objects.get_or_create(
            name="Propaganda", property_name="propaganda"
        )[0]
        theology = Ability.objects.get_or_create(
            name="Theology", property_name="theology"
        )[0]
        unconventional_warface = Ability.objects.get_or_create(
            name="Unconventional Warface", property_name="unconventional_warface"
        )[0]
        vice = Ability.objects.get_or_create(name="Vice", property_name="vice")[0]

        human = ObjectType.objects.get_or_create(
            name="human", type="char", gameline="wod"
        )[0]
        mtahuman = ObjectType.objects.get_or_create(
            name="mtahuman", type="char", gameline="mta"
        )[0]
        mage = ObjectType.objects.get_or_create(
            name="mage", type="char", gameline="mta"
        )[0]
        node = ObjectType.objects.get_or_create(
            name="node", type="loc", gameline="mta"
        )[0]
        
        Sphere.objects.get_or_create(
            name="Correspondence", property_name="correspondence"
        )[0]
        Sphere.objects.get_or_create(name="Spirit", property_name="spirit")[0]
        Sphere.objects.get_or_create(name="Time", property_name="time")[0]
        Sphere.objects.get_or_create(name="Forces", property_name="forces")[0]
        Sphere.objects.get_or_create(name="Matter", property_name="matter")[0]
        Sphere.objects.get_or_create(name="Life", property_name="life")[0]
        Sphere.objects.get_or_create(name="Entropy", property_name="entropy")[0]
        Sphere.objects.get_or_create(name="Prime", property_name="prime")[0]
        Sphere.objects.get_or_create(name="Mind", property_name="mind")[0]

        self.character = Mage.objects.create(name="", owner=self.player)
        for i in range(10):
            Noun.objects.create(name=f"Mage Noun {i}")

        for i in range(5):
            m = Mage.objects.create(name=f"Character {i}", owner=self.player)

        for i in range(15):
            Instrument.objects.create(name=f"Instrument {i}")

        for i in range(5):
            practice = Practice.objects.create(name=f"Practice {i}")
            practice.add_abilities(
                list(random.sample(list(Ability.objects.all()), k=4))
            )
            practice.instruments.set(Instrument.objects.all())
            practice.save()

        for i in range(3):
            paradigm = Paradigm.objects.create(name=f"Paradigm {i}")

        trad = MageFaction.objects.create(name="Traditions")
        MageFaction.objects.create(name="Akashayana", parent=trad)

        for faction in MageFaction.objects.exclude(parent=None):
            faction.paradigms.set(Paradigm.objects.all())
            faction.practices.set(Practice.objects.all())
            faction.save()
            MageFaction.objects.create(name=f"sub-{faction.name}", parent=faction)

        for i in range(5):
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
            Mage.objects.create(name=f"Mage {i}")

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

        for i in range(10):
            Resonance.objects.create(name=f"Resonance {i}")

        for i in range(10):
            for trait in m.get_attributes():
                Specialty.objects.create(
                    name=f"{trait.replace('_', ' ').title()} {i}", stat=trait
                )

            for trait in m.get_abilities():
                Specialty.objects.create(
                    name=f"{trait.replace('_', ' ').title()} {i}", stat=trait
                )

            for trait in m.get_spheres():
                Specialty.objects.create(
                    name=f"{trait.replace('_', ' ').title()} {i}", stat=trait
                )

        for i in range(20):
            Archetype.objects.create(name=f"Archetype {i}")

        for i in range(1, 11):
            Language.objects.create(name=f"Language {i}", frequency=i)
        self.grimoire = Grimoire.objects.create(name="Random Grimoire")
        for i in range(10):
            Noun.objects.create(name=f"Grimoire Noun {i}")

        Ability.objects.get_or_create(name="Awareness", property_name="awareness")[0]
        Ability.objects.get_or_create(name="Art", property_name="art")[0]
        Ability.objects.get_or_create(name="Leadership", property_name="leadership")[0]
        Ability.objects.get_or_create(
            name="Animal Kinship", property_name="animal_kinship"
        )[0]
        Ability.objects.get_or_create(name="Blatancy", property_name="blatancy")[0]
        Ability.objects.get_or_create(name="Carousing", property_name="carousing")[0]
        Ability.objects.get_or_create(name="Do", property_name="do")[0]
        Ability.objects.get_or_create(name="Flying", property_name="flying")[0]
        Ability.objects.get_or_create(name="High Ritual", property_name="high_ritual")[
            0
        ]
        Ability.objects.get_or_create(
            name="Lucid Dreaming", property_name="lucid_dreaming"
        )[0]
        Ability.objects.get_or_create(name="Search", property_name="search")[0]
        Ability.objects.get_or_create(name="Seduction", property_name="seduction")[0]
        Ability.objects.get_or_create(
            name="Martial Arts", property_name="martial_arts"
        )[0]
        Ability.objects.get_or_create(name="Meditation", property_name="meditation")[0]
        Ability.objects.get_or_create(name="Research", property_name="research")[0]
        Ability.objects.get_or_create(name="Survival", property_name="survival")[0]
        Ability.objects.get_or_create(name="Technology", property_name="technology")[0]
        Ability.objects.get_or_create(name="Acrobatics", property_name="acrobatics")[0]
        Ability.objects.get_or_create(name="Archery", property_name="archery")[0]
        Ability.objects.get_or_create(name="Biotech", property_name="biotech")[0]
        Ability.objects.get_or_create(
            name="Energy Weapons", property_name="energy_weapons"
        )[0]
        Ability.objects.get_or_create(name="Hypertech", property_name="hypertech")[0]
        Ability.objects.get_or_create(name="Jetpack", property_name="jetpack")[0]
        Ability.objects.get_or_create(name="Riding", property_name="riding")[0]
        Ability.objects.get_or_create(name="Torture", property_name="torture")[0]
        Ability.objects.get_or_create(name="Cosmology", property_name="cosmology")[0]
        Ability.objects.get_or_create(name="Enigmas", property_name="enigmas")[0]
        Ability.objects.get_or_create(name="Esoterica", property_name="esoterica")[0]
        Ability.objects.get_or_create(name="Law", property_name="law")[0]
        Ability.objects.get_or_create(name="Occult", property_name="occult")[0]
        Ability.objects.get_or_create(name="Politics", property_name="politics")[0]
        Ability.objects.get_or_create(
            name="Area Knowledge", property_name="area_knowledge"
        )[0]
        Ability.objects.get_or_create(
            name="Belief Systems", property_name="belief_systems"
        )[0]
        Ability.objects.get_or_create(
            name="Cryptography", property_name="cryptography"
        )[0]
        Ability.objects.get_or_create(name="Demolitions", property_name="demolitions")[
            0
        ]
        Ability.objects.get_or_create(name="Finance", property_name="finance")[0]
        Ability.objects.get_or_create(name="Lore", property_name="lore")[0]
        Ability.objects.get_or_create(name="Media", property_name="media")[0]
        Ability.objects.get_or_create(
            name="Pharmacopeia", property_name="pharmacopeia"
        )[0]
        Ability.objects.get_or_create(name="Alertness", property_name="alertness")[0]
        Ability.objects.get_or_create(name="Athletics", property_name="athletics")[0]
        Ability.objects.get_or_create(name="Brawl", property_name="brawl")[0]
        Ability.objects.get_or_create(name="Empathy", property_name="empathy")[0]
        Ability.objects.get_or_create(name="Expression", property_name="expression")[0]
        Ability.objects.get_or_create(
            name="Intimidation", property_name="intimidation"
        )[0]
        Ability.objects.get_or_create(name="Streetwise", property_name="streetwise")[0]
        Ability.objects.get_or_create(name="Subterfuge", property_name="subterfuge")[0]
        Ability.objects.get_or_create(name="Crafts", property_name="crafts")[0]
        Ability.objects.get_or_create(name="Drive", property_name="drive")[0]
        Ability.objects.get_or_create(name="Etiquette", property_name="etiquette")[0]
        Ability.objects.get_or_create(name="Firearms", property_name="firearms")[0]
        Ability.objects.get_or_create(name="Melee", property_name="melee")[0]
        Ability.objects.get_or_create(name="Stealth", property_name="stealth")[0]
        Ability.objects.get_or_create(name="Academics", property_name="academics")[0]
        Ability.objects.get_or_create(name="Computer", property_name="computer")[0]
        Ability.objects.get_or_create(
            name="Investigation", property_name="investigation"
        )[0]
        Ability.objects.get_or_create(name="Medicine", property_name="medicine")[0]
        Ability.objects.get_or_create(name="Science", property_name="science")[0]
        Ability.objects.get_or_create(name="Cooking", property_name="cooking")[0]
        Ability.objects.get_or_create(name="Diplomacy", property_name="diplomacy")[0]
        Ability.objects.get_or_create(name="Instruction", property_name="instruction")[
            0
        ]
        Ability.objects.get_or_create(name="Intrigue", property_name="intrigue")[0]
        Ability.objects.get_or_create(name="Intuition", property_name="intuition")[0]
        Ability.objects.get_or_create(name="Mimicry", property_name="mimicry")[0]
        Ability.objects.get_or_create(name="Negotiation", property_name="negotiation")[
            0
        ]
        Ability.objects.get_or_create(name="Newspeak", property_name="newspeak")[0]
        Ability.objects.get_or_create(name="Scan", property_name="scan")[0]
        Ability.objects.get_or_create(name="Scrounging", property_name="scrounging")[0]
        Ability.objects.get_or_create(name="Style", property_name="style")[0]
        Ability.objects.get_or_create(
            name="Blind Fighting", property_name="blind_fighting"
        )[0]
        Ability.objects.get_or_create(name="Climbing", property_name="climbing")[0]
        Ability.objects.get_or_create(name="Disguise", property_name="disguise")[0]
        Ability.objects.get_or_create(name="Elusion", property_name="elusion")[0]
        Ability.objects.get_or_create(name="Escapology", property_name="escapology")[0]
        Ability.objects.get_or_create(name="Fast Draw", property_name="fast_draw")[0]
        Ability.objects.get_or_create(name="Fast Talk", property_name="fast_talk")[0]
        Ability.objects.get_or_create(name="Fencing", property_name="fencing")[0]
        Ability.objects.get_or_create(
            name="Fortune Telling", property_name="fortune_telling"
        )[0]
        Ability.objects.get_or_create(name="Gambling", property_name="gambling")[0]
        Ability.objects.get_or_create(name="Gunsmith", property_name="gunsmith")[0]
        Ability.objects.get_or_create(
            name="Heavy Weapons", property_name="heavy_weapons"
        )[0]
        Ability.objects.get_or_create(name="Hunting", property_name="hunting")[0]
        Ability.objects.get_or_create(name="Hypnotism", property_name="hypnotism")[0]
        Ability.objects.get_or_create(
            name="Jury Rigging", property_name="jury_rigging"
        )[0]
        Ability.objects.get_or_create(
            name="Microgravity Operations", property_name="microgravity_operations"
        )[0]
        Ability.objects.get_or_create(
            name="Misdirection", property_name="misdirection"
        )[0]
        Ability.objects.get_or_create(name="Networking", property_name="networking")[0]
        Ability.objects.get_or_create(name="Pilot", property_name="pilot")[0]
        Ability.objects.get_or_create(name="Psychology", property_name="psychology")[0]
        Ability.objects.get_or_create(name="Security", property_name="security")[0]
        Ability.objects.get_or_create(
            name="Speed Reading", property_name="speed_reading"
        )[0]
        Ability.objects.get_or_create(name="Swimming", property_name="swimming")[0]
        Ability.objects.get_or_create(
            name="Conspiracy Theory", property_name="conspiracy_theory"
        )[0]
        Ability.objects.get_or_create(
            name="Chantry Politics", property_name="chantry_politics"
        )[0]
        Ability.objects.get_or_create(
            name="Covert Culture", property_name="covert_culture"
        )[0]
        Ability.objects.get_or_create(
            name="Cultural Savvy", property_name="cultural_savvy"
        )[0]
        Ability.objects.get_or_create(name="Helmsman", property_name="helmsman")[0]
        Ability.objects.get_or_create(
            name="History Knowledge", property_name="history_knowledge"
        )[0]
        Ability.objects.get_or_create(
            name="Power Brokering", property_name="power_brokering"
        )[0]
        Ability.objects.get_or_create(name="Propaganda", property_name="propaganda")[0]
        Ability.objects.get_or_create(name="Theology", property_name="theology")[0]
        Ability.objects.get_or_create(
            name="Unconventional Warface", property_name="unconventional_warface"
        )[0]
        Ability.objects.get_or_create(name="Vice", property_name="vice")[0]

        Sphere.objects.get_or_create(
            name="Correspondence", property_name="correspondence"
        )[0]
        Sphere.objects.get_or_create(name="Spirit", property_name="spirit")[0]
        Sphere.objects.get_or_create(name="Time", property_name="time")[0]
        Sphere.objects.get_or_create(name="Forces", property_name="forces")[0]
        Sphere.objects.get_or_create(name="Matter", property_name="matter")[0]
        Sphere.objects.get_or_create(name="Life", property_name="life")[0]
        Sphere.objects.get_or_create(name="Entropy", property_name="entropy")[0]
        Sphere.objects.get_or_create(name="Prime", property_name="prime")[0]
        Sphere.objects.get_or_create(name="Mind", property_name="mind")[0]

        abilities = list(Ability.objects.all())
        spheres = list(Sphere.objects.all())
        for i in range(40):
            Instrument.objects.create(name=f"Test Instrument {i}")
        for i in range(20):
            p = Practice.objects.create(name=f"Test Practice {i}")
            p.add_abilities(abilities[i : i + 7])
            p.instruments.add(Instrument.objects.get(name=f"Test Instrument {i}"))
            p.instruments.add(Instrument.objects.get(name=f"Test Instrument {20+i}"))
            p.save()
        for i in range(10):
            Material.objects.create(name=f"Test Material {i}")
            Material.objects.create(name=f"Test Soft Material {i}", is_hard=False)
            Language.objects.create(name=f"Test Language {i}", frequency=i)
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

    def test_trait_cost(self):
        self.assertEqual(self.chantry.trait_cost("allies"), 2)
        self.assertEqual(self.chantry.trait_cost("arcane"), 2)
        self.assertEqual(self.chantry.trait_cost("backup"), 2)
        self.assertEqual(self.chantry.trait_cost("cult"), 2)
        self.assertEqual(self.chantry.trait_cost("elders"), 2)
        self.assertEqual(self.chantry.trait_cost("integrated_effects"), 2)
        self.assertEqual(self.chantry.trait_cost("library_rating"), 2)
        self.assertEqual(self.chantry.trait_cost("retainers"), 2)
        self.assertEqual(self.chantry.trait_cost("spies"), 2)
        self.assertEqual(self.chantry.trait_cost("node_rating"), 3)
        self.assertEqual(self.chantry.trait_cost("resources"), 3)
        self.assertEqual(self.chantry.trait_cost("enhancement"), 4)
        self.assertEqual(self.chantry.trait_cost("requisitions"), 4)
        self.assertEqual(self.chantry.trait_cost("reality_zone_rating"), 5)

    def test_has_node(self):
        self.chantry.node_rating = 1
        self.assertFalse(self.chantry.has_node())
        self.chantry.nodes.add(self.node1)
        self.assertTrue(self.chantry.has_node())

    def test_total_node(self):
        self.assertEqual(self.chantry.total_node(), 0)
        self.chantry.nodes.add(self.node1)
        self.assertEqual(self.chantry.total_node(), 1)
        self.chantry.nodes.add(self.node2)
        self.assertEqual(self.chantry.total_node(), 2)

    def test_create_nodes(self):
        self.chantry.random_faction()
        self.chantry.random_name()
        self.chantry.node_rating = 0
        self.chantry.create_nodes()
        self.assertEqual(self.chantry.nodes.count(), 0)
        self.assertEqual(self.chantry.total_node(), 0)
        self.chantry.node_rating = 12
        self.chantry.create_nodes()
        self.assertGreater(self.chantry.nodes.count(), 0)
        self.assertEqual(self.chantry.total_node(), 12)
        for node in self.chantry.nodes.all():
            self.assertEqual(node.parent, self.chantry)

    def test_has_library(self):
        self.chantry.library_rating = 3
        self.assertFalse(self.chantry.has_library())
        self.chantry.chantry_library = self.library
        self.chantry.save()
        self.assertTrue(self.chantry.has_library())

    def test_create_library(self):
        self.chantry.library_rating = 0
        self.assertFalse(self.chantry.has_library())
        self.chantry.create_library()
        self.assertTrue(self.chantry.has_library())
        self.assertEqual(self.chantry.chantry_library.num_books(), 0)
        self.chantry.library_rating = 4
        self.chantry.create_library()
        self.assertTrue(self.chantry.has_library())
        self.assertEqual(self.chantry.chantry_library.num_books(), 4)

    def test_set_library(self):
        library = Library.objects.create(name="Test Library", rank=0)
        self.assertFalse(self.chantry.has_library())
        self.chantry.set_library(library)
        self.assertTrue(self.chantry.has_library())

    def test_add_node(self):
        node = Node.objects.create(name="Test Node", rank=3)
        self.chantry.node_rating = 3
        self.assertFalse(self.chantry.has_node())
        self.chantry.add_node(node)
        self.assertTrue(self.chantry.has_node())

    def test_points_spent(self):
        self.assertEqual(self.chantry.points_spent(), 0)
        self.chantry.requisitions = 3
        self.assertEqual(self.chantry.points_spent(), 12)
        self.chantry.node_rating = 8
        self.assertEqual(self.chantry.points_spent(), 36)
        self.chantry.arcane = 1
        self.assertEqual(self.chantry.points_spent(), 38)

    def test_set_rank(self):
        self.chantry.set_rank(5)
        self.assertEqual(self.chantry.rank, 5)

    def test_has_faction(self):
        faction = MageFaction.objects.get(name="Test Faction 0")
        self.assertFalse(self.chantry.has_faction())
        self.chantry.faction = faction
        self.chantry.save()
        self.assertTrue(self.chantry.has_faction())

    def test_set_faction(self):
        faction = MageFaction.objects.get(name="Test Faction 0")
        self.assertFalse(self.chantry.has_faction())
        self.assertTrue(self.chantry.set_faction(faction))
        self.assertEqual(self.chantry.faction, faction)
        self.assertTrue(self.chantry.has_faction())

    def test_has_name(self):
        self.assertFalse(self.chantry.has_name())
        self.chantry.name = "Test"
        self.assertTrue(self.chantry.has_name())

    def test_set_name(self):
        self.assertFalse(self.chantry.has_name())
        self.assertTrue(self.chantry.set_name("Test Chantry"))
        self.assertTrue(self.chantry.has_name())

    def test_has_chantry_type(self):
        self.assertFalse(self.chantry.has_chantry_type())
        self.chantry.chantry_type = "war"
        self.assertTrue(self.chantry.has_chantry_type())

    def test_set_chantry_type(self):
        self.assertFalse(self.chantry.has_chantry_type())
        self.chantry.set_chantry_type("war")
        self.assertTrue(self.chantry.has_chantry_type())

    def test_has_season(self):
        self.assertFalse(self.chantry.has_season())
        self.chantry.season = "spring"
        self.assertTrue(self.chantry.has_season())

    def test_set_season(self):
        self.assertFalse(self.chantry.has_season())
        self.chantry.set_season("spring")
        self.assertTrue(self.chantry.has_season())

    def test_get_traits(self):
        self.chantry.allies = 2
        self.chantry.arcane = 3
        self.chantry.backup = 4
        self.chantry.cult = 5
        self.chantry.elders = 6
        self.chantry.integrated_effects = 7
        self.chantry.retainers = 8
        self.chantry.spies = 9
        self.chantry.resources = 10
        self.chantry.enhancement = 11
        self.chantry.requisitions = 12
        self.chantry.reality_zone_rating = 13
        self.chantry.node_rating = 14
        self.chantry.library_rating = 15
        self.chantry.save()

        result = self.chantry.get_traits()
        expected = {
            "allies": 2,
            "arcane": 3,
            "backup": 4,
            "cult": 5,
            "elders": 6,
            "integrated_effects": 7,
            "retainers": 8,
            "spies": 9,
            "resources": 10,
            "enhancement": 11,
            "requisitions": 12,
            "reality_zone": 13,
            "node_rating": 14,
            "library_rating": 15,
        }

        self.assertEqual(result, expected)


class TestRandomChantry(TestCase):
    def setUp(self) -> None:
        self.chantry = Chantry.objects.create(name="")
        self.player = User.objects.create_user(username="Test")
        self.chantry = Chantry.objects.create(name="")
        self.library = Library.objects.create(rank=3)
        self.grimoire1 = Grimoire.objects.create()
        self.grimoire2 = Grimoire.objects.create()
        self.grimoire3 = Grimoire.objects.create()
        self.library.add_book(self.grimoire1)
        self.library.add_book(self.grimoire2)
        self.library.add_book(self.grimoire3)
        self.node1 = Node.objects.create(name="node1", rank=1)
        self.node2 = Node.objects.create(name="node2", rank=1)
        self.human = Human.objects.create(name="human")
        self.cabal = Cabal.objects.create(name="cabal")
        self.faction = MageFaction.objects.create(name="faction")
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
        blatancy = Ability.objects.get_or_create(
            name="Blatancy", property_name="blatancy"
        )[0]
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
        research = Ability.objects.get_or_create(
            name="Research", property_name="research"
        )[0]
        survival = Ability.objects.get_or_create(
            name="Survival", property_name="survival"
        )[0]
        technology = Ability.objects.get_or_create(
            name="Technology", property_name="technology"
        )[0]
        acrobatics = Ability.objects.get_or_create(
            name="Acrobatics", property_name="acrobatics"
        )[0]
        archery = Ability.objects.get_or_create(
            name="Archery", property_name="archery"
        )[0]
        biotech = Ability.objects.get_or_create(
            name="Biotech", property_name="biotech"
        )[0]
        energy_weapons = Ability.objects.get_or_create(
            name="Energy Weapons", property_name="energy_weapons"
        )[0]
        hypertech = Ability.objects.get_or_create(
            name="Hypertech", property_name="hypertech"
        )[0]
        jetpack = Ability.objects.get_or_create(
            name="Jetpack", property_name="jetpack"
        )[0]
        riding = Ability.objects.get_or_create(name="Riding", property_name="riding")[0]
        torture = Ability.objects.get_or_create(
            name="Torture", property_name="torture"
        )[0]
        cosmology = Ability.objects.get_or_create(
            name="Cosmology", property_name="cosmology"
        )[0]
        enigmas = Ability.objects.get_or_create(
            name="Enigmas", property_name="enigmas"
        )[0]
        esoterica = Ability.objects.get_or_create(
            name="Esoterica", property_name="esoterica"
        )[0]
        law = Ability.objects.get_or_create(name="Law", property_name="law")[0]
        occult = Ability.objects.get_or_create(name="Occult", property_name="occult")[0]
        politics = Ability.objects.get_or_create(
            name="Politics", property_name="politics"
        )[0]
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
        finance = Ability.objects.get_or_create(
            name="Finance", property_name="finance"
        )[0]
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
        empathy = Ability.objects.get_or_create(
            name="Empathy", property_name="empathy"
        )[0]
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
        firearms = Ability.objects.get_or_create(
            name="Firearms", property_name="firearms"
        )[0]
        melee = Ability.objects.get_or_create(name="Melee", property_name="melee")[0]
        stealth = Ability.objects.get_or_create(
            name="Stealth", property_name="stealth"
        )[0]
        academics = Ability.objects.get_or_create(
            name="Academics", property_name="academics"
        )[0]
        computer = Ability.objects.get_or_create(
            name="Computer", property_name="computer"
        )[0]
        investigation = Ability.objects.get_or_create(
            name="Investigation", property_name="investigation"
        )[0]
        medicine = Ability.objects.get_or_create(
            name="Medicine", property_name="medicine"
        )[0]
        science = Ability.objects.get_or_create(
            name="Science", property_name="science"
        )[0]
        cooking = Ability.objects.get_or_create(
            name="Cooking", property_name="cooking"
        )[0]
        diplomacy = Ability.objects.get_or_create(
            name="Diplomacy", property_name="diplomacy"
        )[0]
        instruction = Ability.objects.get_or_create(
            name="Instruction", property_name="instruction"
        )[0]
        intrigue = Ability.objects.get_or_create(
            name="Intrigue", property_name="intrigue"
        )[0]
        intuition = Ability.objects.get_or_create(
            name="Intuition", property_name="intuition"
        )[0]
        mimicry = Ability.objects.get_or_create(
            name="Mimicry", property_name="mimicry"
        )[0]
        negotiation = Ability.objects.get_or_create(
            name="Negotiation", property_name="negotiation"
        )[0]
        newspeak = Ability.objects.get_or_create(
            name="Newspeak", property_name="newspeak"
        )[0]
        scan = Ability.objects.get_or_create(name="Scan", property_name="scan")[0]
        scrounging = Ability.objects.get_or_create(
            name="Scrounging", property_name="scrounging"
        )[0]
        style = Ability.objects.get_or_create(name="Style", property_name="style")[0]
        blind_fighting = Ability.objects.get_or_create(
            name="Blind Fighting", property_name="blind_fighting"
        )[0]
        climbing = Ability.objects.get_or_create(
            name="Climbing", property_name="climbing"
        )[0]
        disguise = Ability.objects.get_or_create(
            name="Disguise", property_name="disguise"
        )[0]
        elusion = Ability.objects.get_or_create(
            name="Elusion", property_name="elusion"
        )[0]
        escapology = Ability.objects.get_or_create(
            name="Escapology", property_name="escapology"
        )[0]
        fast_draw = Ability.objects.get_or_create(
            name="Fast Draw", property_name="fast_draw"
        )[0]
        fast_talk = Ability.objects.get_or_create(
            name="Fast Talk", property_name="fast_talk"
        )[0]
        fencing = Ability.objects.get_or_create(
            name="Fencing", property_name="fencing"
        )[0]
        fortune_telling = Ability.objects.get_or_create(
            name="Fortune Telling", property_name="fortune_telling"
        )[0]
        gambling = Ability.objects.get_or_create(
            name="Gambling", property_name="gambling"
        )[0]
        gunsmith = Ability.objects.get_or_create(
            name="Gunsmith", property_name="gunsmith"
        )[0]
        heavy_weapons = Ability.objects.get_or_create(
            name="Heavy Weapons", property_name="heavy_weapons"
        )[0]
        hunting = Ability.objects.get_or_create(
            name="Hunting", property_name="hunting"
        )[0]
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
        security = Ability.objects.get_or_create(
            name="Security", property_name="security"
        )[0]
        speed_reading = Ability.objects.get_or_create(
            name="Speed Reading", property_name="speed_reading"
        )[0]
        swimming = Ability.objects.get_or_create(
            name="Swimming", property_name="swimming"
        )[0]
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
        helmsman = Ability.objects.get_or_create(
            name="Helmsman", property_name="helmsman"
        )[0]
        history_knowledge = Ability.objects.get_or_create(
            name="History Knowledge", property_name="history_knowledge"
        )[0]
        power_brokering = Ability.objects.get_or_create(
            name="Power Brokering", property_name="power_brokering"
        )[0]
        propaganda = Ability.objects.get_or_create(
            name="Propaganda", property_name="propaganda"
        )[0]
        theology = Ability.objects.get_or_create(
            name="Theology", property_name="theology"
        )[0]
        unconventional_warface = Ability.objects.get_or_create(
            name="Unconventional Warface", property_name="unconventional_warface"
        )[0]
        vice = Ability.objects.get_or_create(name="Vice", property_name="vice")[0]

        human = ObjectType.objects.get_or_create(
            name="human", type="char", gameline="wod"
        )[0]
        mtahuman = ObjectType.objects.get_or_create(
            name="mtahuman", type="char", gameline="mta"
        )[0]
        mage = ObjectType.objects.get_or_create(
            name="mage", type="char", gameline="mta"
        )[0]
        node = ObjectType.objects.get_or_create(
            name="node", type="loc", gameline="mta"
        )[0]

        self.character = Mage.objects.create(name="", owner=self.player)
        for i in range(10):
            Noun.objects.create(name=f"Mage Noun {i}")

        for i in range(5):
            m = Mage.objects.create(name=f"Character {i}", owner=self.player)

        for i in range(15):
            Instrument.objects.create(name=f"Instrument {i}")

        for i in range(5):
            practice = Practice.objects.create(name=f"Practice {i}")
            practice.add_abilities(
                list(random.sample(list(Ability.objects.all()), k=4))
            )
            practice.instruments.set(Instrument.objects.all())
            practice.save()

        for i in range(3):
            paradigm = Paradigm.objects.create(name=f"Paradigm {i}")

        trad = MageFaction.objects.create(name="Traditions")
        MageFaction.objects.create(name="Akashayana", parent=trad)

        for faction in MageFaction.objects.exclude(parent=None):
            faction.paradigms.set(Paradigm.objects.all())
            faction.practices.set(Practice.objects.all())
            faction.save()
            MageFaction.objects.create(name=f"sub-{faction.name}", parent=faction)

        for i in range(5):
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
            Mage.objects.create(name=f"Mage {i}")

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

        for i in range(10):
            Resonance.objects.create(name=f"Resonance {i}")

        for i in range(10):
            for trait in m.get_attributes():
                Specialty.objects.create(
                    name=f"{trait.replace('_', ' ').title()} {i}", stat=trait
                )

            for trait in m.get_abilities():
                Specialty.objects.create(
                    name=f"{trait.replace('_', ' ').title()} {i}", stat=trait
                )

            for trait in m.get_spheres():
                Specialty.objects.create(
                    name=f"{trait.replace('_', ' ').title()} {i}", stat=trait
                )

        for i in range(20):
            Archetype.objects.create(name=f"Archetype {i}")

        for i in range(1, 11):
            Language.objects.create(name=f"Language {i}", frequency=i)
        self.grimoire = Grimoire.objects.create(name="Random Grimoire")
        for i in range(10):
            Noun.objects.create(name=f"Grimoire Noun {i}")

        Ability.objects.get_or_create(name="Awareness", property_name="awareness")[0]
        Ability.objects.get_or_create(name="Art", property_name="art")[0]
        Ability.objects.get_or_create(name="Leadership", property_name="leadership")[0]
        Ability.objects.get_or_create(
            name="Animal Kinship", property_name="animal_kinship"
        )[0]
        Ability.objects.get_or_create(name="Blatancy", property_name="blatancy")[0]
        Ability.objects.get_or_create(name="Carousing", property_name="carousing")[0]
        Ability.objects.get_or_create(name="Do", property_name="do")[0]
        Ability.objects.get_or_create(name="Flying", property_name="flying")[0]
        Ability.objects.get_or_create(name="High Ritual", property_name="high_ritual")[
            0
        ]
        Ability.objects.get_or_create(
            name="Lucid Dreaming", property_name="lucid_dreaming"
        )[0]
        Ability.objects.get_or_create(name="Search", property_name="search")[0]
        Ability.objects.get_or_create(name="Seduction", property_name="seduction")[0]
        Ability.objects.get_or_create(
            name="Martial Arts", property_name="martial_arts"
        )[0]
        Ability.objects.get_or_create(name="Meditation", property_name="meditation")[0]
        Ability.objects.get_or_create(name="Research", property_name="research")[0]
        Ability.objects.get_or_create(name="Survival", property_name="survival")[0]
        Ability.objects.get_or_create(name="Technology", property_name="technology")[0]
        Ability.objects.get_or_create(name="Acrobatics", property_name="acrobatics")[0]
        Ability.objects.get_or_create(name="Archery", property_name="archery")[0]
        Ability.objects.get_or_create(name="Biotech", property_name="biotech")[0]
        Ability.objects.get_or_create(
            name="Energy Weapons", property_name="energy_weapons"
        )[0]
        Ability.objects.get_or_create(name="Hypertech", property_name="hypertech")[0]
        Ability.objects.get_or_create(name="Jetpack", property_name="jetpack")[0]
        Ability.objects.get_or_create(name="Riding", property_name="riding")[0]
        Ability.objects.get_or_create(name="Torture", property_name="torture")[0]
        Ability.objects.get_or_create(name="Cosmology", property_name="cosmology")[0]
        Ability.objects.get_or_create(name="Enigmas", property_name="enigmas")[0]
        Ability.objects.get_or_create(name="Esoterica", property_name="esoterica")[0]
        Ability.objects.get_or_create(name="Law", property_name="law")[0]
        Ability.objects.get_or_create(name="Occult", property_name="occult")[0]
        Ability.objects.get_or_create(name="Politics", property_name="politics")[0]
        Ability.objects.get_or_create(
            name="Area Knowledge", property_name="area_knowledge"
        )[0]
        Ability.objects.get_or_create(
            name="Belief Systems", property_name="belief_systems"
        )[0]
        Ability.objects.get_or_create(
            name="Cryptography", property_name="cryptography"
        )[0]
        Ability.objects.get_or_create(name="Demolitions", property_name="demolitions")[
            0
        ]
        Ability.objects.get_or_create(name="Finance", property_name="finance")[0]
        Ability.objects.get_or_create(name="Lore", property_name="lore")[0]
        Ability.objects.get_or_create(name="Media", property_name="media")[0]
        Ability.objects.get_or_create(
            name="Pharmacopeia", property_name="pharmacopeia"
        )[0]
        Ability.objects.get_or_create(name="Alertness", property_name="alertness")[0]
        Ability.objects.get_or_create(name="Athletics", property_name="athletics")[0]
        Ability.objects.get_or_create(name="Brawl", property_name="brawl")[0]
        Ability.objects.get_or_create(name="Empathy", property_name="empathy")[0]
        Ability.objects.get_or_create(name="Expression", property_name="expression")[0]
        Ability.objects.get_or_create(
            name="Intimidation", property_name="intimidation"
        )[0]
        Ability.objects.get_or_create(name="Streetwise", property_name="streetwise")[0]
        Ability.objects.get_or_create(name="Subterfuge", property_name="subterfuge")[0]
        Ability.objects.get_or_create(name="Crafts", property_name="crafts")[0]
        Ability.objects.get_or_create(name="Drive", property_name="drive")[0]
        Ability.objects.get_or_create(name="Etiquette", property_name="etiquette")[0]
        Ability.objects.get_or_create(name="Firearms", property_name="firearms")[0]
        Ability.objects.get_or_create(name="Melee", property_name="melee")[0]
        Ability.objects.get_or_create(name="Stealth", property_name="stealth")[0]
        Ability.objects.get_or_create(name="Academics", property_name="academics")[0]
        Ability.objects.get_or_create(name="Computer", property_name="computer")[0]
        Ability.objects.get_or_create(
            name="Investigation", property_name="investigation"
        )[0]
        Ability.objects.get_or_create(name="Medicine", property_name="medicine")[0]
        Ability.objects.get_or_create(name="Science", property_name="science")[0]
        Ability.objects.get_or_create(name="Cooking", property_name="cooking")[0]
        Ability.objects.get_or_create(name="Diplomacy", property_name="diplomacy")[0]
        Ability.objects.get_or_create(name="Instruction", property_name="instruction")[
            0
        ]
        Ability.objects.get_or_create(name="Intrigue", property_name="intrigue")[0]
        Ability.objects.get_or_create(name="Intuition", property_name="intuition")[0]
        Ability.objects.get_or_create(name="Mimicry", property_name="mimicry")[0]
        Ability.objects.get_or_create(name="Negotiation", property_name="negotiation")[
            0
        ]
        Ability.objects.get_or_create(name="Newspeak", property_name="newspeak")[0]
        Ability.objects.get_or_create(name="Scan", property_name="scan")[0]
        Ability.objects.get_or_create(name="Scrounging", property_name="scrounging")[0]
        Ability.objects.get_or_create(name="Style", property_name="style")[0]
        Ability.objects.get_or_create(
            name="Blind Fighting", property_name="blind_fighting"
        )[0]
        Ability.objects.get_or_create(name="Climbing", property_name="climbing")[0]
        Ability.objects.get_or_create(name="Disguise", property_name="disguise")[0]
        Ability.objects.get_or_create(name="Elusion", property_name="elusion")[0]
        Ability.objects.get_or_create(name="Escapology", property_name="escapology")[0]
        Ability.objects.get_or_create(name="Fast Draw", property_name="fast_draw")[0]
        Ability.objects.get_or_create(name="Fast Talk", property_name="fast_talk")[0]
        Ability.objects.get_or_create(name="Fencing", property_name="fencing")[0]
        Ability.objects.get_or_create(
            name="Fortune Telling", property_name="fortune_telling"
        )[0]
        Ability.objects.get_or_create(name="Gambling", property_name="gambling")[0]
        Ability.objects.get_or_create(name="Gunsmith", property_name="gunsmith")[0]
        Ability.objects.get_or_create(
            name="Heavy Weapons", property_name="heavy_weapons"
        )[0]
        Ability.objects.get_or_create(name="Hunting", property_name="hunting")[0]
        Ability.objects.get_or_create(name="Hypnotism", property_name="hypnotism")[0]
        Ability.objects.get_or_create(
            name="Jury Rigging", property_name="jury_rigging"
        )[0]
        Ability.objects.get_or_create(
            name="Microgravity Operations", property_name="microgravity_operations"
        )[0]
        Ability.objects.get_or_create(
            name="Misdirection", property_name="misdirection"
        )[0]
        Ability.objects.get_or_create(name="Networking", property_name="networking")[0]
        Ability.objects.get_or_create(name="Pilot", property_name="pilot")[0]
        Ability.objects.get_or_create(name="Psychology", property_name="psychology")[0]
        Ability.objects.get_or_create(name="Security", property_name="security")[0]
        Ability.objects.get_or_create(
            name="Speed Reading", property_name="speed_reading"
        )[0]
        Ability.objects.get_or_create(name="Swimming", property_name="swimming")[0]
        Ability.objects.get_or_create(
            name="Conspiracy Theory", property_name="conspiracy_theory"
        )[0]
        Ability.objects.get_or_create(
            name="Chantry Politics", property_name="chantry_politics"
        )[0]
        Ability.objects.get_or_create(
            name="Covert Culture", property_name="covert_culture"
        )[0]
        Ability.objects.get_or_create(
            name="Cultural Savvy", property_name="cultural_savvy"
        )[0]
        Ability.objects.get_or_create(name="Helmsman", property_name="helmsman")[0]
        Ability.objects.get_or_create(
            name="History Knowledge", property_name="history_knowledge"
        )[0]
        Ability.objects.get_or_create(
            name="Power Brokering", property_name="power_brokering"
        )[0]
        Ability.objects.get_or_create(name="Propaganda", property_name="propaganda")[0]
        Ability.objects.get_or_create(name="Theology", property_name="theology")[0]
        Ability.objects.get_or_create(
            name="Unconventional Warface", property_name="unconventional_warface"
        )[0]
        Ability.objects.get_or_create(name="Vice", property_name="vice")[0]

        Sphere.objects.get_or_create(
            name="Correspondence", property_name="correspondence"
        )[0]
        Sphere.objects.get_or_create(name="Spirit", property_name="spirit")[0]
        Sphere.objects.get_or_create(name="Time", property_name="time")[0]
        Sphere.objects.get_or_create(name="Forces", property_name="forces")[0]
        Sphere.objects.get_or_create(name="Matter", property_name="matter")[0]
        Sphere.objects.get_or_create(name="Life", property_name="life")[0]
        Sphere.objects.get_or_create(name="Entropy", property_name="entropy")[0]
        Sphere.objects.get_or_create(name="Prime", property_name="prime")[0]
        Sphere.objects.get_or_create(name="Mind", property_name="mind")[0]

        abilities = list(Ability.objects.all())
        spheres = list(Sphere.objects.all())
        for i in range(40):
            Instrument.objects.create(name=f"Test Instrument {i}")
        for i in range(20):
            p = Practice.objects.create(name=f"Test Practice {i}")
            p.add_abilities(abilities[i : i + 7])
            p.instruments.add(Instrument.objects.get(name=f"Test Instrument {i}"))
            p.instruments.add(Instrument.objects.get(name=f"Test Instrument {20+i}"))
            p.save()
        for i in range(10):
            Material.objects.create(name=f"Test Material {i}")
            Material.objects.create(name=f"Test Soft Material {i}", is_hard=False)
            Language.objects.create(name=f"Test Language {i}", frequency=i)
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

    def test_random_points(self):
        self.chantry.rank = 1
        self.chantry.random_points()
        self.assertGreaterEqual(self.chantry.points, 10)
        self.assertLessEqual(self.chantry.points, 20)
        self.chantry.rank = 2
        self.chantry.random_points()
        self.assertGreaterEqual(self.chantry.points, 21)
        self.assertLessEqual(self.chantry.points, 30)
        self.chantry.rank = 3
        self.chantry.random_points()
        self.assertGreaterEqual(self.chantry.points, 31)
        self.assertLessEqual(self.chantry.points, 70)
        self.chantry.rank = 4
        self.chantry.random_points()
        self.assertGreaterEqual(self.chantry.points, 71)
        self.assertLessEqual(self.chantry.points, 100)
        self.chantry.rank = 5
        self.chantry.random_points()
        self.assertGreaterEqual(self.chantry.points, 101)
        self.assertLessEqual(self.chantry.points, 200)

    def test_random_rank(self):
        self.assertEqual(self.chantry.rank, 0)
        self.chantry.random_rank()
        self.assertNotEqual(self.chantry.rank, 0)

    def test_random(self):
        self.assertFalse(self.chantry.has_faction())
        self.assertFalse(self.chantry.has_name())
        self.assertFalse(self.chantry.has_library())
        self.assertFalse(self.chantry.has_season())
        self.assertFalse(self.chantry.has_chantry_type())
        self.assertTrue(self.chantry.has_node())
        self.chantry.random()
        self.assertTrue(self.chantry.has_season())
        self.assertTrue(self.chantry.has_chantry_type())
        self.assertTrue(self.chantry.has_faction())
        self.assertTrue(self.chantry.has_name())
        self.assertGreater(self.chantry.points, 0)
        self.assertLessEqual(self.chantry.points - self.chantry.points_spent(), 1)

    def test_random_faction(self):
        self.assertFalse(self.chantry.has_faction())
        self.assertTrue(self.chantry.random_faction())
        self.assertTrue(self.chantry.has_faction())

    def test_random_name(self):
        self.assertEqual(self.chantry.name, "")
        m, _ = MageFaction.objects.get_or_create(name="Society of Ether")
        self.chantry.set_faction(m)
        self.assertTrue(self.chantry.random_name())
        self.assertIn("Laboratory", self.chantry.name)

    def test_random_chantry_type(self):
        self.assertFalse(self.chantry.has_chantry_type())
        self.chantry.random_chantry_type()
        self.assertTrue(self.chantry.has_chantry_type())

    def test_random_season(self):
        self.assertFalse(self.chantry.has_season())
        self.chantry.random_season()
        self.assertTrue(self.chantry.has_season())

    def test_random_populate(self):
        chantry = Chantry.objects.create(
            name="Test Chantry",
            season="spring",
            chantry_type="college",
            leadership_type="anarchy",
            rank=1,
        )
        chantry.random_points()
        chantry.random_faction()
        chantry.random_populate()

        # Check that the number of members in the chantry is at least 3.
        self.assertGreaterEqual(chantry.members.count(), 3)

        # Check that the total number of points of the cabals' members
        # is less than or equal to the chantry's points.
        total_cabal_points = sum(
            sum(x.chantry for x in cabal.members.all())
            for cabal in self.chantry.cabals.all()
        )
        self.assertLessEqual(total_cabal_points, chantry.points)

        # Check that each cabal has at least 3 members.
        for cabal in chantry.cabals.all():
            self.assertGreaterEqual(cabal.members.count(), 3)

    def test_random_leadership_type(self):
        chantry = Chantry.objects.create()
        chantry.random_leadership_type()

        leadership_choices = [choice[0] for choice in Chantry.LEADERSHIP_CHOICES]

        self.assertIn(chantry.leadership_type, leadership_choices)


class TestChantryDetailView(TestCase):
    def setUp(self) -> None:
        self.chantry = Chantry.objects.create(name="Test Chantry")
        self.url = self.chantry.get_absolute_url()

    def test_chantry_detail_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_chantry_detail_view_templates(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "locations/mage/chantry/detail.html")


class TestChantryCreateView(TestCase):
    def setUp(self):
        self.valid_data = {
            "name": "Chantry",
            "description": "Test",
            "leadership_type": "panel",
            "season": "spring",
            "chantry_type": "exploration",
            "rank": 3,
            "points": 0,
            "allies": 0,
            "arcane": 0,
            "backup": 0,
            "cult": 0,
            "elders": 0,
            "integrated_effects": 3,
            "retainers": 2,
            "spies": 1,
            "resources": 0,
            "enhancement": 1,
            "requisitions": 2,
            "reality_zone_rating": 2,
            "node_rating": 3,
            "library_rating": 4,
        }
        self.url = Chantry.get_creation_url()

    def test_create_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "locations/mage/chantry/form.html")

    def test_create_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Chantry.objects.count(), 1)
        self.assertEqual(Chantry.objects.first().name, "Chantry")


class TestChantryUpdateView(TestCase):
    def setUp(self):
        self.chantry = Chantry.objects.create(
            name="Test Chantry",
            description="Test description",
        )
        self.valid_data = {
            "name": "Chantry Updated",
            "description": "Test Chantry",
            "leadership_type": "panel",
            "season": "spring",
            "chantry_type": "exploration",
            "rank": 3,
            "points": 0,
            "allies": 0,
            "arcane": 0,
            "backup": 0,
            "cult": 0,
            "elders": 0,
            "integrated_effects": 3,
            "retainers": 2,
            "spies": 1,
            "resources": 0,
            "enhancement": 1,
            "requisitions": 2,
            "reality_zone_rating": 2,
            "node_rating": 3,
            "library_rating": 4,
        }
        self.url = self.chantry.get_update_url()

    def test_update_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_update_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "locations/mage/chantry/form.html")

    def test_update_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.chantry.refresh_from_db()
        self.assertEqual(self.chantry.name, "Chantry Updated")
        self.assertEqual(self.chantry.description, "Test Chantry")
