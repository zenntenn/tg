from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    head_st = models.BooleanField(default=False)
    vtm_st = models.BooleanField(default=False)
    wta_st = models.BooleanField(default=False)
    mta_st = models.BooleanField(default=False)
    ctd_st = models.BooleanField(default=False)
    wto_st = models.BooleanField(default=False)
    htr_st = models.BooleanField(default=False)
    dtf_st = models.BooleanField(default=False)
    mtr_st = models.BooleanField(default=False)

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
        return (
            self.vtm_st
            or self.wta_st
            or self.mta_st
            or self.ctd_st
            or self.wto_st
            or self.htr_st
            or self.dtf_st
            or self.mtr_st
        )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
