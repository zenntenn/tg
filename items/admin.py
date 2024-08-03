from django.contrib import admin
from items.models.core import ItemModel, MeleeWeapon, ThrownWeapon, Weapon


# Register your models here.
@admin.register(ItemModel)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Weapon)
admin.site.register(MeleeWeapon)
admin.site.register(ThrownWeapon)
