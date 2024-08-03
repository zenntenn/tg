from django.contrib import admin
from items.models.core import ItemModel, Weapon


# Register your models here.
@admin.register(ItemModel)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Weapon)
