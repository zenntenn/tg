from django.shortcuts import redirect, render
from django.views.generic import DetailView, View
from items.models.core import ItemModel, MeleeWeapon, RangedWeapon, Weapon, ThrownWeapon


# Create your views here.
class ItemDetailView(DetailView):
    model = ItemModel
    template_name = "items/detail.html"


class WeaponDetailView(DetailView):
    model = Weapon
    template_name = "items/weapon/detail.html"


class MeleeWeaponDetailView(DetailView):
    model = MeleeWeapon
    template_name = "items/meleeweapon/detail.html"


class ThrownWeaponDetailView(DetailView):
    model = ThrownWeapon
    template_name = "items/thrownweapon/detail.html"


class RangedWeaponDetailView(DetailView):
    model = RangedWeapon
    template_name = "items/rangedweapon/detail.html"


class GenericItemDetailView(View):
    views = {
        "item": ItemDetailView,
        "weapon": WeaponDetailView,
        "melee_weapon": MeleeWeaponDetailView,
        "thrown_weapon": ThrownWeaponDetailView,
        "ranged_weapon": RangedWeaponDetailView,
    }

    def get(self, request, *args, **kwargs):
        item = ItemModel.objects.get(pk=kwargs["pk"])
        if item.type in self.views:
            return self.views[item.type].as_view()(request, *args, **kwargs)
