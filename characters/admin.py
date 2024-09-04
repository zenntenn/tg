from characters.models.core import (
    Archetype,
    Character,
    CharacterModel,
    Derangement,
    Group,
    Human,
    MeritFlaw,
    MeritFlawRating,
    Specialty,
)
from characters.models.mage import Effect, Resonance
from characters.models.mage.cabal import Cabal
from characters.models.mage.faction import MageFaction
from characters.models.mage.focus import (
    CorruptedPractice,
    Instrument,
    Paradigm,
    Practice,
    SpecializedPractice,
    Tenet,
)
from characters.models.mage.mage import Mage, PracticeRating, ResRating
from characters.models.mage.mtahuman import MtAHuman
from characters.models.mage.rote import Rote
from characters.models.vampire.vtmhuman import VtMHuman
from characters.models.werewolf.battlescar import BattleScar
from characters.models.werewolf.charm import SpiritCharm
from characters.models.werewolf.gift import Gift
from characters.models.werewolf.renownincident import RenownIncident
from characters.models.werewolf.rite import Rite
from characters.models.werewolf.spirit_character import SpiritCharacter
from characters.models.werewolf.totem import Totem
from characters.models.werewolf.tribe import Tribe
from characters.models.werewolf.wtahuman import WtAHuman
from characters.models.wraith.wtohuman import WtOHuman
from django.contrib import admin

admin.site.register(CharacterModel)


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "chronicle")


@admin.register(Human)
class HumanCharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "chronicle")


@admin.register(Archetype)
class ArchetypeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(MeritFlaw)
class MeritFlawAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(MeritFlawRating)


@admin.register(Derangement)
class DerangementAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "leader", "chronicle")


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ("name", "stat")


@admin.register(Resonance)
class ResonanceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "correspondence",
        "entropy",
        "forces",
        "life",
        "matter",
        "mind",
        "prime",
        "spirit",
        "time",
    )


@admin.register(Effect)
class EffectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "correspondence",
        "entropy",
        "forces",
        "life",
        "matter",
        "mind",
        "prime",
        "spirit",
        "time",
    )


@admin.register(Paradigm)
class ParadigmAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Practice)
class PracticeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(SpecializedPractice)
class SpecializedPracticeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(CorruptedPractice)
class CorruptedPracticeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Tenet)
class TenetAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(MageFaction)
class MageFactionAdmin(admin.ModelAdmin):
    list_display = ("name", "parent")


@admin.register(Rote)
class RoteAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "practice",
        "attribute",
        "ability",
        "correspondence",
        "entropy",
        "forces",
        "matter",
        "mind",
        "life",
        "prime",
        "spirit",
        "time",
    )

    def correspondence(self, obj):
        return obj.effect.correspondence

    def time(self, obj):
        return obj.effect.time

    def spirit(self, obj):
        return obj.effect.spirit

    def matter(self, obj):
        return obj.effect.matter

    def life(self, obj):
        return obj.effect.life

    def forces(self, obj):
        return obj.effect.forces

    def entropy(self, obj):
        return obj.effect.entropy

    def mind(self, obj):
        return obj.effect.mind

    def prime(self, obj):
        return obj.effect.prime


@admin.register(Totem)
class TotemAdmin(admin.ModelAdmin):
    list_display = ("name", "cost")


@admin.register(SpiritCharm)
class SpiritCharmAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(SpiritCharacter)
class SpiritCharacterAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(MtAHuman)


@admin.register(Mage)
class MageAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner",
        "arete",
        "affiliation",
        "faction",
        "subfaction",
        "essence",
        "affinity_sphere",
        "chronicle",
    )
    list_filter = ("owner", "arete", "essence", "affinity_sphere", "chronicle")


@admin.register(ResRating)
class ResRatingAdmin(admin.ModelAdmin):
    list_display = ("mage", "resonance", "rating")


@admin.register(Cabal)
class CabalAdmin(admin.ModelAdmin):
    list_display = ("name", "leader")


admin.site.register(VtMHuman)
admin.site.register(WtOHuman)
admin.site.register(PracticeRating)


admin.site.register(WtAHuman)


@admin.register(Rite)
class RiteAdmin(admin.ModelAdmin):
    list_display = ("name", "level", "type")


@admin.register(Tribe)
class TribeAdmin(admin.ModelAdmin):
    list_display = ("name", "willpower")


@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ("name", "rank", "allowed")


@admin.register(RenownIncident)
class RenownIncidentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "glory",
        "honor",
        "wisdom",
        "posthumous",
        "only_once",
        "breed",
        "rite",
    )


@admin.register(BattleScar)
class BattleScarAdmin(admin.ModelAdmin):
    list_display = ("name", "glory")
