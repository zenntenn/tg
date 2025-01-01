from characters.models.core import Ability, Attribute
from characters.models.mage.effect import Effect
from characters.models.mage.focus import Practice
from core.models import Model
from django.db import models
from django.urls import reverse


class Rote(Model):
    type = "rote"

    effect = models.ForeignKey(Effect, on_delete=models.SET_NULL, null=True)
    practice = models.ForeignKey(
        Practice, on_delete=models.SET_NULL, null=True, blank=True
    )
    attribute = models.ForeignKey(Attribute, on_delete=models.SET_NULL, null=True)
    ability = models.ForeignKey(Ability, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Rote"
        verbose_name_plural = "Rotes"
        ordering = ["practice", "name"]

    def get_absolute_url(self):
        return reverse("characters:mage:rote", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("characters:mage:update:rote", kwargs={"pk": self.pk})

    @classmethod
    def get_creation_url(cls):
        return reverse("characters:mage:create:rote")

    def get_heading(self):
        return "mta_heading"
