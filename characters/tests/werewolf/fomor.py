from characters.models.core.archetype import Archetype
from characters.models.core.specialty import Specialty
from characters.models.werewolf.fomor import Fomor
from characters.models.werewolf.fomoripower import FomoriPower
from core.utils import time_test
from django.test import TestCase


class TestFomor(TestCase):
    def setUp(self):
        self.power1 = FomoriPower.objects.create(name="Power 1")
        self.power2 = FomoriPower.objects.create(name="Power 2")
        self.power3 = FomoriPower.objects.create(name="Power 3")
        self.fomor = Fomor.objects.create(name="Test Fomor", allies=2, contacts=1)

    def test_get_backgrounds(self):
        expected = {
            "allies": 2,
            "contacts": 1,
            "resources": 0,
        }
        self.assertEqual(self.fomor.get_backgrounds(), expected)

    def test_add_power(self):
        self.fomor.add_power(self.power1)
        self.assertEqual(self.fomor.powers.count(), 1)
        self.assertEqual(list(self.fomor.powers.all()), [self.power1])

    def test_filter_powers(self):
        self.fomor.add_power(self.power1)
        self.fomor.add_power(self.power2)
        self.fomor.add_power(self.power3)
        filtered_powers = self.fomor.filter_powers()
        self.assertEqual(filtered_powers.count(), 0)
        self.fomor.powers.remove(self.power3)
        filtered_powers = self.fomor.filter_powers()
        self.assertEqual(filtered_powers.count(), 1)
        self.assertEqual(list(filtered_powers.all()), [self.power3])


class TestRandomFomor(TestCase):
    def setUp(self):
        self.power1 = FomoriPower.objects.create(name="Power 1")
        self.power2 = FomoriPower.objects.create(name="Power 2")
        self.power3 = FomoriPower.objects.create(name="Power 3")
        FomoriPower.objects.create(name="Immunity to the Delirium")
        self.fomor = Fomor.objects.create(name="Test Fomor")
        for attribute in self.fomor.get_attributes():
            Specialty.objects.create(name=f"{attribute} Spec", stat=attribute)
        for ability in self.fomor.get_abilities():
            Specialty.objects.create(name=f"{ability} Spec", stat=ability)
        for i in range(10):
            Archetype.objects.create(name=f"Archetype {i}")

    def test_random_power(self):
        self.assertEqual(self.fomor.powers.count(), 0)
        self.fomor.random_power()
        self.assertEqual(self.fomor.powers.count(), 1)

    def test_random_powers(self):
        self.fomor.random_powers(num_powers=2)
        self.assertGreaterEqual(self.fomor.powers.count(), 2)

    def test_random(self):
        self.fomor.random(freebies=0, xp=0)
        self.assertTrue(self.fomor.has_name())
        self.assertTrue(self.fomor.has_concept())
        self.assertTrue(self.fomor.has_archetypes())
        self.assertTrue(self.fomor.has_attributes(primary=6, secondary=4, tertiary=3))
        self.assertTrue(self.fomor.has_abilities(primary=11, secondary=7, tertiary=3))
        self.assertTrue(self.fomor.has_backgrounds())
        self.assertGreater(self.fomor.powers.count(), 0)

    def test_creation_time(self):
        self.assertLessEqual(time_test(Fomor, self.player, character=True), 0.5)


class TestFomorDetailView(TestCase):
    def setUp(self) -> None:
        self.fomor = Fomor.objects.create(name="Test Fomor")
        self.url = self.fomor.get_absolute_url()

    def test_fomor_detail_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_fomor_detail_view_templates(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "characters/werewolf/fomor/detail.html")


