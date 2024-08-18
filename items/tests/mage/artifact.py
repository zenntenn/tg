from characters.models.mage import Effect
from characters.models.mage.resonance import Resonance
from core.utils import time_test
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from items.models.mage import Artifact


class TestArtifact(TestCase):
    def setUp(self):
        self.artifact = Artifact.objects.create(name="Test Artifact")
        self.power = Effect.objects.create(name="Power")

    def test_set_power(self):
        self.assertFalse(self.artifact.has_power())
        self.assertTrue(self.artifact.set_power(self.power))
        self.assertTrue(self.artifact.has_power())

    def test_has_power(self):
        self.assertFalse(self.artifact.has_power())
        self.artifact.set_power(self.power)
        self.assertTrue(self.artifact.has_power())


class TestRandomArtifact(TestCase):
    def setUp(self):
        self.player, _ = User.objects.get_or_create(username="Test")
        Effect.objects.create(name="Fireball", forces=3, prime=2)
        Effect.objects.create(name="F1", forces=1)
        Effect.objects.create(name="F2", forces=2)
        Effect.objects.create(name="F3", forces=3)
        Effect.objects.create(name="F4", forces=4)
        Effect.objects.create(name="F5", forces=5)
        Resonance.objects.create(name="Test")

    def test_random_power(self):
        a = Artifact.objects.create(name="", rank=3)
        self.assertFalse(a.has_power())
        self.assertTrue(a.random_power())
        self.assertTrue(a.has_power())

    def test_random(self):
        a = Artifact.objects.create(name="")
        a.random()
        self.assertEqual(a.status, "Ran")
        self.assertTrue(a.has_name())
        self.assertTrue(a.has_rank())
        self.assertTrue(a.has_resonance())
        self.assertTrue(a.has_power())
        self.assertEqual(a.quintessence_max, a.rank * 5)
        self.assertEqual(a.background_cost, a.rank * 2)

    def test_creation_time(self):
        self.assertLessEqual(time_test(Artifact, self.player, character=False), 0.01)


class TestArtifactDetailView(TestCase):
    def setUp(self) -> None:
        self.artifact = Artifact.objects.create(name="Test Artifact")
        self.url = self.artifact.get_absolute_url()

    def test_object_detail_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_object_detail_view_templates(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/mage/artifact/detail.html")


class TestArtifactCreateView(TestCase):
    def setUp(self):
        self.valid_data = {
            "name": "Test Artifact",
            "description": "A test description for the artifact.",
            "rank": 2,
            "background_cost": 3,
            "quintessence_max": 5,
        }
        self.url = Artifact.get_creation_url()

    def test_create_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/mage/artifact/form.html")

    def test_create_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Artifact.objects.count(), 1)
        self.assertEqual(Artifact.objects.first().name, "Test Artifact")


class TestArtifactUpdateView(TestCase):
    def setUp(self):
        self.artifact = Artifact.objects.create(
            name="Test Artifact",
            description="Test description",
        )
        self.valid_data = {
            "name": "Test Artifact Updated",
            "description": "A test description for the artifact.",
            "rank": 2,
            "background_cost": 3,
            "quintessence_max": 5,
        }
        self.url = self.artifact.get_update_url()

    def test_update_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_update_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/mage/artifact/form.html")

    def test_update_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.artifact.refresh_from_db()
        self.assertEqual(self.artifact.name, "Test Artifact Updated")
        self.assertEqual(
            self.artifact.description, "A test description for the artifact."
        )
