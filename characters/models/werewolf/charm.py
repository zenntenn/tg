from core.models import Model
from django.db import models
from django.urls import reverse


class SpiritCharm(Model):
    type = "spirit_charm"

    class Meta:
        verbose_name = "Spirit Charm"
        verbose_name_plural = "Spirit Charms"

    def get_absolute_url(self):
        return reverse("characters:werewolf:charm", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("characters:werewolf:update:charm", kwargs={"pk": self.pk})

    def get_heading(self):
        return "wta_heading"
