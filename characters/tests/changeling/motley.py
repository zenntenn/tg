from characters.models.changeling.changeling import Changeling
from characters.models.changeling.motley import Motley
from characters.tests.utils import changeling_setup
from core.utils import time_test
from django.contrib.auth.models import User
from django.test import TestCase


class TestMotley(TestCase):
    def setUp(self):
        self.player = User.objects.create_user(username="Player")
        changeling_setup()

    def test_motley_creation(self):
        motley = Motley.objects.create(name="Motley 1")
        motley.members.set(Changeling.objects.all())
        motley.leader = Changeling.objects.first()
        motley.save()
        self.assertEqual(motley.members.count(), 5)
        self.assertIsNotNone(motley.leader)

    def test_random(self):
        motley = Motley.objects.create(name="Motley 1")
        motley.random(num_chars=5, new_characters=False)
        self.assertEqual(motley.members.count(), 5)
        for changeling in Changeling.objects.all():
            self.assertIn(changeling, motley.members.all())
        motley = Motley.objects.create(name="Motley 2")
        motley.random(num_chars=5, new_characters=True)
        self.assertEqual(motley.members.count(), 5)

    def test_exception(self):
        motley = Motley.objects.create(name="Motley 10")
        with self.assertRaises(ValueError):
            motley.random(num_chars=10, new_characters=False)

    def test_str(self):
        motley = Motley.objects.create(name="Motley 1")
        self.assertEqual(str(motley), "Motley 1")

    def test_creation_time(self):
        self.assertLessEqual(time_test(Motley, self.player, character=True), 1.5)


class TestMotleyDetailView(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="User1", password="12345")
        self.motley = Motley.objects.create(name="Test Motley")

    def test_motley_detail_view_status_code(self):
        response = self.client.get(f"/characters/groups/{self.motley.id}/")
        self.assertEqual(response.status_code, 200)

    def test_motley_detail_view_templates(self):
        response = self.client.get(f"/characters/groups/{self.motley.id}/")
        self.assertTemplateUsed(response, "characters/changeling/motley/detail.html")


class TestMotleyCreateView(TestCase):
    def setUp(self):
        self.valid_data = {
            "name": "Motley",
            "description": "Test",
        }
        self.url = Motley.get_creation_url()

    def test_create_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "characters/changeling/motley/form.html")

    def test_create_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Motley.objects.count(), 1)
        self.assertEqual(Motley.objects.first().name, "Motley")


class TestMotleyUpdateView(TestCase):
    def setUp(self):
        self.motley = Motley.objects.create(
            name="Test Motley",
            description="Test description",
        )
        self.valid_data = {
            "name": "Motley Updated",
            "description": "Test",
        }
        self.url = self.motley.get_update_url()

    def test_update_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_update_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "characters/changeling/motley/form.html")

    def test_update_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.motley.refresh_from_db()
        self.assertEqual(self.motley.name, "Motley Updated")
        self.assertEqual(self.motley.description, "Test")
