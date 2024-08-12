from characters.models.core import (
    Archetype,
    Derangement,
    Human,
    MeritFlaw,
    MeritFlawRating,
)
from core.models import Number
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now
from game.models import ObjectType


# Create your tests here.
class TestHuman(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username="Test")
        self.character = Human.objects.create(name="", owner=self.user)
        for i in range(10):
            Archetype.objects.create(name=f"Archetype {i}")

        for i in [1, 2, 3, 4, 5, 6]:
            Number.objects.create(value=i)
            Number.objects.create(value=-i)

        human = ObjectType.objects.create(
            name=self.character.type, type="char", gameline="wod"
        )

        for i in range(1, 6):
            mf = MeritFlaw.objects.create(name=f"Merit {i}")
            mf.allowed_types.add(human)
            mf.add_rating(i)
            mf = MeritFlaw.objects.create(name=f"Flaw {i}")
            mf.allowed_types.add(human)
            mf.add_rating(-i)

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

    def test_has_archetypes(self):
        self.assertFalse(self.character.has_archetypes())
        self.character.nature = Archetype.objects.first()
        self.character.demeanor = Archetype.objects.first()
        self.assertTrue(self.character.has_archetypes())

    def test_set_archetypes(self):
        self.assertFalse(self.character.has_archetypes())
        self.assertTrue(
            self.character.set_archetypes(
                Archetype.objects.first(), Archetype.objects.first()
            )
        )
        self.assertTrue(self.character.has_archetypes())

    def test_add_mf(self):
        m3 = MeritFlaw.objects.get(name="Merit 3")
        self.assertEqual(self.character.merits_and_flaws.count(), 0)
        self.assertTrue(self.character.add_mf(m3, 3))
        self.assertEqual(self.character.merits_and_flaws.count(), 1)
        self.assertIn(m3, self.character.merits_and_flaws.all())

    def test_has_max_flaws(self):
        self.assertFalse(self.character.has_max_flaws())
        self.character.add_mf(MeritFlaw.objects.get(name="Flaw 3"), -3)
        self.assertFalse(self.character.has_max_flaws())
        self.character.add_mf(MeritFlaw.objects.get(name="Flaw 4"), -4)
        self.assertTrue(self.character.has_max_flaws())

    def test_filter_mfs(self):
        self.assertEqual(len(self.character.filter_mfs()), 10)
        self.character.add_mf(MeritFlaw.objects.get(name="Merit 1"), 1)
        self.assertEqual(len(self.character.filter_mfs()), 9)
        self.character.add_mf(MeritFlaw.objects.get(name="Merit 2"), 2)
        self.assertEqual(len(self.character.filter_mfs()), 8)
        self.character.add_mf(MeritFlaw.objects.get(name="Flaw 2"), -2)
        self.assertEqual(len(self.character.filter_mfs()), 7)
        self.character.add_mf(MeritFlaw.objects.get(name="Flaw 5"), -5)
        self.assertEqual(len(self.character.filter_mfs()), 3)
        m = MeritFlaw.objects.create(name="Test Merit")
        m.add_ratings([1, 2, 3])
        self.assertNotIn(m, self.character.filter_mfs())
        m.allowed_types.add(ObjectType.objects.get(name="human"))
        self.assertIn(m, self.character.filter_mfs())

    def test_total_merits(self):
        self.assertEqual(self.character.total_merits(), 0)
        self.character.add_mf(MeritFlaw.objects.get(name="Merit 3"), 3)
        self.assertEqual(self.character.total_merits(), 3)
        self.character.add_mf(MeritFlaw.objects.get(name="Flaw 3"), -3)
        self.assertEqual(self.character.total_merits(), 3)

    def test_total_flaws(self):
        self.assertEqual(self.character.total_flaws(), 0)
        self.character.add_mf(MeritFlaw.objects.get(name="Flaw 3"), -3)
        self.assertEqual(self.character.total_flaws(), -3)
        self.character.add_mf(MeritFlaw.objects.get(name="Merit 3"), 3)
        self.assertEqual(self.character.total_flaws(), -3)

    def test_mf_rating(self):
        mf = MeritFlaw.objects.create(name="Test Merit Flaw")
        mf.add_ratings([-2, -1])
        MeritFlawRating.objects.create(character=self.character, mf=mf, rating=-2)
        self.assertEqual(self.character.mf_rating(mf), -2)

    def test_add_derangement(self):
        d = Derangement.objects.create(name="Test Derangement")
        self.assertTrue(self.character.add_derangement(d))
        self.assertFalse(self.character.add_derangement(d))


class TestHumanDetailView(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="Test")
        self.human = Human.objects.create(name="Test Human", owner=self.player)
        self.url = self.human.get_absolute_url()

    def test_human_detail_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_mage_detail_view_templates(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "characters/core/human/detail.html")


class TestHumanCreateView(TestCase):
    def setUp(self):
        self.player = User.objects.create_user(username="Test")
        self.valid_data = {
            "name": "Test Human",
            "owner": self.player.id,
            "description": "Test",
            "willpower": 3,
            "childhood": "Test",
            "history": "Test",
            "goals": "Test",
            "notes": "Test",
        }
        self.url = reverse("characters:create:human")

    def test_create_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "characters/core/human/form.html")

    def test_create_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Human.objects.count(), 1)
        self.assertEqual(Human.objects.first().name, "Test Human")


class TestHumanUpdateView(TestCase):
    def setUp(self):
        self.player = User.objects.create_user(username="Test")
        self.human = Human.objects.create(
            name="Test Human",
            owner=self.player,
        )
        self.valid_data = {
            "name": "Test Human Updated",
            "owner": self.player.id,
            "description": "Test",
            "willpower": 3,
            "childhood": "Test",
            "history": "Test",
            "goals": "Test",
            "notes": "Test",
        }
        self.url = self.human.get_update_url()

    def test_update_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_update_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "characters/core/human/form.html")

    def test_update_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.human.refresh_from_db()
        self.assertEqual(self.human.name, "Test Human Updated")
