from characters.models.core.human import Human
from django.db import models
from django.urls import reverse


# Create your models here.
class WtOHuman(Human):
    type = "wto_human"

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

    allies = models.IntegerField(default=0)
    artifact = models.IntegerField(default=0)
    eidolon = models.IntegerField(default=0)
    haunt = models.IntegerField(default=0)
    legacy = models.IntegerField(default=0)
    memoriam = models.IntegerField(default=0)
    notoriety = models.IntegerField(default=0)
    relic = models.IntegerField(default=0)
    status_background = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Human (Wraith)"
        verbose_name_plural = "Humans (Wraith)"

    def get_update_url(self):
        return reverse("characters:wraith:update:wtohuman", kwargs={"pk": self.pk})

    @classmethod
    def get_creation_url(cls):
        return reverse("characters:wraith:create:wtohuman")

    def get_heading(self):
        return "wto_heading"

    def get_talents(self):
        talents = super().get_talents()
        talents.update(
            {
                "awareness": self.awareness,
                "persuasion": self.persuasion,
            }
        )
        return talents

    def get_skills(self):
        skills = super().get_skills()
        skills.update(
            {
                "larceny": self.larceny,
                "meditation": self.meditation,
                "performance": self.performance,
            }
        )
        return skills

    def get_knowledges(self):
        knowledges = super().get_knowledges()
        knowledges.update(
            {
                "bureaucracy": self.bureaucracy,
                "enigmas": self.enigmas,
                "occult": self.occult,
                "politics": self.politics,
                "technology": self.technology,
            }
        )
        return knowledges

    def get_backgrounds(self):
        backgrounds = super().get_backgrounds()
        backgrounds.update(
            {
                "allies": self.allies,
                "artifact": self.artifact,
                "eidolon": self.eidolon,
                "haunt": self.haunt,
                "legacy": self.legacy,
                "memoriam": self.memoriam,
                "notoriety": self.notoriety,
                "relic": self.relic,
                "status_background": self.status_background,
            }
        )
        return backgrounds
