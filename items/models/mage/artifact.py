from characters.models.mage.effect import Effect
from django.db import models
from django.urls import reverse
from items.models.mage.wonder import Wonder


class Artifact(Wonder):
    type = "artifact"

    power = models.ForeignKey(Effect, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Artifact"
        verbose_name_plural = "Artifacts"

    def get_update_url(self):
        return reverse("items:mage:update:artifact", args=[str(self.id)])

    @classmethod
    def get_creation_url(cls):
        return reverse("items:mage:create:artifact")

    def set_power(self, power):
        self.power = power
        self.save()
        return True

    def has_power(self):
        return self.power is not None

    def random_power(self):
        e = Effect.objects.filter(max_sphere=self.rank).order_by("?").first()
        return self.set_power(e)

    def random(self, name=None, rank=None):
        super().random(rank=rank, name=name)
        self.random_power()
        self.quintessence_max = 5 * self.rank
        self.background_cost = 2 * self.rank
