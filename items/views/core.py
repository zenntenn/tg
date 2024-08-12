from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View
from items.models.core import (
    ItemModel,
    Material,
    Medium,
    MeleeWeapon,
    RangedWeapon,
    ThrownWeapon,
    Weapon,
)

from . import mage


# Create your views here.
class ItemDetailView(DetailView):
    model = ItemModel
    template_name = "items/item/detail.html"


class ItemCreateView(CreateView):
    model = ItemModel
    fields = ["name", "description"]
    template_name = "items/item/form.html"


class ItemUpdateView(UpdateView):
    model = ItemModel
    fields = ["name", "description"]
    template_name = "items/item/form.html"


class WeaponDetailView(DetailView):
    model = Weapon
    template_name = "items/weapon/detail.html"


class WeaponCreateView(CreateView):
    model = Weapon
    fields = ["name", "description", "difficulty", "damage", "damage_type", "conceal"]
    template_name = "items/weapon/form.html"


class WeaponUpdateView(UpdateView):
    model = Weapon
    fields = ["name", "description", "difficulty", "damage", "damage_type", "conceal"]
    template_name = "items/weapon/form.html"


class MeleeWeaponDetailView(DetailView):
    model = MeleeWeapon
    template_name = "items/meleeweapon/detail.html"


class MeleeWeaponCreateView(CreateView):
    model = MeleeWeapon
    fields = ["name", "description", "difficulty", "damage", "damage_type", "conceal"]
    template_name = "items/meleeweapon/form.html"


class MeleeWeaponUpdateView(UpdateView):
    model = MeleeWeapon
    fields = ["name", "description", "difficulty", "damage", "damage_type", "conceal"]
    template_name = "items/meleeweapon/form.html"


class ThrownWeaponDetailView(DetailView):
    model = ThrownWeapon
    template_name = "items/thrownweapon/detail.html"


class ThrownWeaponCreateView(CreateView):
    model = ThrownWeapon
    fields = ["name", "description", "difficulty", "damage", "damage_type", "conceal"]
    template_name = "items/thrownweapon/form.html"


class ThrownWeaponUpdateView(UpdateView):
    model = ThrownWeapon
    fields = ["name", "description", "difficulty", "damage", "damage_type", "conceal"]
    template_name = "items/thrownweapon/form.html"


class RangedWeaponDetailView(DetailView):
    model = RangedWeapon
    template_name = "items/rangedweapon/detail.html"


class RangedWeaponCreateView(CreateView):
    model = RangedWeapon
    fields = [
        "name",
        "description",
        "difficulty",
        "damage",
        "damage_type",
        "conceal",
        "range",
        "rate",
        "clip",
    ]
    template_name = "items/rangedweapon/form.html"


class RangedWeaponUpdateView(UpdateView):
    model = RangedWeapon
    fields = [
        "name",
        "description",
        "difficulty",
        "damage",
        "damage_type",
        "conceal",
        "range",
        "rate",
        "clip",
    ]
    template_name = "items/rangedweapon/form.html"


class GenericItemDetailView(View):
    views = {
        "item": ItemDetailView,
        "weapon": WeaponDetailView,
        "melee_weapon": MeleeWeaponDetailView,
        "thrown_weapon": ThrownWeaponDetailView,
        "ranged_weapon": RangedWeaponDetailView,
        "wonder": mage.WonderDetailView,
        "charm": mage.CharmDetailView,
    }

    def get(self, request, *args, **kwargs):
        item = ItemModel.objects.get(pk=kwargs["pk"])
        if item.type in self.views:
            return self.views[item.type].as_view()(request, *args, **kwargs)


class MediumDetailView(DetailView):
    model = Medium
    template_name = "items/medium/detail.html"


class MaterialDetailView(DetailView):
    model = Material
    template_name = "items/material/detail.html"


class MediumCreateView(CreateView):
    model = Medium
    fields = "__all__"
    template_name = "items/medium/form.html"


class MediumUpdateView(UpdateView):
    model = Medium
    fields = "__all__"
    template_name = "items/medium/form.html"


class MaterialCreateView(CreateView):
    model = Material
    fields = "__all__"
    template_name = "items/material/form.html"


class MaterialUpdateView(UpdateView):
    model = Material
    fields = "__all__"
    template_name = "items/material/form.html"
