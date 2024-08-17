import random

from characters.models.mage.faction import MageFaction
from core.utils import weighted_choice
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

    def random_name(self, name=""):
        if name == "":
            name = f"Library {Library.objects.last().pk + 1}"
        return self.set_name(name)

    def increase_rank(self, book=None):
        if book is None or book in self.books.all():
            self.rank += 1
            self.random_book()
        else:
            self.rank += 1
            self.add_book(book)

    def random_faction(self, faction=None):
        if faction is None:
            faction_probs = {}

            for faction in MageFaction.objects.all():
                if faction.parent is None:
                    faction_probs[faction] = 30
                elif faction.parent.parent is None:
                    faction_probs[faction] = 10
                elif faction.parent.parent.parent is None:
                    faction_probs[faction] = 1
                else:
                    faction_probs[faction] = 0
                faction = weighted_choice(faction_probs, ceiling=100)
        self.set_faction(faction)

    def random_book(self):
        book = Grimoire.objects.create(name="", owner=self.owner)
        rank = random.randint(1, self.rank)
        if (
            random.random() < 0.5
            and MageFaction.objects.filter(parent=self.faction).exists()
        ):
            f = MageFaction.objects.filter(parent=self.faction).order_by("?").first()
        else:
            f = self.faction
        book.random(rank=rank, faction=f)
        return self.add_book(book)

    def random_rank(self, rank=None):
        if rank is None:
            rank = random.randint(1, 5)
        return self.set_rank(rank)

    def random(self, name="", faction=None, rank=None):
        self.update_status("Ran")
        self.random_name(name)
        self.random_faction(faction=faction)
        while self.num_books() < self.rank:
            self.random_book()
