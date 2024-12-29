from characters.forms.vampire.vtmhuman import VtMHumanCreationForm
from characters.models.vampire.vtmhuman import VtMHuman
from characters.views.core.human import (
    HumanAttributeView,
    HumanCharacterCreationView,
    HumanDetailView,
)
from core.views.approved_user_mixin import SpecialUserMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, FormView, UpdateView


class VtMHumanDetailView(HumanDetailView):
    model = VtMHuman
    template_name = "characters/vampire/vtmhuman/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context


class VtMHumanCreateView(CreateView):
    model = VtMHuman
    fields = [
        "name",
        "owner",
        "description",
        "nature",
        "demeanor",
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
        "xp",
        "awareness",
        "leadership",
        "animal_ken",
        "larceny",
        "performance",
        "survival",
        "finance",
        "law",
        "occult",
        "politics",
        "technology",
    ]
    template_name = "characters/vampire/vtmhuman/form.html"


class VtMHumanUpdateView(SpecialUserMixin, UpdateView):
    model = VtMHuman
    fields = [
        "name",
        "owner",
        "description",
        "nature",
        "demeanor",
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
        "xp",
        "awareness",
        "leadership",
        "animal_ken",
        "larceny",
        "performance",
        "survival",
        "finance",
        "law",
        "occult",
        "politics",
        "technology",
    ]
    template_name = "characters/vampire/vtmhuman/form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context


class VtMHumanBasicsView(LoginRequiredMixin, FormView):
    form_class = VtMHumanCreationForm
    template_name = "characters/vampire/vtmhuman/basics.html"

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


class VtMHumanAttributeView(HumanAttributeView):
    model = VtMHuman
    template_name = "characters/vampire/vtmhuman/chargen.html"

    primary = 6
    secondary = 4
    tertiary = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context


class VtMHumanCharacterCreationView(HumanCharacterCreationView):
    view_mapping = {
        1: VtMHumanAttributeView,
    }
    model_class = VtMHuman
    key_property = "creation_status"
    default_redirect = VtMHumanDetailView
