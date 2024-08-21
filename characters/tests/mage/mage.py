import random
from unittest import mock
from unittest.mock import Mock

from characters.models.core.ability import Ability
from characters.models.core.archetype import Archetype
from characters.models.core.meritflaw import MeritFlaw
from characters.models.core.specialty import Specialty
from characters.models.mage.effect import Effect
from characters.models.mage.faction import MageFaction
from characters.models.mage.focus import Instrument, Paradigm, Practice
from characters.models.mage.mage import Mage, ResRating
from characters.models.mage.resonance import Resonance
from characters.models.mage.rote import Rote
from core.models import Language, Noun
from django.contrib.auth.models import User
from django.test import TestCase
from game.models import ObjectType
from locations.models.mage.library import Library
from locations.models.mage.node import Node


class TestMage(TestCase):
    def setUp(self):
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

        self.player = User.objects.create_user(username="Test")
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

    def set_abilities(self):
        self.character.alertness = 1
        self.character.art = 2
        self.character.empathy = 3
        self.character.streetwise = 2
        self.character.firearms = 3
        self.character.melee = 4
        self.character.stealth = 2
        self.character.technology = 1
        self.character.cosmology = 3
        self.character.law = 2
        self.character.area_knowledge = 1
        self.character.belief_systems = 1
        self.character.cryptography = 1

    def test_do_is_akashic_only(self):
        self.character.awareness = 2
        self.assertFalse(self.character.add_ability("do"))
        self.character.faction = MageFaction.objects.get(name="Akashayana")
        self.assertTrue(self.character.add_ability("do"))

    def test_do_requires_limbs(self):
        self.character.faction = MageFaction.objects.get(name="Akashayana")
        self.assertFalse(self.character.add_ability("do"))
        self.character.awareness = 2
        self.assertTrue(self.character.add_ability("do"))
        self.character.cosmology = 3
        self.assertTrue(self.character.add_ability("do"))
        self.assertTrue(self.character.add_ability("do"))
        self.assertFalse(self.character.add_ability("do"))

    def set_spheres(self):
        self.character.correspondence = 1
        self.character.time = 2
        self.character.spirit = 3
        self.character.matter = 4
        self.character.forces = 5
        self.character.life = 4
        self.character.entropy = 3
        self.character.mind = 2
        self.character.prime = 1

    def test_get_spheres(self):
        self.assertEqual(
            self.character.get_spheres(),
            {
                "correspondence": 0,
                "time": 0,
                "spirit": 0,
                "matter": 0,
                "forces": 0,
                "life": 0,
                "entropy": 0,
                "mind": 0,
                "prime": 0,
            },
        )
        self.set_spheres()
        self.assertEqual(
            self.character.get_spheres(),
            {
                "correspondence": 1,
                "time": 2,
                "spirit": 3,
                "matter": 4,
                "forces": 5,
                "life": 4,
                "entropy": 3,
                "mind": 2,
                "prime": 1,
            },
        )

    def test_add_sphere(self):
        self.character.arete = 2
        self.assertTrue(self.character.add_sphere("forces"))
        self.assertTrue(self.character.add_sphere("forces"))
        self.assertEqual(self.character.forces, 2)
        self.assertFalse(self.character.add_sphere("forces"))
        self.character.arete = 3
        self.assertTrue(self.character.add_sphere("forces"))
        self.character.arete = 7
        self.assertTrue(self.character.add_sphere("forces"))
        self.assertTrue(self.character.add_sphere("forces"))
        self.assertFalse(self.character.add_sphere("forces"))

    def test_batini_no_entropy(self):
        self.character.faction = MageFaction.objects.create(name="Ahl-i-Batin")
        self.character.add_arete()
        self.assertTrue(self.character.add_sphere("forces"))
        self.assertFalse(self.character.add_sphere("entropy"))

    def test_filter_spheres(self):
        self.character.arete = 3
        self.assertEqual(len(self.character.filter_spheres().keys()), 9)
        self.set_spheres()
        self.assertEqual(len(self.character.filter_spheres(maximum=2).keys()), 4)
        self.assertEqual(
            len(self.character.filter_spheres(minimum=2, maximum=2).keys()), 2
        )
        self.assertEqual(len(self.character.filter_spheres(maximum=1).keys()), 2)

    def test_has_spheres(self):
        self.assertFalse(self.character.has_spheres())
        self.character.arete = 3
        self.character.set_affinity_sphere("forces")
        self.assertFalse(self.character.has_spheres())
        self.character.add_sphere("forces")
        self.assertFalse(self.character.has_spheres())
        self.character.add_sphere("forces")
        self.assertFalse(self.character.has_spheres())
        self.character.add_sphere("matter")
        self.assertFalse(self.character.has_spheres())
        self.character.add_sphere("matter")
        self.assertFalse(self.character.has_spheres())
        self.character.add_sphere("matter")
        self.assertTrue(self.character.has_spheres())

    def test_set_affinity_sphere(self):
        self.character.arete = 1
        self.assertFalse(self.character.has_affinity_sphere())
        self.assertTrue(self.character.set_affinity_sphere("forces"))
        self.assertTrue(self.character.has_affinity_sphere())
        self.assertEqual(self.character.forces, 1)

    def test_has_affinity_sphere(self):
        self.character.arete = 1
        self.assertFalse(self.character.has_affinity_sphere())
        self.character.affinity_sphere = "forces"
        self.character.forces = 1
        self.assertTrue(self.character.has_affinity_sphere())

    def test_sphere_names(self):
        spheres = [
            "correspondence",
            "forces",
            "time",
            "life",
            "spirit",
            "matter",
            "prime",
            "mind",
            "entropy",
        ]
        for sphere in spheres:
            self.assertTrue(hasattr(self.character, f"{sphere}"))
        self.assertEqual(self.character.get_corr_name_display(), "Correspondence")
        self.assertEqual(self.character.get_spirit_name_display(), "Spirit")
        self.assertEqual(self.character.get_prime_name_display(), "Prime")
        self.character.set_corr_name("data")
        self.character.set_prime_name("primal_utility")
        self.character.set_spirit_name("dimensional_science")
        self.assertEqual(self.character.get_corr_name_display(), "Data")
        self.assertEqual(
            self.character.get_spirit_name_display(), "Dimensional Science"
        )
        self.assertEqual(self.character.get_prime_name_display(), "Primal Utility")
        with self.assertRaises(ValueError):
            self.character.set_corr_name("blah")

    def test_add_arete(self):
        self.assertEqual(self.character.arete, 0)
        self.assertTrue(self.character.add_arete())
        self.assertEqual(self.character.arete, 1)
        self.character.arete = 10
        self.assertFalse(self.character.add_arete())

    def test_total_spheres(self):
        self.character.forces = 2
        self.assertEqual(self.character.total_spheres(), 2)
        self.character.matter = 3
        self.assertEqual(self.character.total_spheres(), 5)
        self.character.matter = 2
        self.character.life = 1
        self.assertEqual(self.character.total_spheres(), 5)

    def test_mage_numbers(self):
        # self.assertEqual(self.character.willpower, 5)
        self.assertEqual(self.character.background_points, 7)

    def test_add_background(self):
        num = self.character.total_backgrounds()
        self.assertFalse(self.character.add_background("test"))
        self.assertEqual(num, self.character.total_backgrounds())
        self.assertTrue(self.character.add_background("avatar"))
        self.assertEqual(num + 1, self.character.total_backgrounds())

    def test_get_backgrounds(self):
        self.assertEqual(
            self.character.get_backgrounds(),
            {
                "allies": 0,
                "alternate_identity": 0,
                "arcane": 0,
                "avatar": 0,
                "backup": 0,
                "blessing": 0,
                "certification": 0,
                "chantry": 0,
                "contacts": 0,
                "cult": 0,
                "demesne": 0,
                "destiny": 0,
                "dream": 0,
                "enhancement": 0,
                "fame": 0,
                "familiar": 0,
                "influence": 0,
                "legend": 0,
                "library": 0,
                "mentor": 0,
                "node": 0,
                "past_lives": 0,
                "patron": 0,
                "rank": 0,
                "requisitions": 0,
                "resources": 0,
                "retainers": 0,
                "sanctum": 0,
                "secret_weapons": 0,
                "spies": 0,
                "status_background": 0,
                "totem": 0,
                "wonder": 0,
            },
        )
        self.character.allies = 1
        self.character.avatar = 3
        self.character.chantry = 3
        self.character.legend = 2
        self.character.node = 2
        self.assertEqual(
            self.character.get_backgrounds(),
            {
                "allies": 1,
                "alternate_identity": 0,
                "arcane": 0,
                "avatar": 3,
                "backup": 0,
                "blessing": 0,
                "certification": 0,
                "chantry": 3,
                "contacts": 0,
                "cult": 0,
                "demesne": 0,
                "destiny": 0,
                "dream": 0,
                "enhancement": 0,
                "fame": 0,
                "familiar": 0,
                "influence": 0,
                "legend": 2,
                "library": 0,
                "mentor": 0,
                "node": 2,
                "past_lives": 0,
                "patron": 0,
                "rank": 0,
                "requisitions": 0,
                "resources": 0,
                "retainers": 0,
                "sanctum": 0,
                "secret_weapons": 0,
                "spies": 0,
                "status_background": 0,
                "totem": 0,
                "wonder": 0,
            },
        )

    def test_total_backgrounds(self):
        self.character.allies = 3
        self.character.avatar = 4
        self.character.resources = 1
        self.character.sanctum = 2
        self.assertEqual(self.character.total_backgrounds(), 12)
        self.character.wonder = 2
        self.assertEqual(self.character.total_backgrounds(), 14)

    def test_technocracy_only_backgrounds(self):
        tech_char = Mage.objects.create(name="Tech", owner=self.player)
        tech_char.affiliation = MageFaction.objects.create(name="Technocratic Union")
        trad_char = Mage.objects.create(name="Trad", owner=self.player)
        trad_char.affiliation = MageFaction.objects.get(name="Traditions")
        self.assertTrue(tech_char.add_background("secret_weapons"))
        self.assertFalse(trad_char.add_background("secret_weapons"))
        self.assertEqual(tech_char.total_backgrounds(), 1)
        self.assertEqual(trad_char.total_backgrounds(), 0)
        self.assertTrue(tech_char.add_background("requisitions"))
        self.assertFalse(trad_char.add_background("requisitions"))
        self.assertEqual(tech_char.total_backgrounds(), 2)
        self.assertEqual(trad_char.total_backgrounds(), 0)

    def test_set_faction(self):
        self.assertFalse(self.character.has_focus())
        affiliation = MageFaction.objects.create(name="Affiliation")
        faction = MageFaction.objects.create(name="Faction", parent=affiliation)
        subfaction = MageFaction.objects.create(name="Subfaction", parent=faction)

        affiliation2 = MageFaction.objects.create(name="Affiliation2")
        faction2 = MageFaction.objects.create(name="Faction2", parent=affiliation2)
        subfaction2 = MageFaction.objects.create(name="Subfaction2", parent=faction2)

        self.assertFalse(
            self.character.set_faction(affiliation, faction, subfaction=subfaction2)
        )
        self.assertTrue(
            self.character.set_faction(affiliation, faction, subfaction=subfaction)
        )
        self.assertTrue(self.character.has_faction())
        self.assertTrue(
            self.character.set_faction(
                subfaction2.parent.parent, subfaction2.parent, subfaction=subfaction2
            )
        )
        self.assertTrue(self.character.has_faction())

    def test_has_faction(self):
        self.assertFalse(self.character.has_focus())
        affiliation = MageFaction.objects.create(name="Affiliation")
        faction = MageFaction.objects.create(name="Faction", parent=affiliation)
        subfaction = MageFaction.objects.create(name="Subfaction", parent=faction)
        self.character.set_faction(
            affiliation=affiliation, faction=faction, subfaction=subfaction
        )
        self.assertTrue(self.character.has_faction())

    def test_set_focus(self):
        paradigms = Paradigm.objects.order_by("?")[:2]
        practices = Practice.objects.order_by("?")[:2]
        instruments = Instrument.objects.order_by("?")[:7]
        self.assertFalse(self.character.has_focus())
        self.assertFalse(
            self.character.set_focus(
                paradigms=paradigms, practices=practices, instruments=instruments[:3]
            )
        )
        self.assertTrue(
            self.character.set_focus(
                paradigms=paradigms, practices=practices, instruments=instruments
            )
        )
        self.assertTrue(self.character.has_focus())

    def test_has_focus(self):
        paradigms = Paradigm.objects.order_by("?")[:2]
        practices = Practice.objects.order_by("?")[:2]
        instruments = Instrument.objects.order_by("?")[:7]
        self.assertFalse(self.character.has_focus())
        self.character.set_focus(
            paradigms=paradigms, practices=practices, instruments=instruments
        )
        self.assertTrue(self.character.has_focus())

    def test_set_essence(self):
        self.assertFalse(self.character.has_essence())
        self.assertTrue(self.character.set_essence("questing"))
        self.assertTrue(self.character.has_essence())

    def test_has_essence(self):
        self.assertFalse(self.character.has_essence())
        self.character.set_essence("questing")
        self.assertTrue(self.character.has_essence())

    def test_add_resonance(self):
        res = Resonance.objects.order_by("?").first()
        self.assertEqual(self.character.resonance_rating(res), 0)
        self.assertTrue(self.character.add_resonance(res))
        self.assertEqual(self.character.resonance_rating(res), 1)

    def test_filter_resonance(self):
        self.assertEqual(len(self.character.filter_resonance()), 10)
        for res in Resonance.objects.order_by("?")[:3]:
            self.assertTrue(self.character.add_resonance(res))
        self.assertEqual(len(self.character.filter_resonance(maximum=0)), 7)

    def test_total_resonance(self):
        resonance = Resonance.objects.order_by("?")[:2]
        for res in resonance:
            self.character.add_resonance(res)
            self.character.add_resonance(res)
        self.assertEqual(self.character.total_resonance(), 4)
        self.assertNotEqual(self.character.total_resonance(), 5)
        self.character.add_resonance(resonance[0])
        self.assertEqual(self.character.total_resonance(), 5)

    def test_add_effect(self):
        self.character.arete = 3
        self.character.forces = 3
        self.character.prime = 2
        self.character.random_focus()
        e = Effect.objects.create(name="Fireball", forces=3, prime=2)
        e2 = Effect.objects.create(name="Teleport", correspondence=3)
        num = self.character.rotes.count()
        self.assertTrue(self.character.add_effect(e))
        r = Rote.objects.get(effect=e)
        self.assertEqual(self.character.rotes.count(), num + 1)
        self.assertIn(r, self.character.rotes.all())
        self.assertFalse(self.character.add_effect(e2))
        self.character.correspondence = 3
        self.assertNotIn(
            e2, self.character.rotes.all().values_list("effect", flat=True)
        )
        self.assertTrue(self.character.add_effect(e2))
        r2 = Rote.objects.get(effect=e2)
        self.assertIn(r2, self.character.rotes.all())

    def test_has_effects(self):
        self.character.arete = 3
        self.character.forces = 3
        self.character.prime = 2
        self.character.matter = 1
        self.character.random_focus()
        self.assertFalse(self.character.has_effects())
        self.character.add_effect(Effect.objects.get(name="Forces 3"))
        self.assertFalse(self.character.has_effects())
        self.character.add_effect(Effect.objects.get(name="Matter 1"))
        self.assertFalse(self.character.has_effects())
        self.character.add_effect(Effect.objects.get(name="Prime 1"))
        self.assertFalse(self.character.has_effects())
        self.character.add_effect(Effect.objects.get(name="Forces 1"))
        self.assertTrue(self.character.has_effects())

    def test_total_effects(self):
        self.character.arete = 3
        self.character.forces = 3
        self.character.prime = 2
        self.character.correspondence = 3
        self.character.random_focus()
        r1 = Effect.objects.create(name="Fireball", forces=3, prime=2)
        r2 = Effect.objects.create(name="Teleport", correspondence=3)
        self.character.add_effect(r1)
        self.assertEqual(self.character.total_effects(), 5)
        self.character.add_effect(r2)
        self.assertEqual(self.character.total_effects(), 8)

    def test_filter_effects(self):
        self.character.arete = 5
        self.character.correspondence = 5
        self.character.time = 5
        self.character.spirit = 5
        self.character.forces = 5
        self.character.matter = 5
        self.character.life = 5
        self.character.entropy = 5
        self.character.prime = 5
        self.character.mind = 5
        self.assertEqual(len(self.character.filter_effects()), 45)
        self.character.mind = 4
        self.assertEqual(len(self.character.filter_effects()), 44)
        self.character.prime = 1
        self.assertEqual(len(self.character.filter_effects()), 40)
        self.character.correspondence = 1
        self.character.time = 1
        self.character.spirit = 1
        self.character.forces = 2
        self.character.matter = 0
        self.character.life = 0
        self.character.entropy = 0
        self.character.prime = 0
        self.character.mind = 0
        self.assertEqual(len(self.character.filter_effects()), 5)

    def test_has_mage_history(self):
        self.assertFalse(self.character.has_mage_history())
        self.character.awakening = "Young"
        self.assertFalse(self.character.has_mage_history())
        self.character.seekings = "Several"
        self.assertFalse(self.character.has_mage_history())
        self.character.quiets = "None"
        self.assertFalse(self.character.has_mage_history())
        self.character.age_of_awakening = 13
        self.assertFalse(self.character.has_mage_history())
        self.character.avatar_description = "The Random Graph"
        self.assertTrue(self.character.has_mage_history())

    def test_set_quiet_rating(self):
        self.assertEqual(self.character.quiet, 0)
        self.character.set_quiet_rating(3)
        self.assertEqual(self.character.quiet, 3)

    def test_set_quiet_type(self):
        self.assertEqual(self.character.quiet_type, "none")
        self.character.set_quiet_type("denial")
        self.assertEqual(self.character.quiet_type, "denial")

    def test_marauders_have_quiet(self):
        top_level = MageFaction.objects.create(name="TopLevel Faction", parent=None)
        marauder = MageFaction.objects.create(name="Marauders", parent=None)
        self.assertEqual(self.character.quiet, 0)
        self.assertEqual(self.character.quiet_type, "none")
        self.character.set_faction(top_level, None, None)
        self.assertEqual(self.character.quiet, 0)
        self.assertEqual(self.character.quiet_type, "none")
        self.character.set_faction(marauder, None, None)
        self.assertNotEqual(self.character.quiet, 0)
        self.assertNotEqual(self.character.quiet_type, "none")

    def test_count_limbs(self):
        self.character.alertness = 1
        self.character.athletics = 2
        self.character.do = 3
        self.assertEqual(self.character.count_limbs(), 2)
        self.character.awareness = 1
        self.character.enigmas = 2
        self.character.meditation = 3
        self.assertEqual(self.character.count_limbs(), 3)
        self.character.esoterica = 1
        self.character.medicine = 2
        self.character.survival = 3
        self.assertEqual(self.character.count_limbs(), 5)
        self.character.art = 1
        self.character.crafts = 2
        self.character.etiquette = 3
        self.assertEqual(self.character.count_limbs(), 7)
        self.character.academics = 1
        self.character.belief_systems = 2
        self.character.cosmology = 3
        self.assertEqual(self.character.count_limbs(), 8)
        self.character.melee = 1
        self.character.stealth = 2
        self.character.subterfuge = 3
        self.assertEqual(self.character.count_limbs(), 8)

    def test_resonance_rating(self):
        resonance = Resonance.objects.create(name="test_resonance")
        res_rating = ResRating.objects.create(
            mage=self.character, resonance=resonance, rating=3
        )
        self.assertEqual(self.character.resonance_rating(resonance), res_rating.rating)

    def test_has_specialties(self):
        self.assertTrue(self.character.has_specialties())
        self.character.forces = 4
        self.assertFalse(self.character.has_specialties())
        self.character.add_specialty(Specialty.objects.create(stat="forces"))
        self.assertTrue(self.character.has_specialties())

    def test_has_library(self):
        self.assertFalse(self.character.has_library())
        library = Library.objects.create(name="test_library", rank=3)
        self.character.library_owned = library
        self.character.library = 3
        self.assertTrue(self.character.has_library())

    def test_has_node(self):
        self.assertFalse(self.character.has_node())
        node = Node.objects.create(name="test_node", rank=2)
        self.character.node_owned = node
        self.character.node = 2
        self.assertTrue(self.character.has_node())


