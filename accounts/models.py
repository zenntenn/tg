from characters.models.core.character import Character
from characters.models.mage.mage import Mage
from characters.models.mage.rote import Rote
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from game.models import Chronicle, Scene, STRelationship
from items.models.core.item import ItemModel
from locations.models.core.location import LocationModel


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    preferred_heading = models.CharField(
        max_length=30,
        choices=zip(
            [
                "wod_heading",
                "vtm_heading",
                "wta_heading",
                "mta_heading",
                "ctd_heading",
                "wto_heading",
            ],
            [
                "World of Darkness",
                "Vampire: the Masquerade",
                "Werewolf: the Apocalypse",
                "Mage: the Ascension",
                "Changeling: the Dreaming",
                "Wraith: the Oblivion",
            ],
        ),
        default="wod_heading",
    )
    theme = models.CharField(
        max_length=30,
        choices=zip(
            ["themes/default.css", "themes/dark.css"],
            ["Default", "Dark"],
        ),
        default="themes/default.css",
    )

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def is_st(self):
        num_st = STRelationship.objects.filter(user=self.user).count()
        return num_st > 0

    def st_relations(self):
        str = STRelationship.objects.filter(user=self.user)
        d = {}
        for chron in Chronicle.objects.all():
            if str.filter(chronicle=chron).count() > 0:
                d[chron] = str.filter(chronicle=chron)
        return d

    def my_characters(self):
        return Character.objects.filter(owner=self.user)

    def my_locations(self):
        return LocationModel.objects.filter(owner=self.user)

    def my_items(self):
        return ItemModel.objects.filter(owner=self.user)

    def xp_requests(self):
        return Scene.objects.filter(
            chronicle__in=self.user.chronicle_set.all(),
            finished=True,
            xp_given=False,
        )

    def characters_to_approve(self):
        return Character.objects.filter(
            status__in=["Sub"],
            chronicle__in=self.user.chronicle_set.all(),
        ).order_by("name")

    def items_to_approve(self):
        return ItemModel.objects.filter(
            status__in=["Un", "Sub"],
            chronicle__in=self.user.chronicle_set.all(),
        ).order_by("name")

    def locations_to_approve(self):
        return LocationModel.objects.filter(
            status__in=["Un", "Sub"],
            chronicle__in=self.user.chronicle_set.all(),
        ).order_by("name")

    def rotes_to_approve(self):
        d = {}
        for r in Rote.objects.filter(
            status__in=["Un", "Sub"],
            chronicle__in=self.user.chronicle_set.all(),
        ).order_by("name"):
            d[r] = Mage.objects.filter(rotes__in=[r])
        return d

    def objects_to_approve(self):
        to_approve = list(self.characters_to_approve())
        to_approve.extend(list(self.items_to_approve()))
        to_approve.extend(list(self.locations_to_approve()))
        to_approve.extend(list(self.rotes_to_approve()))
        return to_approve

    def freebies_to_approve(self):
        f = Character.objects.filter(
            chronicle__in=self.user.chronicle_set.all(), freebies_approved=False
        )
        f = [x for x in f if x.creation_status == x.freebie_step]
        return f

    def image_to_approve(self):
        to_approve_images = (
            list(
                Character.objects.filter(
                    chronicle__in=self.user.chronicle_set.all(), image_status="sub"
                ).exclude(image="")
            )
            + list(
                LocationModel.objects.filter(
                    chronicle__in=self.user.chronicle_set.all(), image_status="sub"
                ).exclude(image="")
            )
            + list(
                ItemModel.objects.filter(
                    chronicle__in=self.user.chronicle_set.all(), image_status="sub"
                ).exclude(image="")
            )
        )
        to_approve_images.sort(key=lambda x: x.name)
        return to_approve_images

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("profile", kwargs={"pk": self.pk})


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
