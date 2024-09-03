from core.models import Model, Number
from django.db import models
from django.urls import reverse
from game.models import ObjectType


class MeritFlaw(Model):
    type = "merit_flaw"

    ratings = models.ManyToManyField(Number, blank=True)
    max_rating = models.IntegerField(default=0)
    min_rating = models.IntegerField(default=0)

    allowed_types = models.ManyToManyField(ObjectType, blank=True)

    class Meta:
        verbose_name = "Merit or Flaw"
        verbose_name_plural = "Merits and Flaws"

    def get_absolute_url(self):
        return reverse("characters:meritflaw", args=[str(self.id)])

    def get_update_url(self):
        return reverse("characters:update:meritflaw", kwargs={"pk": self.pk})

    @classmethod
    def get_creation_url(cls):
        return reverse("characters:create:meritflaw")

    def get_heading(self):
        return "wod_heading"

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

    def check_type(self, type_name):
        if self.allowed_types.get(value=type_name).exists():
            return True
        return False


class MeritFlawRating(models.Model):
    character = models.ForeignKey("Human", on_delete=models.SET_NULL, null=True)
    mf = models.ForeignKey(MeritFlaw, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Merit or Flaw Rating"
        verbose_name_plural = "Merit and Flaw Ratings"

    def __str__(self):
        return f"{self.mf}: {self.rating}"
