from characters.models.core import Archetype
from django.views.generic import CreateView, DetailView, ListView, UpdateView


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


class ArchetypeListView(ListView):
    model = Archetype
    ordering = ["name"]
    template_name = "characters/core/archetype/list.html"
