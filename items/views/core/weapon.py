from django.views.generic import CreateView, DetailView, UpdateView
from items.models.core import Weapon


class WeaponDetailView(DetailView):
    model = Weapon
    template_name = "items/core/weapon/detail.html"


class WeaponCreateView(CreateView):
    model = Weapon
    fields = ["name", "description", "difficulty", "damage", "damage_type", "conceal"]
    template_name = "items/core/weapon/form.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["name"].widget.attrs.update({"placeholder": "Enter name here"})
        form.fields["description"].widget.attrs.update(
            {"placeholder": "Enter description here"}
        )
        return form


class WeaponUpdateView(UpdateView):
    model = Weapon
    fields = ["name", "description", "difficulty", "damage", "damage_type", "conceal"]
    template_name = "items/core/weapon/form.html"
