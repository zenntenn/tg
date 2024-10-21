from core.models import Model
from django.db import models
from django.urls import reverse


class Gift(Model):
    type = "gift"

    rank = models.IntegerField(default=0)
    allowed = models.JSONField(default=dict)

    class Meta:
        verbose_name = "Gift"
        verbose_name_plural = "Gifts"

    def save(self, *args, **kwargs):
        if "werewolf" not in self.allowed:
            self.allowed["werewolf"] = []
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("characters:werewolf:gift", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("characters:werewolf:update:gift", kwargs={"pk": self.pk})

    @classmethod
    def get_creation_url(cls):
        return reverse("characters:werewolf:create:gift")

    def get_heading(self):
        return "wta_heading"
