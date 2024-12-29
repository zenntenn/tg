from characters.forms.werewolf.kinfolk import KinfolkCreationForm
from characters.models.core.merit_flaw_block import MeritFlawRating
from characters.models.werewolf.kinfolk import Kinfolk
from characters.views.core.human import HumanAttributeView, HumanCharacterCreationView
from core.views.approved_user_mixin import SpecialUserMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, FormView, UpdateView


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


class KinfolkBasicsView(LoginRequiredMixin, FormView):
    form_class = KinfolkCreationForm
    template_name = "characters/werewolf/kinfolk/basics.html"

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


class KinfolkAttributeView(HumanAttributeView):
    model = Kinfolk
    template_name = "characters/werewolf/kinfolk/chargen.html"

    primary = 6
    secondary = 4
    tertiary = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context


class KinfolkCharacterCreationView(HumanCharacterCreationView):
    view_mapping = {
        1: KinfolkAttributeView,
    }
    model_class = Kinfolk
    key_property = "creation_status"
    default_redirect = KinfolkDetailView
