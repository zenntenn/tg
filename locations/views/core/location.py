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
        "reality_zone",
        "description",
    ]
    template_name = "locations/core/location/form.html"


class LocationUpdateView(UpdateView):
    model = LocationModel
    fields = [
        "name",
        "parent",
        "gauntlet",
        "shroud",
        "dimension_barrier",
        "reality_zone",
        "description",
    ]
    template_name = "locations/core/location/form.html"
