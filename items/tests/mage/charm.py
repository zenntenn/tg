from characters.models.mage import Effect
from characters.models.mage.resonance import Resonance
from django.test import TestCase
from django.urls import reverse
from items.models.mage import Charm


class TestCharm(TestCase):
    def setUp(self):
        self.charm = Charm.objects.create(name="Test Charm")
        self.power = Effect.objects.create(name="Power")

    def test_set_power(self):
        self.assertFalse(self.charm.has_power())
        self.assertTrue(self.charm.set_power(self.power))
        self.assertTrue(self.charm.has_power())

    def test_has_power(self):
        self.assertFalse(self.charm.has_power())
        self.charm.set_power(self.power)
        self.assertTrue(self.charm.has_power())


class TestRandomCharm(TestCase):
    def setUp(self):
        Effect.objects.create(name="Fireball", forces=3, prime=2)
        Effect.objects.create(name="F1", forces=1)
        Effect.objects.create(name="F2", forces=2)
        Effect.objects.create(name="F3", forces=3)
        Effect.objects.create(name="F4", forces=4)
        Effect.objects.create(name="F5", forces=5)
        Resonance.objects.create(name="Test")

    def test_random_power(self):
        c = Charm.objects.create(name="", rank=3)
        self.assertFalse(c.has_power())
        self.assertTrue(c.random_power())
        self.assertTrue(c.has_power())

    def test_random(self):
        c = Charm.objects.create(name="")
        c.random()
        self.assertEqual(c.status, "Ran")
        self.assertTrue(c.has_name())
        self.assertTrue(c.has_rank())
        self.assertTrue(c.has_resonance())
        self.assertTrue(c.has_power())
        self.assertEqual(c.arete, c.rank)
        self.assertEqual(c.background_cost, c.rank)


class TestCharmDetailView(TestCase):
    def setUp(self) -> None:
        self.wonder = Charm.objects.create(name="Test Charm")
        self.url = self.wonder.get_absolute_url()

    def test_object_detail_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_object_detail_view_templates(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/mage/charm/detail.html")


class TestCharmCreateView(TestCase):
    def setUp(self):
        self.valid_data = {
            "name": "Test Charm",
            "description": "A test description for the charm.",
            "rank": 2,
            "background_cost": 3,
            "quintessence_max": 5,
            "arete": 2,
        }
        self.url = Charm.get_creation_url()

    def test_create_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/mage/charm/form.html")

    def test_create_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Charm.objects.count(), 1)
        self.assertEqual(Charm.objects.first().name, "Test Charm")


class TestCharmUpdateView(TestCase):
    def setUp(self):
        self.wonder = Charm.objects.create(
            name="Test Charm",
            description="Test description",
        )
        self.valid_data = {
            "name": "Test Charm Updated",
            "description": "A test description for the wonder.",
            "rank": 2,
            "background_cost": 3,
            "quintessence_max": 5,
            "arete": 2,
        }
        self.url = self.wonder.get_update_url()

    def test_update_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_update_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/mage/charm/form.html")

    def test_update_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.wonder.refresh_from_db()
        self.assertEqual(self.wonder.name, "Test Charm Updated")
        self.assertEqual(self.wonder.description, "A test description for the wonder.")
