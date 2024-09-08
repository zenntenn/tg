from characters.models.werewolf.charm import SpiritCharm
from django.views.generic import CreateView, DetailView, ListView, UpdateView


class SpiritCharmDetailView(DetailView):
    model = SpiritCharm
    template_name = "characters/werewolf/charm/detail.html"


class SpiritCharmCreateView(CreateView):
    model = SpiritCharm
    fields = ["name", "description"]
    template_name = "characters/werewolf/charm/form.html"


class SpiritCharmUpdateView(UpdateView):
    model = SpiritCharm
    fields = ["name", "description"]
    template_name = "characters/werewolf/charm/form.html"


class SpiritCharmListView(ListView):
    model = SpiritCharm
    ordering = ["name"]
    template_name = "characters/werewolf/charm/list.html"
