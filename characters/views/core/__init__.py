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
from django.db.models import OuterRef, Subquery
from django.forms import BaseModelForm
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView, UpdateView, View
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


class CharacterIndexView(ListView):
    model = Human
    template_name = "characters/charlist.html"

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

    def get_queryset(self):
        CharacterGroup = Human.group_set.through

        # Subquery to get the first group id for each character
        first_group_id = Subquery(
            CharacterGroup.objects.filter(human_id=OuterRef("pk"))
            .order_by(
                "group_id"
            )  # Assuming ordering by 'group_id', adjust if different
            .values("group_id")[:1]
        )

        # Annotating the queryset with the first group id
        characters = (
            Human.objects.exclude(status__in=["Dec", "Ret"])
            .exclude(npc=True)
            .annotate(first_group_id=first_group_id)
            .select_related("chronicle")
            .order_by("chronicle__id", "-first_group_id", "name")
        )

        return characters

    def post(self, request, *args, **kwargs):
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
        context = self.get_context_data()
        return render(request, "characters/charlist.html", context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Characters"
        context["button_include"] = True
        context["form"] = CharacterCreationForm(user=self.request.user)
        context["header"] = "wod_heading"
        return context


class RetiredCharacterIndex(ListView):
    model = Character
    template_name = "characters/charlist.html"

    def get_queryset(self):
        CharacterGroup = Human.group_set.through

        # Subquery to get the first group id for each character
        first_group_id = Subquery(
            CharacterGroup.objects.filter(human_id=OuterRef("pk"))
            .order_by(
                "group_id"
            )  # Assuming ordering by 'group_id', adjust if different
            .values("group_id")[:1]
        )

        # Annotating the queryset with the first group id
        characters = (
            Human.objects.filter(status="Ret")
            .annotate(first_group_id=first_group_id)
            .select_related("chronicle")
            .order_by("chronicle__id", "-first_group_id", "name")
        )

        return characters

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Retired Characters"
        return context


class DeceasedCharacterIndex(ListView):
    model = Character
    template_name = "characters/charlist.html"

    def get_queryset(self):
        CharacterGroup = Human.group_set.through

        # Subquery to get the first group id for each character
        first_group_id = Subquery(
            CharacterGroup.objects.filter(human_id=OuterRef("pk"))
            .order_by(
                "group_id"
            )  # Assuming ordering by 'group_id', adjust if different
            .values("group_id")[:1]
        )

        # Annotating the queryset with the first group id
        characters = (
            Human.objects.filter(status="Dec")
            .annotate(first_group_id=first_group_id)
            .select_related("chronicle")
            .order_by("chronicle__id", "-first_group_id", "name")
        )

        return characters

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Deceased Characters"
        return context


class NPCCharacterIndex(ListView):
    model = Character
    template_name = "characters/charlist.html"

    def get_queryset(self):
        CharacterGroup = Human.group_set.through

        # Subquery to get the first group id for each character
        first_group_id = Subquery(
            CharacterGroup.objects.filter(human_id=OuterRef("pk"))
            .order_by(
                "group_id"
            )  # Assuming ordering by 'group_id', adjust if different
            .values("group_id")[:1]
        )

        # Annotating the queryset with the first group id
        characters = (
            Human.objects.filter(npc=True)
            .annotate(first_group_id=first_group_id)
            .select_related("chronicle")
            .order_by("chronicle__id", "-first_group_id", "name")
        )

        return characters

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Deceased Characters"
        return context
