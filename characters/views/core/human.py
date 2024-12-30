from typing import Any
from django.http import HttpResponseRedirect
from django.views import View
from characters.forms.core.freebies import HumanFreebiesForm
from characters.models.core import Human
from characters.models.core.ability_block import Ability
from characters.models.core.attribute_block import Attribute
from characters.models.core.background_block import Background, BackgroundRating
from characters.models.core.merit_flaw_block import MeritFlaw
from characters.views.core.character import CharacterDetailView
from core.views.approved_user_mixin import SpecialUserMixin
from core.views.generic import DictView
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, UpdateView

from game.models import ObjectType


class HumanDetailView(CharacterDetailView):
    model = Human
    template_name = "characters/core/human/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
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
        "merits_and_flaws",
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
        "merits_and_flaws",
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
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
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

    primary = 7
    secondary = 5
    tertiary = 3

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
        if triple != [3 + self.tertiary, 3 + self.secondary, 3 + self.primary]:
            form.add_error(
                None,
                f"Attributes must be distributed {self.primary}/{self.secondary}/{self.tertiary}",
            )
            return self.form_invalid(form)
        self.object.creation_status += 1
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        context["primary"] = self.primary
        context["secondary"] = self.secondary
        context["tertiary"] = self.tertiary
        return context


class HumanBiographicalInformation(SpecialUserMixin, UpdateView):
    model = Human
    fields = [
        "age",
        "apparent_age",
        "date_of_birth",
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
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
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
    # ratings = [x.value for x in mf.ratings.all()]
    # ratings.sort()
    ratings = mf.ratings.all()
    return render(
        request,
        "characters/core/human/load_values_dropdown_list.html",
        {"values": ratings},
    )


class HuamnFreebieFormPopulationView(View):
    primary_class = Human
    template_name = "characters/core/human/load_examples_dropdown_list.html"

    def get(self, request, *args, **kwargs):
        category_choice = request.GET.get("category")
        self.character = self.primary_class.objects.get(pk=request.GET.get("object"))
        examples = []
        if category_choice in self.category_method_map().keys():
            examples = self.category_method_map()[category_choice]()
        else:
            examples = []
        return render(request, self.template_name, {"examples": examples})

    def category_method_map(self):
        return {
            "Attribute": self.attribute_options,
            "Ability": self.ability_options,
            "New Background": self.new_background_options,
            "Existing Background": self.existing_background_options,
            "MeritFlaw": self.meritflaw_options,
        }

    def attribute_options(self):
        return [
            x
            for x in Attribute.objects.all()
            if getattr(self.character, x.property_name, 0) < 5
        ]

    def ability_options(self):
        return [
            x
            for x in Ability.objects.order_by("name")
            if getattr(self.character, x.property_name, 0) < 5
            and hasattr(self.character, x.property_name)
        ]

    def new_background_options(self):
        return Background.objects.filter(
            property_name__in=self.character.allowed_backgrounds
        ).order_by("name")

    def existing_background_options(self):
        return [
            x
            for x in BackgroundRating.objects.filter(char=self.character, rating__lt=5)
        ]

    def meritflaw_options(self):
        chartype = ObjectType.objects.get(name=self.primary_class.type)
        examples = MeritFlaw.objects.filter(allowed_types=chartype)
        if self.character.total_flaws() <= 0:
            examples = examples.exclude(
                max_rating__lt=min(0, -7 - self.character.total_flaws())
            )
        return examples.exclude(min_rating__gt=self.character.freebies)


class HumanFreebiesView(SpecialUserMixin, UpdateView):
    model = Human
    form_class = HumanFreebiesForm
    template_name = "characters/human/human/chargen.html"

    def get_category_functions(self):
        return {
            "attribute": self.object.attribute_freebies,
            "ability": self.object.ability_freebies,
            "new background": self.object.new_background_freebies,
            "existing background": self.object.existing_background_freebies,
            "meritflaw": self.object.meritflaw_freebies,
            "willpower": self.object.willpower_freebies,
        }

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context

    def form_valid(self, form):
        if form.is_valid():
            trait_type = form.data["category"].lower()
            cost = self.object.freebie_cost(trait_type)
            if cost == "rating":
                cost = int(form.data["value"])
            if cost > self.object.freebies:
                form.add_error(None, "Not Enough Freebies!")
                return super().form_invalid(form)
            trait, value, cost = self.get_category_functions()[trait_type](form)
            if "background" in trait_type:
                trait_type = "background"
            d = self.object.freebie_spend_record(trait, trait_type, value, cost=cost)
            self.object.spent_freebies.append(d)
            self.object.save()
            return super().form_valid(form)
        return super().form_invalid(form)
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        print(form.errors)
        return response
    

    def dispatch(self, request, *args, **kwargs):
        obj = get_object_or_404(Human, pk=kwargs.get("pk"))
        if obj.freebies == 0:
            obj.creation_status += 1
            obj.save()
            return HttpResponseRedirect(obj.get_absolute_url())
        return super().dispatch(request, *args, **kwargs)
