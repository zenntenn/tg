from django.views.generic import CreateView, DetailView, UpdateView
from items.models.core import ThrownWeapon


class ThrownWeaponDetailView(DetailView):
    model = ThrownWeapon
    template_name = "items/core/thrownweapon/detail.html"


class ThrownWeaponCreateView(CreateView):
    model = ThrownWeapon
    fields = ["name", "description", "difficulty", "damage", "damage_type", "conceal"]
    template_name = "items/core/thrownweapon/form.html"


class ThrownWeaponUpdateView(UpdateView):
    model = ThrownWeapon
    fields = ["name", "description", "difficulty", "damage", "damage_type", "conceal"]
    template_name = "items/core/thrownweapon/form.html"
