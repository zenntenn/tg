from characters.models.core import CharacterModel
from core.models import Model
from django.db import models
from django.urls import reverse


# Create your models here.
class LocationModel(Model):
    type = "location"

    parent = models.ForeignKey(
        "LocationModel",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="children",
    )
    owned_by = models.ForeignKey(
        CharacterModel, blank=True, null=True, on_delete=models.SET_NULL
    )

    gauntlet = models.IntegerField(default=7)
    shroud = models.IntegerField(default=7)
    dimension_barrier = models.IntegerField(default=6)
    reality_zone = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Location"

    def get_absolute_url(self):
        return reverse("locations:location", args=[str(self.id)])

    def get_update_url(self):
        return reverse("locations:update:location", args=[str(self.id)])

    def get_heading(self):
        return "wod_heading"
