from characters.models.core import Human
from characters.models.core.ability import Ability
from characters.models.core.attribute import Attribute
from characters.models.core.background import Background
from characters.models.core.meritflaw import MeritFlaw
from characters.views.core.character import CharacterDetailView
from core.views.approved_user_mixin import SpecialUserMixin
from core.views.generic import DictView
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView


class HumanDetailView(SpecialUserMixin, CharacterDetailView):
    model = Human
    template_name = "characters/core/human/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(self.object, self.request.user)
        return context

class HumanCreateView(CreateView):
    model = Human
    fields = [
        "name",
        "owner",
        "description",
        "nature",
        "demeanor",
        "specialties",
        "willpower",
        "derangements",
        "age",
        "apparent_age",
        "date_of_birth",
        "hair",
        "eyes",
        "ethnicity",
        "nationality",
        "height",
        "weight",
        "sex",
        "merits_and_flaws",
        "childhood",
        "history",
        "goals",
        "notes",
        "strength",
        "dexterity",
        "stamina",
        "perception",
        "intelligence",
        "wits",
        "charisma",
        "manipulation",
        "appearance",
    ]
    template_name = "characters/core/human/form.html"


class HumanUpdateView(SpecialUserMixin, UpdateView):
    model = Human
    fields = [
        "name",
        "owner",
        "description",
        "nature",
        "demeanor",
        "specialties",
        "willpower",
        "derangements",
        "age",
        "apparent_age",
        "date_of_birth",
        "hair",
        "eyes",
        "ethnicity",
        "nationality",
        "height",
        "weight",
        "sex",
        "merits_and_flaws",
        "childhood",
        "history",
        "goals",
        "notes",
        "strength",
        "dexterity",
        "stamina",
        "perception",
        "intelligence",
        "wits",
        "charisma",
        "manipulation",
        "appearance",
    ]
    template_name = "characters/core/human/form.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(self.object, self.request.user)
        return context


class HumanBasicsView(CreateView):
    model = Human
    fields = [
        "name",
        "nature",
        "demeanor",
        "concept",
    ]
    template_name = "characters/core/human/humanbasics.html"


class HumanAttributeView(SpecialUserMixin, UpdateView):
    model = Human
    fields = [
        "strength",
        "dexterity",
        "stamina",
        "perception",
        "intelligence",
        "wits",
        "charisma",
        "manipulation",
        "appearance",
    ]
    template_name = "characters/core/human/attributes.html"

    def form_valid(self, form):
        strength = form.cleaned_data.get("strength")
        dexterity = form.cleaned_data.get("dexterity")
        stamina = form.cleaned_data.get("stamina")
        perception = form.cleaned_data.get("perception")
        intelligence = form.cleaned_data.get("intelligence")
        wits = form.cleaned_data.get("wits")
        charisma = form.cleaned_data.get("charisma")
        manipulation = form.cleaned_data.get("manipulation")
        appearance = form.cleaned_data.get("appearance")

        for attribute in [
            strength,
            dexterity,
            stamina,
            perception,
            intelligence,
            wits,
            charisma,
            manipulation,
            appearance,
        ]:
            if attribute < 1 or attribute > 5:
                form.add_error(None, "Attributes must range from 1-5")
                return self.form_invalid(form)

        triple = [
            strength + dexterity + stamina,
            perception + intelligence + wits,
            charisma + manipulation + appearance,
        ]
        triple.sort()
        if triple != [3 + 3, 3 + 5, 3 + 7]:
            form.add_error(None, "Attributes must be distributed 7/5/3")
            return self.form_invalid(form)
        self.object.creation_status += 1
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(self.object, self.request.user)
        return context

class HumanBiographicalInformation(SpecialUserMixin, UpdateView):
    model = Human
    fields = [
        "age",
        "apparent_age",
        "date_of_birth",
        "hair",
        "eyes",
        "ethnicity",
        "nationality",
        "height",
        "weight",
        "sex",
        "childhood",
        "history",
        "goals",
        "notes",
    ]
    template_name = "characters/core/human/bio.html"

    def form_valid(self, form):
        self.object.creation_status += 1
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(self.object, self.request.user)
        return context

class HumanCharacterCreationView(DictView):
    view_mapping = {1: HumanAttributeView, 2: HumanBiographicalInformation}
    model_class = Human
    key_property = "creation_status"
    default_redirect = HumanDetailView

    def is_valid_key(self, obj, key):
        return key in self.view_mapping and obj.status == "Un"


def load_examples(request):
    category_choice = request.GET.get("category")
    if category_choice == "Attribute":
        examples = Attribute.objects.all()
    elif category_choice == "Ability":
        examples = Ability.objects.all()
    elif category_choice == "Background":
        examples = Background.objects.all()
    elif category_choice == "MeritFlaw":
        examples = MeritFlaw.objects.all()
    else:
        examples = []
    return render(
        request,
        "characters/core/human/load_examples_dropdown_list.html",
        {"examples": examples},
    )


def load_values(request):
    mf = MeritFlaw.objects.get(pk=request.GET.get("example"))
    ratings = [x.value for x in mf.ratings.all()]
    return render(
        request,
        "characters/core/human/load_values_dropdown_list.html",
        {"values": ratings},
    )
