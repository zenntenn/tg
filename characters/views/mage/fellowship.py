from typing import Any

from characters.models.mage.fellowship import SorcererFellowship
from django.views.generic import CreateView, DetailView, ListView, UpdateView


class SorcererFellowshipDetailView(DetailView):
    model = SorcererFellowship
    template_name = "characters/mage/sorcerer_fellowship/detail.html"


class SorcererFellowshipCreateView(CreateView):
    model = SorcererFellowship
    fields = ["name", "description", "favored_attributes", "favored_paths"]
    template_name = "characters/mage/sorcerer_fellowship/form.html"


class SorcererFellowshipUpdateView(UpdateView):
    model = SorcererFellowship
    fields = ["name", "description", "favored_attributes", "favored_paths"]
    template_name = "characters/mage/sorcerer_fellowship/form.html"


class SorcererFellowshipListView(ListView):
    model = SorcererFellowship
    ordering = ["name"]
    template_name = "characters/mage/sorcerer_fellowship/list.html"
