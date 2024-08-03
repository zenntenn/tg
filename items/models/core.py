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
        return reverse("wod:items:human:update_weapon", args=[str(self.id)])


class MeleeWeapon(Weapon):
    type = "melee_weapon"

    class Meta:
        verbose_name = "Melee Weapon"
        verbose_name_plural = "Melee Weapons"
