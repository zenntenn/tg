from typing import Any

from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView
from locations.models.mage import Node, NodeMeritFlawRating, NodeResonanceRating


class NodeDetailView(DetailView):
    model = Node
    template_name = "locations/mage/node/detail.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["resonance"] = NodeResonanceRating.objects.filter(
            node=self.object
        ).order_by("resonance__name")
        context["merits_and_flaws"] = NodeMeritFlawRating.objects.filter(
            node=self.object
        ).order_by("mf__name")
        return context


class NodeCreateView(CreateView):
    model = Node
    fields = [
        "name",
        "parent",
        "reality_zone",
        "description",
        "rank",
        "size",
        "quintessence_per_week",
        "quintessence_form",
        "tass_per_week",
        "tass_form",
        "merits_and_flaws",
        "resonance",
    ]
    template_name = "locations/mage/node/form.html"


class NodeUpdateView(UpdateView):
    model = Node
    fields = [
        "name",
        "parent",
        "reality_zone",
        "description",
        "rank",
        "size",
        "quintessence_per_week",
        "quintessence_form",
        "tass_per_week",
        "tass_form",
        "merits_and_flaws",
        "resonance",
    ]
    template_name = "locations/mage/node/form.html"
