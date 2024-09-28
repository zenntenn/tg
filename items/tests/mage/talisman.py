from unittest import mock
from unittest.mock import Mock

from characters.models.mage import Effect
from characters.models.mage.resonance import Resonance
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from items.models.mage.talisman import Talisman


class TestTalisman(TestCase):
    def setUp(self):
        self.effect1 = Effect.objects.create(name="Effect 1", forces=3)
        self.effect2 = Effect.objects.create(name="Effect 2", life=2)
        self.effect3 = Effect.objects.create(name="Effect 3", time=3)

    def test_add_power(self):
        talisman = Talisman.objects.create(rank=2)
        self.assertEqual(talisman.powers.count(), 0)
        talisman.add_power(self.effect1)
        self.assertEqual(talisman.powers.count(), 1)
        talisman.add_power(self.effect2)
        self.assertEqual(talisman.powers.count(), 2)

    def test_has_powers(self):
        talisman = Talisman.objects.create(rank=2)
        self.assertFalse(talisman.has_powers())
        talisman.add_power(self.effect1)
        self.assertFalse(talisman.has_powers())
        talisman.add_power(self.effect2)
        self.assertTrue(talisman.has_powers())


class TestRandomTalisman(TestCase):
    def setUp(self):
        self.player, _ = User.objects.get_or_create(username="Test")
        Effect.objects.create(name="Fireball", forces=3, prime=2)
        Effect.objects.create(name="F1", forces=1)
        Effect.objects.create(name="F2", forces=2)
        Effect.objects.create(name="F3", forces=3)
        Effect.objects.create(name="F4", forces=4)
        Effect.objects.create(name="F5", forces=5)
        Resonance.objects.create(name="Test")
        self.effect1 = Effect.objects.create(name="Effect 1", forces=1)
        self.effect2 = Effect.objects.create(name="Effect 2", life=2)
        self.effect3 = Effect.objects.create(name="Effect 3", time=3)

    def test_random_power(self):
        talisman = Talisman.objects.create(rank=2)
        talisman.random_power(1)
        self.assertEqual(talisman.powers.count(), 1)
        self.assertLessEqual(talisman.powers.first().max_sphere, 1)
        talisman.random_power(2)
        self.assertEqual(talisman.powers.count(), 2)
        max_sphere = max(p.max_sphere for p in talisman.powers.all())
        self.assertLessEqual(max_sphere, 2)

    def test_random_powers(self):
        talisman = Talisman.objects.create(rank=2)
        talisman.random_powers()
        self.assertEqual(talisman.powers.count(), 2)
        max_sphere = max(p.max_sphere for p in talisman.powers.all())
        self.assertLessEqual(max_sphere, 2)

    def test_random(self):
        talisman = Talisman.objects.create()
        mocker = Mock()
        mocker.side_effect = [0.8, 0.5, 0.5, 0.5, 0.5, 0.5]
        with mock.patch("random.random", mocker):
            talisman.random(rank=2)
        self.assertTrue(talisman.has_powers())
        max_sphere = max(p.max_sphere for p in talisman.powers.all())
        self.assertLessEqual(max_sphere, 2)
        self.assertEqual(talisman.quintessence_max, 10)
        self.assertEqual(talisman.background_cost, 4)
        self.assertEqual(talisman.arete, 2)


class TestTalismanDetailView(TestCase):
    def setUp(self) -> None:
        self.talisman = Talisman.objects.create(name="Test Talisman")
        self.url = self.talisman.get_absolute_url()

    def test_object_detail_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_object_detail_view_templates(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/mage/talisman/detail.html")


class TestTalismanCreateView(TestCase):
    def setUp(self):
        self.valid_data = {
            "name": "Test Talisman",
            "description": "A test description for the talisman.",
            "rank": 2,
            "background_cost": 3,
            "quintessence_max": 5,
            "arete": 2,
        }
        self.url = Talisman.get_creation_url()

    def test_create_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/mage/talisman/form.html")

    def test_create_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Talisman.objects.count(), 1)
        self.assertEqual(Talisman.objects.first().name, "Test Talisman")


class TestTalismanUpdateView(TestCase):
    def setUp(self):
        self.talisman = Talisman.objects.create(
            name="Test Talisman",
            description="Test description",
        )
        self.valid_data = {
            "name": "Test Talisman Updated",
            "description": "A test description for the talisman.",
            "rank": 2,
            "background_cost": 3,
            "quintessence_max": 5,
            "arete": 2,
        }
        self.url = self.talisman.get_update_url()

    def test_update_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_update_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/mage/talisman/form.html")

    def test_update_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.talisman.refresh_from_db()
        self.assertEqual(self.talisman.name, "Test Talisman Updated")
        self.assertEqual(
            self.talisman.description, "A test description for the talisman."
        )
