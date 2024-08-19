from django.contrib import admin
from characters.models.mage.mtahuman import MtAHuman
from locations.models.core import City, LocationModel
from locations.models.mage import Node, NodeMeritFlawRating, NodeResonanceRating
from locations.models.mage.library import Library
from locations.models.mage.realm import HorizonRealm
from locations.models.mage.sector import Sector

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
admin.site.register(MtAHuman)
