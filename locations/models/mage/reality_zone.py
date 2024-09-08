from characters.models.mage.focus import Practice
from django.db import models
from django.urls import reverse
from locations.models.core.location import LocationModel


class ZoneRating(models.Model):
    zone = models.ForeignKey("RealityZone", on_delete=models.SET_NULL, null=True)
    practice = models.ForeignKey(Practice, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Reality Zone Rating"
        verbose_name_plural = "Reality Zone Ratings"


class RealityZone(models.Model):
    type = "reality_zone"
    
    name = models.CharField(max_length=100)
    practices = models.ManyToManyField(Practice, through=ZoneRating, blank=True)
    description = models.TextField(default="")

    class Meta:
        verbose_name = "Reality Zone"
        verbose_name_plural = "Reality Zone"

    def get_absolute_url(self):
        return reverse("locations:mage:reality_zone", args=[str(self.id)])

    def get_update_url(self):
        return reverse("locations:mage:update:reality_zone", args=[str(self.id)])

    @classmethod
    def get_creation_url(cls):
        return reverse("locations:mage:create:reality_zone")

    def get_heading(self):
        return "mta_heading"

    def __str__(self):
        return self.name
