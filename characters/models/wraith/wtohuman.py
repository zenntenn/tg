from characters.models.core.human import Human
from django.db import models


class WtOHuman(Human):
    type = "wto_human"

    gameline = "wto"

    talents = [
        "alertness",
        "athletics",
        "brawl",
        "empathy",
        "expression",
        "intimidation",
        "streetwise",
        "subterfuge",
        "awareness",
        "persuasion",
    ]
    skills = [
        "crafts",
        "drive",
        "etiquette",
        "firearms",
        "melee",
        "stealth",
        "larceny",
        "meditation",
        "performance",
    ]
    knowledges = [
        "academics",
        "computer",
        "investigation",
        "medicine",
        "science",
        "bureaucracy",
        "enigmas",
        "occult",
        "politics",
        "technology",
    ]
    primary_abilities = [
        "alertness",
        "awareness",
        "persuasion",
        "larceny",
        "meditation",
        "performance",
        "bureaucracy",
        "enigmas",
        "occult",
        "politics",
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
        "artifact",
        "eidolon",
        "haunt",
        "legacy",
        "memoriam",
        "notoriety",
        "relic",
        "status_background",
    ]

    awareness = models.IntegerField(default=0)
    persuasion = models.IntegerField(default=0)

    larceny = models.IntegerField(default=0)
    meditation = models.IntegerField(default=0)
    performance = models.IntegerField(default=0)

    bureaucracy = models.IntegerField(default=0)
    enigmas = models.IntegerField(default=0)
    occult = models.IntegerField(default=0)
    politics = models.IntegerField(default=0)
    technology = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Human (Wraith)"
        verbose_name_plural = "Humans (Wraith)"
