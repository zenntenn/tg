from django.test import TestCase
from locations.models.core import LocationModel


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
        self.assertTemplateUsed(response, "locations/detail.html")
