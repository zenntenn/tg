from django.views import View
from locations.models.core.location import LocationModel
from locations.views.mage.node import NodeDetailView

from .city import CityCreateView, CityDetailView, CityUpdateView
from .location import LocationCreateView, LocationDetailView, LocationUpdateView


class GenericLocationDetailView(View):
    views = {
        "location": LocationDetailView,
        "city": CityDetailView,
        "node": NodeDetailView,
    }

    def get(self, request, *args, **kwargs):
        loc = LocationModel.objects.get(pk=kwargs["pk"])
        if loc.type in self.views:
            return self.views[loc.type].as_view()(request, *args, **kwargs)
