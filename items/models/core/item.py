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
        return reverse("items:update:item", args=[str(self.id)])

    def get_heading(self):
        return "wod_heading"

    def random_name(self, name=None):
        if self.has_name():
            return False
        if name is None:
            name = f"Random Item {ItemModel.objects.count()}"
        return self.set_name(name)
