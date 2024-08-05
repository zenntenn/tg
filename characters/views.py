from characters.models.core import Archetype, Character, Human, MeritFlaw
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


class ArchetypeDetailView(DetailView):
    model = Archetype
    template_name = "characters/archetype/detail.html"


class MeritFlawDetailView(View):
    def get(self, request, *args, **kwargs):
        mf = MeritFlaw.objects.get(pk=kwargs["pk"])
        context = self.get_context(mf)
        return render(request, "characters/meritflaw/detail.html", context)

    def get_context(self, mf):
        context = {}
        context["object"] = mf
        mf_ratings = list(mf.ratings.values_list("value", flat=True))
        mf_ratings.sort()
        context["ratings"] = ", ".join([str(x) for x in mf_ratings])
        return context
