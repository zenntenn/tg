from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView
from locations.models.core import City


class CityDetailView(DetailView):
    model = City
    template_name = "locations/core/city/detail.html"


class CityCreateView(CreateView):
    model = City
    fields = "__all__"
    template_name = "locations/core/city/form.html"


class CityUpdateView(UpdateView):
    model = City
    fields = [
        "name",
        "parent",
        "gauntlet",
        "shroud",
        "dimension_barrier",
        "description",
        "population",
        "mood",
        "theme",
        "media",
        "politicians",
        "characters",
    ]
    template_name = "locations/core/city/form.html"
