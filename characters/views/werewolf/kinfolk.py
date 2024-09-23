from characters.models.core.meritflaw import MeritFlawRating
from characters.models.werewolf.kinfolk import Kinfolk
from core.views.approved_user_mixin import SpecialUserMixin
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView


class KinfolkDetailView(SpecialUserMixin, DetailView):
    model = Kinfolk
    template_name = "characters/werewolf/kinfolk/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        specialties = {}
        for attribute in self.object.get_attributes():
            specialties[attribute] = ", ".join(
                [x.name for x in self.object.specialties.filter(stat=attribute)]
            )
        for ability in self.object.get_abilities():
            specialties[ability] = ", ".join(
                [x.name for x in self.object.specialties.filter(stat=ability)]
            )
        for key, value in specialties.items():
            context[f"{key}_spec"] = value

        context["merits_and_flaws"] = MeritFlawRating.objects.order_by(
            "mf__name"
        ).filter(character=self.object)
        all_gifts = list(context["object"].gifts.all())
        row_length = 3
        all_gifts = [
            all_gifts[i : i + row_length] for i in range(0, len(all_gifts), row_length)
        ]
        context["gifts"] = all_gifts
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context


class KinfolkCreateView(CreateView):
    model = Kinfolk
    fields = [
        "name",
        "description",
        "concept",
        "nature",
        "demeanor",
        "strength",
        "dexterity",
        "stamina",
        "perception",
        "intelligence",
        "wits",
        "charisma",
        "manipulation",
        "appearance",
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
        "specialties",
        "contacts",
        "mentor",
        "languages",
        "willpower",
        "derangements",
        "age",
        "apparent_age",
        "date_of_birth",
        "merits_and_flaws",
        "history",
        "goals",
        "notes",
        "leadership",
        "primal_urge",
        "animal_ken",
        "larceny",
        "performance",
        "survival",
        "enigmas",
        "law",
        "occult",
        "rituals",
        "technology",
        "allies",
        "ancestors",
        "fate",
        "fetish",
        "kinfolk_rating",
        "pure_breed",
        "resources",
        "rites",
        "spirit_heritage",
        "totem",
        "breed",
        "tribe",
        "relation",
        "gifts",
        "gnosis",
        "fetishes_owned",
        "glory",
        "temporary_glory",
        "wisdom",
        "temporary_wisdom",
        "honor",
        "temporary_honor",
    ]
    template_name = "characters/werewolf/kinfolk/form.html"


class KinfolkUpdateView(SpecialUserMixin, UpdateView):
    model = Kinfolk
    fields = [
        "name",
        "description",
        "concept",
        "nature",
        "demeanor",
        "strength",
        "dexterity",
        "stamina",
        "perception",
        "intelligence",
        "wits",
        "charisma",
        "manipulation",
        "appearance",
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
        "specialties",
        "contacts",
        "mentor",
        "languages",
        "willpower",
        "derangements",
        "age",
        "apparent_age",
        "date_of_birth",
        "merits_and_flaws",
        "history",
        "goals",
        "notes",
        "leadership",
        "primal_urge",
        "animal_ken",
        "larceny",
        "performance",
        "survival",
        "enigmas",
        "law",
        "occult",
        "rituals",
        "technology",
        "allies",
        "ancestors",
        "fate",
        "fetish",
        "kinfolk_rating",
        "pure_breed",
        "resources",
        "rites",
        "spirit_heritage",
        "totem",
        "breed",
        "tribe",
        "relation",
        "gifts",
        "gnosis",
        "fetishes_owned",
        "glory",
        "temporary_glory",
        "wisdom",
        "temporary_wisdom",
        "honor",
        "temporary_honor",
    ]
    template_name = "characters/werewolf/kinfolk/form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context
