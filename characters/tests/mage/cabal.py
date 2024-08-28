import random

from characters.models.core.ability import Ability
from characters.models.core.archetype import Archetype
from characters.models.core.meritflaw import MeritFlaw
from characters.models.core.specialty import Specialty
from characters.models.mage.cabal import Cabal
from characters.models.mage.effect import Effect
from characters.models.mage.faction import MageFaction
from characters.models.mage.focus import Instrument, Paradigm, Practice
from characters.models.mage.mage import Mage
from characters.models.mage.resonance import Resonance
from characters.models.mage.sphere import Sphere
from characters.tests.utils import mage_setup
from core.models import Language, Noun
from core.utils import time_test
from django.contrib.auth.models import User
from django.test import TestCase
from game.models import ObjectType


class TestCabal(TestCase):
    def setUp(self):
        self.player = User.objects.create_user(username="Player")
        self.character = Mage.objects.create(name="", owner=self.player)
        mage_setup()
        for i in range(4):
            Mage.objects.create(name=f"Character {i}", owner=self.player)

    def test_cabal_creation(self):
        cabal = Cabal.objects.create(name="Cabal 1")
        cabal.members.set(Mage.objects.all())
        cabal.leader = Mage.objects.first()
        cabal.save()
        self.assertEqual(cabal.members.count(), 5)
        self.assertIsNotNone(cabal.leader)

    def test_random(self):
        cabal = Cabal.objects.create(name="Cabal 1")
        cabal.random(num_chars=5, new_characters=False)
        self.assertEqual(cabal.members.count(), 5)
        for mage in Mage.objects.all():
            self.assertIn(mage, cabal.members.all())
        cabal = Cabal.objects.create(name="Cabal 2")
        cabal.random(num_chars=5, new_characters=True)
        self.assertEqual(cabal.members.count(), 5)

    def test_exception(self):
        cabal = Cabal.objects.create(name="Cabal 10")
        with self.assertRaises(ValueError):
            cabal.random(num_chars=10, new_characters=False)

    def test_str(self):
        cabal = Cabal.objects.create(name="Cabal 1")
        self.assertEqual(str(cabal), "Cabal 1")

    def test_creation_time(self):
        self.assertLessEqual(time_test(Cabal, self.player, character=True), 2)


class TestCabalDetailView(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="User1", password="12345")
        self.cabal = Cabal.objects.create(name="Test Cabal")
        self.url = self.cabal.get_absolute_url()

    def test_cabal_detail_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_cabal_detail_view_templates(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "characters/mage/cabal/detail.html")


class TestCabalCreateView(TestCase):
    def setUp(self):
        self.valid_data = {
            "name": "Test Cabal",
            "description": "Test",
        }
        self.url = Cabal.get_creation_url()

    def test_create_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "characters/mage/cabal/form.html")

    def test_create_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Cabal.objects.count(), 1)
        self.assertEqual(Cabal.objects.first().name, "Test Cabal")


class TestCabalUpdateView(TestCase):
    def setUp(self):
        self.cabal = Cabal.objects.create(name="Test Cabal", description="Test")
        self.valid_data = {
            "name": "Test Cabal Updated",
            "description": "Test",
        }
        self.url = self.cabal.get_update_url()

    def test_update_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_update_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "characters/mage/cabal/form.html")

    def test_update_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.cabal.refresh_from_db()
        self.assertEqual(self.cabal.name, "Test Cabal Updated")
        self.assertEqual(self.cabal.description, "Test")
