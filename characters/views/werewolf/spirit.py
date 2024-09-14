from characters.models.werewolf.spirit_character import SpiritCharacter
from django.views.generic import CreateView, DetailView, UpdateView

from core.views.approved_user_mixin import SpecialUserMixin


class SpiritDetailView(SpecialUserMixin, DetailView):
    model = SpiritCharacter
    template_name = "characters/werewolf/spirit/detail.html"


class SpiritCreateView(CreateView):
    model = SpiritCharacter
    fields = ["name", "description", "willpower", "rage", "gnosis", "essence"]
    template_name = "characters/werewolf/spirit/form.html"


class SpiritUpdateView(SpecialUserMixin, UpdateView):
    model = SpiritCharacter
    fields = ["name", "description", "willpower", "rage", "gnosis", "essence"]
    template_name = "characters/werewolf/spirit/form.html"
