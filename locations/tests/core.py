from characters.models.core import Character
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
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
        self.location = LocationModel.objects.create(
            name="Location 1", description="Test description", reality_zone="Test RZ"
        )
        self.url = self.location.get_absolute_url()

    def test_location_detail_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_location_detail_view_templates(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "locations/location/detail.html")

    def test_detail_view_content(self):
        response = self.client.get(self.url)
        self.assertContains(response, self.location.name)
        self.assertContains(response, self.location.description)
        self.assertContains(response, self.location.gauntlet)
        self.assertContains(response, self.location.reality_zone)


class TestLocationCreateView(TestCase):
    def setUp(self):
        self.valid_data = {
            "name": "Test Name",
            "description": "Test Description",
            "reality_zone": "Test RZ",
            "gauntlet": 6,
            "shroud": 5,
            "dimension_barrier": 5,
        }
        self.invalid_data = {"name": "", "description": ""}
        self.url = reverse("locations:create:location")

    def test_create_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "locations/location/form.html")

    def test_create_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(LocationModel.objects.count(), 1)
        self.assertEqual(LocationModel.objects.first().name, "Test Name")


class TestLocationUpdateView(TestCase):
    def setUp(self):
        self.location = LocationModel.objects.create(
            name="Location 1", description="Test description", reality_zone="Test RZ"
        )
        self.valid_data = {
            "name": "Test Name Updated",
            "description": "Test Description Updated",
            "reality_zone": "Test RZ Updated",
            "gauntlet": 6,
            "shroud": 5,
            "dimension_barrier": 5,
        }
        self.url = self.location.get_update_url()

    def test_update_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_update_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "locations/location/form.html")

    def test_update_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.location.refresh_from_db()
        self.assertEqual(self.location.name, "Test Name Updated")
        self.assertEqual(self.location.description, "Test Description Updated")


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
        self.url = self.location.get_absolute_url()

    def test_location_detail_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_location_detail_view_templates(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "locations/city/detail.html")


class TestCityCreateView(TestCase):
    def setUp(self):
        self.valid_data = {
            "name": "Test City",
            "description": "A test description for the city.",
            "status": "App",
            "gauntlet": 6,
            "shroud": 5,
            "dimension_barrier": 5,
            "reality_zone": "Reality Zone",
            "population": 800000,
            "mood": "None",
            "theme": "Test theme",
            "media": "Only National",
            "politicians": "White dudes",
        }
        self.url = reverse("locations:create:city")

    def test_create_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "locations/city/form.html")

    def test_create_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(City.objects.count(), 1)
        self.assertEqual(City.objects.first().name, "Test City")


class TestCityUpdateView(TestCase):
    def setUp(self):
        self.location = City.objects.create(
            name="Location 1",
            description="Test description",
            reality_zone="Test RZ",
            population=10000,
        )
        self.valid_data = {
            "name": "Test City Updated",
            "description": "A test description for the city.",
            "status": "App",
            "gauntlet": 6,
            "shroud": 5,
            "dimension_barrier": 5,
            "reality_zone": "Reality Zone",
            "population": 2,
            "mood": "None",
            "theme": "Test theme",
            "media": "Only National",
            "politicians": "White dudes",
        }
        self.url = self.location.get_update_url()

    def test_update_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_update_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "locations/city/form.html")

    def test_update_view_successful_post(self):
        self.assertEqual(self.location.population, 10000)
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.location.refresh_from_db()
        self.assertEqual(self.location.name, "Test City Updated")
        self.assertEqual(self.location.description, "A test description for the city.")
        self.assertEqual(self.location.population, 2)
