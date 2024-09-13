from typing import Any

from characters.forms.core.advancement import AdvancementForm
from characters.forms.core.ally import AllyForm
from characters.forms.core.specialty import SpecialtiesForm
from characters.forms.mage.advancement import MageAdvancementForm
from characters.forms.mage.effect import EffectFormSet
from characters.forms.mage.practiceform import PracticeRatingFormSet
from characters.forms.mage.rote import RoteCreationForm
from characters.models.core.ability import Ability
from characters.models.core.archetype import Archetype
from characters.models.core.attribute import Attribute
from characters.models.core.background import Background
from characters.models.core.human import Human
from characters.models.core.meritflaw import MeritFlaw
from characters.models.core.specialty import Specialty
from characters.models.core.statistic import Statistic
from characters.models.mage.effect import Effect
from characters.models.mage.faction import MageFaction
from characters.models.mage.focus import Practice, Tenet
from characters.models.mage.mage import Mage, PracticeRating, ResRating
from characters.models.mage.mtahuman import MtAHuman
from characters.models.mage.resonance import Resonance
from characters.models.mage.rote import Rote
from characters.models.mage.sphere import Sphere
from characters.models.werewolf.spirit_character import SpiritCharacter
from characters.views.core.human import (
    HumanAttributeView,
    HumanCharacterCreationView,
    HumanDetailView,
)
from characters.views.mage.mtahuman import MtAHumanAbilityView
from core.forms.language import HumanLanguageForm
from core.models import Language
from core.views.generic import MultipleFormsetsMixin
from core.widgets import AutocompleteTextInput
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.forms import BaseModelForm, SelectDateWidget, formset_factory
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import CreateView, FormView, UpdateView
from items.forms.mage.wonder import WonderForm, WonderResonancePracticeRatingFormSet
from items.models.core.item import ItemModel
from items.models.mage.artifact import Artifact
from items.models.mage.charm import Charm
from items.models.mage.talisman import Talisman
from items.models.mage.wonder import Wonder, WonderResonanceRating
from locations.forms.core.sanctum import SanctumForm
from locations.forms.mage.node import (
    NodeForm,
    NodeMeritFlawFormSet,
    NodeResonancePracticeRatingFormSet,
    NodeResonanceRatingForm,
)
from locations.forms.mage.reality_zone import RealityZonePracticeRatingFormSet
from locations.models.mage.node import Node, NodeMeritFlawRating, NodeResonanceRating
from locations.models.mage.reality_zone import RealityZone, ZoneRating
from locations.models.mage.sanctum import Sanctum


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
            examples = Ability.objects.all()
            examples = [
                x
                for x in examples
                if getattr(m, x.property_name, 0) < 5 and hasattr(m, x.property_name)
            ]
        elif category_choice == "Background":
            examples = Background.objects.all()
            examples = [
                x
                for x in examples
                if getattr(m, x.property_name, 0) < 5 and hasattr(m, x.property_name)
            ]
        elif category_choice == "MeritFlaw":
            examples = m.filter_mfs()
            if m.total_flaws() <= -7:
                examples = examples.exclude(max_rating__lt=0)
            examples = examples.exclude(min_rating__gt=m.freebies)
        elif category_choice == "Sphere":
            examples = Sphere.objects.all()
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
        elif category_choice == "Practice":
            examples = Practice.objects.all()
            ids = PracticeRating.objects.filter(mage=m, rating=5).values_list(
                "practice__id", flat=True
            )
            examples = examples.exclude(pk__in=ids)
        else:
            examples = []

        return render(request, self.template_name, {"examples": examples})


def get_abilities(request):
    object_id = request.GET.get("object")
    object = Mage.objects.get(id=object_id)
    practice_id = request.GET.get("practice_id")
    prac = Practice.objects.get(id=practice_id)
    abilities = prac.abilities.all().order_by("name")
    abilities = [x for x in abilities if getattr(object, x.property_name) > 0]
    abilities_list = [{"id": ability.id, "name": ability.name} for ability in abilities]
    return JsonResponse(abilities_list, safe=False)


