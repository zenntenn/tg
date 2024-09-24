from characters.models.core.statistic import Statistic
from django.db import models


class Background(Statistic):
    type = "background"

    models.IntegerField(default=1)


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
