from characters.forms.werewolf.wtahuman import WtAHumanCreationForm
from characters.models.werewolf.wtahuman import WtAHuman
from characters.views.core.human import (
    HumanAttributeView,
    HumanCharacterCreationView,
    HumanDetailView,
)
from core.views.approved_user_mixin import SpecialUserMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, FormView, UpdateView


class WtAHumanDetailView(HumanDetailView):
    model = WtAHuman
    template_name = "characters/werewolf/wtahuman/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context


class WtAHumanCreateView(CreateView):
    model = WtAHuman
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
    ]
    template_name = "characters/werewolf/wtahuman/form.html"


class WtAHumanUpdateView(SpecialUserMixin, UpdateView):
    model = WtAHuman
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
    ]
    template_name = "characters/werewolf/wtahuman/form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context


class WtAHumanBasicsView(LoginRequiredMixin, FormView):
    form_class = WtAHumanCreationForm
    template_name = "characters/werewolf/wtahuman/basics.html"

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


class WtAHumanAttributeView(HumanAttributeView):
    model = WtAHuman
    template_name = "characters/werewolf/wtahuman/chargen.html"

    primary = 6
    secondary = 4
    tertiary = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context


class WtAHumanCharacterCreationView(HumanCharacterCreationView):
    view_mapping = {
        1: WtAHumanAttributeView,
        # TODO: Abilities
        # TODO: Backgrounds
        # TODO: Backstory
        # TODO: Freebies
        # TODO: Languages
        # TODO: Expanded Backgrounds
        # TODO: Specialties
    }
    model_class = WtAHuman
    key_property = "creation_status"
    default_redirect = WtAHumanDetailView
