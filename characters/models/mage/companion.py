from collections import defaultdict

from characters.models.mage.faction import MageFaction
from characters.models.mage.mage import Mage
from characters.models.mage.mtahuman import MtAHuman
from characters.models.werewolf.charm import SpiritCharm
from core.models import Model, Number
from django.db import models


class Advantage(Model):
    type = "advantage"

    ratings = models.ManyToManyField(Number, blank=True)
    max_rating = models.IntegerField(default=0)
    min_rating = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Special Advantage"
        verbose_name_plural = "Special Advantage"
        ordering = ["name"]

    def update_max_rating(self):
        if self.ratings.all().count() == 0:
            self.max_rating = 0
        else:
            self.max_rating = max(self.ratings.all().values_list("value", flat=True))
        self.save()

    def update_min_rating(self):
        if self.ratings.all().count() == 0:
            self.min_rating = 0
        else:
            self.min_rating = min(self.ratings.all().values_list("value", flat=True))
        self.save()

    def get_ratings(self):
        tmp = list(self.ratings.all().values_list("value", flat=True))
        tmp.sort()
        return tmp

    def add_rating(self, number):
        n = Number.objects.get_or_create(value=number)[0]
        self.ratings.add(n)
        self.update_max_rating()
        self.update_min_rating()

    def add_ratings(self, num_list):
        for x in num_list:
            self.add_rating(x)


class Companion(MtAHuman):
    type = "companion"

    gameline = "mta"

    affiliation = models.ForeignKey(
        MageFaction,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="companion_affiliations",
    )
    faction = models.ForeignKey(
        MageFaction,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="companion_factions",
    )
    subfaction = models.ForeignKey(
        MageFaction,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="companion_subfactions",
    )

    companion_type = models.CharField(
        max_length=20,
        choices=[
            ("companion", "Companion"),
            ("familiar", "Familiar"),
        ],
        default="companion",
    )

    companion_of = models.ForeignKey(
        Mage, blank=True, null=True, on_delete=models.SET_NULL
    )

    advantages = models.ManyToManyField(
        Advantage, blank=True, through="AdvantageRating", related_name="advantaged"
    )

    background_points = 5
    essence = models.IntegerField(default=0)
    rage = models.IntegerField(default=0)
    charms = models.ManyToManyField(SpiritCharm, blank=True)

    class Meta:
        verbose_name = "Companion"
        verbose_name_plural = "Companion"

    def get_heading(self):
        return "mta_heading"

    def freebie_cost(self, trait):
        cost = super().freebie_cost(trait)
        if cost != 10000:
            return cost
        costs = defaultdict(
            lambda: 10000,
            {
                "advantage": "rating",
                "charms": 1,
            },
        )
        return costs[trait]

    def add_advantage(self, advantage, rating):
        if rating in advantage.get_ratings():
            ar, _ = AdvantageRating.objects.get_or_create(
                character=self, advantage=advantage
            )
            ar.rating = rating
            ar.save()
            return True
        return False

    def get_advantage_and_rating_list(self):
        return [(x.name, self.advantage_rating(x)) for x in self.advantages.all()]

    def advantage_rating(self, advantage):
        if advantage not in self.advantages.all():
            return 0
        return AdvantageRating.objects.get(character=self, advantage=advantage).rating

    def add_charm(self, trait):
        if trait in self.charms.all():
            return False
        self.charms.add(trait)
        return True


class AdvantageRating(models.Model):
    character = models.ForeignKey(Companion, on_delete=models.SET_NULL, null=True)
    advantage = models.ForeignKey(Advantage, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Advantage Rating"
        verbose_name_plural = "Advantage Ratings"

    def __str__(self):
        return f"{self.advantage}: {self.rating}"