class TestRandomMage(TestCase):
    def setUp(self):
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

        self.player = User.objects.create_user(username="Test")
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

        for i in range(10):
            Resonance.objects.create(name=f"Resonance {i}")

        for i in range(20):
            Archetype.objects.create(name=f"Archetype {i}")

        for i in range(1, 11):
            Language.objects.create(name=f"Language {i}", frequency=i)

    def test_random_affinity_sphere(self):
        self.assertFalse(self.character.has_affinity_sphere())
        self.character.random_affinity_sphere()
        self.assertTrue(self.character.has_affinity_sphere())

    def test_random_faction(self):
        self.assertFalse(self.character.has_faction())
        self.character.random_faction()
        self.assertTrue(self.character.has_faction())
        mage = Mage.objects.create(name="Random Character", owner=self.player)
        mocker = Mock()
        mocker.side_effect = [0.01]
        with mock.patch("random.random", mocker):
            mage.random_faction()
        self.assertIsNotNone(mage.subfaction)

    def test_random_focus(self):
        self.assertFalse(self.character.has_focus())
        self.character.random_focus()
        self.assertTrue(self.character.has_focus())

    def test_random_sphere(self):
        self.character.arete = 3
        self.character.affinity_sphere = "forces"
        num = self.character.total_spheres()
        self.character.random_sphere()
        self.assertEqual(self.character.total_spheres(), num + 1)

    def test_random_spheres(self):
        self.character.arete = 3
        self.assertFalse(self.character.has_spheres())
        self.character.random_spheres()
        self.assertTrue(self.character.has_spheres())

    def test_random_arete(self):
        self.assertEqual(self.character.arete, 0)
        self.character.random_arete()
        self.assertNotEqual(self.character.arete, 0)

    def test_random_essence(self):
        self.assertFalse(self.character.has_essence())
        self.character.random_essence()
        self.assertTrue(self.character.has_essence())

    def test_random_resonance(self):
        self.assertEqual(self.character.total_resonance(), 0)
        self.character.random_resonance()
        self.assertEqual(self.character.total_resonance(), 1)

    def test_random_effect(self):
        self.character.arete = 3
        self.character.forces = 3
        self.character.prime = 2
        self.character.matter = 1
        self.character.random_focus()
        num = self.character.rotes.count()
        self.character.random_effect()
        self.assertEqual(self.character.rotes.count(), num + 1)

    def test_random_effects(self):
        self.character.arete = 3
        self.character.forces = 3
        self.character.prime = 2
        self.character.matter = 1
        self.character.random_focus()
        self.assertFalse(self.character.has_effects())
        self.character.random_effects()
        self.assertTrue(self.character.has_effects())

    # def test_created_node_when_has_node(self):
    #     self.character.node = 3
    #     self.assertFalse(self.character.has_node())
    #     self.character.random_node()
    #     self.assertTrue(self.character.has_node())

    # def test_created_library_when_has_library(self):
    #     self.character.library = 3
    #     self.assertFalse(self.character.has_library())
    #     self.character.random_library()
    #     self.assertTrue(self.character.has_library())

    def test_random_specialties(self):
        self.character.forces = 4
        self.character.random_specialties()
        self.assertTrue(self.character.has_specialties())
        self.assertGreater(self.character.specialties.filter(stat="forces").count(), 0)

    def test_random_quiet(self):
        self.character.random_quiet()
        self.assertGreater(self.character.quiet, 0)
        self.assertNotEqual(self.character.quiet_type, "none")

    def test_random(self):
        self.assertFalse(self.character.has_name())
        self.assertFalse(self.character.has_concept())
        self.assertFalse(self.character.has_archetypes())
        self.assertFalse(self.character.has_attributes())
        self.assertFalse(self.character.has_abilities())
        self.assertFalse(self.character.has_backgrounds())
        self.assertFalse(self.character.has_finishing_touches())
        self.assertFalse(self.character.has_history())
        self.assertFalse(self.character.has_spheres())
        self.assertFalse(self.character.has_affinity_sphere())
        self.assertFalse(self.character.has_faction())
        self.assertFalse(self.character.has_focus())
        self.assertFalse(self.character.has_essence())
        self.assertFalse(self.character.has_effects())
        self.assertFalse(self.character.has_mage_history())
        self.character.random(freebies=0, xp=0)
        self.assertTrue(self.character.has_name())
        self.assertTrue(self.character.has_concept())
        self.assertTrue(self.character.has_archetypes())
        self.assertTrue(self.character.has_attributes())
        self.assertTrue(self.character.has_abilities())
        self.assertTrue(self.character.has_specialties())
        self.assertTrue(self.character.has_backgrounds())
        self.assertTrue(self.character.has_finishing_touches())
        self.assertTrue(self.character.has_history())
        self.assertTrue(self.character.has_spheres())
        self.assertTrue(self.character.has_affinity_sphere())
        self.assertTrue(self.character.has_faction())
        self.assertTrue(self.character.has_focus())
        self.assertTrue(self.character.has_essence())
        self.assertTrue(self.character.has_effects())
        self.assertTrue(self.character.has_mage_history())
        # if self.character.node != 0:
        #     self.assertTrue(self.character.has_node())
        # else:
        #     self.assertFalse(self.character.has_node())
        # if self.character.library != 0:
        #     self.assertTrue(self.character.has_library())
        # else:
        #     self.assertFalse(self.character.has_library())

    def test_choose_random_resonance(self):
        res = self.character.choose_random_resonance()
        self.assertIsNotNone(res)
        self.assertIsInstance(res, Resonance)

    def test_random_mage_history(self):
        self.character.random_mage_history()
        self.assertIsNotNone(self.character.awakening)
        self.assertIsNotNone(self.character.seekings)
        self.assertIsNotNone(self.character.quiets)
        self.assertIsNotNone(self.character.age_of_awakening)
        self.assertIsNotNone(self.character.avatar_description)

    def test_random_abilities(self):
        self.character.random_abilities()
        triple = [
            self.character.total_talents(),
            self.character.total_skills(),
            self.character.total_knowledges(),
        ]
        triple.sort()
        self.assertEqual(triple, [5, 9, 13])

    def test_random_ability(self):
        self.character.random_ability()
        self.assertGreater(self.character.total_abilities(), 0)


