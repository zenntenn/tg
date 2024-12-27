from typing import Any

from characters.forms.core.ally import AllyForm
from characters.forms.core.backgroundform import BackgroundRatingFormSet
from characters.forms.core.specialty import SpecialtiesForm
from characters.forms.mage.familiar import FamiliarForm
from characters.forms.mage.freebies import MageFreebiesForm
from characters.forms.mage.practiceform import PracticeRatingFormSet
from characters.forms.mage.rote import RoteCreationForm
from characters.forms.mage.xp import MageXPForm
from characters.models.core.ability_block import Ability
from characters.models.core.archetype import Archetype
from characters.models.core.attribute_block import Attribute
from characters.models.core.background_block import (
    Background,
    BackgroundRating,
    PooledBackgroundRating,
)
from characters.models.core.human import Human
from characters.models.core.merit_flaw_block import MeritFlaw
from characters.models.core.specialty import Specialty
from characters.models.mage.faction import MageFaction
from characters.models.mage.focus import Practice, SpecializedPractice, Tenet
from characters.models.mage.mage import Mage, PracticeRating
from characters.models.mage.resonance import Resonance
from characters.models.mage.rote import Rote
from characters.models.mage.sphere import Sphere
from characters.views.core.generic_background import GenericBackgroundView
from characters.views.core.human import (
    HumanAttributeView,
    HumanCharacterCreationView,
    HumanDetailView,
)
from characters.views.mage.background_views import MtAEnhancementView
from characters.views.mage.mtahuman import MtAHumanAbilityView
from core.forms.language import HumanLanguageForm
from core.models import Language
from core.views.approved_user_mixin import SpecialUserMixin
from core.views.generic import MultipleFormsetsMixin
from core.widgets import AutocompleteTextInput
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.forms import ValidationError
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, FormView, UpdateView
from game.models import ObjectType
from items.forms.mage.wonder import WonderForm
from items.models.core.item import ItemModel
from locations.forms.mage.library import LibraryForm
from locations.forms.mage.node import NodeForm
from locations.forms.mage.sanctum import SanctumForm


def load_factions(request):
    affiliation_id = request.GET.get("affiliation")
    factions = MageFaction.objects.filter(parent=affiliation_id).order_by("name")
    return render(
        request,
        "characters/mage/mage/load_faction_dropdown_list.html",
        {"factions": factions},
    )


def load_subfactions(request):
    faction_id = request.GET.get("faction")
    subfactions = MageFaction.objects.filter(parent=faction_id).order_by("name")
    return render(
        request,
        "characters/mage/mage/load_subfaction_dropdown_list.html",
        {"subfactions": subfactions},
    )


def load_mf_ratings(request):
    mf_id = request.GET.get("mf")
    ratings = MeritFlaw.objects.get(pk=mf_id).ratings
    return render(
        request,
        "characters/mage/mage/load_mf_rating_dropdown_list.html",
        {"ratings": ratings},
    )


class LoadExamplesView(View):
    template_name = "characters/core/human/load_examples_dropdown_list.html"

    def get(self, request, *args, **kwargs):
        category_choice = request.GET.get("category")
        object_id = request.GET.get("object")
        m = Mage.objects.get(pk=object_id)

        category_choice = request.GET.get("category")
        if category_choice == "Attribute":
            examples = Attribute.objects.all()
            examples = [x for x in examples if getattr(m, x.property_name, 0) < 5]
        elif category_choice == "Ability":
            examples = Ability.objects.order_by("name")
            examples = [
                x
                for x in examples
                if getattr(m, x.property_name, 0) < 5 and hasattr(m, x.property_name)
            ]
        elif category_choice == "New Background":
            examples = Background.objects.filter(
                property_name__in=m.allowed_backgrounds
            ).order_by("name")
        elif category_choice == "Existing Background":
            examples = [
                x for x in BackgroundRating.objects.filter(char=m, rating__lt=5)
            ]
        elif category_choice == "MeritFlaw":
            mage = ObjectType.objects.get(name="mage")
            examples = MeritFlaw.objects.filter(allowed_types=mage)
            if m.total_flaws() <= 0:
                examples = examples.exclude(max_rating__lt=min(0, -7 - m.total_flaws()))
            examples = examples.exclude(min_rating__gt=m.freebies)
        elif category_choice == "Sphere":
            examples = Sphere.objects.all().order_by("name")
            examples = [
                x
                for x in examples
                if getattr(m, x.property_name, 0) < m.arete
                and hasattr(m, x.property_name)
            ]
        elif category_choice == "Resonance":
            examples = Resonance.objects.all()
        elif category_choice == "Tenet":
            metaphysical_tenet_q = (
                Q(id=m.metaphysical_tenet.id) if m.metaphysical_tenet else Q()
            )
            personal_tenet_q = Q(id=m.personal_tenet.id) if m.personal_tenet else Q()
            ascension_tenet_q = Q(id=m.ascension_tenet.id) if m.ascension_tenet else Q()
            other_tenets_q = Q(id__in=m.other_tenets.all().values_list("id", flat=True))
            related_tenets_q = (
                metaphysical_tenet_q
                | personal_tenet_q
                | ascension_tenet_q
                | other_tenets_q
            )
            examples = Tenet.objects.exclude(related_tenets_q)
        elif category_choice in ["Practice", "Arete"]:
            examples = Practice.objects.exclude(
                polymorphic_ctype__model="specializedpractice"
            ).exclude(polymorphic_ctype__model="corruptedpractice")
            spec = SpecializedPractice.objects.filter(faction=m.faction)
            if spec.count() > 0:
                examples = examples.exclude(
                    id__in=[x.parent_practice.id for x in spec]
                ) | Practice.objects.filter(id__in=[x.id for x in spec])
            ids = PracticeRating.objects.filter(mage=m, rating=5).values_list(
                "practice__id", flat=True
            )
            examples = examples.exclude(pk__in=ids).order_by("name")
            examples = [
                x
                for x in examples
                if (
                    sum([getattr(m, abb.property_name) for abb in x.abilities.all()])
                    / 2
                    > m.practice_rating(x) + 1
                )
            ]
        else:
            examples = []

        return render(request, self.template_name, {"examples": examples})


