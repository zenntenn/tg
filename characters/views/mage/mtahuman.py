from characters.forms.core.freebies import HumanFreebiesForm
from characters.forms.mage.mtahuman import MtAHumanCreationForm
from characters.models.core.ability_block import Ability
from characters.models.core.attribute_block import Attribute
from characters.models.core.background_block import (
    Background,
    BackgroundRating,
    PooledBackgroundRating,
)
from characters.models.core.merit_flaw_block import MeritFlaw
from characters.models.mage.mtahuman import MtAHuman
from characters.views.core.backgrounds import HumanBackgroundsView
from characters.views.core.human import (
    HumanAttributeView,
    HumanCharacterCreationView,
    HumanDetailView,
)
from core.models import Language
from core.views.approved_user_mixin import SpecialUserMixin
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, FormView, UpdateView


class MtAHumanDetailView(HumanDetailView):
    model = MtAHuman
    template_name = "characters/mage/mtahuman/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context


class MtAHumanCreateView(CreateView):
    model = MtAHuman
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
    ]
    template_name = "characters/mage/mtahuman/form.html"


class MtAHumanUpdateView(SpecialUserMixin, UpdateView):
    model = MtAHuman
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
    ]
    template_name = "characters/mage/mtahuman/form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context


class MtAHumanAbilityView(SpecialUserMixin, UpdateView):
    model = MtAHuman
    fields = [
        "awareness",
        "art",
        "leadership",
        "larceny",
        "meditation",
        "research",
        "survival",
        "technology",
        "cosmology",
        "enigmas",
        "finance",
        "law",
        "occult",
        "politics",
        "alertness",
        "athletics",
        "brawl",
        "empathy",
        "expression",
        "intimidation",
        "streetwise",
        "subterfuge",
        "crafts",
        "drive",
        "etiquette",
        "firearms",
        "melee",
        "stealth",
        "academics",
        "computer",
        "investigation",
        "medicine",
        "science",
    ]
    template_name = "characters/mage/mtahuman/chargen.html"

    primary = 11
    secondary = 7
    tertiary = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["primary"] = self.primary
        context["secondary"] = self.secondary
        context["tertiary"] = self.tertiary
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context

    def form_valid(self, form):
        awareness = form.cleaned_data.get("awareness")
        art = form.cleaned_data.get("art")
        leadership = form.cleaned_data.get("leadership")
        larceny = form.cleaned_data.get("larceny")
        meditation = form.cleaned_data.get("meditation")
        research = form.cleaned_data.get("research")
        survival = form.cleaned_data.get("survival")
        technology = form.cleaned_data.get("technology")
        cosmology = form.cleaned_data.get("cosmology")
        enigmas = form.cleaned_data.get("enigmas")
        finance = form.cleaned_data.get("finance")
        law = form.cleaned_data.get("law")
        occult = form.cleaned_data.get("occult")
        politics = form.cleaned_data.get("politics")
        alertness = form.cleaned_data.get("alertness")
        athletics = form.cleaned_data.get("athletics")
        brawl = form.cleaned_data.get("brawl")
        empathy = form.cleaned_data.get("empathy")
        expression = form.cleaned_data.get("expression")
        intimidation = form.cleaned_data.get("intimidation")
        streetwise = form.cleaned_data.get("streetwise")
        subterfuge = form.cleaned_data.get("subterfuge")
        crafts = form.cleaned_data.get("crafts")
        drive = form.cleaned_data.get("drive")
        etiquette = form.cleaned_data.get("etiquette")
        firearms = form.cleaned_data.get("firearms")
        melee = form.cleaned_data.get("melee")
        stealth = form.cleaned_data.get("stealth")
        academics = form.cleaned_data.get("academics")
        computer = form.cleaned_data.get("computer")
        investigation = form.cleaned_data.get("investigation")
        medicine = form.cleaned_data.get("medicine")
        science = form.cleaned_data.get("science")

        for ability in [
            awareness,
            art,
            leadership,
            larceny,
            meditation,
            research,
            survival,
            technology,
            cosmology,
            enigmas,
            finance,
            law,
            occult,
            politics,
            alertness,
            athletics,
            brawl,
            empathy,
            expression,
            intimidation,
            streetwise,
            subterfuge,
            crafts,
            drive,
            etiquette,
            firearms,
            melee,
            stealth,
            academics,
            computer,
            investigation,
            medicine,
            science,
        ]:
            if ability < 0 or ability > 3:
                form.add_error(None, "Abilities must range from 0-3")
                return self.form_invalid(form)

        triple = [
            alertness
            + art
            + athletics
            + awareness
            + brawl
            + empathy
            + expression
            + intimidation
            + leadership
            + streetwise
            + subterfuge,
            crafts
            + drive
            + etiquette
            + firearms
            + larceny
            + meditation
            + melee
            + research
            + stealth
            + survival
            + technology,
            academics
            + computer
            + cosmology
            + enigmas
            + finance
            + investigation
            + law
            + medicine
            + occult
            + politics
            + science,
        ]
        triple.sort()
        if triple != [self.tertiary, self.secondary, self.primary]:
            form.add_error(
                None,
                f"Abilities must be distributed {self.primary}/{self.secondary}/{self.tertiary}",
            )
            return self.form_invalid(form)
        self.object.creation_status += 1
        self.object.save()
        return super().form_valid(form)


class MtAHumanBasicsView(LoginRequiredMixin, FormView):
    form_class = MtAHumanCreationForm
    template_name = "characters/mage/mtahuman/basics.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["storyteller"] = False
        if self.request.user.profile.is_st():
            context["storyteller"] = True
        return context

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()


class MtAHumanAttributeView(HumanAttributeView):
    model = MtAHuman
    template_name = "characters/mage/mtahuman/chargen.html"

    primary = 6
    secondary = 4
    tertiary = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context


class MtAHumanBackgroundsView(HumanBackgroundsView):
    template_name = "characters/mage/mtahuman/chargen.html"


class MtAHumanExtrasView(SpecialUserMixin, UpdateView):
    model = MtAHuman
    fields = [
        "date_of_birth",
        "apparent_age",
        "age",
        "description",
        "history",
        "goals",
        "notes",
        "public_info",
    ]
    template_name = "characters/mage/mtahuman/chargen.html"

    def get_context_data(self, **kwargs):
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


class MtAHumanFreebiesView(SpecialUserMixin, UpdateView):
    model = MtAHuman
    form_class = HumanFreebiesForm
    template_name = "characters/mage/mtahuman/chargen.html"

    def get_context_data(self, **kwargs):
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


class MtAHumanCharacterCreationView(HumanCharacterCreationView):
    view_mapping = {
        1: MtAHumanAttributeView,
        2: MtAHumanAbilityView,
        3: MtAHumanBackgroundsView,
        4: MtAHumanExtrasView,
        5: MtAHumanFreebiesView,
        # TODO: Languages
        # TODO: Expanded Backgrounds
        # TODO: Specialties
    }
    model_class = MtAHuman
    key_property = "creation_status"
    default_redirect = MtAHumanDetailView
