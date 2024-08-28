from typing import Any

from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView
from items.models.mage import WonderResonanceRating
from items.models.mage.talisman import Talisman


class TalismanDetailView(DetailView):
    model = Talisman
    template_name = "items/mage/talisman/detail.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["resonance"] = WonderResonanceRating.objects.filter(
            wonder=self.object
        ).order_by("resonance__name")
        return context


class TalismanCreateView(CreateView):
    model = Talisman
    fields = [
        "name",
        "rank",
        "background_cost",
        "quintessence_max",
        "description",
        "powers",
    ]
    template_name = "items/mage/talisman/form.html"


class TalismanUpdateView(UpdateView):
    model = Talisman
    fields = [
        "name",
        "rank",
        "background_cost",
        "quintessence_max",
        "description",
        "powers",
    ]
    template_name = "items/mage/talisman/form.html"
