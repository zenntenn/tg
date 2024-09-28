from characters.models.mage.mtahuman import MtAHuman
from characters.views.core.human import HumanDetailView
from core.views.approved_user_mixin import SpecialUserMixin
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView


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
        "do",
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
        "hypertech",
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
        "do",
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
        "hypertech",
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


class MtAHumanAbilityView(UpdateView):
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
    template_name = "characters/mage/mtahuman/ability_block_form.html"

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
        if triple != [5, 9, 13]:
            form.add_error(None, "Abilities must be distributed 13/9/5")
            return self.form_invalid(form)
        self.object.creation_status += 1
        self.object.save()
        return super().form_valid(form)
