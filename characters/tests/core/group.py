from characters.models.core import Group
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now


# Create your tests here.
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


class TestGroupCreateView(TestCase):
    def setUp(self):
        self.valid_data = {
            "name": "Test Group",
            "description": "test",
        }
        self.url = reverse("characters:create:group")

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
        response = self.client.get(f"/characters/groups/{self.group.id}/")
        self.assertTemplateUsed(response, "characters/core/group/detail.html")