class LoadXPExamplesView(View):
    template_name = "characters/core/human/load_examples_dropdown_list.html"

    def get(self, request, *args, **kwargs):
        category_choice = request.GET.get("category")
        object_id = request.GET.get("object")
        self.character = Mage.objects.get(pk=object_id)
        examples = []

        if category_choice == "Attribute":
            filtered_attributes = [
                attribute
                for attribute in Attribute.objects.all()
                if getattr(self.character, attribute.property_name) < 5
            ]
            filtered_for_xp_cost = [
                x
                for x in filtered_attributes
                if self.character.xp_cost(
                    "attribute",
                    getattr(self.character, x.property_name),
                )
                <= self.character.xp
            ]
            examples = filtered_for_xp_cost
        elif category_choice == "Ability":
            filtered_abilities = [
                ability
                for ability in Ability.objects.filter(
                    property_name__in=self.character.talents
                    + self.character.skills
                    + self.character.knowledges
                )
                if getattr(self.character, ability.property_name) < 5
            ]
            filtered_for_xp_cost = [
                x
                for x in filtered_abilities
                if self.character.xp_cost(
                    "ability",
                    getattr(self.character, x.property_name),
                )
                <= self.character.xp
            ]
            examples = filtered_for_xp_cost
        elif category_choice == "New Background":
            examples = Background.objects.filter(
                property_name__in=self.character.allowed_backgrounds
            ).order_by("name")
        elif category_choice == "Existing Background":
            bgs = self.character.backgrounds.filter(rating__lt=5)
            filtered_for_xp_cost = [
                x
                for x in bgs
                if self.character.xp_cost(
                    "background",
                    x.rating,
                )
                <= self.character.xp
            ]
            examples = filtered_for_xp_cost
        elif category_choice == "MeritFlaw":
            mage = ObjectType.objects.get(name="mage")
            examples = MeritFlaw.objects.filter(allowed_types=mage, max_rating__gte=0)
            examples = [
                x for x in examples if self.character.mf_rating(x) != x.max_rating
            ]
            examples = [
                x
                for x in examples
                if (
                    min([y for y in x.get_ratings() if y > self.character.mf_rating(x)])
                    - self.character.mf_rating(x)
                )
                * 3
                <= self.character.xp
            ]
        elif category_choice == "Sphere":
            filtered_spheres = [
                sphere
                for sphere in Sphere.objects.all()
                if getattr(self.character, sphere.property_name) < self.character.arete
            ]
            filtered_for_xp_cost = [
                x
                for x in filtered_spheres
                if self.character.xp_cost(
                    self.character.sphere_to_trait_type(x.property_name),
                    getattr(self.character, x.property_name),
                )
                <= self.character.xp
            ]
            examples = filtered_for_xp_cost
        elif category_choice == "Tenet":
            examples = Tenet.objects.exclude(
                id__in=[
                    self.character.metaphysical_tenet.id,
                    self.character.personal_tenet.id,
                    self.character.ascension_tenet.id,
                ]
            )
            examples = examples.exclude(
                id__in=[x.id for x in self.character.other_tenets.all()]
            )
        elif category_choice == "Remove Tenet":
            examples = self.character.other_tenets.all()
            types = [x.tenet_type for x in examples]
            if "met" in types:
                examples |= Tenet.objects.filter(
                    id__in=[self.character.metaphysical_tenet.id]
                )
            if "asc" in types:
                examples |= Tenet.objects.filter(
                    id__in=[self.character.ascension_tenet.id]
                )
            if "per" in types:
                examples |= Tenet.objects.filter(
                    id__in=[self.character.personal_tenet.id]
                )
        elif category_choice == "Practice":
            examples = Practice.objects.exclude(
                polymorphic_ctype__model="specializedpractice"
            ).exclude(polymorphic_ctype__model="corruptedpractice")
            spec = SpecializedPractice.objects.filter(faction=self.character.faction)
            if spec.count() > 0:
                examples = examples.exclude(
                    id__in=[x.parent_practice.id for x in spec]
                ) | Practice.objects.filter(id__in=[x.id for x in spec])

            ids = PracticeRating.objects.filter(
                mage=self.character, rating=5
            ).values_list("practice__id", flat=True)

            filtered_practices = examples.exclude(pk__in=ids).order_by("name")
            examples = [
                x
                for x in filtered_practices
                if self.character.xp_cost(
                    "practice",
                    self.character.practice_rating(x),
                )
                <= self.character.xp
            ]
            examples = [
                x
                for x in examples
                if (
                    sum(
                        [
                            getattr(self.character, abb.property_name)
                            for abb in x.abilities.all()
                        ]
                    )
                    / 2
                    > self.character.practice_rating(x) + 1
                )
            ]
        return render(request, self.template_name, {"examples": examples})


def get_abilities(request):
    object_id = request.GET.get("object")
    object = Human.objects.get(id=object_id)
    practice_id = request.GET.get("practice_id")
    prac = Practice.objects.get(id=practice_id)
    abilities = prac.abilities.all().order_by("name")
    abilities = [x for x in abilities if getattr(object, x.property_name) > 0]
    abilities_list = [{"id": "", "name": "--------"}]  # Empty option
    abilities_list += [
        {"id": ability.id, "name": ability.name} for ability in abilities
    ]
    return JsonResponse(abilities_list, safe=False)


