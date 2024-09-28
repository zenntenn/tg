from characters.models.werewolf.garou import Werewolf
from core.views.approved_user_mixin import SpecialUserMixin
from django.views.generic import CreateView, DetailView, UpdateView


class WerewolfDetailView(SpecialUserMixin, DetailView):
    model = Werewolf
    template_name = "characters/werewolf/garou/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context


class WerewolfUpdateView(SpecialUserMixin, UpdateView):
    model = Werewolf
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
        "rank",
        "auspice",
        "breed",
        "tribe",
        "camps",
        "gnosis",
        "rage",
        "glory",
        "temporary_glory",
        "wisdom",
        "temporary_wisdom",
        "honor",
        "temporary_honor",
        "gifts",
        "rites_known",
        "fetishes_owned",
        "first_change",
        "battle_scars",
        "age_of_first_change",
    ]
    template_name = "characters/werewolf/garou/form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context


class WerewolfCreateView(CreateView):
    model = Werewolf
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
        "rank",
        "auspice",
        "breed",
        "tribe",
        "camps",
        "gnosis",
        "rage",
        "glory",
        "temporary_glory",
        "wisdom",
        "temporary_wisdom",
        "honor",
        "temporary_honor",
        "gifts",
        "rites_known",
        "fetishes_owned",
        "first_change",
        "battle_scars",
        "age_of_first_change",
    ]
    template_name = "characters/werewolf/garou/form.html"
