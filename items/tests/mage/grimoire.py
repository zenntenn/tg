import random
from unittest import mock
from unittest.mock import Mock

from characters.models.core.ability import Ability
from characters.models.mage import Effect
from characters.models.mage.faction import MageFaction
from characters.models.mage.focus import Instrument, Practice
from characters.models.mage.resonance import Resonance
from characters.models.mage.sphere import Sphere
from core.models import Language, Noun
from django.db.models.query import QuerySet
from django.test import TestCase
from django.urls import reverse
from items.models.core.material import Material
from items.models.core.medium import Medium
from items.models.mage.grimoire import Grimoire


class TestGrimoire(TestCase):
    def setUp(self):
        self.grimoire = Grimoire.objects.create(name="Test Grimoire")
        self.faction = MageFaction.objects.create(name="Test Faction")
        science = Ability.objects.create(name="Science", property_name="science")
        art = Ability.objects.create(name="Art", property_name="art")
        crafts = Ability.objects.create(name="Crafts", property_name="crafts")
        self.abilities = [science, art, crafts]
        self.date_written = 1325
        self.language = Language.objects.create(name="Test Language")
        self.length = 100
        self.practices = [
            Practice.objects.create(name=f"Test Practice {i}") for i in range(3)
        ]
        self.instruments = [
            Instrument.objects.create(name=f"Test Instrument {i}") for i in range(3)
        ]
        self.cover_material = Material.objects.create(name="Test Cover Material")
        self.inner_material = Material.objects.create(name="Test Inner Material")
        self.medium = Medium.objects.create(name="Test Medium")
        self.effects = [
            Effect.objects.create(name=f"Test Effect {i}") for i in range(4)
        ]
        correspondence = Sphere.objects.create(
            name="Correspondence", property_name="correspondence"
        )
        forces = Sphere.objects.create(name="Forces", property_name="forces")
        matter = Sphere.objects.create(name="Matter", property_name="matter")
        self.spheres = [correspondence, forces, matter]

    def test_set_rank(self):
        self.assertEqual(self.grimoire.rank, 0)
        self.assertTrue(self.grimoire.set_rank(3))
        self.assertEqual(self.grimoire.rank, 3)

    def test_has_rank(self):
        self.assertFalse(self.grimoire.has_rank())
        self.grimoire.set_rank(3)
        self.assertTrue(self.grimoire.has_rank())

    def test_set_is_primer(self):
        self.assertFalse(self.grimoire.is_primer)
        self.assertTrue(self.grimoire.set_is_primer(True))
        self.assertTrue(self.grimoire.is_primer)

    def test_set_faction(self):
        self.assertIsNone(self.grimoire.faction)
        self.assertTrue(self.grimoire.set_faction(self.faction))
        self.assertEqual(self.grimoire.faction, self.faction)

    def test_has_faction(self):
        self.assertFalse(self.grimoire.has_faction())
        self.grimoire.set_faction(self.faction)
        self.assertTrue(self.grimoire.has_faction())

    def test_set_focus(self):
        self.assertEqual(self.grimoire.practices.count(), 0)
        self.assertEqual(self.grimoire.instruments.count(), 0)
        self.assertTrue(self.grimoire.set_focus(self.practices, self.instruments))
        self.assertEqual(set(self.grimoire.practices.all()), set(self.practices))
        self.assertEqual(set(self.grimoire.instruments.all()), set(self.instruments))

    def test_has_focus(self):
        self.assertFalse(self.grimoire.has_focus())
        self.grimoire.set_focus(self.practices, self.instruments)
        self.assertTrue(self.grimoire.has_focus())

    def test_set_abilities(self):
        self.assertEqual(self.grimoire.abilities.count(), 0)
        self.assertTrue(self.grimoire.set_abilities(self.abilities))
        self.assertEqual(set(self.grimoire.abilities.all()), set(self.abilities))

    def test_has_abilities(self):
        self.assertFalse(self.grimoire.has_abilities())
        self.grimoire.set_abilities(self.abilities)
        self.assertTrue(self.grimoire.has_abilities())

    def test_set_materials(self):
        self.assertIsNone(self.grimoire.cover_material)
        self.assertIsNone(self.grimoire.inner_material)
        self.assertTrue(
            self.grimoire.set_materials(self.cover_material, self.inner_material)
        )
        self.assertEqual(self.grimoire.cover_material, self.cover_material)
        self.assertEqual(self.grimoire.inner_material, self.inner_material)

    def test_has_materials(self):
        self.assertFalse(self.grimoire.has_materials())
        self.grimoire.set_materials(self.cover_material, self.inner_material)
        self.assertTrue(self.grimoire.has_materials())

    def test_set_language(self):
        self.assertIsNone(self.grimoire.language)
        self.assertTrue(self.grimoire.set_language(self.language))
        self.assertEqual(self.grimoire.language, self.language)

    def test_has_language(self):
        self.assertFalse(self.grimoire.has_language())
        self.grimoire.set_language(self.language)
        self.assertTrue(self.grimoire.has_language())

    def test_set_medium(self):
        self.assertIsNone(self.grimoire.medium)
        self.assertTrue(self.grimoire.set_medium(self.medium))
        self.assertEqual(self.grimoire.medium, self.medium)

    def test_has_medium(self):
        self.assertFalse(self.grimoire.has_medium())
        self.grimoire.set_medium(self.medium)
        self.assertTrue(self.grimoire.has_medium())

    def test_set_length(self):
        self.assertEqual(self.grimoire.length, 0)
        self.assertTrue(self.grimoire.set_length(self.length))
        self.assertEqual(self.grimoire.length, self.length)

    def test_has_length(self):
        self.assertFalse(self.grimoire.has_length())
        self.grimoire.set_length(self.length)
        self.assertTrue(self.grimoire.has_length())

    def test_set_date_written(self):
        self.assertEqual(self.grimoire.date_written, -5000)
        self.assertTrue(self.grimoire.set_date_written(self.date_written))
        self.assertEqual(self.grimoire.date_written, self.date_written)

    def test_has_date_written(self):
        self.assertFalse(self.grimoire.has_date_written())
        self.grimoire.set_date_written(self.date_written)
        self.assertTrue(self.grimoire.has_date_written())

    def test_set_spheres(self):
        self.assertEqual(self.grimoire.spheres.count(), 0)
        self.assertTrue(self.grimoire.set_spheres(self.spheres))
        self.assertEqual(set(self.grimoire.spheres.all()), set(self.spheres))

    def test_has_spheres(self):
        self.assertFalse(self.grimoire.has_spheres())
        self.grimoire.set_spheres(self.spheres)
        self.assertTrue(self.grimoire.has_spheres())

    def test_set_effects(self):
        self.assertEqual(self.grimoire.effects.count(), 0)
        self.assertTrue(self.grimoire.set_effects(self.effects))
        self.assertEqual(set(self.grimoire.effects.all()), set(self.effects))

    def test_has_effects(self):
        self.grimoire.rank = 4
        self.grimoire.save()
        self.grimoire.practices.add(Practice.objects.get(name="Test Practice 0"))
        self.grimoire.abilities.add(Ability.objects.get(name="Science"))
        self.grimoire.spheres.add(Sphere.objects.get(name="Forces"))
        self.assertFalse(self.grimoire.has_effects())
        self.grimoire.set_effects(self.effects)
        self.assertTrue(self.grimoire.has_effects())


