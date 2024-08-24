import random

from characters.models.mage.resonance import Resonance
from core.utils import fast_selector
from django.db import models
from django.urls import reverse
from items.models.core import ItemModel


# Create your models here.
class WonderResonanceRating(models.Model):
    class Meta:
        verbose_name = "Wonder Resonance Rating"
        verbose_name_plural = "Wonder Resonance Ratings"

    wonder = models.ForeignKey("Wonder", on_delete=models.SET_NULL, null=True)
    resonance = models.ForeignKey(
        "characters.Resonance", on_delete=models.SET_NULL, null=True
    )
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.resonance}: {self.rating}"


class Wonder(ItemModel):
    type = "wonder"

    rank = models.IntegerField(default=0)
    background_cost = models.IntegerField(default=0)
    quintessence_max = models.IntegerField(default=0)

    resonance = models.ManyToManyField(
        "characters.Resonance", blank=True, through=WonderResonanceRating
    )

    class Meta:
        verbose_name = "Wonder"
        verbose_name_plural = "Wonders"

    def get_update_url(self):
        return reverse("items:mage:update:wonder", args=[str(self.id)])

    @classmethod
    def get_creation_url(cls):
        return reverse("items:mage:create:wonder")

    def get_heading(self):
        return "mta_heading"

    def set_rank(self, rank):
        self.rank = rank
        return True

    def has_rank(self):
        return self.rank != 0

    def add_resonance(self, resonance):
        r, _ = WonderResonanceRating.objects.get_or_create(
            resonance=resonance, wonder=self
        )
        if r.rating == 5:
            return False
        r.rating += 1
        r.save()
        return True

    def resonance_rating(self, resonance):
        if resonance in self.resonance.all():
            return WonderResonanceRating.objects.get(
                wonder=self, resonance=resonance
            ).rating
        return 0

    def filter_resonance(self, minimum=0, maximum=5):
        all_res = Resonance.objects.all()

        maxed_resonance = [
            x.resonance.id
            for x in WonderResonanceRating.objects.filter(
                wonder=self, rating__gt=maximum
            )
        ]
        mined_resonance = [
            x.resonance.id
            for x in WonderResonanceRating.objects.filter(
                wonder=self, rating__lt=minimum
            )
        ]
        all_res = all_res.exclude(pk__in=maxed_resonance)
        all_res = all_res.exclude(pk__in=mined_resonance)
        if minimum > 0:
            all_res = all_res.filter(
                pk__in=[
                    x.resonance.id
                    for x in WonderResonanceRating.objects.filter(
                        wonder=self, rating__gt=0
                    )
                ]
            )
        return all_res

    def total_resonance(self):
        return sum(x.rating for x in WonderResonanceRating.objects.filter(wonder=self))

    def has_resonance(self):
        return self.total_resonance() >= self.rank

    def random_points(self):
        return 3 * (self.rank - 1) + random.randint(1, 3)

    def random_rank(self, rank=None):
        if rank is None:
            rank = random.randint(1, 5)
        return self.set_rank(rank)

    def random_resonance(self):
        if random.random() < 0.7:
            possible = self.filter_resonance(minimum=1, maximum=4)
            if possible.count() > 0:
                choice = random.choice(possible)
                if self.add_resonance(choice):
                    return True
        res = fast_selector(Resonance)
        return self.add_resonance(res)

    def random(self, rank=None, name=None):
        self.update_status("Ran")
        self.random_name(name=name)
        self.random_rank(rank=rank)
        while not self.has_resonance():
            self.random_resonance()
        self.background_cost = 2 * self.rank
