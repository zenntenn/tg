from characters.models.wraith.wtohuman import WtOHuman
from characters.views.core.human import HumanDetailView
from core.views.approved_user_mixin import SpecialUserMixin
from django.views.generic import CreateView, DetailView, UpdateView


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
        "allies",
        "artifact",
        "eidolon",
        "haunt",
        "legacy",
        "memoriam",
        "notoriety",
        "relic",
        "status_background",
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
        "allies",
        "artifact",
        "eidolon",
        "haunt",
        "legacy",
        "memoriam",
        "notoriety",
        "relic",
        "status_background",
    ]
    template_name = "characters/wraith/wtohuman/form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context
