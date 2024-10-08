from characters.models.vampire.vtmhuman import VtMHuman
from characters.views.core.human import HumanDetailView
from core.views.approved_user_mixin import SpecialUserMixin
from django.views.generic import CreateView, DetailView, UpdateView


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
        "allies",
        "alternate_identity",
        "black_hand_membership",
        "domain",
        "fame",
        "generation",
        "herd",
        "influence",
        "resources",
        "retainers",
        "rituals",
        "status_background",
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
        "allies",
        "alternate_identity",
        "black_hand_membership",
        "domain",
        "fame",
        "generation",
        "herd",
        "influence",
        "resources",
        "retainers",
        "rituals",
        "status_background",
    ]
    template_name = "characters/vampire/vtmhuman/form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context
