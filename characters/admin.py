from characters.models.core import (
    Archetype,
    Character,
    CharacterModel,
    Derangement,
    Group,
    Human,
    MeritFlaw,
    MeritFlawRating,
)
from django.contrib import admin

# Register your models here.
admin.site.register(CharacterModel)


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "owner")


@admin.register(Human)
class HumanCharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "owner")


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