class MageDetailView(HumanDetailView):
    model = Mage
    template_name = "characters/mage/mage/detail.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["items_owned"] = ItemModel.objects.filter(owned_by=self.object)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        if "form" not in context:
            context["form"] = MageXPForm(character=self.object)
        context["rote_form"] = RoteCreationForm(instance=self.object)
        context["spec_form"] = SpecialtiesForm(
            object=self.object, specialties_needed=self.object.needed_specialties()
        )
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        form = MageXPForm(request.POST, request.FILES, character=self.object)
        rote_form = RoteCreationForm(request.POST, instance=self.object)
        form_errors = False
        if "spend_xp" in form.data.keys():
            if form.is_valid():
                category = form.cleaned_data["category"]
                example = form.cleaned_data["example"]
                value = form.cleaned_data["value"]
                note = form.cleaned_data["note"]
                pooled = form.cleaned_data["pooled"]
                image_field = form.cleaned_data["image_field"]
                resonance = form.cleaned_data["resonance"]
                if category == "Image":
                    self.object.image = image_field
                    self.object.save()
                if category not in ["Image", "Rote"]:
                    if category == "Attribute":
                        trait = example.name
                        trait_type = "attribute"
                        value = getattr(self.object, example.property_name)
                        cost = self.object.xp_cost("attribute", value)
                        d = self.object.xp_spend_record(
                            trait, trait_type, value + 1, cost=cost
                        )
                    elif category == "Ability":
                        trait = example.name
                        trait_type = "ability"
                        value = getattr(self.object, example.property_name)
                        cost = self.object.xp_cost("ability", value)
                        d = self.object.xp_spend_record(
                            trait, trait_type, value + 1, cost=cost
                        )
                    elif category == "New Background":
                        if note:
                            trait = example.name + f" ({note})"
                        else:
                            trait = example.name
                        trait_type = "new background"
                        value = 1
                        cost = self.object.xp_cost("new background", value)
                        d = self.object.xp_spend_record(
                            trait, trait_type, value, cost=cost
                        )
                    elif category == "Existing Background":
                        trait = example.bg.name + f" ({example.note})"
                        trait_type = "background"
                        value = example.rating
                        cost = self.object.xp_cost("background", value)
                        d = self.object.xp_spend_record(
                            trait, trait_type, value + 1, cost=cost
                        )
                    elif category == "Willpower":
                        trait = "Willpower"
                        trait_type = "willpower"
                        value = self.object.willpower
                        cost = self.object.xp_cost("willpower", value)
                        d = self.object.xp_spend_record(
                            trait, trait_type, value + 1, cost=cost
                        )
                    elif category == "MeritFlaw":
                        current_rating = self.object.mf_rating(example)
                        trait = example.name
                        trait_type = "meritflaw"
                        cost = self.object.xp_cost("meritflaw", value - current_rating)
                        d = self.object.xp_spend_record(
                            trait, trait_type, value, cost=cost
                        )
                    elif category == "Sphere":
                        trait = example.name
                        trait_type = "sphere"
                        value = getattr(self.object, example.property_name) + 1
                        cost = self.object.xp_cost(
                            self.object.sphere_to_trait_type(example.property_name),
                            getattr(self.object, example.property_name),
                        )
                        d = self.object.xp_spend_record(
                            trait, trait_type, value, cost=cost
                        )
                    elif category == "Rote Points":
                        trait = "Rote Points"
                        trait_type = "rotes"
                        cost = self.object.xp_cost("rotes", 1)
                        value = (
                            self.object.total_effects() + self.object.rote_points + 3
                        )
                        d = self.object.xp_spend_record(
                            trait, trait_type, value, cost=cost
                        )
                    elif category == "Resonance":
                        trait = f"Resonance ({resonance})"
                        r = Resonance.objects.get_or_create(name=resonance)[0]
                        trait_type = "resonance"
                        value = self.object.resonance_rating(r)
                        cost = self.object.xp_cost("resonance", value)
                        d = self.object.xp_spend_record(
                            trait, trait_type, value + 1, cost=cost
                        )
                        self.object.xp -= cost
                        self.object.spent_xp.append(d)
                        self.object.save()
                    elif category == "Tenet":
                        trait = example.name
                        trait_type = "tenet"
                        cost = self.object.xp_cost("tenet", 1)
                        d = self.object.xp_spend_record(trait, trait_type, 0, cost=cost)
                    elif category == "Remove Tenet":
                        trait = "Remove " + example.name
                        trait_type = "remove tenet"
                        cost = self.object.xp_cost(
                            "remove tenet", self.object.other_tenets.count() + 3
                        )
                        d = self.object.xp_spend_record(
                            trait, trait_type, None, cost=cost
                        )
                    elif category == "Practice":
                        trait = example.name
                        trait_type = "practice"
                        value = self.object.practice_rating(example)
                        cost = self.object.xp_cost("practice", value)
                        d = self.object.xp_spend_record(
                            trait, trait_type, value + 1, cost=cost
                        )
                    elif category == "Arete":
                        trait = "Arete"
                        trait_type = "arete"
                        value = self.object.arete
                        cost = self.object.xp_cost("arete", value)
                        d = self.object.xp_spend_record(
                            trait, trait_type, value + 1, cost=cost
                        )
                    if d not in self.object.spent_xp:
                        self.object.xp -= cost
                        self.object.spent_xp.append(d)
                        self.object.save()
                    else:
                        form.add_error(
                            None, "Wait for trait to be approved before buying again!"
                        )
                        context["form"] = form
                        form_errors = True
                elif category == "Rote":
                    if rote_form.is_valid():
                        if (
                            not rote_form.cleaned_data["select_or_create_rote"]
                            and not rote_form.cleaned_data["rote_options"]
                        ):
                            rote_form.add_error(None, "Must create or select a rote")
                            return render(
                                request, self.template_name, self.get_context_data()
                            )
                        if rote_form.cleaned_data["select_or_create_rote"]:
                            if (
                                not rote_form.cleaned_data["select_or_create_effect"]
                                and not rote_form.cleaned_data["effect_options"]
                            ):
                                rote_form.add_error(
                                    None, "Must create or select an effect"
                                )
                                return render(
                                    request, self.template_name, self.get_context_data()
                                )
                            if not rote_form.cleaned_data["name"]:
                                rote_form.add_error(None, "Must choose rote name")
                                return render(
                                    request, self.template_name, self.get_context_data()
                                )
                            if not rote_form.cleaned_data["practice"]:
                                rote_form.add_error(None, "Must choose rote Practice")
                                return render(
                                    request, self.template_name, self.get_context_data()
                                )
                            if not rote_form.cleaned_data["attribute"]:
                                rote_form.add_error(None, "Must choose rote Attribute")
                                return render(
                                    request, self.template_name, self.get_context_data()
                                )
                            if not rote_form.cleaned_data["ability"]:
                                rote_form.add_error(None, "Must choose rote Ability")
                                return render(
                                    request, self.template_name, self.get_context_data()
                                )
                            if not rote_form.cleaned_data["description"]:
                                rote_form.add_error(
                                    None, "Must choose rote description"
                                )
                                return render(
                                    request, self.template_name, self.get_context_data()
                                )
                            if rote_form.cleaned_data["select_or_create_effect"]:
                                if not rote_form.cleaned_data["systems"]:
                                    rote_form.add_error(
                                        None, "Must choose rote systems"
                                    )
                                    return render(
                                        request,
                                        self.template_name,
                                        self.get_context_data(),
                                    )
                                if (
                                    rote_form.cleaned_data["correspondence"]
                                    + rote_form.cleaned_data["entropy"]
                                    + rote_form.cleaned_data["forces"]
                                    + rote_form.cleaned_data["life"]
                                    + rote_form.cleaned_data["matter"]
                                    + rote_form.cleaned_data["mind"]
                                    + rote_form.cleaned_data["prime"]
                                    + rote_form.cleaned_data["spirit"]
                                    + rote_form.cleaned_data["time"]
                                    == 0
                                ):
                                    rote_form.add_error(
                                        None, "Effects must have sphere ratings"
                                    )
                                    return render(
                                        request,
                                        self.template_name,
                                        self.get_context_data(),
                                    )
                        try:
                            rote_form.save(self.object)
                        except forms.ValidationError:
                            return render(
                                request, self.template_name, self.get_context_data()
                            )
            else:
                print("errors", form.errors)
        if "Approve" in form.data.values():
            xp_index = [x for x in form.data.keys() if form.data[x] == "Approve"][0]
            index = "_".join(xp_index.split("_")[:-1])
            d = [x for x in self.object.spent_xp if x["index"] == index][0]
            i = self.object.spent_xp.index(d)
            self.object.spent_xp[i]["approved"] = "Approved"
            char_id, trait_type, trait, value = index.split("_")
            value = int(value)
            if trait_type == "attribute":
                att = Attribute.objects.get(name=trait)
                setattr(self.object, att.property_name, value)
                self.object.save()
            elif trait_type == "ability":
                abb = Ability.objects.get(name=trait)
                setattr(self.object, abb.property_name, value)
                self.object.save()
            elif trait_type == "background":
                trait, note = trait.replace("-", " ").split(" (")
                note = note[:-1]
                bgr = self.object.backgrounds.filter(bg__name=trait, note=note).first()
                bgr.rating += 1
                bgr.save()
                self.object.save()
            elif trait_type == "new-background":
                trait = trait.replace("-", " ")
                if "(" not in trait:
                    note = ""
                    trait = trait
                else:
                    trait, note = trait.split("(")
                    note = note[:-1]
                trait = trait.strip()
                note = note.strip()
                BackgroundRating.objects.create(
                    bg=Background.objects.get(name=trait),
                    rating=1,
                    char=self.object,
                    note=note,
                )
                self.object.save()
            elif trait_type == "willpower":
                self.object.willpower = value
                self.object.save()
            elif trait_type == "meritflaw":
                trait = trait.replace("-", " ")
                value = int(value)
                mf = MeritFlaw.objects.get(name=trait)
                self.object.add_mf(mf, value)
                self.object.save()
            elif trait_type == "sphere":
                s = Sphere.objects.get(name=trait)
                setattr(self.object, s.property_name, value)
                self.object.save()
            elif trait_type == "arete":
                self.object.arete = value
                self.object.save()
            elif trait_type == "tenet":
                t = Tenet.objects.get(name=trait.replace("-", " "))
                self.object.other_tenets.add(t)
                self.object.save()
            elif trait_type == "remove-tenet":
                trait = " ".join(trait.split("-")[1:])
                tenet = Tenet.objects.get(name=trait)
                if tenet in self.object.other_tenets.all():
                    self.object.other_tenets.remove(tenet)
                    self.object.save()
                else:
                    replacement = self.object.other_tenets.filter(
                        tenet_type=tenet.tenet_type
                    ).first()
                    if tenet.tenet_type == "met":
                        self.object.metaphysical_tenet = replacement
                    elif tenet.tenet_type == "per":
                        self.object.personal_tenet = replacement
                    elif tenet.tenet_type == "asc":
                        self.object.ascension_tenet = replacement
                    self.object.other_tenets.remove(replacement)
                    self.object.save()
            elif trait_type == "practice":
                trait = trait.replace("-", " ")
                practice = Practice.objects.get(name=trait)
                self.object.add_practice(practice)
                self.object.save()
            elif trait_type == "rotes":
                self.object.rote_points += 3
                self.object.save()
            elif trait_type == "resonance":
                t = trait.split("-")
                detail = " ".join(t[1:])[1:-1]
                trait = t[0]
                self.object.add_resonance(detail)
                self.object.save()
        if "Reject" in form.data.values():
            xp_index = [x for x in form.data.keys() if form.data[x] == "Reject"][0]
            index = "_".join(xp_index.split("_")[:-1])
            spends = [x for x in self.object.spent_xp if x["index"] == index]
            for spend in spends:
                self.object.xp += spend["cost"]
            self.object.spent_xp = [
                x
                for x in self.object.spent_xp
                if x["index"] != index
                or not (x["index"] == index and x["approved"] == "Pending")
            ]
            self.object.save()
        if "specialties" in form.data.keys():
            specs = {
                k: v
                for k, v in form.data.items()
                if k not in ["csrfmiddlewaretoken", "specialties"]
            }
            for stat, spec in specs.items():
                spec = Specialty.objects.get_or_create(name=spec, stat=stat)[0]
                self.object.specialties.add(spec)
            self.object.save()
        if form_errors:
            return self.render_to_response(context)
        return redirect(reverse("characters:character", kwargs={"pk": self.object.pk}))


