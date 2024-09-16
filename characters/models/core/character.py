from core.models import Model
from django.db import models
from django.db.models.signals import m2m_changed, post_save
from django.urls import reverse


class CharacterModel(Model):
    npc = models.BooleanField(default=False)

    gameline = "wod"

    class Meta:
        verbose_name = "Character Model"
        verbose_name_plural = "Character Models"


class Character(CharacterModel):
    type = "character"

    gameline = "wod"

    concept = models.CharField(max_length=100)
    creation_status = models.IntegerField(default=1)

    class Meta:
        verbose_name = "Character"
        verbose_name_plural = "Characters"

    def get_type(self):
        if "human" in self.type:
            return "Human"
        if "spirit_character" == self.type:
            return "Spirit"
        return self.type.title()

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

    def random_concept(self):
        self.set_concept("Random")

    def random_name(self):
        self.set_name(f"Random Character {Character.objects.count()}")

    def get_absolute_url(self):
        return reverse("characters:character", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("characters:update:character", kwargs={"pk": self.pk})

    @classmethod
    def get_creation_url(cls):
        return reverse("characters:create:character")
