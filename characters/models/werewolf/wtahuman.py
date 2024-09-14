from characters.models.core.human import Human
from django.db import models
from django.urls import reverse


class WtAHuman(Human):
    type = "wta_human"

    gameline = "wta"

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

    allies = models.IntegerField(default=0)
    ancestors = models.IntegerField(default=0)
    fate = models.IntegerField(default=0)
    fetish = models.IntegerField(default=0)
    kinfolk_rating = models.IntegerField(default=0)
    pure_breed = models.IntegerField(default=0)
    resources = models.IntegerField(default=0)
    rites = models.IntegerField(default=0)
    spirit_heritage = models.IntegerField(default=0)
    totem = models.IntegerField(default=0)

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

    def get_backgrounds(self):
        tmp = super().get_backgrounds()
        tmp.update(
            {
                "allies": self.allies,
                "ancestors": self.ancestors,
                "fate": self.fate,
                "fetish": self.fetish,
                "kinfolk_rating": self.kinfolk_rating,
                "pure_breed": self.pure_breed,
                "resources": self.resources,
                "rites": self.rites,
                "spirit_heritage": self.spirit_heritage,
                "totem": self.totem,
            }
        )
        return tmp

    def get_talents(self):
        tmp = super().get_talents()
        tmp.update(
            {
                "leadership": self.leadership,
                "primal_urge": self.primal_urge,
            }
        )
        return tmp

    def get_skills(self):
        tmp = super().get_skills()
        tmp.update(
            {
                "animal_ken": self.animal_ken,
                "larceny": self.larceny,
                "performance": self.performance,
                "survival": self.survival,
            }
        )
        return tmp

    def get_knowledges(self):
        tmp = super().get_knowledges()
        tmp.update(
            {
                "enigmas": self.enigmas,
                "law": self.law,
                "occult": self.occult,
                "rituals": self.rituals,
                "technology": self.technology,
            }
        )
        return tmp
