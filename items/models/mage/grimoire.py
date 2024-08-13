from characters.models.core.ability import Ability
from characters.models.mage.effect import Effect
from characters.models.mage.focus import Instrument, Paradigm, Practice
from characters.models.mage.sphere import Sphere
from core.models import Language
from django.db import models
from django.urls import reverse
from items.models.core.material import Material
from items.models.core.medium import Medium
from items.models.mage.wonder import Wonder


class Grimoire(Wonder):
    type = "grimoire"

    abilities = models.ManyToManyField(Ability, blank=True)
    spheres = models.ManyToManyField(Sphere, blank=True)
    date_written = models.IntegerField(default=-5000)
    faction = models.ForeignKey(
        "characters.MageFaction", null=True, blank=True, on_delete=models.SET_NULL
    )
    paradigms = models.ManyToManyField(Paradigm, blank=True)
    practices = models.ManyToManyField(Practice, blank=True)
    instruments = models.ManyToManyField(Instrument, blank=True)
    is_primer = models.BooleanField(default=False)
    language = models.ForeignKey(
        Language, null=True, blank=True, on_delete=models.SET_NULL
    )
    length = models.IntegerField(default=0)
    cover_material = models.ForeignKey(
        Material,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="is_cover",
    )
    inner_material = models.ForeignKey(
        Material,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="is_inner",
    )
    medium = models.ForeignKey(Medium, null=True, blank=True, on_delete=models.SET_NULL)
    effects = models.ManyToManyField(Effect, blank=True)

    class Meta:
        verbose_name = "Grimoire"
        verbose_name_plural = "Grimoires"

    def get_update_url(self):
        return reverse("items:mage:update:grimoire", args=[str(self.id)])

    def set_abilities(self, abilities):
        for ability in abilities:
            if not isinstance(ability, Ability):
                return False
            self.abilities.add(ability)
        return True

    def has_abilities(self):
        return self.abilities.count() != 0

    def set_date_written(self, date_written):
        self.date_written = date_written
        return True

    def has_date_written(self):
        return self.date_written != -5000

    def set_faction(self, faction):
        self.faction = faction
        return True

    def has_faction(self):
        return self.faction is not None

    def set_focus(self, paradigms, practices, instruments):
        self.paradigms.set(paradigms)
        self.practices.set(practices)
        self.instruments.set(instruments)
        self.save()
        return True

    def has_focus(self):
        return (
            self.paradigms.count() != 0
            and self.practices.count() != 0
            and self.instruments.count() != 0
        )

    def set_language(self, language):
        self.language = language
        return True

    def has_language(self):
        return self.language is not None

    def set_length(self, length):
        self.length = length
        return True

    def has_length(self):
        return self.length != 0

    def set_materials(self, cover_material, inner_material):
        self.cover_material = cover_material
        self.inner_material = inner_material
        return True

    def has_materials(self):
        return self.cover_material is not None and self.inner_material is not None

    def set_medium(self, medium):
        self.medium = medium
        return True

    def has_medium(self):
        return self.medium is not None

    def set_rank(self, rank):
        rank = min(5, rank)
        rank = max(1, rank)
        self.rank = rank
        return True

    def has_rank(self):
        return self.rank != 0

    def set_effects(self, effects):
        self.effects.set(effects)
        self.save()
        return True

    def has_effects(self):
        return self.effects.count() != 0

    def set_spheres(self, spheres):
        for sphere in spheres:
            if not isinstance(sphere, Sphere):
                return False
            self.spheres.add(sphere)
        return True

    def has_spheres(self):
        return self.spheres.count() != 0

    def set_is_primer(self, is_primer):
        self.is_primer = is_primer
        return True
