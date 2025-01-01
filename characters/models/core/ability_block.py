from characters.models.core.statistic import Statistic
from core.utils import add_dot
from django.db import models


class Ability(Statistic):
    type = "ability"


class AbilityBlock(models.Model):
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

    alertness = models.IntegerField(default=0)
    athletics = models.IntegerField(default=0)
    brawl = models.IntegerField(default=0)
    empathy = models.IntegerField(default=0)
    expression = models.IntegerField(default=0)
    intimidation = models.IntegerField(default=0)
    streetwise = models.IntegerField(default=0)
    subterfuge = models.IntegerField(default=0)

    crafts = models.IntegerField(default=0)
    drive = models.IntegerField(default=0)
    etiquette = models.IntegerField(default=0)
    firearms = models.IntegerField(default=0)
    melee = models.IntegerField(default=0)
    stealth = models.IntegerField(default=0)

    academics = models.IntegerField(default=0)
    computer = models.IntegerField(default=0)
    investigation = models.IntegerField(default=0)
    medicine = models.IntegerField(default=0)
    science = models.IntegerField(default=0)

    class Meta:
        abstract = True

    def add_ability(self, ability, maximum=4):
        return add_dot(self, ability, maximum)

    def get_abilities(self):
        tmp = {}
        tmp.update(self.get_talents())
        tmp.update(self.get_skills())
        tmp.update(self.get_knowledges())
        return tmp

    def filter_abilities(self, minimum=0, maximum=5):
        return {
            k: v for k, v in self.get_abilities().items() if minimum <= v <= maximum
        }

    def get_talents(self):
        return {k: getattr(self, k) for k in self.talents}

    def get_skills(self):
        return {k: getattr(self, k) for k in self.skills}

    def get_knowledges(self):
        return {k: getattr(self, k) for k in self.knowledges}

    def total_talents(self):
        return sum(self.get_talents().values())

    def total_skills(self):
        return sum(self.get_skills().values())

    def total_knowledges(self):
        return sum(self.get_knowledges().values())

    def total_abilities(self):
        return sum(self.get_abilities().values())

    def has_abilities(self, primary=13, secondary=9, tertiary=5):
        triple = [self.total_talents(), self.total_skills(), self.total_knowledges()]
        triple.sort()
        return triple == [tertiary, secondary, primary]

    def get_secondaries_for_display(self):
        secondary_talents = {
            k: v
            for k, v in self.get_talents().items()
            if k not in self.primary_abilities and v != 0
        }
        secondary_skills = {
            k: v
            for k, v in self.get_skills().items()
            if k not in self.primary_abilities and v != 0
        }
        secondary_knowledges = {
            k: v
            for k, v in self.get_knowledges().items()
            if k not in self.primary_abilities and v != 0
        }

        if "History Knowledge" in secondary_knowledges:
            secondary_knowledges["History"] = secondary_knowledges.pop(
                "History Knowledge"
            )

        secondary_talents = list(secondary_talents.items())
        secondary_skills = list(secondary_skills.items())
        secondary_knowledges = list(secondary_knowledges.items())

        secondary_talents = [
            (k.replace("_", " ").title(), v, k) for k, v in secondary_talents
        ]
        secondary_skills = [
            (k.replace("_", " ").title(), v, k) for k, v in secondary_skills
        ]
        secondary_knowledges = [
            (k.replace("_", " ").title(), v, k) for k, v in secondary_knowledges
        ]

        secondary_talents.sort(key=lambda x: x[0])
        secondary_skills.sort(key=lambda x: x[0])
        secondary_knowledges.sort(key=lambda x: x[0])

        num_sec_tal = len(secondary_talents)
        num_sec_ski = len(secondary_skills)
        num_sec_kno = len(secondary_knowledges)
        m = max(num_sec_tal, num_sec_ski, num_sec_kno)
        for _ in range(m - num_sec_tal):
            secondary_talents.append(("", 0, ""))
        for _ in range(m - num_sec_ski):
            secondary_skills.append(("", 0, ""))
        for _ in range(m - num_sec_kno):
            secondary_knowledges.append(("", 0, ""))
        return list(zip(secondary_talents, secondary_skills, secondary_knowledges))

    def ability_freebies(self, form):
        cost = 2
        trait = form.cleaned_data["example"]
        value = getattr(self, trait.property_name) + 1
        self.add_ability(trait.property_name)
        self.freebies -= cost
        trait = trait.name
        return trait, value, cost
