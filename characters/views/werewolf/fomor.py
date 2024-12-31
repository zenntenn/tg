from characters.forms.werewolf.fomor import FomorCreationForm
from characters.models.werewolf.fomor import Fomor
from characters.views.core.backgrounds import HumanBackgroundsView
from characters.views.core.human import HumanAttributeView, HumanCharacterCreationView
from characters.views.werewolf.wtahuman import WtAHumanAbilityView
from core.views.approved_user_mixin import SpecialUserMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, FormView, UpdateView


class FomorDetailView(SpecialUserMixin, DetailView):
    model = Fomor
    template_name = "characters/werewolf/fomor/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context


class FomorCreateView(CreateView):
    model = Fomor
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
        "rage",
        "gnosis",
        "powers",
    ]
    template_name = "characters/werewolf/fomor/form.html"


class FomorUpdateView(SpecialUserMixin, UpdateView):
    model = Fomor
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
        "rage",
        "gnosis",
        "powers",
    ]
    template_name = "characters/werewolf/fomor/form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context


class FomorBasicsView(LoginRequiredMixin, FormView):
    form_class = FomorCreationForm
    template_name = "characters/werewolf/fomor/basics.html"

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


class FomorAttributeView(HumanAttributeView):
    model = Fomor
    template_name = "characters/werewolf/fomor/chargen.html"

    primary = 6
    secondary = 4
    tertiary = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context


class FomorAbilityView(WtAHumanAbilityView):
    model = Fomor
    template_name = "characters/werewolf/fomor/chargen.html"


class FomorBackgroundsView(HumanBackgroundsView):
    template_name = "characters/werewolf/fomor/chargen.html"


class FomorCharacterCreationView(HumanCharacterCreationView):
    view_mapping = {
        1: FomorAttributeView,
        2: FomorAbilityView,
        3: FomorBackgroundsView,
        # TODO: Powers
        # TODO: Backstory
        # TODO: Freebies
        # TODO: Languages
        # TODO: Expanded Backgrounds
        # TODO: Specialties
    }
    model_class = Fomor
    key_property = "creation_status"
    default_redirect = FomorDetailView
