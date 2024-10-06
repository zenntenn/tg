from characters.models.core.statistic import Statistic
from django.db import models


class Background(Statistic):
    type = "background"

    multiplier = models.IntegerField(default=1)

    class Meta:
        ordering = ["name"]


class BackgroundRating(models.Model):
    bg = models.ForeignKey(Background, on_delete=models.SET_NULL, null=True)
    char = models.ForeignKey(
        "characters.Human",
        on_delete=models.SET_NULL,
        null=True,
        related_name="backgrounds",
    )
    rating = models.IntegerField(default=0)
    note = models.CharField(default="", max_length=100)
    url = models.CharField(default="", max_length=500)
    complete = models.BooleanField(default=False)
    pooled = models.BooleanField(default=False)

    class Meta:
        ordering = ["bg__name"]

    def __str__(self):
        return f"{self.bg} ({self.note})"


class PooledBackgroundRating(models.Model):
    bg = models.ForeignKey(Background, on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(
        "characters.Group",
        on_delete=models.SET_NULL,
        null=True,
        related_name="pooled_backgrounds",
    )
    rating = models.IntegerField(default=0)
    note = models.CharField(default="", max_length=100)
    url = models.CharField(default="", max_length=500)
    complete = models.BooleanField(default=False)

    class Meta:
        ordering = ["bg__name"]

    def __str__(self):
        return f"{self.bg} ({self.note})"