class TestMageDetailView(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="User1", password="12345")
        self.mage = Mage.objects.create(name="Test Mage", owner=self.player)
        self.url = self.mage.get_absolute_url()

    def test_mage_detail_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_mage_detail_view_templates(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "characters/mage/mage/detail.html")


class TestMageCreateView(TestCase):
    def setUp(self):
        self.valid_data = {
            "name": "Test Mage",
            "description": 0,
            "willpower": 0,
            "age": 0,
            "apparent_age": 0,
            "hair": 0,
            "eyes": 0,
            "ethnicity": 0,
            "nationality": 0,
            "height": 0,
            "weight": 0,
            "sex": 0,
            "childhood": 0,
            "history": 0,
            "goals": 0,
            "notes": 0,
            "strength": 0,
            "dexterity": 0,
            "stamina": 0,
            "perception": 0,
            "intelligence": 0,
            "wits": 0,
            "charisma": 0,
            "manipulation": 0,
            "appearance": 0,
            "awareness": 0,
            "art": 0,
            "leadership": 0,
            "animal_kinship": 0,
            "blatancy": 0,
            "carousing": 0,
            "do": 0,
            "flying": 0,
            "high_ritual": 0,
            "lucid_dreaming": 0,
            "search": 0,
            "seduction": 0,
            "martial_arts": 0,
            "meditation": 0,
            "research": 0,
            "survival": 0,
            "technology": 0,
            "acrobatics": 0,
            "archery": 0,
            "biotech": 0,
            "energy_weapons": 0,
            "hypertech": 0,
            "jetpack": 0,
            "riding": 0,
            "torture": 0,
            "cosmology": 0,
            "enigmas": 0,
            "esoterica": 0,
            "law": 0,
            "occult": 0,
            "politics": 0,
            "area_knowledge": 0,
            "belief_systems": 0,
            "cryptography": 0,
            "demolitions": 0,
            "finance": 0,
            "lore": 0,
            "media": 0,
            "pharmacopeia": 0,
            "cooking": 0,
            "diplomacy": 0,
            "instruction": 0,
            "intrigue": 0,
            "intuition": 0,
            "mimicry": 0,
            "negotiation": 0,
            "newspeak": 0,
            "scan": 0,
            "scrounging": 0,
            "style": 0,
            "blind_fighting": 0,
            "climbing": 0,
            "disguise": 0,
            "elusion": 0,
            "escapology": 0,
            "fast_draw": 0,
            "fast_talk": 0,
            "fencing": 0,
            "fortune_telling": 0,
            "gambling": 0,
            "gunsmith": 0,
            "heavy_weapons": 0,
            "hunting": 0,
            "hypnotism": 0,
            "jury_rigging": 0,
            "microgravity_operations": 0,
            "misdirection": 0,
            "networking": 0,
            "pilot": 0,
            "psychology": 0,
            "security": 0,
            "speed_reading": 0,
            "swimming": 0,
            "conspiracy_theory": 0,
            "chantry_politics": 0,
            "covert_culture": 0,
            "cultural_savvy": 0,
            "helmsman": 0,
            "history_knowledge": 0,
            "power_brokering": 0,
            "propaganda": 0,
            "theology": 0,
            "unconventional_warface": 0,
            "vice": 0,
            "allies": 0,
            "alternate_identity": 0,
            "arcane": 0,
            "avatar": 0,
            "backup": 0,
            "blessing": 0,
            "certification": 0,
            "chantry": 0,
            "cult": 0,
            "demesne": 0,
            "destiny": 0,
            "dream": 0,
            "enhancement": 0,
            "fame": 0,
            "familiar": 0,
            "influence": 0,
            "legend": 0,
            "library": 0,
            "node": 0,
            "past_lives": 0,
            "patron": 0,
            "rank": 0,
            "requisitions": 0,
            "resources": 0,
            "retainers": 0,
            "sanctum": 0,
            "secret_weapons": 0,
            "spies": 0,
            "status_background": 0,
            "totem": 0,
            "wonder": 0,
            "essence": "Dynamic",
            "correspondence": 0,
            "time": 0,
            "spirit": 0,
            "mind": 0,
            "entropy": 0,
            "prime": 0,
            "forces": 0,
            "matter": 0,
            "life": 0,
            "arete": 2,
            "affinity_sphere": "forces",
            "corr_name": "correspondence",
            "prime_name": "prime",
            "spirit_name": "spirit",
            "awakening": "dhghd",
            "seekings": "fgdgj",
            "quiets": "sfgjsfgj",
            "age_of_awakening": 18,
            "avatar_description": "sfjgsj",
            "rote_points": 0,
            "quintessence": 0,
            "paradox": 0,
            "quiet": 0,
            "quiet_type": "none",
        }
        self.url = Mage.get_creation_url()

    def test_create_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "characters/mage/mage/form.html")

    def test_create_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Mage.objects.count(), 1)
        self.assertEqual(Mage.objects.first().name, "Test Mage")


