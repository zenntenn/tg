from characters.models.core.human import Human
from django.db import models
from django.urls import reverse


class WtAHuman(Human):
    type = "wta_human"

    gameline = "wta"

    talents = [
        "alertness",
        "athletics",
        "brawl",
        "empathy",
        "expression",
        "intimidation",
        "streetwise",
        "subterfuge",
        "leadership",
        "primal_urge",
    ]
    skills = [
        "crafts",
        "drive",
        "etiquette",
        "firearms",
        "melee",
        "stealth",
    ]
    knowledges = [
        "academics",
        "computer",
        "investigation",
        "medicine",
        "science",
        "enigmas",
        "law",
        "occult",
        "rituals",
        "technology",
    ]
    primary_abilities = [
        "alertness",
        "leadership",
        "primal_urge",
        "animal_ken",
        "larceny",
        "performance",
        "survival",
        "enigmas",
        "law",
        "occult",
        "rituals",
        "technology",
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

    allowed_backgrounds = [
        "contacts",
        "mentor",
        "allies",
        "ancestors",
        "fate",
        "fetish",
        "kinfolk_rating",
        "pure_breed",
        "resources",
        "rites",
        "spirit_heritage",
        "totem",
    ]

    leadership = models.IntegerField(default=0)
    primal_urge = models.IntegerField(default=0)

    animal_ken = models.IntegerField(default=0)
    larceny = models.IntegerField(default=0)
    performance = models.IntegerField(default=0)
    survival = models.IntegerField(default=0)

    enigmas = models.IntegerField(default=0)
    law = models.IntegerField(default=0)
    occult = models.IntegerField(default=0)
    rituals = models.IntegerField(default=0)
    technology = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Human (Werewolf)"
        verbose_name_plural = "Humans (Werewolf)"

    def get_update_url(self):
        return reverse("characters:werewolf:update:wta_human", kwargs={"pk": self.pk})

    @classmethod
    def get_creation_url(cls):
        return reverse("characters:werewolf:create:wta_human")

    def get_heading(self):
        return "wta_heading"
