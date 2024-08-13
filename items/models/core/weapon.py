from characters.models.core import CharacterModel
from core.models import Model
from django.db import models
from django.urls import reverse
from items.models.core.item import ItemModel
from locations.models.core import LocationModel


# Create your models here.
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
        return reverse("items:update:weapon", args=[str(self.id)])