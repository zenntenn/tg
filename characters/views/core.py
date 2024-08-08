from characters.models.core import (
    Archetype,
    Character,
    Derangement,
    Group,
    Human,
    MeritFlaw,
    Specialty,
)
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View


# Create your views here.
class CharacterDetailView(DetailView):
    model = Character
    template_name = "characters/character/detail.html"


class CharacterCreateView(CreateView):
    model = Character
    fields = "__all__"
    template_name = "characters/character/form.html"


class CharacterUpdateView(UpdateView):
    model = Character
    fields = "__all__"
    template_name = "characters/character/form.html"


class HumanDetailView(DetailView):
    model = Human
    template_name = "characters/human/detail.html"


class HumanCreateView(CreateView):
    model = Human
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
        "hair",
        "eyes",
        "ethnicity",
        "nationality",
        "height",
        "weight",
        "sex",
        "merits_and_flaws",
        "childhood",
        "history",
        "goals",
        "notes",
    ]
    template_name = "characters/human/form.html"

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        print(form.data)
        return super().form_invalid(form)

    def form_valid(self, form):
        print("VALID")
        print(form.data)
        return super().form_valid(form)


class HumanUpdateView(UpdateView):
    model = Human
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
        "hair",
        "eyes",
        "ethnicity",
        "nationality",
        "height",
        "weight",
        "sex",
        "merits_and_flaws",
        "childhood",
        "history",
        "goals",
        "notes",
    ]
    template_name = "characters/human/form.html"


class GenericCharacterDetailView(View):
    character_views = {
        "character": CharacterDetailView,
        "human": HumanDetailView,
    }

    def get(self, request, *args, **kwargs):
        char = Character.objects.get(pk=kwargs["pk"])
        if char.type in self.character_views:
            return self.character_views[char.type].as_view()(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        char = Character.objects.get(pk=kwargs["pk"])
        if char.type in self.character_views:
            return self.character_views[char.type].as_view()(request, *args, **kwargs)


class ArchetypeDetailView(DetailView):
    model = Archetype
    template_name = "characters/archetype/detail.html"


class ArchetypeCreateView(CreateView):
    model = Archetype
    fields = ["name", "description"]
    template_name = "characters/archetype/form.html"


class ArchetypeUpdateView(UpdateView):
    model = Archetype
    fields = ["name", "description"]
    template_name = "characters/archetype/form.html"


class MeritFlawDetailView(View):
    def get(self, request, *args, **kwargs):
        mf = MeritFlaw.objects.get(pk=kwargs["pk"])
        context = self.get_context(mf)
        return render(request, "characters/meritflaw/detail.html", context)

    def get_context(self, mf):
        context = {}
        context["object"] = mf
        mf_ratings = list(mf.ratings.values_list("value", flat=True))
        mf_ratings.sort()
        context["ratings"] = ", ".join([str(x) for x in mf_ratings])
        return context


class MeritFlawCreateView(CreateView):
    model = MeritFlaw
    fields = ["name", "description", "ratings", "allowed_types"]
    template_name = "characters/meritflaw/form.html"


class MeritFlawUpdateView(UpdateView):
    model = MeritFlaw
    fields = ["name", "description", "ratings", "allowed_types"]
    template_name = "characters/meritflaw/form.html"


class DerangementDetailView(DetailView):
    model = Derangement
    template_name = "characters/derangement/detail.html"


class DerangementCreateView(CreateView):
    model = Derangement
    fields = ["name", "description"]
    template_name = "characters/derangement/form.html"


class DerangementUpdateView(UpdateView):
    model = Derangement
    fields = ["name", "description"]
    template_name = "characters/derangement/form.html"


class GroupDetailView(DetailView):
    model = Group
    template_name = "characters/group/detail.html"


class GroupCreateView(CreateView):
    model = Group
    fields = ["name", "description", "members", "leader"]
    template_name = "characters/group/form.html"


class GroupUpdateView(UpdateView):
    model = Group
    fields = ["name", "description", "members", "leader"]
    template_name = "characters/group/form.html"


class GenericGroupDetailView(View):
    group_views = {
        "group": GroupDetailView,
    }

    def get(self, request, *args, **kwargs):
        group = Group.objects.get(pk=kwargs["pk"])
        if group.type in self.group_views:
            return self.group_views[group.type].as_view()(request, *args, **kwargs)


class SpecialtyDetailView(DetailView):
    model = Specialty
    template_name = "characters/specialty/detail.html"


class SpecialtyCreateView(CreateView):
    model = Specialty
    fields = ["name", "stat"]
    template_name = "characters/specialty/form.html"


class SpecialtyUpdateView(UpdateView):
    model = Specialty
    fields = ["name", "stat"]
    template_name = "characters/specialty/form.html"