class MageDetailView(HumanDetailView):
    model = Mage
    template_name = "characters/mage/mage/detail.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["resonance"] = ResRating.objects.filter(
            mage=self.object, rating__gte=1
        ).order_by("resonance__name")
        all_effects = list(Rote.objects.filter(mage=context["object"]))
        row_length = 2
        all_effects = [
            all_effects[i : i + row_length]
            for i in range(0, len(all_effects), row_length)
        ]
        context["rotes"] = all_effects
        context["practices"] = PracticeRating.objects.filter(
            mage=self.object, rating__gt=0
        )
        context["sanctum_owned"] = None
        if Sanctum.objects.filter(owned_by=self.object).count() > 0:
            context["sanctum_owned"] = Sanctum.objects.filter(
                owned_by=self.object
            ).last()
        context["node_owned"] = None
        if Node.objects.filter(owned_by=self.object).count() > 0:
            context["node_owned"] = Node.objects.filter(owned_by=self.object).last()
        context["items_owned"] = ItemModel.objects.filter(owned_by=self.object)
        return context


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
        "awareness",
        "art",
        "leadership",
        "animal_kinship",
        "blatancy",
        "carousing",
        "do",
        "flying",
        "high_ritual",
        "lucid_dreaming",
        "search",
        "seduction",
        "martial_arts",
        "meditation",
        "research",
        "survival",
        "technology",
        "acrobatics",
        "archery",
        "biotech",
        "energy_weapons",
        "hypertech",
        "jetpack",
        "riding",
        "torture",
        "cosmology",
        "enigmas",
        "esoterica",
        "law",
        "occult",
        "politics",
        "area_knowledge",
        "belief_systems",
        "cryptography",
        "demolitions",
        "finance",
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
        "allies",
        "alternate_identity",
        "arcane",
        "avatar",
        "backup",
        "blessing",
        "certification",
        "chantry",
        "cult",
        "demesne",
        "destiny",
        "dream",
        "enhancement",
        "fame",
        "familiar",
        "influence",
        "legend",
        "library",
        "node",
        "past_lives",
        "patron",
        "rank",
        "requisitions",
        "resources",
        "retainers",
        "sanctum",
        "secret_weapons",
        "spies",
        "status_background",
        "totem",
        "wonder",
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
        "awakening",
        "seekings",
        "quiets",
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
    ]
    template_name = "characters/mage/mage/form.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["affiliation"].queryset = MageFaction.objects.filter(parent=None)
        form.fields["faction"].queryset = MageFaction.objects.none()
        form.fields["subfaction"].queryset = MageFaction.objects.none()
        return form


class MageUpdateView(UpdateView):
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
        "awareness",
        "art",
        "leadership",
        "animal_kinship",
        "blatancy",
        "carousing",
        "do",
        "flying",
        "high_ritual",
        "lucid_dreaming",
        "search",
        "seduction",
        "martial_arts",
        "meditation",
        "research",
        "survival",
        "technology",
        "acrobatics",
        "archery",
        "biotech",
        "energy_weapons",
        "hypertech",
        "jetpack",
        "riding",
        "torture",
        "cosmology",
        "enigmas",
        "esoterica",
        "law",
        "occult",
        "politics",
        "area_knowledge",
        "belief_systems",
        "cryptography",
        "demolitions",
        "finance",
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
        "allies",
        "alternate_identity",
        "arcane",
        "avatar",
        "backup",
        "blessing",
        "certification",
        "chantry",
        "cult",
        "demesne",
        "destiny",
        "dream",
        "enhancement",
        "fame",
        "familiar",
        "influence",
        "legend",
        "library",
        "node",
        "past_lives",
        "patron",
        "rank",
        "requisitions",
        "resources",
        "retainers",
        "sanctum",
        "secret_weapons",
        "spies",
        "status_background",
        "totem",
        "wonder",
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
        "awakening",
        "seekings",
        "quiets",
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
    ]
    template_name = "characters/mage/mage/form.html"


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
    ]
    template_name = "characters/mage/mage/magebasics.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["nature"].queryset = Archetype.objects.all().order_by("name")
        form.fields["demeanor"].queryset = Archetype.objects.all().order_by("name")
        form.fields["affiliation"].queryset = MageFaction.objects.filter(parent=None)
        form.fields["faction"].queryset = MageFaction.objects.none()
        form.fields["subfaction"].queryset = MageFaction.objects.none()
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
        return super().form_valid(form)


class MageAttributeView(HumanAttributeView):
    model = Mage
    template_name = "characters/mage/mage/chargen.html"


class MageAbilityView(MtAHumanAbilityView):
    model = Mage
    template_name = "characters/mage/mage/chargen.html"


