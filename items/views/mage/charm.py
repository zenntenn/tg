from typing import Any

from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView
from items.models.mage import Charm, WonderResonanceRating


class CharmDetailView(DetailView):
    model = Charm
    template_name = "items/mage/charm/detail.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["resonance"] = WonderResonanceRating.objects.filter(
            wonder=self.object
        ).order_by("resonance__name")
        return context


class CharmCreateView(CreateView):
    model = Charm
    fields = [
        "name",
        "rank",
        "background_cost",
        "quintessence_max",
        "description",
        "power",
        "arete",
    ]
    template_name = "items/mage/charm/form.html"


class CharmUpdateView(UpdateView):
    model = Charm
    fields = [
        "name",
        "rank",
        "background_cost",
        "quintessence_max",
        "description",
        "power",
        "arete",
    ]
    template_name = "items/mage/charm/form.html"