class TestFomorCreateView(TestCase):
    def setUp(self):
        self.valid_data = {
            "name": "Fomor",
            "description": "Test",
            "concept": 0,
            "strength": 0,
            "dexterity": 0,
            "stamina": 0,
            "perception": 0,
            "intelligence": 0,
            "wits": 0,
            "charisma": 0,
            "manipulation": 0,
            "appearance": 0,
            "alertness": 0,
            "athletics": 0,
            "brawl": 0,
            "empathy": 0,
            "expression": 0,
            "intimidation": 0,
            "streetwise": 0,
            "subterfuge": 0,
            "crafts": 0,
            "drive": 0,
            "etiquette": 0,
            "firearms": 0,
            "melee": 0,
            "stealth": 0,
            "academics": 0,
            "computer": 0,
            "investigation": 0,
            "medicine": 0,
            "science": 0,
            "contacts": 0,
            "mentor": 0,
            "willpower": 0,
            "age": 0,
            "apparent_age": 0,
            "hair": "aasf",
            "eyes": "aasf",
            "ethnicity": "aasf",
            "nationality": "aasf",
            "height": "aasf",
            "weight": "aasf",
            "sex": "aasf",
            "childhood": "aasf",
            "history": "aasf",
            "goals": "aasf",
            "notes": "aasf",
            "leadership": 0,
            "primal_urge": 0,
            "animal_ken": 0,
            "larceny": 0,
            "performance": 0,
            "survival": 0,
            "enigmas": 0,
            "law": 0,
            "occult": 0,
            "rituals": 0,
            "technology": 0,
            "allies": 0,
            "ancestors": 0,
            "fate": 0,
            "fetish": 0,
            "kinfolk_rating": 0,
            "pure_breed": 0,
            "resources": 0,
            "rites": 0,
            "spirit_heritage": 0,
            "totem": 0,
            "rage": 1,
            "gnosis": 1,
        }
        self.url = Fomor.get_creation_url()

    def test_create_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "characters/werewolf/fomor/form.html")

    def test_create_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Fomor.objects.count(), 1)
        self.assertEqual(Fomor.objects.first().name, "Fomor")


class TestFomorUpdateView(TestCase):
    def setUp(self):
        self.fomor = Fomor.objects.create(
            name="Test Fomor",
            description="Test description",
        )
        self.valid_data = {
            "name": "Fomor Updated",
            "description": "Test",
            "concept": 0,
            "strength": 0,
            "dexterity": 0,
            "stamina": 0,
            "perception": 0,
            "intelligence": 0,
            "wits": 0,
            "charisma": 0,
            "manipulation": 0,
            "appearance": 0,
            "alertness": 0,
            "athletics": 0,
            "brawl": 0,
            "empathy": 0,
            "expression": 0,
            "intimidation": 0,
            "streetwise": 0,
            "subterfuge": 0,
            "crafts": 0,
            "drive": 0,
            "etiquette": 0,
            "firearms": 0,
            "melee": 0,
            "stealth": 0,
            "academics": 0,
            "computer": 0,
            "investigation": 0,
            "medicine": 0,
            "science": 0,
            "contacts": 0,
            "mentor": 0,
            "willpower": 0,
            "age": 0,
            "apparent_age": 0,
            "hair": "aasf",
            "eyes": "aasf",
            "ethnicity": "aasf",
            "nationality": "aasf",
            "height": "aasf",
            "weight": "aasf",
            "sex": "aasf",
            "childhood": "aasf",
            "history": "aasf",
            "goals": "aasf",
            "notes": "aasf",
            "leadership": 0,
            "primal_urge": 0,
            "animal_ken": 0,
            "larceny": 0,
            "performance": 0,
            "survival": 0,
            "enigmas": 0,
            "law": 0,
            "occult": 0,
            "rituals": 0,
            "technology": 0,
            "allies": 0,
            "ancestors": 0,
            "fate": 0,
            "fetish": 0,
            "kinfolk_rating": 0,
            "pure_breed": 0,
            "resources": 0,
            "rites": 0,
            "spirit_heritage": 0,
            "totem": 0,
            "rage": 1,
            "gnosis": 1,
        }
        self.url = self.fomor.get_update_url()

    def test_update_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_update_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "characters/werewolf/fomor/form.html")

    def test_update_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.fomor.refresh_from_db()
        self.assertEqual(self.fomor.name, "Fomor Updated")
        self.assertEqual(self.fomor.description, "Test")
