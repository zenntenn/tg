from django.test import TestCase
from django.urls import reverse
from items.models.core import (
    ItemModel,
    Material,
    Medium,
    MeleeWeapon,
    RangedWeapon,
    ThrownWeapon,
    Weapon,
)


# Create your tests here.
class TestItemDetailView(TestCase):
    def setUp(self) -> None:
        self.item = ItemModel.objects.create(name="Test Item")
        self.url = self.item.get_absolute_url()

    def test_object_detail_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_object_detail_view_templates(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/item/detail.html")


class TestItemCreateView(TestCase):
    def setUp(self):
        self.valid_data = {
            "name": "Test Item",
            "description": "A test description for the item.",
        }
        self.url = reverse("items:create_item")

    def test_create_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/item/form.html")

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
        self.assertTemplateUsed(response, "items/item/form.html")

    def test_update_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.item.refresh_from_db()
        self.assertEqual(self.item.name, "Test Item Updated")
        self.assertEqual(self.item.description, "A test description for the item.")


class TestWeaponDetailView(TestCase):
    def setUp(self) -> None:
        self.item = Weapon.objects.create(name="Test Weapon")
        self.url = self.item.get_absolute_url()

    def test_object_detail_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_object_detail_view_templates(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/weapon/detail.html")


class TestWeaponCreateView(TestCase):
    def setUp(self):
        self.valid_data = {
            "name": "Test Weapon",
            "description": "A test description for the weapon.",
            "difficulty": 6,
            "damage": 2,
            "damage_type": "L",
            "conceal": "P",
        }
        self.url = reverse("items:create_weapon")

    def test_create_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/weapon/form.html")

    def test_create_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Weapon.objects.count(), 1)
        self.assertEqual(Weapon.objects.first().name, "Test Weapon")


class TestWeaponUpdateView(TestCase):
    def setUp(self):
        self.item = Weapon.objects.create(
            name="Weapon 1",
            description="Test description",
        )
        self.valid_data = {
            "name": "Test Weapon 2",
            "description": "A test description for the weapon.",
            "difficulty": 6,
            "damage": 2,
            "damage_type": "L",
            "conceal": "P",
        }
        self.url = self.item.get_update_url()

    def test_update_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_update_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/weapon/form.html")

    def test_update_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.item.refresh_from_db()
        self.assertEqual(self.item.name, "Test Weapon 2")
        self.assertEqual(self.item.description, "A test description for the weapon.")


class TestMeleeWeaponDetailView(TestCase):
    def setUp(self) -> None:
        self.item = MeleeWeapon.objects.create(name="Test Weapon")
        self.url = self.item.get_absolute_url()

    def test_object_detail_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_object_detail_view_templates(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/meleeweapon/detail.html")


class TestMeleeWeaponCreateView(TestCase):
    def setUp(self):
        self.valid_data = {
            "name": "Test Weapon",
            "description": "A test description for the weapon.",
            "difficulty": 6,
            "damage": 2,
            "damage_type": "L",
            "conceal": "P",
        }
        self.url = reverse("items:create_meleeweapon")

    def test_create_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/meleeweapon/form.html")

    def test_create_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(MeleeWeapon.objects.count(), 1)
        self.assertEqual(MeleeWeapon.objects.first().name, "Test Weapon")


class TestMeleeWeaponUpdateView(TestCase):
    def setUp(self):
        self.item = MeleeWeapon.objects.create(
            name="Weapon 1",
            description="Test description",
        )
        self.valid_data = {
            "name": "Test Weapon 2",
            "description": "A test description for the weapon.",
            "difficulty": 6,
            "damage": 2,
            "damage_type": "L",
            "conceal": "P",
        }
        self.url = self.item.get_update_url()

    def test_update_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_update_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/meleeweapon/form.html")

    def test_update_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.item.refresh_from_db()
        self.assertEqual(self.item.name, "Test Weapon 2")
        self.assertEqual(self.item.description, "A test description for the weapon.")


class TestThrownWeaponDetailView(TestCase):
    def setUp(self) -> None:
        self.item = ThrownWeapon.objects.create(name="Test Weapon")
        self.url = self.item.get_absolute_url()

    def test_object_detail_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_object_detail_view_templates(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/thrownweapon/detail.html")


class TestThrownWeaponCreateView(TestCase):
    def setUp(self):
        self.valid_data = {
            "name": "Test Weapon",
            "description": "A test description for the weapon.",
            "difficulty": 6,
            "damage": 2,
            "damage_type": "L",
            "conceal": "P",
        }
        self.url = reverse("items:create_thrownweapon")

    def test_create_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/thrownweapon/form.html")

    def test_create_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ThrownWeapon.objects.count(), 1)
        self.assertEqual(ThrownWeapon.objects.first().name, "Test Weapon")


class TestThrownWeaponUpdateView(TestCase):
    def setUp(self):
        self.item = ThrownWeapon.objects.create(
            name="Weapon 1",
            description="Test description",
        )
        self.valid_data = {
            "name": "Test Weapon 2",
            "description": "A test description for the weapon.",
            "difficulty": 6,
            "damage": 2,
            "damage_type": "L",
            "conceal": "P",
        }
        self.url = self.item.get_update_url()

    def test_update_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_update_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/thrownweapon/form.html")

    def test_update_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.item.refresh_from_db()
        self.assertEqual(self.item.name, "Test Weapon 2")
        self.assertEqual(self.item.description, "A test description for the weapon.")


class TestRangedWeaponDetailView(TestCase):
    def setUp(self) -> None:
        self.item = RangedWeapon.objects.create(name="Test Weapon")
        self.url = self.item.get_absolute_url()

    def test_object_detail_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_object_detail_view_templates(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/rangedweapon/detail.html")


class TestRangedWeaponCreateView(TestCase):
    def setUp(self):
        self.valid_data = {
            "name": "Test Weapon",
            "description": "A test description for the weapon.",
            "difficulty": 6,
            "damage": 2,
            "damage_type": "L",
            "conceal": "P",
            "range": 100,
            "rate": 3,
            "clip": 17,
        }
        self.url = reverse("items:create_rangedweapon")

    def test_create_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/rangedweapon/form.html")

    def test_create_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(RangedWeapon.objects.count(), 1)
        self.assertEqual(RangedWeapon.objects.first().name, "Test Weapon")


class TestRangedWeaponUpdateView(TestCase):
    def setUp(self):
        self.item = RangedWeapon.objects.create(
            name="Weapon 1",
            description="Test description",
        )
        self.valid_data = {
            "name": "Test Weapon",
            "description": "A test description for the weapon.",
            "difficulty": 6,
            "damage": 2,
            "damage_type": "L",
            "conceal": "P",
            "range": 100,
            "rate": 3,
            "clip": 17,
        }
        self.url = self.item.get_update_url()

    def test_update_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_update_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/rangedweapon/form.html")

    def test_update_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.item.refresh_from_db()
        self.assertEqual(self.item.name, "Test Weapon 2")
        self.assertEqual(self.item.description, "A test description for the weapon.")


class TestMediumDetailView(TestCase):
    def setUp(self) -> None:
        self.medium = Medium.objects.create(
            name="Test Medium", length_modifier_type="/", length_modifier=4
        )
        self.url = self.medium.get_absolute_url()

    def test_medium_detail_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_medium_detail_view_templates(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/medium/detail.html")


class TestMediumCreateView(TestCase):
    def setUp(self):
        self.valid_data = {
            "name": "Test Medium",
            "length_modifier_type": "/",
            "length_modifier": 4,
        }
        self.url = reverse("items:create_medium")

    def test_create_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/medium/form.html")

    def test_create_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Medium.objects.count(), 1)
        self.assertEqual(Medium.objects.first().name, "Test Medium")


class TestMediumUpdateView(TestCase):
    def setUp(self):
        self.medium = Medium.objects.create(
            name="Test Medium", length_modifier_type="/", length_modifier=4
        )
        self.valid_data = {
            "name": "Test Medium 2",
            "length_modifier_type": "/",
            "length_modifier": 4,
        }
        self.url = self.medium.get_update_url()

    def test_update_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_update_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/medium/form.html")

    def test_update_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.medium.refresh_from_db()
        self.assertEqual(self.medium.name, "Test Medium 2")


class TestMaterialDetailView(TestCase):
    def setUp(self) -> None:
        self.material = Material.objects.create(name="Test Material")
        self.url = self.material.get_absolute_url()

    def test_material_detail_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_material_detail_view_templates(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/material/detail.html")


class TestMaterialCreateView(TestCase):
    def setUp(self):
        self.valid_data = {"name": "Test Material", "is_hard": True}
        self.url = reverse("items:create_material")

    def test_create_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/material/form.html")

    def test_create_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Material.objects.count(), 1)
        self.assertEqual(Material.objects.first().name, "Test Material")


class TestMaterialUpdateView(TestCase):
    def setUp(self):
        self.material = Material.objects.create(name="Test Material")
        self.valid_data = {"name": "Test Material Update", "is_hard": False}
        self.url = self.material.get_update_url()

    def test_update_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_update_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "items/material/form.html")

    def test_update_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.material.refresh_from_db()
        self.assertEqual(self.material.name, "Test Material Updated")
        self.assertFalse(self.material.is_hard)