class TestMageHumanUpdateView(TestCase):
    def setUp(self):
        self.mage = Mage.objects.create(name="Test Mage", description="Test")
        self.valid_data = {
            "name": "Test Mage 2",
            "description": 0,
            "willpower": 0,
            "age": 0,
            "apparent_age": 0,
            "hair": 0,
            "eyes": 0,
            "ethnicity": 0,
            "nationality": 0,
            "height": 0,
            "weight": 0,
            "sex": 0,
            "childhood": 0,
            "history": 0,
            "goals": 0,
            "notes": 0,
            "strength": 0,
            "dexterity": 0,
            "stamina": 0,
            "perception": 0,
            "intelligence": 0,
            "wits": 0,
            "charisma": 0,
            "manipulation": 0,
            "appearance": 0,
            "awareness": 0,
            "art": 0,
            "leadership": 0,
            "animal_kinship": 0,
            "blatancy": 0,
            "carousing": 0,
            "do": 0,
            "flying": 0,
            "high_ritual": 0,
            "lucid_dreaming": 0,
            "search": 0,
            "seduction": 0,
            "martial_arts": 0,
            "meditation": 0,
            "research": 0,
            "survival": 0,
            "technology": 0,
            "acrobatics": 0,
            "archery": 0,
            "biotech": 0,
            "energy_weapons": 0,
            "hypertech": 0,
            "jetpack": 0,
            "riding": 0,
            "torture": 0,
            "cosmology": 0,
            "enigmas": 0,
            "esoterica": 0,
            "law": 0,
            "occult": 0,
            "politics": 0,
            "area_knowledge": 0,
            "belief_systems": 0,
            "cryptography": 0,
            "demolitions": 0,
            "finance": 0,
            "lore": 0,
            "media": 0,
            "pharmacopeia": 0,
            "cooking": 0,
            "diplomacy": 0,
            "instruction": 0,
            "intrigue": 0,
            "intuition": 0,
            "mimicry": 0,
            "negotiation": 0,
            "newspeak": 0,
            "scan": 0,
            "scrounging": 0,
            "style": 0,
            "blind_fighting": 0,
            "climbing": 0,
            "disguise": 0,
            "elusion": 0,
            "escapology": 0,
            "fast_draw": 0,
            "fast_talk": 0,
            "fencing": 0,
            "fortune_telling": 0,
            "gambling": 0,
            "gunsmith": 0,
            "heavy_weapons": 0,
            "hunting": 0,
            "hypnotism": 0,
            "jury_rigging": 0,
            "microgravity_operations": 0,
            "misdirection": 0,
            "networking": 0,
            "pilot": 0,
            "psychology": 0,
            "security": 0,
            "speed_reading": 0,
            "swimming": 0,
            "conspiracy_theory": 0,
            "chantry_politics": 0,
            "covert_culture": 0,
            "cultural_savvy": 0,
            "helmsman": 0,
            "history_knowledge": 0,
            "power_brokering": 0,
            "propaganda": 0,
            "theology": 0,
            "unconventional_warface": 0,
            "vice": 0,
            "allies": 0,
            "alternate_identity": 0,
            "arcane": 0,
            "avatar": 0,
            "backup": 0,
            "blessing": 0,
            "certification": 0,
            "chantry": 0,
            "cult": 0,
            "demesne": 0,
            "destiny": 0,
            "dream": 0,
            "enhancement": 0,
            "fame": 0,
            "familiar": 0,
            "influence": 0,
            "legend": 0,
            "library": 0,
            "node": 0,
            "past_lives": 0,
            "patron": 0,
            "rank": 0,
            "requisitions": 0,
            "resources": 0,
            "retainers": 0,
            "sanctum": 0,
            "secret_weapons": 0,
            "spies": 0,
            "status_background": 0,
            "totem": 0,
            "wonder": 0,
            "essence": "Dynamic",
            "correspondence": 0,
            "time": 0,
            "spirit": 0,
            "mind": 0,
            "entropy": 0,
            "prime": 0,
            "forces": 0,
            "matter": 0,
            "life": 0,
            "arete": 2,
            "affinity_sphere": "forces",
            "corr_name": "correspondence",
            "prime_name": "prime",
            "spirit_name": "spirit",
            "awakening": "dhghd",
            "seekings": "fgdgj",
            "quiets": "sfgjsfgj",
            "age_of_awakening": 18,
            "avatar_description": "sfjgsj",
            "rote_points": 0,
            "quintessence": 0,
            "paradox": 0,
            "quiet": 0,
            "quiet_type": "none",
        }
        self.url = self.mage.get_update_url()

    def test_update_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_update_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "characters/mage/mage/form.html")

    def test_update_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.mage.refresh_from_db()
        self.assertEqual(self.mage.name, "Test Mage 2")