class MageCreateView(CreateView):
    model = Mage
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
        "awareness",
        "art",
        "leadership",
        "animal_kinship",
        "blatancy",
        "carousing",
        "flying",
        "high_ritual",
        "lucid_dreaming",
        "search",
        "seduction",
        "larceny",
        "meditation",
        "research",
        "survival",
        "technology",
        "acrobatics",
        "archery",
        "biotech",
        "energy_weapons",
        "jetpack",
        "riding",
        "torture",
        "cosmology",
        "enigmas",
        "finance",
        "law",
        "occult",
        "politics",
        "area_knowledge",
        "belief_systems",
        "cryptography",
        "demolitions",
        "lore",
        "media",
        "pharmacopeia",
        "cooking",
        "diplomacy",
        "instruction",
        "intrigue",
        "intuition",
        "mimicry",
        "negotiation",
        "newspeak",
        "scan",
        "scrounging",
        "style",
        "blind_fighting",
        "climbing",
        "disguise",
        "elusion",
        "escapology",
        "fast_draw",
        "fast_talk",
        "fencing",
        "fortune_telling",
        "gambling",
        "gunsmith",
        "heavy_weapons",
        "hunting",
        "hypnotism",
        "jury_rigging",
        "microgravity_operations",
        "misdirection",
        "networking",
        "pilot",
        "psychology",
        "security",
        "speed_reading",
        "swimming",
        "conspiracy_theory",
        "chantry_politics",
        "covert_culture",
        "cultural_savvy",
        "helmsman",
        "history_knowledge",
        "power_brokering",
        "propaganda",
        "theology",
        "unconventional_warface",
        "vice",
        "essence",
        "correspondence",
        "time",
        "spirit",
        "mind",
        "entropy",
        "time",
        "forces",
        "matter",
        "life",
        "arete",
        "affinity_sphere",
        "corr_name",
        "prime_name",
        "spirit_name",
        "age_of_awakening",
        "avatar_description",
        "rote_points",
        "quintessence",
        "paradox",
        "quiet",
        "quiet_type",
        "affiliation",
        "faction",
        "subfaction",
        "public_info",
    ]
    template_name = "characters/mage/mage/form.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["affiliation"].queryset = MageFaction.objects.filter(parent=None)
        form.fields["faction"].queryset = MageFaction.objects.none()
        form.fields["subfaction"].queryset = MageFaction.objects.none()
        return form


class MageUpdateView(SpecialUserMixin, UpdateView):
    model = Mage
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
        "awareness",
        "art",
        "leadership",
        "animal_kinship",
        "blatancy",
        "carousing",
        "flying",
        "high_ritual",
        "lucid_dreaming",
        "search",
        "seduction",
        "larceny",
        "meditation",
        "research",
        "survival",
        "technology",
        "acrobatics",
        "archery",
        "biotech",
        "energy_weapons",
        "jetpack",
        "riding",
        "torture",
        "cosmology",
        "enigmas",
        "finance",
        "law",
        "occult",
        "politics",
        "area_knowledge",
        "belief_systems",
        "cryptography",
        "demolitions",
        "lore",
        "media",
        "pharmacopeia",
        "cooking",
        "diplomacy",
        "instruction",
        "intrigue",
        "intuition",
        "mimicry",
        "negotiation",
        "newspeak",
        "scan",
        "scrounging",
        "style",
        "blind_fighting",
        "climbing",
        "disguise",
        "elusion",
        "escapology",
        "fast_draw",
        "fast_talk",
        "fencing",
        "fortune_telling",
        "gambling",
        "gunsmith",
        "heavy_weapons",
        "hunting",
        "hypnotism",
        "jury_rigging",
        "microgravity_operations",
        "misdirection",
        "networking",
        "pilot",
        "psychology",
        "security",
        "speed_reading",
        "swimming",
        "conspiracy_theory",
        "chantry_politics",
        "covert_culture",
        "cultural_savvy",
        "helmsman",
        "history_knowledge",
        "power_brokering",
        "propaganda",
        "theology",
        "unconventional_warface",
        "vice",
        "essence",
        "correspondence",
        "time",
        "spirit",
        "mind",
        "entropy",
        "prime",
        "forces",
        "matter",
        "life",
        "arete",
        "affinity_sphere",
        "corr_name",
        "prime_name",
        "spirit_name",
        "age_of_awakening",
        "avatar_description",
        "rote_points",
        "quintessence",
        "paradox",
        "quiet",
        "quiet_type",
        "affiliation",
        "faction",
        "subfaction",
        "public_info",
    ]
    template_name = "characters/mage/mage/form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context


