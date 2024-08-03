from characters.models.core import Character, CharacterModel, Human
from django.contrib import admin

# Register your models here.
admin.site.register(CharacterModel)


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "owner")


@admin.register(Human)
class HumanCharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "owner")
