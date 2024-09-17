from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView
from locations.models import LocationModel


class LocationDetailView(DetailView):
    model = LocationModel
    template_name = "locations/core/location/detail.html"


class LocationCreateView(CreateView):
    model = LocationModel
    fields = [
        "name",
        "parent",
        "gauntlet",
        "shroud",
        "dimension_barrier",
        "description",
    ]
    template_name = "locations/core/location/form.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["name"].widget.attrs.update({"placeholder": "Enter name here"})
        form.fields["description"].widget.attrs.update(
            {"placeholder": "Enter description here"}
        )
        form.fields["parent"].empty_label = "Parent Location"
        return form


class LocationUpdateView(UpdateView):
    model = LocationModel
    fields = [
        "name",
        "parent",
        "gauntlet",
        "shroud",
        "dimension_barrier",
        "description",
    ]
    template_name = "locations/core/location/form.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["name"].widget.attrs.update({"placeholder": "Enter name here"})
        form.fields["description"].widget.attrs.update(
            {"placeholder": "Enter description here"}
        )
        form.fields["parent"].empty_label = "Parent Location"
        return form
