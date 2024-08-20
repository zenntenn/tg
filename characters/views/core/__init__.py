from characters.forms.core.character_creation import CharacterCreationForm
from characters.models.core import Character, Derangement, Group, Human
from characters.views import mage, werewolf
from core.utils import get_gameline_name
from django.forms import BaseModelForm
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View
from game.models import Chronicle, ObjectType

from .archetype import ArchetypeCreateView, ArchetypeDetailView, ArchetypeUpdateView
from .character import CharacterCreateView, CharacterDetailView, CharacterUpdateView
from .derangement import (
    DerangementCreateView,
    DerangementDetailView,
    DerangementUpdateView,
)
from .group import GroupCreateView, GroupDetailView, GroupUpdateView
from .human import HumanCreateView, HumanDetailView, HumanUpdateView
from .meritflaw import MeritFlawCreateView, MeritFlawDetailView, MeritFlawUpdateView
from .specialty import SpecialtyCreateView, SpecialtyDetailView, SpecialtyUpdateView


# Create your views here.
class GenericCharacterDetailView(View):
    character_views = {
        "character": CharacterDetailView,
        "human": HumanDetailView,
        "spirit": werewolf.SpiritDetailView,
        "mta_human": mage.MtAHumanDetailView,
    }

    def get(self, request, *args, **kwargs):
        char = Character.objects.get(pk=kwargs["pk"])
        if char.type in self.character_views:
            return self.character_views[char.type].as_view()(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        char = Character.objects.get(pk=kwargs["pk"])
        if char.type in self.character_views:
            return self.character_views[char.type].as_view()(request, *args, **kwargs)


class GenericGroupDetailView(View):
    group_views = {
        "group": GroupDetailView,
    }

    def get(self, request, *args, **kwargs):
        group = Group.objects.get(pk=kwargs["pk"])
        if group.type in self.group_views:
            return self.group_views[group.type].as_view()(request, *args, **kwargs)


class CharacterIndexView(View):
    chars = {}

    def get(self, request, *args, **kwargs):
        context = self.get_context(kwargs)
        return render(request, "characters/index.html", context)

    def post(self, request, *args, **kwargs):
        context = self.get_context(kwargs)
        action = request.POST.get("action")
        char_type = request.POST["char_type"]
        gameline = kwargs["gameline"]
        if action == "create":
            if gameline == "wod":
                redi = f"characters:create:{char_type}"
            elif gameline == "wta":
                redi = f"characters:werewolf:create:{char_type}"
            elif gameline == "mta":
                redi = f"characters:mage:create:{char_type}"
            return redirect(redi)
        elif action == "random":
            if request.user.is_authenticated:
                user = request.user
            else:
                user = None
            try:
                char = self.chars[request.POST["char_type"]].objects.create(
                    name=request.POST["name"], owner=user
                )
            except KeyError:
                raise Http404
            if request.POST["rank"] is None:
                rank = None
            else:
                rank = int(request.POST["rank"])
            try:
                char.random(rank=rank)
            except:
                raise Http404
            char.save()
            return redirect(char.get_absolute_url())
        return render(request, "characters/index.html", context)

    def get_context(self, kwargs):
        gameline = kwargs["gameline"]
        game_characters = ObjectType.objects.filter(gameline=gameline, type="char")
        game_character_types = [x.name for x in game_characters]
        context = {"objects": game_characters, "gameline": get_gameline_name(gameline)}

        chron_char_dict = {}
        chron_group_dict = {}
        for chron in list(Chronicle.objects.all()) + [None]:
            c = Character.objects.filter(chronicle=chron).order_by("name")
            g = Group.objects.filter(chronicle=chron).order_by("name")
            characters = [x for x in c if x.type in game_character_types]
            groups = [x for x in g if x.type in game_character_types]

            c = Character.objects.filter(
                id__in=[x.id for x in characters], chronicle=chron
            ).order_by("name")
            g = Group.objects.filter(
                id__in=[x.id for x in groups], chronicle=chron
            ).order_by("name")
            chron_char_dict[chron] = c
            chron_group_dict[chron] = g

        context["chron_char_dict"] = chron_char_dict
        context["chron_group_dict"] = chron_group_dict
        context["form"] = CharacterCreationForm(gameline=gameline)
        return context
