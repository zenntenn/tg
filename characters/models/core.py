from core.models import Model
from core.utils import add_dot
from django.db import models
from django.urls import reverse


# Create your models here.
class Archetype(Model):
    type = "archetype"

    class Meta:
        verbose_name = "Archetype"
        verbose_name_plural = "Archetypes"

    def get_absolute_url(self):
        return reverse("characters:archetype", kwargs={"pk": self.pk})

    def get_heading(self):
        return "wod_heading"


class CharacterModel(Model):
    npc = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Character Model"
        verbose_name_plural = "Character Models"


class Character(CharacterModel):
    type = "character"

    concept = models.CharField(max_length=100)
    creation_status = models.IntegerField(default=1)

    class Meta:
        verbose_name = "Character"
        verbose_name_plural = "Characters"

    def get_heading(self):
        return "wod_heading"

    def next_stage(self):
        self.creation_status += 1
        self.save()

    def prev_stage(self):
        self.creation_status -= 1
        self.save()

    def has_concept(self):
        return self.concept != ""

    def set_concept(self, concept):
        self.concept = concept
        return True

    def get_absolute_url(self):
        return reverse("characters:character", kwargs={"pk": self.pk})


class Human(Character):
    type = "human"

    nature = models.ForeignKey(
        Archetype,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="nature_of",
    )
    demeanor = models.ForeignKey(
        Archetype,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="demeanor_of",
    )

    willpower = models.IntegerField(default=3)

    age = models.IntegerField(blank=True, null=True)
    apparent_age = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    hair = models.CharField(blank=True, null=True, max_length=100)
    eyes = models.CharField(blank=True, null=True, max_length=100)
    ethnicity = models.CharField(blank=True, null=True, max_length=100)
    nationality = models.CharField(blank=True, null=True, max_length=100)
    height = models.CharField(blank=True, null=True, max_length=100)
    weight = models.CharField(blank=True, null=True, max_length=100)
    sex = models.CharField(blank=True, null=True, max_length=100)

    childhood = models.TextField(default="", blank=True, null=True)
    history = models.TextField(default="", blank=True, null=True)
    goals = models.TextField(default="", blank=True, null=True)
    notes = models.TextField(default="", blank=True, null=True)

    xp = models.IntegerField(default=0)
    spent_xp = models.TextField(default="")

    current_health_levels = models.CharField(default="", max_length=100, blank=True)
    max_health_levels = models.IntegerField(default=7)

    freebies = 15
    background_points = 5

    class Meta:
        verbose_name = "Human"
        verbose_name_plural = "Humans"

    def get_heading(self):
        return "wod_heading"

    def add_willpower(self):
        return add_dot(self, "willpower", 10)

    def has_finishing_touches(self):
        return (
            self.age is not None
            and self.date_of_birth is not None
            and self.hair is not None
            and self.eyes is not None
            and self.ethnicity is not None
            and self.nationality is not None
            and self.height is not None
            and self.weight is not None
            and self.sex is not None
            and self.description is not None
            and self.apparent_age is not None
        )

    def has_history(self):
        return self.childhood != "" and self.history != "" and self.goals != ""

    def get_wound_penalty(self):
        health_levels = len(self.current_health_levels)
        if health_levels <= self.max_health_levels - 6:
            return 0
        if health_levels <= self.max_health_levels - 4:
            return -1
        if health_levels <= self.max_health_levels - 2:
            return -2
        if health_levels <= self.max_health_levels - 1:
            return -5
        return -1000

    def add_bashing(self):
        if len(self.current_health_levels) < self.max_health_levels:
            self.current_health_levels += "B"
        elif "B" in self.current_health_levels:
            self.current_health_levels = self.current_health_levels.replace("B", "L", 1)
        self.current_health_levels = "".join(
            sorted(self.current_health_levels, key=self.sort_damage)
        )

    @staticmethod
    def sort_damage(damage_type):
        if damage_type == "B":
            return 2
        if damage_type == "L":
            return 1
        # All other damage should be Aggravated
        return 0

    def add_aggravated(self):
        if len(self.current_health_levels) < self.max_health_levels:
            self.current_health_levels += "A"
        self.current_health_levels = "".join(
            sorted(self.current_health_levels, key=self.sort_damage)
        )

    def add_lethal(self):
        if len(self.current_health_levels) < self.max_health_levels:
            self.current_health_levels += "L"
        self.current_health_levels = "".join(
            sorted(self.current_health_levels, key=self.sort_damage)
        )

    def has_archetypes(self):
        return self.nature is not None and self.demeanor is not None

    def set_archetypes(self, nature, demeanor):
        self.nature = nature
        self.demeanor = demeanor
        return True