class TestRandomGrimoire(TestCase):
    def setUp(self):
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
                            d = {str(sphere_1): i, str(sphere_2): j}
                            Effect.objects.create(
                                name=f"{str(sphere_1)}/{str(sphere_2)} Test Effect {5*i+j}",
                                **d,
                            )
            for i in range(5):
                Resonance.objects.get_or_create(
                    name=f"{str(sphere_1).title()} Resonance {i}",
                    **{str(sphere_1): True},
                )

    def test_random_name(self):
        g = Grimoire.objects.create(name="")
        g.random_medium()
        g.random_spheres()
        self.assertFalse(g.has_name())
        self.assertTrue(g.random_name())
        self.assertTrue(g.has_name())

    def test_random_rank(self):
        mocker = Mock()
        mocker.side_effect = [0.0001, 0.00001]
        with mock.patch("random.random", mocker):
            self.grimoire.random_rank()
            self.assertEqual(self.grimoire.rank, 4)
            self.grimoire.random_rank()
            self.assertEqual(self.grimoire.rank, 5)

    def test_random_is_primer(self):
        mocker = Mock()
        mocker.side_effect = [0.01, 0.11]
        with mock.patch("random.random", mocker):
            self.grimoire.random_is_primer()
            self.assertTrue(self.grimoire.is_primer)
            self.grimoire.random_is_primer()
            self.assertFalse(self.grimoire.is_primer)

    def test_random_faction(self):
        self.assertFalse(self.grimoire.has_faction())
        self.grimoire.random_faction()
        self.assertTrue(self.grimoire.has_faction())

    def test_random_practices(self):
        self.grimoire.faction = MageFaction.objects.get(name="Test Faction 0")
        # Test that random_practices() returns a queryset
        self.assertTrue(isinstance(self.grimoire.random_practices(None), QuerySet))

        # Test that random_practices() returns the correct number of practices
        random_num_practices = random.randint(1, 3)
        practices = Practice.objects.order_by("?")[:random_num_practices]
        self.assertEqual(
            len(self.grimoire.random_practices(practices)), random_num_practices
        )

        # Test that random_practices() returns at least one practice
        self.assertTrue(len(self.grimoire.random_practices(None)) >= 1)

    def test_random_instruments(self):
        # Test that random_instruments() returns a queryset
        self.assertTrue(isinstance(self.grimoire.random_instruments(None), QuerySet))

        # Test that random_instruments() returns the correct number of instruments
        random_num_instruments = random.randint(1, 3)
        instruments = Instrument.objects.order_by("?")[:random_num_instruments]
        self.assertEqual(
            len(self.grimoire.random_instruments(instruments)), random_num_instruments
        )

        # Test that random_instruments() returns at least one instrument
        self.assertTrue(len(self.grimoire.random_instruments(None)) >= 1)

    def test_random_focus(self):
        self.grimoire.faction = MageFaction.objects.get(name="Test Faction 0")
        self.assertFalse(self.grimoire.has_focus())
        self.grimoire.random_focus()
        self.assertTrue(self.grimoire.has_focus())

    def test_random_abilities(self):
        self.grimoire.faction = MageFaction.objects.get(name="Test Faction 0")
        self.assertFalse(self.grimoire.has_abilities())
        self.grimoire.random_focus()
        self.grimoire.random_abilities()
        self.assertTrue(self.grimoire.has_abilities())

    def test_random_materials(self):
        self.assertFalse(self.grimoire.has_materials())
        self.grimoire.random_faction()
        self.grimoire.random_material()
        self.assertTrue(self.grimoire.has_materials())

    def test_random_language(self):
        self.assertFalse(self.grimoire.has_language())
        self.grimoire.random_language()
        self.assertTrue(self.grimoire.has_language())

    def test_random_medium(self):
        self.assertFalse(self.grimoire.has_medium())
        self.grimoire.random_medium()
        self.assertTrue(self.grimoire.has_medium())

    def test_random_length(self):
        self.assertFalse(self.grimoire.has_length())
        self.grimoire.random_length()
        self.assertTrue(self.grimoire.has_length())

    def test_random_date_written(self):
        self.assertFalse(self.grimoire.has_date_written())
        self.grimoire.random_date_written()
        self.assertTrue(self.grimoire.has_date_written())

    def test_random_spheres(self):
        self.assertFalse(self.grimoire.has_spheres())
        self.grimoire.random_spheres()
        self.assertTrue(self.grimoire.has_spheres())

    def test_random_effects(self):
        self.grimoire.random_rank()
        self.grimoire.faction = MageFaction.objects.get(name="Test Faction 0")
        self.grimoire.practices.add(Practice.objects.get(name="Test Practice 0"))
        self.grimoire.abilities.add(Ability.objects.get(name="Awareness"))
        self.grimoire.spheres.add(Sphere.objects.get(name="Correspondence"))
        self.assertFalse(self.grimoire.has_effects())
        self.grimoire.random_effects()
        self.assertTrue(self.grimoire.has_effects())

    def test_random(self):
        self.assertFalse(self.grimoire.has_rank())
        self.assertFalse(self.grimoire.has_faction())
        self.assertFalse(self.grimoire.has_medium())
        self.assertFalse(self.grimoire.has_materials())
        self.assertFalse(self.grimoire.has_length())
        self.assertFalse(self.grimoire.has_focus())
        self.assertFalse(self.grimoire.has_date_written())
        self.assertFalse(self.grimoire.has_abilities())
        self.assertFalse(self.grimoire.has_language())
        self.assertFalse(self.grimoire.has_spheres())
        self.assertFalse(self.grimoire.has_effects())
        self.grimoire.random()
        self.assertTrue(self.grimoire.has_rank())
        self.assertTrue(self.grimoire.has_faction())
        self.assertTrue(self.grimoire.has_medium())
        self.assertTrue(self.grimoire.has_materials())
        self.assertTrue(self.grimoire.has_length())
        self.assertTrue(self.grimoire.has_focus())
        self.assertTrue(self.grimoire.has_date_written())
        self.assertTrue(self.grimoire.has_abilities())
        self.assertTrue(self.grimoire.has_language())
        self.assertTrue(self.grimoire.has_spheres())
        self.assertTrue(self.grimoire.has_effects())


