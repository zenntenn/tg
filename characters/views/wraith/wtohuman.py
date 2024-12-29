from characters.forms.wraith.wtohuman import WtOHumanCreationForm
from characters.models.wraith.wtohuman import WtOHuman
from characters.views.core.human import (
    HumanAttributeView,
    HumanCharacterCreationView,
    HumanDetailView,
)
from core.views.approved_user_mixin import SpecialUserMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, FormView, UpdateView


class WtOHumanDetailView(HumanDetailView):
    model = WtOHuman
    template_name = "characters/wraith/wtohuman/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context


class WtOHumanCreateView(CreateView):
    model = WtOHuman
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
        "awareness",
        "persuasion",
        "larceny",
        "meditation",
        "performance",
        "bureaucracy",
        "enigmas",
        "occult",
        "politics",
        "technology",
    ]
    template_name = "characters/wraith/wtohuman/form.html"


class WtOHumanUpdateView(SpecialUserMixin, UpdateView):
    model = WtOHuman
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
        "awareness",
        "persuasion",
        "larceny",
        "meditation",
        "performance",
        "bureaucracy",
        "enigmas",
        "occult",
        "politics",
        "technology",
    ]
    template_name = "characters/wraith/wtohuman/form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context


class WtOHumanBasicsView(LoginRequiredMixin, FormView):
    form_class = WtOHumanCreationForm
    template_name = "characters/wraith/wtohuman/basics.html"

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


class WtOHumanAttributeView(HumanAttributeView):
    model = WtOHuman
    template_name = "characters/wraith/wtohuman/chargen.html"

    primary = 6
    secondary = 4
    tertiary = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context


class WtOHumanCharacterCreationView(HumanCharacterCreationView):
    view_mapping = {
        1: WtOHumanAttributeView,
        # TODO: Abilities
        # TODO: Backgrounds
        # TODO: Backstory
        # TODO: Freebies
        # TODO: Languages
        # TODO: Expanded Backgrounds
        # TODO: Specialties
    }
    model_class = WtOHuman
    key_property = "creation_status"
    default_redirect = WtOHumanDetailView
