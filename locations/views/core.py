from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView
from locations.models import LocationModel
from locations.models.core import City


# Create your views here.
class LocationDetailView(DetailView):
    model = LocationModel
    template_name = "locations/location/detail.html"


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
    template_name = "locations/location/form.html"


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
    template_name = "locations/location/form.html"


class CityDetailView(DetailView):
    model = City
    template_name = "locations/city/detail.html"


class CityCreateView(CreateView):
    model = City
    fields = "__all__"
    template_name = "locations/city/form.html"


class CityUpdateView(UpdateView):
    model = City
    fields = [
        "name",
        "parent",
        "gauntlet",
        "shroud",
        "dimension_barrier",
        "reality_zone",
        "description",
        "population",
        "mood",
        "theme",
        "media",
        "politicians",
        "characters",
    ]
    template_name = "locations/city/form.html"


class GenericLocationDetailView(View):
    views = {
        "location": LocationDetailView,
        "city": CityDetailView,
    }

    def get(self, request, *args, **kwargs):
        loc = LocationModel.objects.get(pk=kwargs["pk"])
        if loc.type in self.views:
            return self.views[loc.type].as_view()(request, *args, **kwargs)