class MageBackgroundsView(UpdateView):
    model = Mage
    fields = [
        "allies",
        "alternate_identity",
        "arcane",
        "avatar",
        "backup",
        "blessing",
        "certification",
        "chantry",
        "contacts",
        "cult",
        "demesne",
        "destiny",
        "dream",
        "enhancement",
        "fame",
        "familiar",
        "influence",
        "legend",
        "library",
        "node",
        "past_lives",
        "patron",
        "rank",
        "requisitions",
        "resources",
        "retainers",
        "sanctum",
        "secret_weapons",
        "spies",
        "status_background",
        "totem",
        "mentor",
        "wonder",
    ]
    template_name = "characters/mage/mage/chargen.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["requisitions"].required = False
        form.fields["secret_weapons"].required = False
        return form

    def form_valid(self, form):
        allies = form.cleaned_data.get("allies")
        alternate_identity = form.cleaned_data.get("alternate_identity")
        arcane = form.cleaned_data.get("arcane")
        avatar = form.cleaned_data.get("avatar")
        backup = form.cleaned_data.get("backup")
        blessing = form.cleaned_data.get("blessing")
        certification = form.cleaned_data.get("certification")
        chantry = form.cleaned_data.get("chantry")
        cult = form.cleaned_data.get("cult")
        contacts = form.cleaned_data.get("contacts")
        demesne = form.cleaned_data.get("demesne")
        destiny = form.cleaned_data.get("destiny")
        dream = form.cleaned_data.get("dream")
        enhancement = form.cleaned_data.get("enhancement")
        fame = form.cleaned_data.get("fame")
        familiar = form.cleaned_data.get("familiar")
        influence = form.cleaned_data.get("influence")
        legend = form.cleaned_data.get("legend")
        library = form.cleaned_data.get("library")
        node = form.cleaned_data.get("node")
        past_lives = form.cleaned_data.get("past_lives")
        patron = form.cleaned_data.get("patron")
        rank = form.cleaned_data.get("rank")
        requisitions = form.cleaned_data.get("requisitions")
        resources = form.cleaned_data.get("resources")
        retainers = form.cleaned_data.get("retainers")
        sanctum = form.cleaned_data.get("sanctum")
        secret_weapons = form.cleaned_data.get("secret_weapons")
        spies = form.cleaned_data.get("spies")
        status_background = form.cleaned_data.get("status_background")
        totem = form.cleaned_data.get("totem")
        wonder = form.cleaned_data.get("wonder")
        mentor = form.cleaned_data.get("mentor")

        if secret_weapons is None:
            secret_weapons = 0
        if requisitions is None:
            requisitions = 0

        for background in [
            allies,
            alternate_identity,
            contacts,
            arcane,
            avatar,
            backup,
            blessing,
            certification,
            chantry,
            cult,
            demesne,
            destiny,
            dream,
            enhancement,
            fame,
            familiar,
            influence,
            legend,
            library,
            node,
            past_lives,
            patron,
            rank,
            requisitions,
            mentor,
            resources,
            retainers,
            sanctum,
            secret_weapons,
            spies,
            status_background,
            totem,
            wonder,
        ]:
            if background < 0 or background > 5:
                form.add_error(None, "Backgrounds must range from 0-5")
                return self.form_invalid(form)

        bg_points = (
            sum(
                [
                    allies,
                    alternate_identity,
                    arcane,
                    avatar,
                    backup,
                    blessing,
                    certification,
                    chantry,
                    cult,
                    demesne,
                    destiny,
                    dream,
                    enhancement,
                    fame,
                    familiar,
                    contacts,
                    influence,
                    legend,
                    library,
                    mentor,
                    node,
                    past_lives,
                    patron,
                    rank,
                    requisitions,
                    resources,
                    retainers,
                    sanctum,
                    secret_weapons,
                    spies,
                    status_background,
                    totem,
                    wonder,
                ]
            )
            + enhancement
            + sanctum
            + totem
        )
        if bg_points != self.object.background_points:
            form.add_error(
                None, f"Backgrounds must total {self.object.background_points} points"
            )
            return self.form_invalid(form)
        self.object.creation_status += 1
        self.object.quintessence = avatar
        self.object.save()
        self.object.willpower = 5
        self.object.save()
        return super().form_valid(form)


