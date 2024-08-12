from django.contrib import admin
from locations.models.core import City, LocationModel
from locations.models.mage import Node, NodeMeritFlawRating, NodeResonanceRating

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