class TestGrimoireDetailView(TestCase):
    def setUp(self) -> None:
        self.grimoire = Grimoire.objects.create(name="Test Grimoire")
        self.url = self.grimoire.get_absolute_url()

    def test_object_detail_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_object_detail_view_templates(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/mage/grimoire/detail.html")


class TestGrimoireCreateView(TestCase):
    def setUp(self):
        self.valid_data = {
            "name": "Test Grimoire",
            "description": "Test",
            "date_written": 1000,
            "is_primer": False,
            "length": 3,
        }
        self.url = reverse("items:mage:create:grimoire")

    def test_create_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/mage/grimoire/form.html")

    def test_create_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Grimoire.objects.count(), 1)
        self.assertEqual(Grimoire.objects.first().name, "Test Grimoire")


class TestGrimoireUpdateView(TestCase):
    def setUp(self):
        self.grimoire = Grimoire.objects.create(
            name="Test Grimoire",
            description="Test description",
        )
        self.valid_data = {
            "name": "Test Grimoire Updated",
            "description": "A test description for the grimoire.",
            "date_written": 1000,
            "is_primer": False,
            "length": 3,
        }
        self.url = self.grimoire.get_update_url()

    def test_update_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_update_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/mage/grimoire/form.html")

    def test_update_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.grimoire.refresh_from_db()
        self.assertEqual(self.grimoire.name, "Test Grimoire Updated")
        self.assertEqual(
            self.grimoire.description, "A test description for the grimoire."
        )
