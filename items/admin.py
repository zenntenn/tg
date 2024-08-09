from django.contrib import admin
from items.models.core import (
    ItemModel,
    Material,
    Medium,
    MeleeWeapon,
    RangedWeapon,
    ThrownWeapon,
    Weapon,
)


# Register your models here.
@admin.register(ItemModel)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Weapon)
admin.site.register(MeleeWeapon)
admin.site.register(ThrownWeapon)
admin.site.register(RangedWeapon)


@admin.register(Medium)
class MediumAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Medium"
        verbose_name_plural = "Mediums"


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materials"

@admin.register(Wonder)
class WonderAdmin(admin.ModelAdmin):
    list_display = ("name", "rank", "background_cost", "quintessence_max")

