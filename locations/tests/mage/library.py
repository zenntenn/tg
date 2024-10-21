from characters.models.core.ability_block import Ability
from characters.models.mage.effect import Effect
from characters.models.mage.faction import MageFaction
from characters.models.mage.focus import Instrument, Practice
from characters.models.mage.resonance import Resonance
from characters.models.mage.sphere import Sphere
from characters.tests.utils import mage_setup
from core.models import Language, Noun
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
        mage_setup()

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
