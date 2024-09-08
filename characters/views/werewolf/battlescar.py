from characters.models.werewolf.battlescar import BattleScar
from django.views.generic import CreateView, DetailView, ListView, UpdateView


class BattleScarDetailView(DetailView):
    model = BattleScar
    template_name = "characters/werewolf/battlescar/detail.html"


class BattleScarCreateView(CreateView):
    model = BattleScar
    fields = ["name", "description", "glory"]
    template_name = "characters/werewolf/battlescar/form.html"


class BattleScarUpdateView(UpdateView):
    model = BattleScar
    fields = ["name", "description", "glory"]
    template_name = "characters/werewolf/battlescar/form.html"


class BattleScarListView(ListView):
    model = BattleScar
    ordering = ["name"]
    template_name = "characters/werewolf/battlescar/list.html"
