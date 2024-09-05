import random

from characters.models.core.group import Group
from characters.models.werewolf.garou import Werewolf
from characters.models.werewolf.totem import Totem
from django.db import models
from django.urls import reverse


class Pack(Group):
    type = "pack"

    totem = models.ForeignKey(Totem, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Pack"
        verbose_name_plural = "Packs"

    @classmethod
    def get_creation_url(cls):
        return reverse("characters:werewolf:create:pack")

    def get_update_url(self):
        return reverse("characters:werewolf:update:pack", kwargs={"pk": self.pk})

    def get_heading(self):
        return "wta_heading"

    def random(self, num_chars=None, new_characters=True, freebies=15, xp=0, user=None):
        super().random(
            num_chars=num_chars,
            new_characters=new_characters,
            freebies=freebies,
            xp=xp,
            user=user,
            member_type=Werewolf,
        )
        self.random_totem()

    def set_totem(self, totem):
        self.totem = totem
        self.save()
        return True

    def has_totem(self):
        return self.totem is not None

    def random_totem(self):
        filtered = list(Totem.objects.filter(cost__lte=self.total_totem()))
        if len(filtered) == 0:
            return False
        return self.set_totem(random.choice(filtered))

    def total_totem(self):
        return sum(x.totem for x in self.members.all())
