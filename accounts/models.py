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

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