class MageBasicsView(LoginRequiredMixin, CreateView):
    model = Mage
    fields = [
        "name",
        "nature",
        "demeanor",
        "concept",
        "affiliation",
        "faction",
        "subfaction",
        "essence",
        "chronicle",
        "image",
        "npc",
    ]
    template_name = "characters/mage/mage/magebasics.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["storyteller"] = False
        if self.request.user.profile.is_st():
            context["storyteller"] = True
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["nature"].queryset = Archetype.objects.all().order_by("name")
        form.fields["demeanor"].queryset = Archetype.objects.all().order_by("name")
        form.fields["affiliation"].queryset = MageFaction.objects.filter(parent=None)
        form.fields["faction"].queryset = MageFaction.objects.none()
        form.fields["subfaction"].queryset = MageFaction.objects.none()
        form.fields["name"].widget.attrs.update({"placeholder": "Enter name here"})
        form.fields["concept"].widget.attrs.update(
            {"placeholder": "Enter concept here"}
        )
        form.fields["image"].required = False
        if not self.request.user.profile.is_st():
            form.fields["affiliation"].queryset = form.fields[
                "affiliation"
            ].queryset.exclude(name__in=["Nephandi", "Marauders"])
        return form

    def form_invalid(self, form):
        errors = form.errors
        if "faction" in errors:
            del errors["faction"]
        if "subfaction" in errors:
            del errors["subfaction"]

        if not errors:
            return self.form_valid(form)
        return super().form_invalid(form)

    def form_valid(self, form):
        if form.data["faction"]:
            form.instance.faction = MageFaction.objects.get(pk=form.data["faction"])
        if form.data["subfaction"]:
            form.instance.subfaction = MageFaction.objects.get(
                pk=form.data["subfaction"]
            )
        form.instance.owner = self.request.user
        self.object = form.save()
        return super().form_valid(form)


class MageAttributeView(HumanAttributeView):
    model = Mage
    template_name = "characters/mage/mage/chargen.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context


class MageAbilityView(SpecialUserMixin, MtAHumanAbilityView):
    model = Mage
    template_name = "characters/mage/mage/chargen.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context


class MageBackgroundsView(SpecialUserMixin, MultipleFormsetsMixin, UpdateView):
    model = Mage
    fields = []
    template_name = "characters/mage/mage/chargen.html"
    formsets = {
        "bg_form": BackgroundRatingFormSet,
    }

    def get_formset_context(self, formset_class, formset_prefix):
        context, js_code = super().get_formset_context(formset_class, formset_prefix)
        formset = context["formset"]
        empty_form = context["empty_form"]
        for form in formset:
            form.fields["bg"].queryset = Background.objects.filter(
                property_name__in=self.object.allowed_backgrounds
            )
        empty_form.fields["bg"].queryset = Background.objects.filter(
            property_name__in=self.object.allowed_backgrounds
        )
        return context, js_code

    def form_valid(self, form):
        context = self.get_context_data()
        mage = context["object"]

        bg_data = self.get_form_data("bg_form", blankable=["note"])
        for res in bg_data:
            res["bg"] = Background.objects.get(id=res["bg"])
            res["rating"] = int(res["rating"])
            res["pooled"] = res.get("pooled", False) == "on"
            res["display_alt_name"] = res.get("display_alt_name", False) == "on"
        total_bg = sum([x["rating"] * x["bg"].multiplier for x in bg_data])
        if total_bg != self.object.background_points:
            form.add_error(
                None, f"Backgrounds must total {self.object.background_points} points"
            )
            return super().form_invalid(form)
        for bg in bg_data:
            if bg["rating"] != 0:
                if bg["pooled"] and mage.is_group_member():
                    BackgroundRating.objects.create(
                        bg=bg["bg"],
                        rating=bg["rating"],
                        char=mage,
                        note=bg["note"],
                        pooled=bg["pooled"],
                        display_alt_name=bg["display_alt_name"],
                        complete=True,
                    )
                    pbgr = PooledBackgroundRating.objects.get_or_create(
                        bg=bg["bg"], note=bg["note"], group=mage.get_group()
                    )[0]
                    pbgr.rating += bg["rating"]
                    pbgr.save()
                else:
                    BackgroundRating.objects.create(
                        bg=bg["bg"],
                        rating=bg["rating"],
                        char=mage,
                        note=bg["note"],
                        display_alt_name=bg["display_alt_name"],
                    )

        self.object.creation_status += 1
        self.object.quintessence = self.object.total_background_rating("avatar")
        self.object.save()
        self.object.willpower = 5
        self.object.save()
        return HttpResponseRedirect(mage.get_absolute_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context


class MageFocusView(SpecialUserMixin, UpdateView):
    model = Mage
    fields = [
        "metaphysical_tenet",
        "personal_tenet",
        "ascension_tenet",
        "other_tenets",
    ]
    template_name = "characters/mage/mage/chargen.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["metaphysical_tenet"].queryset = Tenet.objects.filter(
            tenet_type="met"
        )
        form.fields["personal_tenet"].queryset = Tenet.objects.filter(tenet_type="per")
        form.fields["ascension_tenet"].queryset = Tenet.objects.filter(tenet_type="asc")
        form.fields["other_tenets"].queryset = Tenet.objects.filter(tenet_type="oth")
        form.fields["personal_tenet"].empty_label = "Choose Personal Tenet"
        form.fields["ascension_tenet"].empty_label = "Choose Ascension Tenet"
        form.fields["metaphysical_tenet"].empty_label = "Choose Metaphysical Tenet"
        return form

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["practice_formset"] = PracticeRatingFormSet(
                self.request.POST, instance=self.object, mage=self.object
            )
        else:
            context["practice_formset"] = PracticeRatingFormSet(
                instance=self.object, mage=self.object
            )
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        context["form"].full_clean()
        if context["form"].cleaned_data["metaphysical_tenet"] is None:
            context["form"].add_error(None, "Must include Metaphysical Tenet")
            return self.form_invalid(context["form"])
        if context["form"].cleaned_data["personal_tenet"] is None:
            context["form"].add_error(None, "Must include Personal Tenet")
            return self.form_invalid(context["form"])
        if context["form"].cleaned_data["ascension_tenet"] is None:
            context["form"].add_error(None, "Must include Ascension Tenet")
            return self.form_invalid(context["form"])
        practice_formset = context["practice_formset"]

        if practice_formset.is_valid():
            self.object = form.save()
            ratings = [x.cleaned_data.get("rating") for x in practice_formset]
            ratings = [x for x in ratings if x is not None]
            practice_total = sum(ratings)
            if practice_total != self.object.arete:
                form.add_error(None, "Starting Practices must add up to Arete rating")
                return self.form_invalid(form)
            for practice_form in practice_formset:
                practice = practice_form.cleaned_data.get("practice")
                rating = practice_form.cleaned_data.get("rating")
                if practice is not None:
                    ability_total = 0
                    for ability in practice.abilities.all():
                        ability_total += getattr(self.object, ability.property_name, 0)
                    if (
                        practice is not None
                        and rating is not None
                        and rating <= ability_total / 2
                    ):
                        pr = PracticeRating.objects.create(
                            mage=self.object, practice=practice, rating=rating
                        )
                    else:
                        form.add_error(
                            None,
                            "You must have at least 2 dots in associated abilities for each dot of a Practice",
                        )
                        return self.form_invalid(form)
            self.object.creation_status += 1
            self.object.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response


