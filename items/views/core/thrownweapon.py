from django.views.generic import CreateView, DetailView, UpdateView
from items.models.core import ThrownWeapon


class ThrownWeaponDetailView(DetailView):
    model = ThrownWeapon
    template_name = "items/core/thrownweapon/detail.html"


class ThrownWeaponCreateView(CreateView):
    model = ThrownWeapon
    fields = ["name", "description", "difficulty", "damage", "damage_type", "conceal"]
    template_name = "items/core/thrownweapon/form.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["name"].widget.attrs.update({"placeholder": "Enter name here"})
        form.fields["description"].widget.attrs.update(
            {"placeholder": "Enter description here"}
        )
        return form


class ThrownWeaponUpdateView(UpdateView):
    model = ThrownWeapon
    fields = ["name", "description", "difficulty", "damage", "damage_type", "conceal"]
    template_name = "items/core/thrownweapon/form.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["name"].widget.attrs.update({"placeholder": "Enter name here"})
        form.fields["description"].widget.attrs.update(
            {"placeholder": "Enter description here"}
        )
        return form
