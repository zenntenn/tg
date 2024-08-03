from django.utils.timezone import now
from django.test import TestCase
from django.contrib.auth.models import User

from characters.models.core import Character, Human


# Create your tests here.
class TestCharacter(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="User1", password="12345")
        self.character = Character.objects.create(owner=self.player, name="")

    def test_has_name(self):
        self.assertFalse(self.character.has_name())
        self.character.set_name("Test")
        self.assertTrue(self.character.has_name())

    def test_set_name(self):
        self.assertEqual(self.character.name, "")
        self.assertTrue(self.character.set_name("Test"))
        self.assertNotEqual(self.character.name, "")

    def test_has_concept(self):
        self.assertFalse(self.character.has_concept())
        self.character.set_concept("Test")
        self.assertTrue(self.character.has_concept())

    def test_set_concept(self):
        self.assertEqual(self.character.concept, "")
        self.assertTrue(self.character.set_concept("Test"))
        self.assertNotEqual(self.character.concept, "")

    def test_absolute_url(self):
        self.assertEqual(
            self.character.get_absolute_url(), f"/characters/{self.character.id}/"
        )


class TestHuman(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username="Test")
        self.character = Human.objects.create(name="", owner=self.user)

    def test_add_willpower(self):
        self.assertEqual(self.character.willpower, 3)
        self.assertTrue(self.character.add_willpower())
        self.assertEqual(self.character.willpower, 4)

    def test_has_finishing_touches(self):
        self.assertFalse(self.character.has_finishing_touches())
        self.character.age = 18
        self.assertFalse(self.character.has_finishing_touches())
        self.character.date_of_birth = now()
        self.assertFalse(self.character.has_finishing_touches())
        self.character.hair = "Black"
        self.assertFalse(self.character.has_finishing_touches())
        self.character.eyes = "Brown"
        self.assertFalse(self.character.has_finishing_touches())
        self.character.ethnicity = "White"
        self.assertFalse(self.character.has_finishing_touches())
        self.character.nationality = "American"
        self.assertFalse(self.character.has_finishing_touches())
        self.character.height = "5'11\""
        self.assertFalse(self.character.has_finishing_touches())
        self.character.weight = "150 lbs"
        self.assertFalse(self.character.has_finishing_touches())
        self.character.sex = "Male"
        self.assertFalse(self.character.has_finishing_touches())
        self.character.description = "Hardcore Asshole"
        self.assertFalse(self.character.has_finishing_touches())
        self.character.apparent_age = 18
        self.assertTrue(self.character.has_finishing_touches())

    def test_has_history(self):
        self.assertFalse(self.character.has_history())
        self.character.childhood = "Was a kid, it sucked."
        self.assertFalse(self.character.has_history())
        self.character.history = "Got older."
        self.assertFalse(self.character.has_history())
        self.character.goals = "Get older still."
        self.assertTrue(self.character.has_history())

    def test_static_numbers(self):
        self.assertEqual(self.character.willpower, 3)
        self.assertEqual(self.character.background_points, 5)
        self.assertEqual(self.character.freebies, 15)

    def test_add_damage(self):
        self.assertEqual(self.character.get_wound_penalty(), 0)
        self.character.add_bashing()
        self.assertEqual(self.character.get_wound_penalty(), 0)
        self.character.add_aggravated()
        self.assertEqual(self.character.current_health_levels, "AB")
        self.assertEqual(self.character.get_wound_penalty(), -1)
        self.character.add_lethal()
        self.assertEqual(self.character.current_health_levels, "ALB")
        self.assertEqual(self.character.get_wound_penalty(), -1)
        self.character.add_bashing()
        self.assertEqual(self.character.get_wound_penalty(), -2)
        self.character.add_bashing()
        self.assertEqual(self.character.get_wound_penalty(), -2)
        self.character.add_bashing()
        self.assertEqual(self.character.get_wound_penalty(), -5)
        self.character.add_bashing()
        self.assertEqual(self.character.current_health_levels, "ALBBBBB")
        self.character.add_bashing()
        self.assertEqual(self.character.current_health_levels, "ALLBBBB")
        self.character.add_aggravated()
        self.assertEqual(self.character.get_wound_penalty(), -1000)


class TestHumanDetailView(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="Test")
        self.human = Human.objects.create(name="Test Human", owner=self.player)

    def test_human_detail_view_status_code(self):
        response = self.client.get(f"/characters/{self.human.id}/")
        self.assertEqual(response.status_code, 200)

    def test_mage_detail_view_templates(self):
        response = self.client.get(f"/characters/{self.human.id}/")
        self.assertTemplateUsed(response, "characters/human/detail.html")


class TestGenericCharacterDetailViews(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="Test")
        self.character = Character.objects.create(
            name="Test Character", owner=self.player
        )
        self.human = Human.objects.create(name="Test Human", owner=self.player)

    def test_character_detail_view_templates(self):
        response = self.client.get(f"/characters/{self.character.id}/")
        self.assertTemplateUsed(response, "characters/character/detail.html")
        response = self.client.get(f"/characters/{self.human.id}/")
        self.assertTemplateUsed(response, "characters/human/detail.html")
