from collections import defaultdict

from characters.models.core.background_block import (
    BackgroundRating,
    PooledBackgroundRating,
)
from characters.models.core.character import Character
from characters.models.core.human import Human
from core.models import Model
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Group(Model):
    type = "group"

    members = models.ManyToManyField(Character, blank=True)
    leader = models.ForeignKey(
        Character,
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

    def get_display_type(self):
        return self.type.title()

    def get_update_url(self):
        return reverse("characters:update:group", kwargs={"pk": self.pk})

    @classmethod
    def get_creation_url(cls):
        return reverse("characters:create:group")

    def update_pooled_backgrounds(self):
        bgs = BackgroundRating.objects.filter(char__in=self.members.all(), pooled=True)
        d = defaultdict(lambda: defaultdict(int))
        for bgr in bgs:
            d[bgr.bg][bgr.note] += bgr.rating
        for bg in d.keys():
            for note in d[bg].keys():
                p = PooledBackgroundRating.objects.get_or_create(
                    bg=bg, note=note, group=self
                )[0]
                p.rating = d[bg][note]
                p.save()
