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
    attribute = models.CharField(max_length=50)
    ability = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Rote"
        verbose_name_plural = "Rotes"

    def get_absolute_url(self):
        return reverse("characters:mage:rote", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("characters:mage:update:rote", kwargs={"pk": self.pk})

    def get_heading(self):
        return "mtas_heading"
