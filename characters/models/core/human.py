import random
from datetime import date, timedelta

from characters.models.core.ability_block import AbilityBlock
from characters.models.core.archetype import Archetype
from characters.models.core.attribute_block import AttributeBlock
from characters.models.core.background_block import BackgroundBlock
from characters.models.core.character import Character
from characters.models.core.derangement import Derangement
from characters.models.core.health_block import HealthBlock
from characters.models.core.human_url_block import HumanUrlBlock
from characters.models.core.merit_flaw_block import MeritFlawBlock
from characters.models.core.specialty import Specialty
from characters.utils import random_ethnicity, random_height, random_name, random_weight
from core.models import Language
from core.utils import add_dot, get_short_gameline_name, weighted_choice
from django.db import models
from django.urls import reverse


class Human(
    HumanUrlBlock,
    AbilityBlock,
    MeritFlawBlock,
    HealthBlock,
    BackgroundBlock,
    AttributeBlock,
    Character,
):
    type = "human"

    gameline = "wod"

    allowed_backgrounds = ["contacts", "mentor"]
    talents = [
        "alertness",
        "athletics",
        "brawl",
        "empathy",
        "expression",
        "intimidation",
        "streetwise",
        "subterfuge",
    ]
    skills = ["crafts", "drive", "etiquette", "firearms", "melee", "stealth"]
    knowledges = ["academics", "computer", "investigation", "medicine", "science"]
    primary_abilities = [
        "alertness",
        "athletics",
        "brawl",
        "empathy",
        "expression",
        "intimidation",
        "streetwise",
        "subterfuge",
        "crafts",
        "drive",
        "etiquette",
        "firearms",
        "melee",
        "stealth",
        "academics",
        "computer",
        "investigation",
        "medicine",
        "science",
    ]

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

    languages = models.ManyToManyField(Language, blank=True)

    willpower = models.IntegerField(default=3)
    derangements = models.ManyToManyField("Derangement", blank=True)

    age = models.IntegerField(blank=True, null=True)
    apparent_age = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    history = models.TextField(default="", blank=True, null=True)
    goals = models.TextField(default="", blank=True, null=True)

    xp = models.IntegerField(default=0)
    spent_xp = models.JSONField(default=list)

    freebies = models.IntegerField(default=15)
    spent_freebies = models.JSONField(default=list)
    background_points = 5

    class Meta:
        verbose_name = "Human"
        verbose_name_plural = "Humans"
        ordering = ["name"]

    def total_freebies(self):
        return self.freebies + sum([x["cost"] for x in self.spent_freebies])

    def is_group_member(self):
        from characters.models.core.group import Group

        return Group.objects.filter(members=self).count() > 0

    def get_group(self):
        from characters.models.core.group import Group

        if self.is_group_member():
            return Group.objects.get(members=self)
        return False

    def get_heading(self):
        return f"{self.gameline}_heading"

    def add_willpower(self):
        return add_dot(self, "willpower", 10)

    def has_finishing_touches(self):
        return (
            self.age is not None
            and self.date_of_birth is not None
            and self.description is not None
            and self.apparent_age is not None
        )

    def has_history(self):
        return self.history != "" and self.goals != ""

    def has_archetypes(self):
        return self.nature is not None and self.demeanor is not None

    def set_archetypes(self, nature, demeanor):
        self.nature = nature
        self.demeanor = demeanor
        return True

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

    def random_name(self, ethnicity=None):
        ethnicity = random_ethnicity()
        sex = random.random()
        if sex < 0.495:
            sex = "Male"
            gender = "m"
        elif sex < 0.99:
            sex = "Female"
            gender = "f"
        else:
            sex = "Other"
            gender = "mf"
        self.notes += f"\nEthnicity: {ethnicity}, Sex {sex}"
        if not self.has_name():
            name = random_name(gender, ethnicity)
            count = 0
            while Character.objects.filter(name=name).exists() and count < 20:
                self.ethnicity = random_ethnicity()
                name = random_name(gender, ethnicity)
                count += 1
            if count == 20:
                name = f"Random Name {random.randint(1, 10000000000)}"
            self.set_name(name)

    def random_archetypes(self):
        self.nature = Archetype.objects.order_by("?").first()
        self.demeanor = Archetype.objects.order_by("?").first()

    def add_specialty(self, specialty):
        if getattr(self, specialty.stat) < 4 and specialty.stat not in [
            "arts",
            "athletics",
            "crafts",
            "firearms",
            "melee",
            "academics",
            "occult",
            "lore",
            "politics",
            "science",
        ]:
            return False
        if specialty in self.specialties.all():
            return False
        self.specialties.add(specialty)
        return True

    def has_specialties(self):
        output = True
        for attribute in self.filter_attributes(minimum=4):
            output = output and (self.specialties.filter(stat=attribute).count() > 0)
        for ability in self.filter_abilities(minimum=4):
            output = output and (self.specialties.filter(stat=ability).count() > 0)
        for ability in [
            x
            for x in self.filter_abilities(minimum=1)
            if x
            in [
                "arts",
                "athletics",
                "crafts",
                "firearms",
                "melee",
                "academics",
                "occult",
                "lore",
                "politics",
                "science",
            ]
        ]:
            output = output and (self.specialties.filter(stat=ability).count() > 0)
        return output

    def random_specialty(self, stat):
        options = self.filter_specialties(stat=stat)
        return self.add_specialty(random.choice(options))

    def random_specialties(self):
        need_specialty = []
        for attribute in self.filter_attributes(minimum=4):
            if attribute not in need_specialty:
                need_specialty.append(attribute)
        for ability in self.filter_abilities(minimum=4):
            if ability not in need_specialty:
                need_specialty.append(ability)
        for ability in [
            x
            for x in self.filter_abilities(minimum=1)
            if x
            in [
                "arts",
                "athletics",
                "crafts",
                "firearms",
                "melee",
                "academics",
                "occult",
                "lore",
                "politics",
                "science",
            ]
        ]:
            if ability not in need_specialty:
                need_specialty.append(ability)
        for stat in need_specialty:
            self.specialties.add(random.choice(self.filter_specialties(stat=stat)))

    def add_random_language(self):
        d = {
            l.name: l.frequency
            for l in Language.objects.all()
            if l not in self.languages.all()
        }
        if len(d) == 0:
            return False
        choice = weighted_choice(d)
        choice = Language.objects.get(name=choice)
        self.languages.add(choice)
        self.save()
        return True

    def random_derangement(self):
        d = (
            Derangement.objects.exclude(pk__in=self.derangements.all())
            .order_by("?")
            .first()
        )
        return self.add_derangement(d)

    def random_birthdate(self, age):
        earliest_date = date.today() - timedelta(days=(age + 1) * 365)
        int_delta = 365 * 24 * 60 * 60
        random_second = random.randrange(int_delta)
        return earliest_date + timedelta(seconds=random_second)

    def random_finishing_touches(self):
        self.age = random.randint(18, 80)
        birthday = self.random_birthdate(self.age)
        self.date_of_birth = birthday
        self.description = "Description"
        self.apparent_age = self.age
        self.save()

    def random_history(self):
        self.history = "History"
        self.goals = "Goals"
        self.save()

    def mf_based_corrections(self):
        if self.merits_and_flaws.filter(name="Ability Deficit").exists():
            stats_to_lose = random.choice(
                [self.get_talents(), self.get_skills(), self.get_knowledges()]
            )
            total_removed = 0
            for key, value in stats_to_lose.items():
                if value > 3:
                    total_removed += value - 3
                    stats_to_lose[key] = 3
                    setattr(self, key, 3)
            while total_removed > 5:
                tmp = {k: v for k, v in stats_to_lose.item() if v < 3}
                new_stat = weighted_choice(tmp)
                if self.add_ability(new_stat):
                    stats_to_lose[new_stat] += 1
                    total_removed -= 1
            while total_removed < 5:
                new_stat = weighted_choice(stats_to_lose)
                stats_to_lose[new_stat] -= 1
                setattr(self, new_stat, stats_to_lose[new_stat])
                total_removed += 1

    def random(self, freebies=15, xp=0, ethnicity=None):
        self.update_status("Ran")
        self.freebies = freebies
        self.xp = xp
        self.random_name(ethnicity=ethnicity)
        self.random_concept()
        self.random_archetypes()
        self.random_attributes()
        self.random_abilities()
        self.random_backgrounds()
        self.mf_based_corrections()
        self.random_specialties()
        self.random_finishing_touches()
        self.random_history()

    def freebie_costs(self):
        return {
            "attribute": 5,
            "ability": 2,
            "background": 1,
            "willpower": 1,
            "meritflaw": "rating",
        }

    def freebie_cost(self, trait_type):
        costs = self.freebie_costs()
        if trait_type not in costs.keys():
            return 10000
        return costs[trait_type]

    def freebie_spend_record(self, trait, trait_type, value, cost=None):
        if cost is None:
            cost = self.freebie_cost(trait_type)
        return {
            "trait": trait,
            "value": value,
            "cost": cost,
        }

    def xp_cost(self, trait_type, trait_value):
        costs = {
            "new_ability": 3,
            "attribute": 4,
            "ability": 2,
            "background": 3,
            "willpower": 1,
        }
        if trait_type == "ability" and trait_value == 0:
            return costs["new_ability"]
        return costs["trait_type"] * trait_value
