from characters.models.core.archetype import Archetype
from characters.models.core.character import Character
from characters.models.core.meritflaw import MeritFlaw, MeritFlawRating
from characters.models.core.specialty import Specialty
from core.utils import add_dot
from django.db import models
from django.db.models import F, Q
from django.urls import reverse
from game.models import ObjectType


# Create your models here.
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

    specialties = models.ManyToManyField(Specialty, blank=True)

    willpower = models.IntegerField(default=3)
    derangements = models.ManyToManyField("Derangement", blank=True)

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

    merits_and_flaws = models.ManyToManyField(
        MeritFlaw, blank=True, through=MeritFlawRating, related_name="flawed"
    )

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

    def get_update_url(self):
        return reverse("characters:update:human", kwargs={"pk": self.pk})

    @classmethod
    def get_creation_url(cls):
        return reverse("characters:create:human")

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

    def get_mf_and_rating_list(self):
        return [(x.name, self.mf_rating(x)) for x in self.merits_and_flaws.all()]

    def add_mf(self, mf, rating):
        if rating in mf.get_ratings():
            mfr, _ = MeritFlawRating.objects.get_or_create(character=self, mf=mf)
            mfr.rating = rating
            mfr.save()
            if mf.name in ["Language", "Natural Linguist"]:
                num_languages = self.mf_rating(MeritFlaw.objects.get(name="Language"))
                if self.merits_and_flaws.filter(name="Natural Linguist").exists():
                    num_languages *= 2
                while self.languages.count() < num_languages:
                    self.add_random_language()
            if mf.name == "Deranged":
                self.random_derangement()
            return True
        return False

    def filter_mfs(self):
        character_type = self.type
        if character_type in ["fomor"]:
            character_type = "human"

        new_mfs = MeritFlaw.objects.exclude(pk__in=self.merits_and_flaws.all())

        non_max_mf = MeritFlawRating.objects.filter(character=self).exclude(
            Q(rating=F("mf__max_rating"))
        )

        had_mfs = MeritFlaw.objects.filter(pk__in=non_max_mf)
        mf = new_mfs | had_mfs
        if self.has_max_flaws():
            mf = mf.filter(max_rating__gt=0)
        character_type_object = ObjectType.objects.get(name=character_type)
        return mf.filter(allowed_types=character_type_object)

    def mf_rating(self, mf):
        if mf not in self.merits_and_flaws.all():
            return 0
        return MeritFlawRating.objects.get(character=self, mf=mf).rating

    def has_max_flaws(self):
        return self.total_flaws() <= -7

    def total_flaws(self):
        return sum(
            x.rating
            for x in MeritFlawRating.objects.filter(character=self)
            if x.rating < 0
        )

    def total_merits(self):
        return sum(
            x.rating
            for x in MeritFlawRating.objects.filter(character=self)
            if x.rating > 0
        )

    def add_derangement(self, derangement):
        if derangement in self.derangements.all():
            return False
        self.derangements.add(derangement)
        return True

    def get_specialty(self, stat):
        spec = self.specialties.filter(stat=stat).first()
        if spec is None:
            return None
        return spec.name

    def filter_specialties(self, stat=None):
        if stat is None:
            return Specialty.objects.all().exclude(pk__in=self.specialties.all())
        return Specialty.objects.filter(stat=stat).exclude(
            pk__in=self.specialties.all()
        )
