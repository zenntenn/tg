from characters.models.core import Group
from characters.models.core.human import Human
from characters.models.core.specialty import Specialty
from characters.tests.utils import human_setup
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now


class TestGroupDetailView(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="User1", password="12345")
        self.group = Group.objects.create(name="Test Group")
        self.url = self.group.get_absolute_url()

    def test_group_detail_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_group_detail_view_templates(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "characters/core/group/detail.html")


class TestRandomGroup(TestCase):
    def setUp(self):
        human_setup()
        self.group = Group.objects.create()
        for key in list(Human().get_abilities().keys()) + list(
            Human().get_attributes().keys()
        ):
            for i in range(5):
                Specialty.objects.create(name=f"{key.title()} Specialty {i}", stat=key)

    def test_random_name(self):
        self.group.random_name()
        self.assertTrue(self.group.name.startswith("Random Group"))

    def test_random(self):
        self.group.random(
            num_chars=5, new_characters=True, random_names=True, freebies=15, xp=0
        )
        self.assertEqual(self.group.members.count(), 5)
        self.assertIsNotNone(self.group.leader)
        self.assertIn(self.group.leader, self.group.members.all())


class TestGroupCreateView(TestCase):
    def setUp(self):
        self.valid_data = {
            "name": "Test Group",
            "description": "test",
        }
        self.url = Group.get_creation_url()

    def test_create_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "characters/core/group/form.html")

    def test_create_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Group.objects.count(), 1)
        self.assertEqual(Group.objects.first().name, "Test Group")


class TestGroupUpdateView(TestCase):
    def setUp(self):
        self.player = User.objects.create_user(username="User1", password="12345")
        self.group = Group.objects.create(name="Test Group")
        self.valid_data = {"name": "Test Group Updated", "description": "Test"}
        self.url = self.group.get_update_url()

    def test_update_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_update_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "characters/core/group/form.html")

    def test_update_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.group.refresh_from_db()
        self.assertEqual(self.group.name, "Test Group Updated")


class TestGenericGroupDetailView(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="Test")
        self.group = Group.objects.create(name="Group Test")

    def test_generic_group_detail_view_templates(self):
        response = self.client.get(self.group.get_absolute_url())
        self.assertTemplateUsed(response, "characters/core/group/detail.html")
