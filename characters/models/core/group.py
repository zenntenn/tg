from characters.models.core.human import Human
from core.models import Model
from django.db import models
from django.urls import reverse


# Create your models here.
class Group(Model):
    type = "group"

    members = models.ManyToManyField(Human, blank=True)
    leader = models.ForeignKey(
        Human,
        blank=True,
        related_name="leads_group",
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    def get_absolute_url(self):
        return reverse("characters:group", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("characters:update:group", kwargs={"pk": self.pk})

    @classmethod
    def get_creation_url(cls):
        return reverse("characters:create:group")
