from characters.models.core import CharacterModel
from core.models import Model
from django.db import models
from django.urls import reverse
from locations.models.core import LocationModel

# Create your models here.


class ItemModel(Model):
    type = "item"

    owned_by = models.ForeignKey(
        CharacterModel, blank=True, null=True, on_delete=models.SET_NULL
    )
    located_at = models.ForeignKey(
        LocationModel, blank=True, null=True, on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def get_absolute_url(self):
        return reverse("items:item", args=[str(self.id)])

    def get_update_url(self):
        return reverse("items:update_item", args=[str(self.id)])

    def get_heading(self):
        return "wod_heading"


class Weapon(ItemModel):
    type = "weapon"

    class Meta:
        verbose_name = "Weapon"
        verbose_name_plural = "Weapons"

    difficulty = models.IntegerField(default=0)
    damage = models.IntegerField(default=0)
    damage_type = models.CharField(
        max_length=1,
        default="L",
        choices=[("B", "Bashing"), ("L", "Lethal"), ("A", "Aggravated")],
    )
    conceal = models.CharField(
        max_length=1,
        default="P",
        choices=[
            ("P", "Pocket"),
            ("J", "Jacket"),
            ("T", "Trenchcoat"),
            ("N", "Not Applicable"),
        ],
    )

    def get_update_url(self):
        return reverse("items:update_weapon", args=[str(self.id)])


class MeleeWeapon(Weapon):
    type = "melee_weapon"

    class Meta:
        verbose_name = "Melee Weapon"
        verbose_name_plural = "Melee Weapons"

    def get_update_url(self):
        return reverse("items:update_meleeweapon", args=[str(self.id)])


class ThrownWeapon(Weapon):
    type = "thrown_weapon"

    class Meta:
        verbose_name = "Thrown Weapon"
        verbose_name_plural = "Thrown Weapons"

    def get_update_url(self):
        return reverse("items:update_thrownweapon", args=[str(self.id)])


class RangedWeapon(Weapon):
    type = "ranged_weapon"

    range = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)
    clip = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Ranged Weapon"
        verbose_name_plural = "Ranged Weapons"

    def get_update_url(self):
        return reverse("items:update_rangedweapon", args=[str(self.id)])


class Medium(models.Model):
    """Class managing Medium data"""

    name = models.TextField(default="")
    length_modifier_type = models.CharField(
        max_length=1, default="/", blank=True, null=True
    )
    length_modifier = models.IntegerField(default=1, blank=True, null=True)

    class Meta:
        verbose_name = "Medium"
        verbose_name_plural = "Media"

    def get_absolute_url(self):
        return reverse("items:medium", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("items:update_medium", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name}"


class Material(models.Model):
    """Class managing Material data"""

    name = models.TextField(default="")
    is_hard = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materials"

    def get_absolute_url(self):
        return reverse("items:material", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("items:update_material", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name}"
