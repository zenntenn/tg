from core.models import Model
from django.db import models
from django.urls import reverse


class Tribe(Model):
    type = "tribe"

    willpower = models.IntegerField(default=3)

    class Meta:
        verbose_name = "Tribe"
        verbose_name_plural = "Tribes"

    def get_absolute_url(self):
        return reverse("characters:werewolf:tribe", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("characters:werewolf:update:tribe", kwargs={"pk": self.pk})

    @classmethod
    def get_creation_url(cls):
        return reverse("characters:werewolf:create:tribe")

    def get_heading(self):
        return "wta_heading"
