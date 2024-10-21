from characters.forms.core.character_creation import CharacterCreationForm
from characters.models.core import Character, Derangement, Group, Human
from characters.models.core.ability_block import Ability
from characters.models.core.archetype import Archetype
from characters.models.core.merit_flaw_block import MeritFlaw
from characters.models.core.specialty import Specialty
from characters.models.core.statistic import Statistic
from characters.models.mage.effect import Effect
from characters.models.mage.faction import MageFaction
from characters.models.mage.focus import (
    CorruptedPractice,
    Instrument,
    Paradigm,
    Practice,
    SpecializedPractice,
    Tenet,
)
from characters.models.mage.mage import Mage
from characters.models.mage.mtahuman import MtAHuman
from characters.models.mage.resonance import Resonance
from characters.models.mage.rote import Rote
from characters.models.mage.sphere import Sphere
from characters.models.vampire.vtmhuman import VtMHuman
from characters.models.werewolf.charm import SpiritCharm
from characters.models.werewolf.spirit_character import SpiritCharacter
from characters.models.werewolf.totem import Totem
from characters.views import changeling, mage, vampire, werewolf, wraith
from core.utils import get_gameline_name
from core.views.generic import DictView
from django.forms import BaseModelForm
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View
from game.models import Chronicle, ObjectType

from .archetype import (
    ArchetypeCreateView,
    ArchetypeDetailView,
    ArchetypeListView,
    ArchetypeUpdateView,
)
from .character import CharacterCreateView, CharacterDetailView, CharacterUpdateView
from .derangement import (
    DerangementCreateView,
    DerangementDetailView,
    DerangementListView,
    DerangementUpdateView,
)
from .group import GroupCreateView, GroupDetailView, GroupUpdateView
from .human import (
    HumanAttributeView,
    HumanBasicsView,
    HumanCharacterCreationView,
    HumanCreateView,
    HumanDetailView,
    HumanUpdateView,
)
from .meritflaw import (
    MeritFlawCreateView,
    MeritFlawDetailView,
    MeritFlawListView,
    MeritFlawUpdateView,
)
from .specialty import (
    SpecialtyCreateView,
    SpecialtyDetailView,
    SpecialtyListView,
    SpecialtyUpdateView,
)


class GenericCharacterDetailView(DictView):
    view_mapping = {
        "character": CharacterDetailView,
        "human": HumanCharacterCreationView,
        "spirit_character": werewolf.SpiritDetailView,
        "mta_human": mage.MtAHumanDetailView,
        "mage": mage.MageCharacterCreationView,
        "vtm_human": vampire.VtMHumanDetailView,
        "wto_human": wraith.WtOHumanDetailView,
        "wta_human": werewolf.WtAHumanDetailView,
        "kinfolk": werewolf.KinfolkDetailView,
        "werewolf": werewolf.WerewolfDetailView,
        "fomor": werewolf.FomorDetailView,
        "changeling": changeling.ChangelingDetailView,
        "ctd_human": changeling.CtDHumanDetailView,
        "companion": mage.CopanionCharacterCreationView,
        "sorcerer": mage.SorcererCharacterCreationView,
    }
    model_class = Character
    key_property = "type"
    default_redirect = "characters:index wod"


class GenericGroupDetailView(DictView):
    view_mapping = {
        "group": GroupDetailView,
        "cabal": mage.CabalDetailView,
        "pack": werewolf.PackDetailView,
        "motley": changeling.MotleyDetailView,
    }
    model_class = Group
    key_property = "type"
    default_redirect = "characters:index wod"


class CharacterIndexView(View):
    chars = {
        "human": Human,
        "statistic": Statistic,
        "specialty": Specialty,
        "meritflaw": MeritFlaw,
        "group": Group,
        "derangement": Derangement,
        "character": Character,
        "archetype": Archetype,
        "ability": Ability,
        "vtm_human": VtMHuman,
        "totem": Totem,
        "spirit": SpiritCharacter,
        "spirit_charm": SpiritCharm,
        "sphere": Sphere,
        "rote": Rote,
        "resonance": Resonance,
        "instrument": Instrument,
        "practice": Practice,
        "specialized_practice": SpecializedPractice,
        "corrupted_practice": CorruptedPractice,
        "tenet": Tenet,
        "paradigm": Paradigm,
        "mage_faction": MageFaction,
        "effect": Effect,
        "mage": Mage,
        "mta_human": MtAHuman,
    }

    def get(self, request, *args, **kwargs):
        context = self.get_context()
        return render(request, "characters/index.html", context)

    def post(self, request, *args, **kwargs):
        context = self.get_context()
        action = request.POST.get("action")
        char_type = request.POST["char_type"]
        obj = ObjectType.objects.get(name=char_type)
        gameline = obj.gameline
        if action == "create":
            if gameline == "wod":
                redi = f"characters:create:{char_type}"
            elif gameline == "vtm":
                redi = f"characters:vampire:create:{char_type}"
            elif gameline == "wta":
                redi = f"characters:werewolf:create:{char_type}"
            elif gameline == "mta":
                redi = f"characters:mage:create:{char_type}"
            elif gameline == "wto":
                redi = f"characters:wraith:create:{char_type}"
            elif gameline == "ctd":
                redi = f"characters:changeling:create:{char_type}"
            return redirect(redi)
        if action == "index":
            if gameline == "wod":
                redi = f"characters:list:{char_type}"
            elif gameline == "vtm":
                redi = f"characters:vampire:list:{char_type}"
            elif gameline == "wta":
                redi = f"characters:werewolf:list:{char_type}"
            elif gameline == "mta":
                redi = f"characters:mage:list:{char_type}"
            elif gameline == "wto":
                redi = f"characters:wraith:list:{char_type}"
            elif gameline == "ctd":
                redi = f"characters:changeling:list:{char_type}"
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
                print("KEYERROR")
                raise Http404
            try:
                char.random()
            except Exception as e:
                raise Http404
            char.save()
            return redirect(char.get_absolute_url())
        return render(request, "characters/index.html", context)

    def get_context(self):
        game_characters = ObjectType.objects.filter(type="char")
        game_character_types = [x.name for x in game_characters]
        context = {
            "objects": game_characters,
        }

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
        context["form"] = CharacterCreationForm()
        if self.request.user.is_authenticated:
            context["header"] = self.request.user.profile.preferred_heading
        else:
            context["header"] = "wod_heading"

        return context
