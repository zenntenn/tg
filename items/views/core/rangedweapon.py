from django.views.generic import CreateView, DetailView, UpdateView
from items.models.core import RangedWeapon


class RangedWeaponDetailView(DetailView):
    model = RangedWeapon
    template_name = "items/core/rangedweapon/detail.html"


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
    template_name = "items/core/rangedweapon/form.html"


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
    template_name = "items/core/rangedweapon/form.html"
