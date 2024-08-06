from characters.models.core import Character
from django.contrib.auth.models import User
from django.test import TestCase
from locations.models.core import City, LocationModel


# Create your tests here.
class TestLocation(TestCase):
    def setUp(self) -> None:
        self.location = LocationModel.objects.create(name="Location 1")
        self.child = LocationModel.objects.create(
            name="Location 2", parent=self.location
        )

    def test_location_parent(self):
        self.assertEqual(self.child.parent, self.location)
        self.assertIn(self.child, self.location.children.all())


class TestLocationDetailView(TestCase):
    def setUp(self) -> None:
        self.location = LocationModel.objects.create(name="Location 1")

    def test_location_detail_view_status_code(self):
        response = self.client.get(f"/locations/{self.location.id}/")
        self.assertEqual(response.status_code, 200)

    def test_location_detail_view_templates(self):
        response = self.client.get(f"/locations/{self.location.id}/")
        self.assertTemplateUsed(response, "locations/location/detail.html")


class TestCity(TestCase):
    """Manage Tests for City"""

    def test_add_character(self):
        city = City.objects.create(name="New York City", population=28000000)
        player = User.objects.create_user(username="User")
        char = Character.objects.create(name="NPC 1", owner=player)
        city.add_character(char)
        self.assertIn(char, city.characters.all())


class TestCityDetailView(TestCase):
    def setUp(self) -> None:
        self.location = City.objects.create(name="Test Location")

    def test_location_detail_view_status_code(self):
        response = self.client.get(f"/locations/{self.location.id}/")
        self.assertEqual(response.status_code, 200)

    def test_location_detail_view_templates(self):
        response = self.client.get(f"/locations/{self.location.id}/")
        self.assertTemplateUsed(response, "locations/city/detail.html")
