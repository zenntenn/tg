from characters.models.core import CharacterModel
from core.models import Model
from django.db import models
from django.urls import reverse
from locations.models.core import LocationModel

# Create your models here.


class Material(models.Model):
    type = "material"

    name = models.TextField(default="")
    is_hard = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materials"

    def get_absolute_url(self):
        return reverse("items:material", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("items:update:material", kwargs={"pk": self.pk})

    @classmethod
    def get_creation_url(cls):
        return reverse("items:create:material")

    def __str__(self):
        return f"{self.name}"
