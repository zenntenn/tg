from django.contrib import admin
from locations.models.core import City, LocationModel

# Register your models here.
admin.site.register(LocationModel)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "parent")
