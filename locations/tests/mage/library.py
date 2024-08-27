from characters.models.core.ability import Ability
from characters.models.mage.effect import Effect
from characters.models.mage.faction import MageFaction
from characters.models.mage.focus import Instrument, Practice
from characters.models.mage.resonance import Resonance
from characters.models.mage.sphere import Sphere
from core.models import Language, Noun
from core.utils import time_test
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from items.models.core.material import Material
from items.models.core.medium import Medium
from items.models.mage.grimoire import Grimoire
from locations.models.mage.library import Library


class TestLibrary(TestCase):
    def setUp(self):
        self.grimoire_1 = Grimoire.objects.create(name="Grimoire 1", rank=1)
        self.grimoire_2 = Grimoire.objects.create(name="Grimoire 2", rank=2)
        self.grimoire_3 = Grimoire.objects.create(name="Grimoire 3", rank=3)
        self.grimoire_4 = Grimoire.objects.create(name="Grimoire 4", rank=4)
        self.grimoire_5 = Grimoire.objects.create(name="Grimoire 5", rank=5)
        self.library = Library.objects.create(name="Test Library")

    def test_set_rank(self):
        self.assertEqual(self.library.rank, 1)
        self.assertTrue(self.library.set_rank(3))
        self.assertEqual(self.library.rank, 3)

    def test_add_book(self):
        g = Grimoire.objects.create(name="Book To Add")
        count = self.library.num_books()
        self.assertTrue(self.library.add_book(g))
        self.assertEqual(self.library.num_books(), count + 1)

    def test_set_faction(self):
        faction = MageFaction.objects.create(name="Test Faction")
        self.assertFalse(self.library.has_faction())
        self.assertTrue(self.library.set_faction(faction))
        self.assertTrue(self.library.has_faction())

    def test_has_faction(self):
        faction = MageFaction.objects.create(name="Test Faction")
        self.assertFalse(self.library.has_faction())
        self.library.set_faction(faction)
        self.assertTrue(self.library.has_faction())

    def test_has_books(self):
        self.library.rank = 3
        self.assertEqual(self.library.books.count(), 0)
        self.library.books.add(self.grimoire_1)
        self.library.books.add(self.grimoire_2)
        self.library.books.add(self.grimoire_3)
        self.assertEqual(self.library.books.count(), 3)

    def test_num_books(self):
        self.assertEqual(self.library.num_books(), 0)
        self.library.rank = 3
        self.library.books.add(self.grimoire_1)
        self.assertEqual(self.library.num_books(), 1)
        self.library.books.add(self.grimoire_2)
        self.assertEqual(self.library.num_books(), 2)
        self.library.books.add(self.grimoire_3)
        self.assertEqual(self.library.num_books(), 3)


class TestRandomLibrary(TestCase):
    def setUp(self):
        self.player, _ = User.objects.get_or_create(username="Test")
        self.library = Library.objects.create(name="", rank=2)
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

    def test_increase_rank(self):
        self.assertEqual(self.library.num_books(), 0)
        self.library.increase_rank()
        self.library.increase_rank()
        self.assertEqual(self.library.num_books(), 2)

    def test_random_name(self):
        self.assertFalse(self.library.has_name())
        self.assertTrue(self.library.random_name())
        self.assertTrue(self.library.has_name())

    def test_random_rank(self):
        self.assertEqual(self.library.rank, 2)
        self.library.random_rank(rank=0)
        self.assertEqual(self.library.rank, 0)
        self.library.random_rank()
        self.assertNotEqual(self.library.rank, 0)

    def test_random_faction(self):
        self.library.random_faction()
        self.assertIsNotNone(self.library.faction)

    def test_random_book(self):
        num_books = self.library.num_books()
        self.library.random_faction()
        self.library.save()
        self.library.random_book()
        self.assertEqual(num_books + 1, self.library.num_books())

    def test_random(self):
        self.library.random()
        self.assertEqual(self.library.status, "Ran")
        self.assertIsNotNone(self.library.faction)
        self.assertEqual(self.library.num_books(), self.library.rank)

    def test_creation_time(self):
        self.assertLessEqual(time_test(Library, self.player, character=False), 0.1)


class TestLibraryDetailView(TestCase):
    def setUp(self):
        self.library = Library.objects.create(name="Test Library")
        self.url = self.library.get_absolute_url()

    def test_library_detail_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_library_detail_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "locations/mage/library/detail.html")


class TestLibraryCreateView(TestCase):
    def setUp(self):
        self.valid_data = {
            "name": "Library",
            "description": "Test",
            "rank": 2,
        }
        self.url = Library.get_creation_url()

    def test_create_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "locations/mage/library/form.html")

    def test_create_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Library.objects.count(), 1)
        self.assertEqual(Library.objects.first().name, "Library")


class TestLibraryUpdateView(TestCase):
    def setUp(self):
        self.library = Library.objects.create(
            name="Test Library",
            description="Test description",
        )
        self.valid_data = {
            "name": "Library Updated",
            "description": "Test",
            "rank": 2,
        }
        self.url = self.library.get_update_url()

    def test_update_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_update_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "locations/mage/library/form.html")

    def test_update_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.library.refresh_from_db()
        self.assertEqual(self.library.name, "Library Updated")
        self.assertEqual(self.library.description, "Test")
