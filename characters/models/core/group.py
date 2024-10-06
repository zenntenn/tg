import random

from characters.models.core.human import Human
from core.models import Model
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Group(Model):
    type = "group"

    members = models.ManyToManyField(Human, blank=True)
    leader = models.ForeignKey(
        Human,
        blank=True,
        related_name="leads_group",
        on_delete=models.SET_NULL,
        null=True,
    )
    permitted_users = models.ManyToManyField(
        User, blank=True, related_name="groups_permitted"
    )

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    def get_absolute_url(self):
        return reverse("characters:group", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("characters:update:group", kwargs={"pk": self.pk})

    @classmethod
    def get_creation_url(cls):
        return reverse("characters:create:group")

    def random_name(self):
        self.name = f"Random Group {Group.objects.count()}"
        return True

    def random(
        self,
        num_chars=None,
        new_characters=True,
        random_names=True,
        freebies=15,
        xp=0,
        user=None,
        member_type=Human,
        character_kwargs=None,
    ):
        self.update_status("Ran")
        if character_kwargs is None:
            character_kwargs = {}
        if self.name == "":
            self.random_name()
        if num_chars is None:
            num_chars = random.randint(3, 7)
        if not new_characters and member_type.objects.count() < num_chars:
            raise ValueError(f"Not enough {member_type}!")
        if not new_characters:
            self.members.set(member_type.objects.order_by("?")[:num_chars])
        else:
            if user is None:
                user = User.objects.get_or_create(username="New User")[0]
            for _ in range(num_chars):
                if not random_names:
                    name = f"{self.name} {self.members.count() + 1}"
                else:
                    name = ""
                m = member_type.objects.create(
                    name=name,
                    owner=user,
                )
                m.random(freebies=freebies, xp=xp, **character_kwargs)
                self.members.add(m)
        self.leader = self.members.order_by("?").first()
        self.save()