class MageFocusView(UpdateView):
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
        return form

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["practice_formset"] = PracticeRatingFormSet(
                self.request.POST, instance=self.object
            )
        else:
            context["practice_formset"] = PracticeRatingFormSet(instance=self.object)
        context["resonance"] = ResRating.objects.filter(
            mage=self.object, rating__gte=1
        ).order_by("resonance__name")
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        practice_formset = context["practice_formset"]
        if practice_formset.is_valid():
            self.object = form.save()
            ratings = [x.cleaned_data.get("rating") for x in practice_formset]
            practice_total = sum(ratings)
            if practice_total != self.object.arete:
                form.add_error(None, "Starting Practices must add up to Arete rating")
                return self.form_invalid(form)
            for practice_form in practice_formset:
                practice = practice_form.cleaned_data.get("practice")
                rating = practice_form.cleaned_data.get("rating")
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
                    return super().form_invalid(form)
            self.object.creation_status += 1
            self.object.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)


class MageSpheresView(UpdateView):
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
        ].queryset = self.object.get_affinity_sphere_options()
        form.fields["resonance"].widget = AutocompleteTextInput(
            suggestions=[x.name.title() for x in Resonance.objects.order_by("name")]
        )
        return form

    def form_valid(self, form):
        arete = form.cleaned_data.get("arete")
        correspondence = form.cleaned_data.get("correspondence")
        time = form.cleaned_data.get("time")
        spirit = form.cleaned_data.get("spirit")
        forces = form.cleaned_data.get("forces")
        matter = form.cleaned_data.get("matter")
        life = form.cleaned_data.get("life")
        entropy = form.cleaned_data.get("entropy")
        mind = form.cleaned_data.get("mind")
        prime = form.cleaned_data.get("prime")
        affinity_sphere = form.cleaned_data.get("affinity_sphere")
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
            self.object.freebie_spend_record("Arete", "arete", i + 2)
        self.object.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors
        if "resonance" in errors and "resonance" in form.data:
            del errors["resonance"]
        if not errors:
            return self.form_valid(form)
        return super().form_invalid(form)


class MageExtrasView(UpdateView):

    model = Mage
    fields = [
        "date_of_birth",
        "apparent_age",
        "age_of_awakening",
        "hair",
        "eyes",
        "ethnicity",
        "nationality",
        "height",
        "weight",
        "age",
        "sex",
        "description",
        "childhood",
        "history",
        "awakening",
        "seekings",
        "quiets",
        "avatar_description",
        "goals",
        "notes",
    ]
    template_name = "characters/mage/mage/chargen.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["practices"] = PracticeRating.objects.filter(
            mage=self.object, rating__gt=0
        )
        context["resonance"] = ResRating.objects.filter(
            mage=self.object, rating__gte=1
        ).order_by("resonance__name")
        return context

    def form_valid(self, form):
        self.object.creation_status += 1
        self.object.save()
        return super().form_valid(form)


