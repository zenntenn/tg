from django.db import models
from core.models import Model
from characters.models.core import CharacterModel

# Create your models here.
class LocationModel(Model):
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

    class Meta:
        verbose_name = "Location Model"
        verbose_name_plural = "Location Models"