class MageSpheresView(SpecialUserMixin, UpdateView):
    model = Mage
    fields = [
        "arete",
        "correspondence",
        "time",
        "spirit",
        "forces",
        "matter",
        "life",
        "entropy",
        "mind",
        "prime",
        "affinity_sphere",
        "corr_name",
        "prime_name",
        "spirit_name",
        "resonance",
    ]
    template_name = "characters/mage/mage/chargen.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields[
            "affinity_sphere"
        ].queryset = self.object.get_affinity_sphere_options().order_by("name")
        form.fields["affinity_sphere"].empty_label = "Choose an Affinity"
        form.fields["resonance"].widget = AutocompleteTextInput(
            suggestions=[x.name.title() for x in Resonance.objects.order_by("name")]
        )
        form.fields["affinity_sphere"].required = True
        return form

    def get_initial(self) -> dict[str, Any]:
        initial = super().get_initial()
        initial["arete"] = 1
        initial["resonance"] = ""
        return initial

    def form_valid(self, form):
        arete = form.cleaned_data.get("arete", 1)
        correspondence = form.cleaned_data.get("correspondence", 0)
        time = form.cleaned_data.get("time", 0)
        spirit = form.cleaned_data.get("spirit", 0)
        forces = form.cleaned_data.get("forces", 0)
        matter = form.cleaned_data.get("matter", 0)
        life = form.cleaned_data.get("life", 0)
        entropy = form.cleaned_data.get("entropy", 0)
        mind = form.cleaned_data.get("mind", 0)
        prime = form.cleaned_data.get("prime", 0)
        affinity_sphere = form.cleaned_data.get("affinity_sphere")
        if affinity_sphere is None:  # This will catch the 'empty_label' selection
            raise ValidationError("You must select a valid affinity sphere.")
        corr_name = form.cleaned_data.get("corr_name")
        prime_name = form.cleaned_data.get("prime_name")
        spirit_name = form.cleaned_data.get("spirit_name")
        resonance = form.data.get("resonance")
        self.object.add_resonance(resonance)

        if arete > 3:
            form.add_error(None, "Arete may not exceed 3 at character creation")
            return self.form_invalid(form)

        for sphere in [
            correspondence,
            time,
            spirit,
            forces,
            matter,
            life,
            entropy,
            mind,
            prime,
        ]:
            if (
                sphere < 0
                or sphere > arete
                or getattr(self.object, self.object.affinity_sphere.property_name) == 0
            ):
                form.add_error(
                    None,
                    "Spheres must range from 0-Arete Rating and Affinity Sphere must be nonzero",
                )
                return self.form_invalid(form)

        tot_spheres = sum(
            [correspondence, time, spirit, forces, matter, life, entropy, mind, prime]
        )
        if tot_spheres != 6:
            form.add_error(None, "Spheres must total 6")
            return self.form_invalid(form)
        self.object.creation_status += 1
        for i in range(arete - 1):
            self.object.freebies -= 4
            self.object.spent_freebies.append(
                self.object.freebie_spend_record("Arete", "arete", i + 2)
            )
        self.object.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors
        if "resonance" in errors and "resonance" in form.data:
            del errors["resonance"]
        if not errors:
            return self.form_valid(form)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context


class MageExtrasView(SpecialUserMixin, UpdateView):
    model = Mage
    fields = [
        "date_of_birth",
        "apparent_age",
        "age_of_awakening",
        "age",
        "description",
        "history",
        "avatar_description",
        "goals",
        "notes",
        "public_info",
    ]
    template_name = "characters/mage/mage/chargen.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context

    def form_valid(self, form):
        self.object.creation_status += 1
        self.object.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["date_of_birth"].widget = forms.DateInput(attrs={"type": "date"})
        form.fields["description"].widget.attrs.update(
            {
                "placeholder": "Describe your character's physical appeareance. Be detailed, this will be visible to other players."
            }
        )
        form.fields["history"].widget.attrs.update(
            {
                "placeholder": "Describe character history/backstory. Include information about their childhood, when and how they Awakened, and how they've interacted with mage society since, particularly mentioning important backgrounds."
            }
        )
        form.fields["avatar_description"].widget.attrs.update(
            {
                "placeholder": "Describe your Avatar. Both how it appears to you, how you relate to it, and anything it is, in particular, pushing you towards."
            }
        )
        form.fields["goals"].widget.attrs.update(
            {
                "placeholder": "Describe your character's long and short term goals, whether personal, professional, or magical."
            }
        )
        form.fields["notes"].widget.attrs.update({"placeholder": "Notes"})
        form.fields["public_info"].widget.attrs.update(
            {
                "placeholder": "This will be displayed to all players who look at your character, include Fame and anything else that would be publicly seen beyond physical description"
            }
        )
        return form


