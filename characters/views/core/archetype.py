from characters.models.core import Archetype
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView


class ArchetypeDetailView(DetailView):
    model = Archetype
    template_name = "characters/core/archetype/detail.html"


class ArchetypeCreateView(CreateView):
    model = Archetype
    fields = ["name", "description"]
    template_name = "characters/core/archetype/form.html"


class ArchetypeUpdateView(UpdateView):
    model = Archetype
    fields = ["name", "description"]
    template_name = "characters/core/archetype/form.html"
