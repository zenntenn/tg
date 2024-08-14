from characters.models.werewolf.charm import SpiritCharm
from django.views.generic import CreateView, DetailView, UpdateView


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
