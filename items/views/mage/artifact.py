from typing import Any

from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView
from items.models.mage import WonderResonanceRating
from items.models.mage.artifact import Artifact


class ArtifactDetailView(DetailView):
    model = Artifact
    template_name = "items/mage/artifact/detail.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["resonance"] = WonderResonanceRating.objects.filter(
            wonder=self.object
        ).order_by("resonance__name")
        return context


class ArtifactCreateView(CreateView):
    model = Artifact
    fields = [
        "name",
        "rank",
        "background_cost",
        "quintessence_max",
        "description",
        "power",
    ]
    template_name = "items/mage/artifact/form.html"


class ArtifactUpdateView(UpdateView):
    model = Artifact
    fields = [
        "name",
        "rank",
        "background_cost",
        "quintessence_max",
        "description",
        "power",
    ]
    template_name = "items/mage/artifact/form.html"
