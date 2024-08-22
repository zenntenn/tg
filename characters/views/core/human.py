from characters.models.core import Human
from characters.views.core.character import CharacterDetailView
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView


# Create your views here.
class HumanDetailView(CharacterDetailView):
    model = Human
    template_name = "characters/core/human/detail.html"


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
        "strength",
        "dexterity",
        "stamina",
        "perception",
        "intelligence",
        "wits",
        "charisma",
        "manipulation",
        "appearance",
    ]
    template_name = "characters/core/human/form.html"


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
        "strength",
        "dexterity",
        "stamina",
        "perception",
        "intelligence",
        "wits",
        "charisma",
        "manipulation",
        "appearance",
    ]
    template_name = "characters/core/human/form.html"


class HumanBasicsView(CreateView):
    model = Human
    fields = [
        "name",
        "nature",
        "demeanor",
        "concept",
    ]
    template_name = "characters/core/human/humanbasics.html"


class HumanAttributeView(UpdateView):
    model = Human
    fields = [
        "strength",
        "dexterity",
        "stamina",
        "perception",
        "intelligence",
        "wits",
        "charisma",
        "manipulation",
        "appearance",
    ]
    template_name = "characters/core/human/attributes.html"

    def form_valid(self, form):
        strength = form.cleaned_data.get("strength")
        dexterity = form.cleaned_data.get("dexterity")
        stamina = form.cleaned_data.get("stamina")
        perception = form.cleaned_data.get("perception")
        intelligence = form.cleaned_data.get("intelligence")
        wits = form.cleaned_data.get("wits")
        charisma = form.cleaned_data.get("charisma")
        manipulation = form.cleaned_data.get("manipulation")
        appearance = form.cleaned_data.get("appearance")

        triple = [
            strength + dexterity + stamina,
            perception + intelligence + wits,
            charisma + manipulation + appearance,
        ]
        triple.sort()
        if triple != [3 + 3, 3 + 5, 3 + 7]:
            form.add_error(None, "Attributes must be distributed 7/5/3")
            return self.form_invalid(form)
        self.object.creation_status += 1
        self.object.save()
        return super().form_valid(form)


class HumanCharacterCreationView(View):
    creation_status = {1: HumanAttributeView}

    def get(self, request, *args, **kwargs):
        char = Human.objects.get(pk=kwargs["pk"])
        if char.creation_status in self.creation_status and char.status == "Un":
            return self.creation_status[char.creation_status].as_view()(
                request, *args, **kwargs
            )
        return HumanDetailView.as_view()(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        char = Human.objects.get(pk=kwargs["pk"])
        if char.creation_status in self.creation_status and char.status == "Un":
            return self.creation_status[char.creation_status].as_view()(
                request, *args, **kwargs
            )
        return HumanDetailView.as_view()(request, *args, **kwargs)