class MageFreebiesView(UpdateView):
    model = Mage
    form_class = MageAdvancementForm
    template_name = "characters/mage/mage/chargen.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["practices"] = PracticeRating.objects.filter(
            mage=self.object, rating__gt=0
        )
        context["resonance"] = ResRating.objects.filter(
            mage=self.object, rating__gte=1
        ).order_by("resonance__name")
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
            in ["Attribute", "Ability", "Background", "Sphere", "Tenet", "Practice"]
            and form.data["example"] == ""
        ):
            form.add_error(None, "Must Choose Trait")
            return super().form_invalid(form)
        elif form.data["category"] == "Resonance" and form.data["resonance"] == "":
            form.add_error(None, "Must Choose Resonance")
            return super().form_invalid(form)
        trait_type = form.data["category"].lower()
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
        elif form.data["category"] == "Background":
            trait = Background.objects.get(pk=form.data["example"])
            value = getattr(self.object, trait.property_name) + 1
            self.object.add_background(trait.property_name)
            self.object.freebies -= cost
            trait = trait.name
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
            if self.object.arete >= 3:
                form.add_error(
                    None, "Arete Cannot Be Raised Above 3 At Character Creation"
                )
                return super().form_invalid(form)
            trait = "Arete"
            value = getattr(self.object, "arete") + 1
            self.object.add_arete()
            self.object.freebies -= cost
        elif form.data["category"] == "Quintessence":
            trait = "Quintessence"
            value = 4
            self.object.rote_points += 4
            self.object.freebies -= cost
        if form.data["category"] != "MeritFlaw":
            self.object.spent_freebies.append(
                self.object.freebie_spend_record(trait, trait_type, value)
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


class MageLanguagesView(FormView):
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

        num_languages = form.cleaned_data.get("num_languages", 1)
        for i in range(num_languages):
            language_name = form.cleaned_data.get(f"language_{i}")
            if language_name:
                language, created = Language.objects.get_or_create(name=language_name)
                human.languages.add(language)
        human.creation_status += 1
        human.save()
        return HttpResponseRedirect(human.get_absolute_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = get_object_or_404(Human, pk=self.kwargs.get("pk"))
        return context


class MageRoteView(CreateView):
    model = Rote
    form_class = RoteCreationForm
    template_name = "characters/mage/mage/chargen.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        mage_id = self.kwargs.get("pk")
        context["object"] = Mage.objects.get(id=mage_id)
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        mage_id = self.kwargs.get("pk")
        mage = Mage.objects.get(pk=mage_id)
        kwargs["instance"] = mage
        return kwargs

    def form_invalid(self, form):
        errors = form.errors
        if "ability" in errors:
            del errors["ability"]
        if not errors:
            return self.form_valid(form)
        return super().form_invalid(form)

    def form_valid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        mage = context["object"]
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
                    if getattr(mage, step) == 0:
                        mage.creation_status += 1
                    else:
                        mage.save()
                        break
            return HttpResponseRedirect(mage.get_absolute_url())
        return super().form_invalid(form)


class MageNodeView(MultipleFormsetsMixin, FormView):
    form_class = NodeForm
    template_name = "characters/mage/mage/chargen.html"
    formsets = {
        "rz_form": RealityZonePracticeRatingFormSet,
        "resonance_form": NodeResonancePracticeRatingFormSet,
        "mf_form": NodeMeritFlawFormSet,
    }

    def form_valid(self, form):
        context = self.get_context_data()
        mage = context["object"]
        n = Node(
            name=form.cleaned_data["name"],
            description=form.cleaned_data["description"],
            ratio=form.cleaned_data["ratio"],
            size=form.cleaned_data["size"],
            quintessence_form=form.cleaned_data["quintessence_form"],
            tass_form=form.cleaned_data["tass_form"],
            gauntlet=3,
            owned_by=mage,
            chronicle=mage.chronicle,
            owner=mage.owner,
            status="Sub",
        )
        n.set_rank(mage.node)
        n.points -= form.cleaned_data["ratio"]
        n.points -= form.cleaned_data["size"]

        resonance_data = self.get_form_data("resonance_form")
        for res in resonance_data:
            res["resonance"] = Resonance.objects.get_or_create(name=res["resonance"])[0]
            res["rating"] = int(res["rating"])
            if res["rating"] > 5:
                form.add_error(
                    None,
                    "Resonance may not be higher than 5",
                )
                return self.form_invalid(form)
        total_resonance = sum([x["rating"] for x in resonance_data])

        mf_data = self.get_form_data("mf_form")
        for res in mf_data:
            res["mf"] = MeritFlaw.objects.get(id=res["mf"])
            res["rating"] = int(res["rating"])
        total_mfs = sum([x["rating"] for x in mf_data])

        rz_data = self.get_form_data("rz_form")
        for res in rz_data:
            res["practice"] = Practice.objects.get(id=res["practice"])
            res["rating"] = int(res["rating"])
        total_rz = sum([x["rating"] for x in rz_data])
        total_positive = sum([x["rating"] for x in rz_data if x["rating"] > 0])
        if total_rz != 0:
            form.add_error(None, "Ratings must total 0")
            return super().form_invalid(form)
        if total_positive != mage.node:
            form.add_error(None, "Positive Ratings must equal Node rating")
            return super().form_invalid(form)

        if total_resonance < n.rank:
            form.add_error(None, "Resonance total must match or exceed rank")
            return self.form_invalid(form)
        n.points -= total_resonance - n.rank
        n.points -= total_mfs
        if n.points < 0:
            form.add_error(
                None,
                "Node invalid: spend fewer points on merits/flaws, resonance, size, or ratio",
            )
            return self.form_invalid(form)
        n.update_output()
        n.save()

        for resonance in resonance_data:
            NodeResonanceRating.objects.create(
                node=n, resonance=resonance["resonance"], rating=resonance["rating"]
            )

        for mf in mf_data:
            NodeMeritFlawRating.objects.create(node=n, mf=mf["mf"], rating=mf["rating"])

        rzone = RealityZone.objects.create(name="{n.name} Reality Zone")
        n.reality_zone = rzone
        n.save()
        for rz in rz_data:
            ZoneRating.objects.create(
                zone=rzone, practice=rz["practice"], rating=rz["rating"]
            )

        mage.creation_status += 1
        mage.save()
        for step in [
            "library",
            "familiar",
            "wonder",
            "enhancement",
            "sanctum",
            "allies",
        ]:
            if getattr(mage, step) == 0:
                mage.creation_status += 1
            else:
                mage.save()
                break
        mage.save()
        return HttpResponseRedirect(mage.get_absolute_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = get_object_or_404(Human, pk=self.kwargs.get("pk"))
        return context


class MageLibraryView:
    # Skip if Familiar == 0
    # Skip if Wonder == 0
    # Skip if Enhancement == 0
    # skip if sanctum == 0
    # skip if allies == 0
    pass


class MageFamiliarView:
    # Skip if Wonder == 0
    # Skip if Enhancement == 0
    # skip if sanctum == 0
    # skip if allies == 0
    pass


class MageWonderView(MultipleFormsetsMixin, FormView):
    form_class = WonderForm
    formsets = {
        "effects_form": EffectFormSet,
        "resonance_form": WonderResonancePracticeRatingFormSet,
    }
    template_name = "characters/mage/mage/chargen.html"

    wonder_classes = {
        "charm": Charm,
        "artifact": Artifact,
        "talisman": Talisman,
    }

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["object"] = Mage.objects.get(id=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        mage = context["object"]
        w = self.wonder_classes[form.cleaned_data["wonder_type"]](
            name=form.cleaned_data["name"],
            description=form.cleaned_data["description"],
            arete=form.cleaned_data["arete"],
            rank=mage.wonder,
            owned_by=mage,
            chronicle=mage.chronicle,
            owner=mage.owner,
            status="Sub",
        )
        points = 3 * w.rank

        resonance_data = self.get_form_data("resonance_form")
        for res in resonance_data:
            res["resonance"] = Resonance.objects.get_or_create(name=res["resonance"])[0]
            res["rating"] = int(res["rating"])
            if res["rating"] > 5:
                form.add_error(
                    None,
                    "Resonance may not be higher than 5",
                )
                return self.form_invalid(form)
        total_resonance = sum([x["rating"] for x in resonance_data])
        if total_resonance < w.rank:
            form.add_error(None, "Resonance must be at least rank")
            return self.form_invalid(form)
        if form.cleaned_data["wonder_type"] == "charm":
            max_cost = w.rank
        else:
            max_cost = 2 * w.rank

        effects = []
        total_effect_cost = 0
        effects_data = self.get_form_data("effects_form")
        if form.cleaned_data["wonder_type"] == "charm" and len(effects_data) > 1:
            form.add_error(None, "Charms can only have one power")
            return self.form_invalid(form)
        elif form.cleaned_data["wonder_type"] == "artifact" and len(effects_data) > 1:
            form.add_error(None, "Artifacts can only have one power")
            return self.form_invalid(form)
        elif (
            form.cleaned_data["wonder_type"] == "talisman"
            and len(effects_data) > w.rank
        ):
            form.add_error(None, "Talismans may up to their rank in effects")
            return self.form_invalid(form)
        for effect in effects_data:
            for sphere in Sphere.objects.all():
                effect[sphere.property_name] = int(effect[sphere.property_name])
            e = Effect(**effect)
            effects.append(e)
            total_effect_cost += e.cost()
            if total_effect_cost > max_cost:
                form.add_error(
                    None,
                    "Effects cost more than allowed: rank for Charms, twice rank for Artifacts and Talismans",
                )
                return self.form_invalid(form)
        if (total_resonance - w.rank) + total_effect_cost + (w.arete - w.rank) > points:
            form.add_error(
                None,
                "Extra Resonance, Arete, and Effects must be less than 3 times the rank of the Wonder",
            )
            return self.form_invalid(form)

        w.save()
        for e in effects:
            e.save()
            if form.cleaned_data["wonder_type"] in ["charm", "artifact"]:
                w.power = e
            else:
                w.powers.add(e)
        w.save()

        for resonance in resonance_data:
            WonderResonanceRating.objects.create(
                wonder=None,
                resonance=resonance["resonance"],
                rating=resonance["rating"],
            )

        mage.creation_status += 1
        mage.save()
        for step in [
            "enhancement",
            "sanctum",
            "allies",
        ]:
            if getattr(mage, step) == 0:
                mage.creation_status += 1
            else:
                mage.save()
                break
        mage.save()
        return HttpResponseRedirect(mage.get_absolute_url())


class MageEnhancementView:
    # skip if sanctum == 0
    # skip if allies == 0
    pass


class MageSanctumView(CreateView):
    model = Sanctum
    form_class = SanctumForm
    template_name = "characters/mage/mage/chargen.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mage_id = self.kwargs.get("pk")
        context["object"] = Mage.objects.get(id=mage_id)
        context["rz_form"] = RealityZonePracticeRatingFormSet()
        context["form"].fields["name"].initial = f"{context['object']}'s Sanctum"
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        mage = context["object"]
        rz_form = context["rz_form"]
        practices = [
            v
            for k, v in form.data.items()
            if k.startswith("zonerating_set-") and k.endswith("-practice")
        ]
        ratings = [
            int(v)
            for k, v in form.data.items()
            if k.startswith("zonerating_set-") and k.endswith("-rating")
        ]
        pairs = [
            (Practice.objects.get(id=practice), rating)
            for practice, rating in zip(practices, ratings)
            if rating != 0
        ]
        total_rating = sum([v for k, v in pairs])
        total_positive = sum([v for k, v in pairs if v > 0])
        if total_rating != 0:
            form.add_error(None, "Ratings must total 0")
            return super().form_invalid(form)
        if total_positive != mage.sanctum:
            form.add_error(None, "Positive Ratings must equal Sanctum rating")
            return super().form_invalid(form)
        rz = RealityZone.objects.create(name=f"{mage.name}'s Sanctum Reality Zone")
        for p, r in pairs:
            ZoneRating.objects.create(zone=rz, practice=p, rating=r)
        if form.save(mage, reality_zone=rz):
            mage.creation_status += 1
            mage.save()
            for step in [
                "allies",
            ]:
                if getattr(mage, step) == 0:
                    mage.creation_status += 1
                else:
                    mage.save()
                    break
            mage.save()
            return HttpResponseRedirect(mage.get_absolute_url())
        return super().form_invalid(form)


class MageAlliesView(FormView):
    form_class = AllyForm
    template_name = "characters/mage/mage/chargen.html"

    ally_types = {"human": MtAHuman, "mage": Mage, "spirit": SpiritCharacter}

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["object"] = Mage.objects.get(id=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        mage = context["object"]
        char_class = self.ally_types[form.cleaned_data["ally_type"]]
        a = char_class.objects.create(
            name=form.cleaned_data["name"],
            concept=form.cleaned_data["name"],
            notes=form.cleaned_data["name"]
            + f"<br> Rank {mage.allies} Ally for {mage.name}",
            chronicle=mage.chronicle,
            npc=True,
            status="Un",
        )
        mage.allied_characters.add(a)
        mage.creation_status += 1
        mage.save()
        return HttpResponseRedirect(mage.get_absolute_url())


class MageSpecialtiesView(FormView):
    form_class = SpecialtiesForm
    template_name = "characters/mage/mage/chargen.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["object"] = Mage.objects.get(id=self.kwargs["pk"])
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        mage = Mage.objects.get(id=self.kwargs["pk"])
        kwargs["object"] = mage
        stats = (
            list(Attribute.objects.all())
            + list(Ability.objects.all())
            + list(Sphere.objects.all())
        )
        stats = [x for x in stats if getattr(mage, x.property_name, 0) >= 4] + [
            x
            for x in stats
            if getattr(mage, x.property_name, 0) >= 1
            and x.property_name
            in [
                "arts",
                "athletics",
                "crafts",
                "firearms",
                "martial_arts",
                "melee",
                "academics",
                "esoterica",
                "lore",
                "politics",
                "science",
            ]
        ]
        kwargs["specialties_needed"] = [x.property_name for x in stats]
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
        # 11: Library,
        # 12: Familiar,
        13: MageWonderView,
        # 14: Enhancements,
        15: MageSanctumView,
        16: MageAlliesView,
        17: MageSpecialtiesView,
    }
    model_class = Mage
    key_property = "creation_status"
    default_redirect = MageDetailView