class MageFreebiesView(SpecialUserMixin, UpdateView):
    model = Mage
    form_class = MageFreebiesForm
    template_name = "characters/mage/mage/chargen.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context

    def form_valid(self, form):
        if form.data["category"] == "-----":
            form.add_error(None, "Must Choose Freebie Expenditure Type")
            return super().form_invalid(form)
        elif form.data["category"] == "MeritFlaw" and (
            form.data["example"] == "" or form.data["value"] == ""
        ):
            form.add_error(None, "Must Choose Merit/Flaw and rating")
            return super().form_invalid(form)
        elif (
            form.data["category"]
            in [
                "Attribute",
                "Ability",
                "New Background",
                "Existing Background",
                "Sphere",
                "Tenet",
                "Practice",
            ]
            and form.data["example"] == ""
        ):
            form.add_error(None, "Must Choose Trait")
            return super().form_invalid(form)
        elif form.data["category"] == "Resonance" and form.data["resonance"] == "":
            form.add_error(None, "Must Choose Resonance")
            return super().form_invalid(form)
        trait_type = form.data["category"].lower()
        if "background" in trait_type:
            trait_type = "background"
        cost = self.object.freebie_cost(trait_type)
        if cost == "rating":
            cost = int(form.data["value"])
        if cost > self.object.freebies:
            form.add_error(None, "Not Enough Freebies!")
            return super().form_invalid(form)
        if form.data["category"] == "Attribute":
            trait = Attribute.objects.get(pk=form.data["example"])
            value = getattr(self.object, trait.property_name) + 1
            self.object.add_attribute(trait.property_name)
            self.object.freebies -= cost
            trait = trait.name
        elif form.data["category"] == "Ability":
            trait = Ability.objects.get(pk=form.data["example"])
            value = getattr(self.object, trait.property_name) + 1
            self.object.add_ability(trait.property_name)
            self.object.freebies -= cost
            trait = trait.name
        elif form.data["category"] == "New Background":
            trait = Background.objects.get(pk=form.data["example"])
            cost *= trait.multiplier
            value = 1
            if "pooled" in form.data.keys():
                pbgr = PooledBackgroundRating.objects.get_or_create(
                    bg=trait, group=self.object.get_group(), note=form.data["note"]
                )[0]
                pbgr.rating += 1
                pbgr.save()
                BackgroundRating.objects.create(
                    bg=trait,
                    rating=1,
                    char=self.object,
                    note=form.data["note"],
                    complete=True,
                    pooled=True,
                )
            else:
                BackgroundRating.objects.create(
                    bg=trait,
                    rating=1,
                    char=self.object,
                    note=form.data["note"],
                    pooled=False,
                )
            self.object.freebies -= cost
            trait = str(trait)
            if form.data["note"]:
                trait += f" ({form.data['note']})"
        elif form.data["category"] == "Existing Background":
            trait = BackgroundRating.objects.get(pk=form.data["example"])
            if trait.pooled:
                pbgr = PooledBackgroundRating.objects.get(
                    bg=trait.bg, group=self.object.get_group(), note=trait.note
                )
                pbgr.rating += 1
                pbgr.save()
            cost *= trait.bg.multiplier
            value = trait.rating + 1
            trait.rating += 1
            trait.save()
            self.object.freebies -= cost
            trait = str(trait)
        elif form.data["category"] == "Willpower":
            trait = "Willpower"
            value = self.object.willpower + 1
            self.object.add_willpower()
            self.object.freebies -= cost
        elif form.data["category"] == "MeritFlaw":
            trait = MeritFlaw.objects.get(pk=form.data["example"])
            value = int(form.data["value"])
            self.object.add_mf(trait, value)
            self.object.freebies -= cost
            trait = trait.name
        elif form.data["category"] == "Sphere":
            trait = Sphere.objects.get(pk=form.data["example"])
            value = getattr(self.object, trait.property_name) + 1
            self.object.add_sphere(trait.property_name)
            self.object.freebies -= cost
            trait = trait.name
        elif form.data["category"] == "Rotes":
            trait = "Rote Points"
            value = 4
            self.object.rote_points += 4
            self.object.freebies -= cost
        elif form.data["category"] == "Resonance":
            trait = Resonance.objects.get(name=form.data["resonance"])
            value = self.object.resonance_rating(trait) + 1
            self.object.add_resonance(trait.name)
            self.object.freebies -= cost
            trait = trait.name
        elif form.data["category"] == "Tenet":
            trait = Tenet.objects.get(pk=form.data["example"])
            value = ""
            self.object.add_tenet(trait)
            self.object.freebies -= cost
            trait = trait.name
        elif form.data["category"] == "Practice":
            trait = Practice.objects.get(pk=form.data["example"])
            value = self.object.practice_rating(trait) + 1
            self.object.add_practice(trait)
            self.object.freebies -= cost
            trait = trait.name
        elif form.data["category"] == "Arete":
            if self.object.arete >= 3 and self.object.total_freebies() != 45:
                form.add_error(
                    None, "Arete Cannot Be Raised Above 3 At Character Creation"
                )
                return super().form_invalid(form)
            if self.object.arete >= 4 and self.object.total_freebies() == 45:
                form.add_error(
                    None, "Arete Cannot Be Raised Above 4 At Character Creation"
                )
                return super().form_invalid(form)
            prac = Practice.objects.get(pk=form.data["example"])
            trait = f"Arete ({prac.name})"
            value = getattr(self.object, "arete") + 1
            self.object.add_practice(prac)
            self.object.add_arete()
            self.object.freebies -= cost
        elif form.data["category"] == "Quintessence":
            trait = "Quintessence"
            value = 4
            self.object.quintessence += 4
            self.object.freebies -= cost
        if form.data["category"] != "MeritFlaw":
            self.object.spent_freebies.append(
                self.object.freebie_spend_record(trait, trait_type, value, cost=cost)
            )
        else:
            self.object.spent_freebies.append(
                self.object.freebie_spend_record(trait, trait_type, value, cost=cost)
            )
        if self.object.freebies == 0:
            self.object.creation_status += 1
            if "Language" not in self.object.merits_and_flaws.values_list(
                "name", flat=True
            ):
                self.object.creation_status += 1
                self.object.languages.add(Language.objects.get(name="English"))
        self.object.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        if form.data["category"] == "-----":
            form.add_error(None, "Must Choose Freebie Expenditure Type")
            return super().form_invalid(form)
        elif form.data["category"] == "MeritFlaw" and (
            form.data["example"] == "" or form.data["value"] == ""
        ):
            form.add_error(None, "Must Choose Merit/Flaw and rating")
            return super().form_invalid(form)
        elif (
            form.data["category"]
            in ["Attribute", "Ability", "Background", "Sphere", "Tenet", "Practice"]
            and form.data["example"] == ""
        ):
            form.add_error(None, "Must Choose Trait")
            return super().form_invalid(form)
        elif form.data["category"] == "Resonance" and form.data["resonance"] == "":
            form.add_error(None, "Must Choose Resonance")
            return super().form_invalid(form)
        return self.form_valid(form)


