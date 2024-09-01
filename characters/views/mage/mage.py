from typing import Any

from characters.forms.core.advancement import AdvancementForm
from characters.forms.mage.practiceform import PracticeRatingFormSet
from characters.models.core.archetype import Archetype
from characters.models.core.meritflaw import MeritFlaw
from characters.models.mage.faction import MageFaction
from characters.models.mage.focus import Tenet
from characters.models.mage.mage import Mage, PracticeRating, ResRating
from characters.models.mage.resonance import Resonance
from characters.models.mage.rote import Rote
from characters.views.core.human import (
    HumanAttributeView,
    HumanCharacterCreationView,
    HumanDetailView,
)
from characters.views.mage.mtahuman import MtAHumanAbilityView
from core.widgets import AutocompleteTextInput
from django import forms
from django.forms import BaseModelForm, SelectDateWidget, formset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, FormView, UpdateView


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
        context["practices"] = PracticeRating.objects.filter(mage=self.object)
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


class MageBasicsView(CreateView):
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
        form.instance.faction = MageFaction.objects.get(pk=form.data["faction"])
        form.instance.subfaction = MageFaction.objects.get(pk=form.data["subfaction"])
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
        self.object.save()
        return super().form_valid(form)


class MageFocusView(UpdateView):
    model = Mage
    fields = [
        "metaphysical_tenet",
        "personal_tenet",
        "ascension_tenet",
        "other_tenets",
        # "practices",
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

    def form_valid(self, form):
        self.object.creation_status += 1
        self.object.save()
        return super().form_valid(form)


class MageFreebiesView(UpdateView):
    model = Mage
    form_class = AdvancementForm
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
        # freebies: includes merits and flaws and languages (which are a merit anyway)
        # Rotes
        # Nodes/Libraries/Wonders
    }
    model_class = Mage
    key_property = "creation_status"
    default_redirect = MageDetailView
