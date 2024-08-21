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
    fields = "__all__"
    template_name = "locations/mage/chantry/form.html"


class ChantryUpdateView(UpdateView):
    model = Chantry
    fields = "__all__"
    template_name = "locations/mage/chantry/form.html"
