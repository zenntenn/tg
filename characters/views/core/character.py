from typing import Any

from characters.models.core import Character
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView
from game.models import Scene


# Create your views here.
class CharacterDetailView(DetailView):
    model = Character
    template_name = "characters/core/character/detail.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["scenes"] = Scene.objects.filter(characters=context["object"]).order_by(
            "date_of_scene"
        )
        return context


class CharacterCreateView(CreateView):
    model = Character
    fields = "__all__"
    template_name = "characters/core/character/form.html"


class CharacterUpdateView(UpdateView):
    model = Character
    fields = "__all__"
    template_name = "characters/core/character/form.html"
