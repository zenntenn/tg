from django.db import models
from django.urls import reverse
from locations.models.core.location import LocationModel


# Create your models here.
class Sector(LocationModel):
    type = "sector"

    SECTOR_CLASS = [
        ("virgin", "Virgin Web"),
        ("grid", "Grid"),
        ("formatted", "Formatted Web"),
        ("corrupted", "Corrupted Web"),
        ("junklands", "Junklands"),
        ("haunts", "Haunts"),
        ("trash", "Trash"),
        ("streamland", "Streamland"),
    ]

    sector_class = models.CharField(max_length=10, choices=SECTOR_CLASS, default="")
    constraints = models.TextField(default="")

    class Meta:
        verbose_name = "Sector"
        verbose_name_plural = "Sectors"

    def get_update_url(self):
        return reverse("locations:mage:update:sector", args=[str(self.id)])

    @classmethod
    def get_creation_url(cls):
        return reverse("locations:mage:create:sector")

    def get_heading(self):
        return "mta_heading"
