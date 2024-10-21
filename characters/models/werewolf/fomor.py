import random

from characters.models.werewolf.fomoripower import FomoriPower
from characters.models.werewolf.wtahuman import WtAHuman
from django.db import models
from django.urls import reverse


class Fomor(WtAHuman):
    type = "fomor"

    rage = models.IntegerField(default=0)
    gnosis = models.IntegerField(default=0)
    powers = models.ManyToManyField(FomoriPower, blank=True)

    allowed_backgrounds = ["allies", "contacts", "resources"]

    background_points = 3

    class Meta:
        verbose_name = "Fomor"
        verbose_name_plural = "Fomori"

    def add_power(self, power):
        self.powers.add(power)
        return True

    def filter_powers(self):
        return FomoriPower.objects.exclude(pk__in=self.powers.all())

    def random_power(self):
        options = self.filter_powers()
        return self.add_power(random.choice(options))

    def random_powers(self, num_powers=2):
        while self.powers.count() < num_powers:
            self.random_power()
        choice = (
            FomoriPower.objects.filter(
                name__in=["Armored Skin", "Berserker", "Gifted Fomor"]
            )
            .exclude(pk__in=self.powers.all())
            .order_by("?")
            .first()
        )
        self.add_power(choice)
        self.add_power(FomoriPower.objects.get(name="Immunity to the Delirium"))

    def random(self, freebies=15, xp=0, ethnicity=None):
        self.update_status("Ran")
        self.willpower = 3
        self.freebies = freebies
        self.xp = xp
        self.random_name(ethnicity=ethnicity)
        self.random_concept()
        self.random_archetypes()
        self.random_attributes(primary=6, secondary=4, tertiary=3)
        self.random_abilities(primary=11, secondary=7, tertiary=3)
        self.random_backgrounds()
        self.random_powers(num_powers=random.randint(1, 3))
        self.random_history()
        self.random_finishing_touches()
        self.mf_based_corrections()
        self.random_specialties()
        self.save()
