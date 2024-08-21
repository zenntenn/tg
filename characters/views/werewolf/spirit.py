from characters.models.werewolf.spirit_character import SpiritCharacter
from django.views.generic import CreateView, DetailView, UpdateView


class SpiritDetailView(DetailView):
    model = SpiritCharacter
    template_name = "characters/werewolf/spirit/detail.html"


class SpiritCreateView(CreateView):
    model = SpiritCharacter
    fields = ["name", "description", "willpower", "rage", "gnosis", "essence"]
    template_name = "characters/werewolf/spirit/form.html"


class SpiritUpdateView(UpdateView):
    model = SpiritCharacter
    fields = ["name", "description", "willpower", "rage", "gnosis", "essence"]
    template_name = "characters/werewolf/spirit/form.html"
