from characters.models.mage.faction import MageFaction
from django.db import models
from django.urls import reverse
from items.models.mage.grimoire import Grimoire
from locations.models.core.location import LocationModel


class Library(LocationModel):
    type = "library"

    rank = models.IntegerField(default=1)
    faction = models.ForeignKey(
        MageFaction, null=True, blank=True, on_delete=models.SET_NULL
    )
    books = models.ManyToManyField(Grimoire, blank=True)

    class Meta:
        verbose_name = "Library"
        verbose_name_plural = "Libraries"

    def get_update_url(self):
        return reverse("locations:mage:update:library", args=[str(self.id)])

    def get_heading(self):
        return "mtas_heading"

    def add_book(self, grimoire):
        self.books.add(grimoire)
        self.save()
        return True

    def set_faction(self, faction):
        self.faction = faction
        return True

    def has_faction(self):
        return self.faction is not None

    def num_books(self):
        return self.books.count()

    def set_rank(self, rank):
        self.rank = rank
        self.save()
        return True
