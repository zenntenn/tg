from django.test import TestCase
from django.urls import reverse
from items.models.core import ItemModel


# Create your tests here.
class TestRandomItem(TestCase):
    def test_random_name(self):
        # create an item without a name
        item = ItemModel.objects.create()

        # call random_name method
        item.random_name()

        # assert that the item has a name now
        self.assertTrue(item.has_name())

        # assert that the name is in the correct format
        self.assertTrue(item.name.startswith("Random Item "))


class TestItemDetailView(TestCase):
    def setUp(self) -> None:
        self.item = ItemModel.objects.create(name="Test Item")
        self.url = self.item.get_absolute_url()

    def test_object_detail_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_object_detail_view_templates(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/core/item/detail.html")


class TestItemCreateView(TestCase):
    def setUp(self):
        self.valid_data = {
            "name": "Test Item",
            "description": "A test description for the item.",
        }
        self.url = reverse("items:create:item")

    def test_create_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/core/item/form.html")

    def test_create_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ItemModel.objects.count(), 1)
        self.assertEqual(ItemModel.objects.first().name, "Test Item")


class TestItemUpdateView(TestCase):
    def setUp(self):
        self.item = ItemModel.objects.create(
            name="Test Item",
            description="Test description",
        )
        self.valid_data = {
            "name": "Test Item Updated",
            "description": "A test description for the item.",
        }
        self.url = self.item.get_update_url()

    def test_update_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_update_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/core/item/form.html")

    def test_update_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.item.refresh_from_db()
        self.assertEqual(self.item.name, "Test Item Updated")
        self.assertEqual(self.item.description, "A test description for the item.")
