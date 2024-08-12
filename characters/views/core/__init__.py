from characters.models.core import Character, Derangement, Group, Human
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View

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
