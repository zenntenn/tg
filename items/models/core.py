from django.db import models
from core.models import Model
from characters.models.core import CharacterModel

# Create your models here.

class ItemModel(Model):
    owned_by = models.ForeignKey(
        CharacterModel, blank=True, null=True, on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = "Item Model"
        verbose_name_plural = "Item Models"
