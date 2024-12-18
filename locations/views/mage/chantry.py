from typing import Any

from characters.models.core.background_block import Background, BackgroundRating
from characters.views.core.generic_background import GenericBackgroundView
from core.views.generic import DictView
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DetailView, FormView, UpdateView
from locations.forms.mage.chantry import ChantryPointForm
from locations.forms.mage.sanctum import SanctumForm
from locations.models.mage.chantry import Chantry, ChantryBackgroundRating


class ChantryDetailView(DetailView):
    model = Chantry
    template_name = "locations/mage/chantry/detail.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        factions = []
        f = self.object.faction
        while f is not None:
            factions.append(f)
            f = f.parent
        factions.reverse()
        factions = [f'<a href="{x.get_absolute_url()}">{x}</a>' for x in factions]
        factions = "/".join(factions)
        context["factions"] = factions
        return context


class ChantryCreateView(CreateView):
    model = Chantry
    fields = [
        "name",
        "parent",
        "description",
        "faction",
        "leadership_type",
        "leaders",
        "season",
        "chantry_type",
        "total_points",
        "integrated_effects",
        "members",
        "cabals",
        "ambassador",
        "node_tender",
        "investigator",
        "guardian",
        "teacher",
    ]
    template_name = "locations/mage/chantry/form.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["name"].widget.attrs.update({"placeholder": "Enter name here"})
        form.fields["description"].widget.attrs.update(
            {"placeholder": "Enter description here"}
        )
        return form


class ChantryUpdateView(UpdateView):
    model = Chantry
    fields = [
        "name",
        "parent",
        "description",
        "faction",
        "leadership_type",
        "leaders",
        "season",
        "chantry_type",
        "total_points",
        "integrated_effects",
        "members",
        "cabals",
        "ambassador",
        "node_tender",
        "investigator",
        "guardian",
        "teacher",
    ]
    template_name = "locations/mage/chantry/form.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["name"].widget.attrs.update({"placeholder": "Enter name here"})
        form.fields["description"].widget.attrs.update(
            {"placeholder": "Enter description here"}
        )
        return form


class LoadExamplesView(View):
    template_name = "characters/core/human/load_examples_dropdown_list.html"

    def get(self, request, *args, **kwargs):
        category_choice = request.GET.get("category")
        object_id = request.GET.get("object")
        m = Chantry.objects.get(pk=object_id)

        category_choice = request.GET.get("category")
        if category_choice == "New Background":
            examples = Background.objects.filter(
                property_name__in=m.allowed_backgrounds
            ).order_by("name")
            if m.points < 5:
                examples = examples.exclude(property_name__in=["sanctum"])
            if m.points < 4:
                examples = examples.exclude(
                    property_name__in=["enhancement", "requisitions"]
                )
            if m.points < 3:
                examples = examples.exclude(property_name__in=["node", "resources"])
            if m.points < 2:
                examples = examples.exclude(
                    property_name__in=[
                        "allies",
                        "arcane",
                        "backup",
                        "cult",
                        "elders",
                        "library",
                        "retainers",
                        "spies",
                    ]
                )
        elif category_choice == "Existing Background":
            examples = [
                x
                for x in ChantryBackgroundRating.objects.filter(chantry=m, rating__lt=5)
            ]
            if m.points < 5:
                examples = examples.exclude(bg__property_name__in=["sanctum"])
            if m.points < 4:
                examples = examples.exclude(
                    bg__property_name__in=["enhancement", "requisitions"]
                )
            if m.points < 3:
                examples = examples.exclude(bg__property_name__in=["node", "resources"])
            if m.points < 2:
                examples = examples.exclude(
                    bg__property_name__in=[
                        "allies",
                        "arcane",
                        "backup",
                        "cult",
                        "elders",
                        "library",
                        "retainers",
                        "spies",
                    ]
                )
        else:
            examples = []

        return render(request, self.template_name, {"examples": examples})


class ChantryBasicsView(CreateView):
    model = Chantry
    fields = [
        "name",
        "parent",
        "description",
        "faction",
        "leadership_type",
        "season",
        "chantry_type",
        "total_points",
        "gauntlet",
        "shroud",
        "dimension_barrier",
    ]
    template_name = "locations/mage/chantry/basics.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["name"].widget.attrs.update({"placeholder": "Enter name here"})
        form.fields["description"].widget.attrs.update(
            {"placeholder": "Enter description here"}
        )
        return form


class ChantryPointsView(FormView):
    form_class = ChantryPointForm
    template_name = "locations/mage/chantry/locgen.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["pk"] = self.kwargs.get("pk")
        self.object = Chantry.objects.get(pk=self.kwargs["pk"])
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = self.object
        return context

    def get_success_url(self):
        return self.object.get_absolute_url()

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ChantryNodeView(GenericBackgroundView):
    primary_object_class = Chantry
    background_name = "node"
    potential_skip = ["library", "allies", "sanctum"]
    form_class = SanctumForm
    template_name = "locations/mage/chantry/locgen.html"


class ChantryLibrarysView(GenericBackgroundView):
    primary_object_class = Chantry
    background_name = "library"
    potential_skip = ["allies", "sanctum"]
    form_class = SanctumForm
    template_name = "locations/mage/chantry/locgen.html"


class ChantryAlliesView(GenericBackgroundView):
    primary_object_class = Chantry
    background_name = "allies"
    potential_skip = ["sanctum"]
    form_class = SanctumForm
    template_name = "locations/mage/chantry/locgen.html"


class ChantrySanctumView(GenericBackgroundView):
    primary_object_class = Chantry
    background_name = "sanctum"
    potential_skip = []
    form_class = SanctumForm
    template_name = "locations/mage/chantry/locgen.html"


class ChantryIntegratedEffectsView(View):
    pass


class ChantryPersonnelView(View):
    pass


class ChantryCreationView(DictView):
    view_mapping = {
        1: ChantryPointsView,  # Backgrounds
        2: ChantryIntegratedEffectsView,  # effects
        3: ChantryNodeView,  # Nodes
        4: ChantryLibrarysView,  # Libraries
        5: ChantryAlliesView,  # allies
        6: ChantrySanctumView,  # sanctum
        7: ChantryPersonnelView,  # personnel?
    }
    model_class = Chantry
    key_property = "creation_status"
    default_redirect = ChantryDetailView

    def is_valid_key(self, obj, key):
        return key in self.view_mapping and obj.status == "Un"
