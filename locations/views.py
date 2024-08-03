from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import DetailView
from locations.models import LocationModel


# Create your views here.
class LocationDetailView(DetailView):
    model = LocationModel
    template_name = "locations/detail.html"


class GenericLocationDetailView(View):
    views = {
        "location": LocationDetailView,
    }

    def get(self, request, *args, **kwargs):
        loc = LocationModel.objects.get(pk=kwargs["pk"])
        if loc.type in self.views:
            return self.views[loc.type].as_view()(request, *args, **kwargs)
