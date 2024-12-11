from typing import Any

from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView
from items.forms.mage.wonder import WonderForm
from items.models.mage import Wonder, WonderResonanceRating


class WonderDetailView(DetailView):
    model = Wonder
    template_name = "items/mage/wonder/detail.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["resonance"] = WonderResonanceRating.objects.filter(
            wonder=self.object
        ).order_by("resonance__name")
        return context


class WonderCreateView(CreateView):
    form_class = WonderForm
    template_name = "items/mage/wonder/form.html"


class WonderUpdateView(UpdateView):
    form_class = WonderForm
    template_name = "items/mage/wonder/form.html"
