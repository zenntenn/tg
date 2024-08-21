from characters.models.mage.cabal import Cabal
from django.contrib import admin
from locations.models.core import City, LocationModel
from locations.models.mage import Node, NodeMeritFlawRating, NodeResonanceRating
from locations.models.mage.chantry import Chantry
from locations.models.mage.library import Library
from locations.models.mage.realm import HorizonRealm
from locations.models.mage.sector import Sector
from locations.models.werewolf.caern import Caern

# Register your models here.
admin.site.register(LocationModel)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "parent")


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ("name", "rank", "parent")


admin.site.register(NodeMeritFlawRating)
admin.site.register(NodeResonanceRating)


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ("name", "rank", "faction", "parent")


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(HorizonRealm)


@admin.register(Caern)
class CaernAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Cabal)
class CabalAdmin(admin.ModelAdmin):
    list_display = ("name", "leader")


@admin.register(Chantry)
class ChantryAdmin(admin.ModelAdmin):
    list_display = ("name", "rank", "parent", "faction")
