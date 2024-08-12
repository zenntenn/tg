from core.models import Model
from django.urls import reverse


# Create your models here.
class Archetype(Model):
    type = "archetype"

    class Meta:
        verbose_name = "Archetype"
        verbose_name_plural = "Archetypes"

    def get_absolute_url(self):
        return reverse("characters:archetype", kwargs={"pk": self.pk})

    def get_heading(self):
        return "wod_heading"

    def get_update_url(self):
        return reverse("characters:update:archetype", kwargs={"pk": self.pk})
