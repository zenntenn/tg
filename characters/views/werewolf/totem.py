from characters.models.werewolf.totem import Totem
from django.views.generic import CreateView, DetailView, ListView, UpdateView


class TotemDetailView(DetailView):
    model = Totem
    template_name = "characters/werewolf/totem/detail.html"


class TotemCreateView(CreateView):
    model = Totem
    fields = [
        "name",
        "description",
        "cost",
        "totem_type",
        "individual_traits",
        "pack_traits",
        "ban",
    ]
    template_name = "characters/werewolf/totem/form.html"


class TotemUpdateView(UpdateView):
    model = Totem
    fields = [
        "name",
        "description",
        "cost",
        "totem_type",
        "individual_traits",
        "pack_traits",
        "ban",
    ]
    template_name = "characters/werewolf/totem/form.html"


class TotemListView(ListView):
    model = Totem
    ordering = ["name"]
    template_name = "characters/werewolf/totem/list.html"
