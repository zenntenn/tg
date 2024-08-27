import random
from unittest import mock
from unittest.mock import Mock

from characters.models.core.ability import Ability
from characters.models.mage import Effect
from characters.models.mage.faction import MageFaction
from characters.models.mage.focus import Instrument, Practice
from characters.models.mage.resonance import Resonance
from characters.models.mage.sphere import Sphere
from characters.tests.utils import mage_setup
from core.models import Language, Noun
from core.utils import time_test
from django.contrib.auth.models import User
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
        self.player, _ = User.objects.get_or_create(username="Test")
        self.grimoire = Grimoire.objects.create(name="Random Grimoire")
        mage_setup()

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

    def test_creation_time(self):
        self.assertLessEqual(time_test(Grimoire, self.player, character=False), 0.05)


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
        self.url = Grimoire.get_creation_url()

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
