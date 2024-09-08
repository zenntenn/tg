from characters.models.werewolf.rite import Rite
from django.views.generic import CreateView, DetailView, ListView, UpdateView


class RiteDetailView(DetailView):
    model = Rite
    template_name = "characters/werewolf/rite/detail.html"


class RiteCreateView(CreateView):
    model = Rite
    fields = ["name", "level", "rite_type", "description"]
    template_name = "characters/werewolf/rite/form.html"


class RiteUpdateView(UpdateView):
    model = Rite
    fields = ["name", "level", "rite_type", "description"]
    template_name = "characters/werewolf/rite/form.html"


class RiteListView(ListView):
    model = Rite
    ordering = ["name"]
    template_name = "characters/werewolf/rite/list.html"