class MageLanguagesView(SpecialUserMixin, FormView):
    form_class = HumanLanguageForm
    template_name = "characters/mage/mage/chargen.html"

    # Overriding `get_form_kwargs` to pass custom arguments to the form
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        human_pk = self.kwargs.get("pk")
        num_languages = Human.objects.get(pk=human_pk).num_languages()
        kwargs.update({"pk": human_pk, "num_languages": int(num_languages)})
        return kwargs

    # Overriding `form_valid` to handle saving the data
    def form_valid(self, form):
        # Get the human instance from the pased `pk`
        human_pk = self.kwargs.get("pk")
        human = get_object_or_404(Human, pk=human_pk)
        num_languages = human.num_languages()
        human.languages.add(Language.objects.get(name="English"))
        for i in range(num_languages):
            language_name = form.cleaned_data.get(f"language_{i+1}")
            if language_name:
                language, created = Language.objects.get_or_create(name=language_name)
                human.languages.add(language)
        human.creation_status += 1
        human.save()
        return HttpResponseRedirect(human.get_absolute_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = get_object_or_404(Human, pk=self.kwargs.get("pk"))
        context["is_approved_user"] = self.check_if_special_user(
            context["object"], self.request.user
        )
        return context


class MageRoteView(SpecialUserMixin, CreateView):
    model = Rote
    form_class = RoteCreationForm
    template_name = "characters/mage/mage/chargen.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        mage_id = self.kwargs.get("pk")
        context["object"] = Mage.objects.get(id=mage_id)
        context["is_approved_user"] = self.check_if_special_user(
            context["object"], self.request.user
        )
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        mage_id = self.kwargs.get("pk")
        mage = Mage.objects.get(pk=mage_id)
        kwargs["instance"] = mage
        return kwargs

    def form_invalid(self, form):
        errors = form.errors
        print(errors)
        # if "ability" in errors:
        #     del errors["ability"]
        if not errors:
            return self.form_valid(form)
        return super().form_invalid(form)

    def form_valid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        mage = context["object"]
        if (
            not form.cleaned_data["select_or_create_rote"]
            and not form.cleaned_data["rote_options"]
        ):
            form.add_error(None, "Must create or select a rote")
            return super().form_invalid(form)
        if form.cleaned_data["select_or_create_rote"]:
            if (
                not form.cleaned_data["select_or_create_effect"]
                and not form.cleaned_data["effect_options"]
            ):
                form.add_error(None, "Must create or select an effect")
                return super().form_invalid(form)
            if not form.cleaned_data["name"]:
                form.add_error(None, "Must choose rote name")
                return super().form_invalid(form)
            if not form.cleaned_data["practice"]:
                form.add_error(None, "Must choose rote Practice")
                return super().form_invalid(form)
            if not form.cleaned_data["attribute"]:
                form.add_error(None, "Must choose rote Attribute")
                return super().form_invalid(form)
            if not form.cleaned_data["ability"]:
                form.add_error(None, "Must choose rote Ability")
                return super().form_invalid(form)
            if not form.cleaned_data["description"]:
                form.add_error(None, "Must choose rote description")
                return super().form_invalid(form)
            if form.cleaned_data["select_or_create_effect"]:
                if not form.cleaned_data["systems"]:
                    form.add_error(None, "Must choose rote systems")
                    return super().form_invalid(form)
                if (
                    form.cleaned_data["correspondence"]
                    + form.cleaned_data["entropy"]
                    + form.cleaned_data["forces"]
                    + form.cleaned_data["life"]
                    + form.cleaned_data["matter"]
                    + form.cleaned_data["mind"]
                    + form.cleaned_data["prime"]
                    + form.cleaned_data["spirit"]
                    + form.cleaned_data["time"]
                    == 0
                ):
                    form.add_error(None, "Effects must have sphere ratings")
                    return super().form_invalid(form)

        if form.save(mage):
            if mage.rote_points == 0:
                mage.creation_status += 1
                mage.save()
                for step in [
                    "node",
                    "library",
                    "familiar",
                    "wonder",
                    "enhancement",
                    "sanctum",
                    "allies",
                ]:
                    if (
                        BackgroundRating.objects.filter(
                            bg=Background.objects.get(property_name=step),
                            char=mage,
                            complete=False,
                        ).count()
                        == 0
                    ):
                        mage.creation_status += 1
                    else:
                        mage.save()
                        break
                    mage.save()
            return HttpResponseRedirect(mage.get_absolute_url())
        return super().form_invalid(form)


class MageAlliesView(GenericBackgroundView):
    primary_object_class = Mage
    background_name = "allies"
    form_class = AllyForm
    template_name = "characters/mage/mage/chargen.html"


class MageEnhancementView(MtAEnhancementView):
    template_name = "characters/mage/mage/chargen.html"


class MageFamiliarView(GenericBackgroundView):
    primary_object_class = Mage
    background_name = "familiar"
    form_class = FamiliarForm
    template_name = "characters/mage/mage/chargen.html"

    def special_valid_action(self, background_object):
        background_object.freebies = 10 * self.current_background.rating
        background_object.status = "Un"
        background_object.save()
        return background_object


class MageLibraryView(GenericBackgroundView):
    primary_object_class = Mage
    background_name = "library"
    form_class = LibraryForm
    template_name = "characters/mage/mage/chargen.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        obj = get_object_or_404(self.primary_object_class, pk=self.kwargs.get("pk"))
        form.fields["name"].initial = (
            self.current_background.note or f"{obj.name}'s Library"
        )
        tmp = [obj.affiliation, obj.faction, obj.subfaction]
        tmp = [x.pk for x in tmp if hasattr(x, "pk")]
        form.fields["faction"].queryset = MageFaction.objects.filter(pk__in=tmp)
        return form


class MageNodeView(GenericBackgroundView):
    primary_object_class = Mage
    background_name = "node"
    form_class = NodeForm
    template_name = "characters/mage/mage/chargen.html"


class MageSpecialtiesView(SpecialUserMixin, FormView):
    form_class = SpecialtiesForm
    template_name = "characters/mage/mage/chargen.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["object"] = Mage.objects.get(id=self.kwargs["pk"])
        context["is_approved_user"] = self.check_if_special_user(
            context["object"], self.request.user
        )
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        mage = Mage.objects.get(id=self.kwargs["pk"])
        kwargs["object"] = mage
        kwargs["specialties_needed"] = mage.needed_specialties()
        return kwargs

    def form_valid(self, form):
        context = self.get_context_data()
        mage = context["object"]
        for field in form.fields:
            spec = Specialty.objects.get_or_create(name=form.data[field], stat=field)[0]
            mage.specialties.add(spec)
        mage.status = "Sub"
        mage.save()
        return HttpResponseRedirect(mage.get_absolute_url())


class MageWonderView(GenericBackgroundView):
    primary_object_class = Mage
    background_name = "wonder"
    potential_skip = [
        "enhancement",
        "sanctum",
        "allies",
    ]
    form_class = WonderForm
    template_name = "characters/mage/mage/chargen.html"
    multiple_ownership = True


class MageSanctumView(GenericBackgroundView):
    primary_object_class = Mage
    background_name = "sanctum"
    potential_skip = [
        "allies",
    ]
    form_class = SanctumForm
    template_name = "characters/mage/mage/chargen.html"


class MageCharacterCreationView(HumanCharacterCreationView):
    view_mapping = {
        1: MageAttributeView,
        2: MageAbilityView,
        3: MageBackgroundsView,
        4: MageSpheresView,
        5: MageFocusView,
        6: MageExtrasView,
        7: MageFreebiesView,
        8: MageLanguagesView,
        9: MageRoteView,
        10: MageNodeView,
        11: MageLibraryView,
        12: MageFamiliarView,
        13: MageWonderView,
        14: MageEnhancementView,
        15: MageSanctumView,
        16: MageAlliesView,
        17: MageSpecialtiesView,
    }
    model_class = Mage
    key_property = "creation_status"
    default_redirect = MageDetailView
