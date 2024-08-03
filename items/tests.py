from django.test import TestCase
from items.models.core import ItemModel, Weapon


# Create your tests here.
class TestItemDetailView(TestCase):
    def setUp(self) -> None:
        self.item = ItemModel.objects.create(name="Test Item")

    def test_object_detail_view_status_code(self):
        response = self.client.get(f"/items/{self.item.id}/")
        self.assertEqual(response.status_code, 200)

    def test_object_detail_view_templates(self):
        response = self.client.get(f"/items/{self.item.id}/")
        self.assertTemplateUsed(response, "items/detail.html")


class TestWeaponDetailView(TestCase):
    def setUp(self) -> None:
        self.item = Weapon.objects.create(name="Test Weapon")

    def test_object_detail_view_status_code(self):
        response = self.client.get(f"/items/{self.item.id}/")
        self.assertEqual(response.status_code, 200)

    def test_object_detail_view_templates(self):
        response = self.client.get(f"/items/{self.item.id}/")
        self.assertTemplateUsed(response, "items/weapon/detail.html")
