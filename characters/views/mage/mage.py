from typing import Any

from characters.models.core.meritflaw import MeritFlaw
from characters.models.mage.faction import MageFaction
from characters.models.mage.mage import Mage, ResRating
from characters.models.mage.resonance import Resonance
from characters.models.mage.rote import Rote
from characters.views.core.human import HumanAttributeView, HumanDetailView
from characters.views.mage.mtahuman import MtAHumanAbilityView
from django.forms import BaseModelForm, formset_factory
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View


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


class MageAttributeView(HumanAttributeView):
    model = Mage
    template_name = "characters/mage/mage/attributes.html"


class MageAbilityView(MtAHumanAbilityView):
    model = Mage
    template_name = "characters/mage/mage/abilities.html"


class MageBackgroundsView(UpdateView):
    model = Mage
    fields = []
    template_name = "characters/mage/mage/backgrounds.html"


class MageFocusView(UpdateView):
    model = Mage
    fields = []
    template_name = "characters/mage/mage/focus.html"


class MageSpheresView(UpdateView):
    model = Mage
    fields = []
    template_name = "characters/mage/mage/spheres.html"


class MageCharacterCreationView(View):
    creation_status = {
        1: MageAttributeView,
        2: MageAbilityView,
        3: MageBackgroundsView,
        4: MageFocusView,
        5: MageSpheresView,
    }

    def get(self, request, *args, **kwargs):
        char = Mage.objects.get(pk=kwargs["pk"])
        if char.creation_status in self.creation_status and char.status == "Un":
            return self.creation_status[char.creation_status].as_view()(
                request, *args, **kwargs
            )
        return HumanDetailView.as_view()(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        char = Mage.objects.get(pk=kwargs["pk"])
        if char.creation_status in self.creation_status and char.status == "Un":
            return self.creation_status[char.creation_status].as_view()(
                request, *args, **kwargs
            )
        return HumanDetailView.as_view()(request, *args, **kwargs)
