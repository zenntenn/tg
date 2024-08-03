from characters.models.core import Character, Human
from django.shortcuts import redirect, render
from django.views.generic import DetailView, View


# Create your views here.
class CharacterDetailView(DetailView):
    model = Character
    template_name = "characters/character/detail.html"


class HumanDetailView(DetailView):
    model = Human
    template_name = "characters/human/detail.html"


class GenericCharacterDetailView(View):
    character_views = {
        "character": CharacterDetailView,
        "human": HumanDetailView,
    }

    def get(self, request, *args, **kwargs):
        char = Character.objects.get(pk=kwargs["pk"])
        if char.type in self.character_views:
            return self.character_views[char.type].as_view()(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        char = Character.objects.get(pk=kwargs["pk"])
        if char.type in self.character_views:
            return self.character_views[char.type].as_view()(request, *args, **kwargs)
