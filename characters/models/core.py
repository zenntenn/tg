from django.db import models
from core.models import Model


# Create your models here.
class CharacterModel(Model):
    npc = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Character Model"
        verbose_name_plural = "Character Models"
