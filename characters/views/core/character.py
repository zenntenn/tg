from characters.models.core import Character
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView


# Create your views here.
class CharacterDetailView(DetailView):
    model = Character
    template_name = "characters/core/character/detail.html"


class CharacterCreateView(CreateView):
    model = Character
    fields = "__all__"
    template_name = "characters/core/character/form.html"


class CharacterUpdateView(UpdateView):
    model = Character
    fields = "__all__"
    template_name = "characters/core/character/form.html"
