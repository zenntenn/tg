from core.models import Model
from django.urls import reverse


# Create your models here.
class Derangement(Model):
    type = "derangement"

    class Meta:
        verbose_name = "Derangement"
        verbose_name_plural = "Derangements"

    def get_absolute_url(self):
        return reverse("characters:derangement", args=[str(self.id)])

    def get_update_url(self):
        return reverse("characters:update:derangement", args=[str(self.id)])

    def get_heading(self):
        return "wod_heading"
