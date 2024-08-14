from characters.models.werewolf.spirit import Spirit
from django.views.generic import CreateView, DetailView, UpdateView


class SpiritDetailView(DetailView):
    model = Spirit
    template_name = "characters/werewolf/spirit/detail.html"


class SpiritCreateView(CreateView):
    model = Spirit
    fields = ["name", "description", "willpower", "rage", "gnosis", "essence"]
    template_name = "characters/werewolf/spirit/form.html"


class SpiritUpdateView(UpdateView):
    model = Spirit
    fields = ["name", "description", "willpower", "rage", "gnosis", "essence"]
    template_name = "characters/werewolf/spirit/form.html"
