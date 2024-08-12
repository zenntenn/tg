from django.views.generic import CreateView, DetailView, UpdateView
from items.models.core import Weapon


# Create your views here.
class WeaponDetailView(DetailView):
    model = Weapon
    template_name = "items/core/weapon/detail.html"


class WeaponCreateView(CreateView):
    model = Weapon
    fields = ["name", "description", "difficulty", "damage", "damage_type", "conceal"]
    template_name = "items/core/weapon/form.html"


class WeaponUpdateView(UpdateView):
    model = Weapon
    fields = ["name", "description", "difficulty", "damage", "damage_type", "conceal"]
    template_name = "items/core/weapon/form.html"
