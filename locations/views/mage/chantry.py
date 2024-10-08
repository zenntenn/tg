from typing import Any

from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView
from locations.models.mage.chantry import Chantry


class ChantryDetailView(DetailView):
    model = Chantry
    template_name = "locations/mage/chantry/detail.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        factions = []
        f = self.object.faction
        while f is not None:
            factions.append(f.name)
            f = f.parent
        factions.reverse()
        factions = "/".join(factions)
        context["factions"] = factions
        return context


class ChantryCreateView(CreateView):
    model = Chantry
    fields = [
        "name",
        "parent",
        "description",
        "faction",
        "leadership_type",
        "leaders",
        "season",
        "chantry_type",
        "rank",
        "points",
        "allies",
        "arcane",
        "backup",
        "cult",
        "elders",
        "integrated_effects",
        "retainers",
        "spies",
        "resources",
        "enhancement",
        "requisitions",
        "reality_zone_rating",
        "node_rating",
        "library_rating",
        "chantry_library",
        "nodes",
        "members",
        "cabals",
        "ambassador",
        "node_tender",
        "investigator",
        "guardian",
        "teacher",
    ]
    template_name = "locations/mage/chantry/form.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["name"].widget.attrs.update({"placeholder": "Enter name here"})
        form.fields["description"].widget.attrs.update(
            {"placeholder": "Enter description here"}
        )
        return form


class ChantryUpdateView(UpdateView):
    model = Chantry
    fields = [
        "name",
        "parent",
        "description",
        "faction",
        "leadership_type",
        "leaders",
        "season",
        "chantry_type",
        "rank",
        "points",
        "allies",
        "arcane",
        "backup",
        "cult",
        "elders",
        "integrated_effects",
        "retainers",
        "spies",
        "resources",
        "enhancement",
        "requisitions",
        "reality_zone_rating",
        "node_rating",
        "library_rating",
        "chantry_library",
        "nodes",
        "members",
        "cabals",
        "ambassador",
        "node_tender",
        "investigator",
        "guardian",
        "teacher",
    ]
    template_name = "locations/mage/chantry/form.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["name"].widget.attrs.update({"placeholder": "Enter name here"})
        form.fields["description"].widget.attrs.update(
            {"placeholder": "Enter description here"}
        )
        return form
