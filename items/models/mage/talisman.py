import random

from characters.models.mage.effect import Effect
from django.db import models
from django.urls import reverse
from items.models.mage.wonder import Wonder


class Talisman(Wonder):
    type = "talisman"

    arete = models.IntegerField(default=0)
    powers = models.ManyToManyField(Effect, blank=True)

    class Meta:
        verbose_name = "Talisman"
        verbose_name_plural = "Talismans"

    def get_update_url(self):
        return reverse("items:mage:update:talisman", args=[str(self.id)])

    def add_power(self, power):
        self.powers.add(power)
        return True

    def has_powers(self):
        return self.powers.count() == self.rank

    def random_power(self, rank):
        e = Effect.objects.filter(max_sphere=rank).order_by("?").first()
        return self.add_power(e)

    def random_powers(self):
        self.random_power(self.rank)
        while not self.has_powers():
            self.random_power(random.randint(1, self.rank))

    def random(self, name=None, rank=None):
        super().random(rank=rank, name=name)
        self.random_powers()
        self.quintessence_max = 5 * self.rank
        self.background_cost = 2 * self.rank
        self.arete = self.rank
        while random.random() < 0.3:
            self.arete += 1
            self.background_cost += 1
            self.quintessence_max += 5
