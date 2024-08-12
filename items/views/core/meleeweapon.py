from django.views.generic import CreateView, DetailView, UpdateView
from items.models.core import MeleeWeapon


# Create your views here.
class MeleeWeaponDetailView(DetailView):
    model = MeleeWeapon
    template_name = "items/core/meleeweapon/detail.html"


class MeleeWeaponCreateView(CreateView):
    model = MeleeWeapon
    fields = ["name", "description", "difficulty", "damage", "damage_type", "conceal"]
    template_name = "items/core/meleeweapon/form.html"


class MeleeWeaponUpdateView(UpdateView):
    model = MeleeWeapon
    fields = ["name", "description", "difficulty", "damage", "damage_type", "conceal"]
    template_name = "items/core/meleeweapon/form.html"
