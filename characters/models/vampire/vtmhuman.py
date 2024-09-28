from characters.models.core.human import Human
from django.db import models
from django.urls import reverse


class VtMHuman(Human):
    type = "vtm_human"
    gameline = "vtm"

    allowed_backgrounds = [
        "contacts",
        "mentor",
        "allies",
        "alternate_identity",
        "black_hand_membership",
        "domain",
        "fame",
        "generation",
        "herd",
        "influence",
        "resources",
        "retainers",
        "rituals",
        "status_background",
    ]

    awareness = models.IntegerField(default=0)
    leadership = models.IntegerField(default=0)
    animal_ken = models.IntegerField(default=0)
    larceny = models.IntegerField(default=0)
    performance = models.IntegerField(default=0)
    survival = models.IntegerField(default=0)
    finance = models.IntegerField(default=0)
    law = models.IntegerField(default=0)
    occult = models.IntegerField(default=0)
    politics = models.IntegerField(default=0)
    technology = models.IntegerField(default=0)

    allies = models.IntegerField(default=0)
    alternate_identity = models.IntegerField(default=0)
    black_hand_membership = models.IntegerField(default=0)
    domain = models.IntegerField(default=0)
    fame = models.IntegerField(default=0)
    generation = models.IntegerField(default=0)
    herd = models.IntegerField(default=0)
    influence = models.IntegerField(default=0)
    resources = models.IntegerField(default=0)
    retainers = models.IntegerField(default=0)
    rituals = models.IntegerField(default=0)
    status_background = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Human (Vampire)"
        verbose_name_plural = "Humans (Vampire)"

    def get_update_url(self):
        return reverse("characters:vampire:update:vtm_human", kwargs={"pk": self.pk})

    @classmethod
    def get_creation_url(cls):
        return reverse("characters:vampire:create:vtm_human")

    def get_heading(self):
        return "vtm_heading"

    def get_talents(self):
        talents = super().get_talents()
        talents.update(
            {
                "awareness": self.awareness,
                "leadership": self.leadership,
            }
        )
        return talents

    def get_skills(self):
        skills = super().get_skills()
        skills.update(
            {
                "animal_ken": self.animal_ken,
                "larceny": self.larceny,
                "performance": self.performance,
                "survival": self.survival,
            }
        )
        return skills

    def get_knowledges(self):
        knowledges = super().get_knowledges()
        knowledges.update(
            {
                "finance": self.finance,
                "law": self.law,
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
                "alternate_identity": self.alternate_identity,
                "black_hand_membership": self.black_hand_membership,
                "domain": self.domain,
                "fame": self.fame,
                "generation": self.generation,
                "herd": self.herd,
                "influence": self.influence,
                "resources": self.resources,
                "retainers": self.retainers,
                "rituals": self.rituals,
                "status_background": self.status_background,
            }
        )
        return backgrounds
