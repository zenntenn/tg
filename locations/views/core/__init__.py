from django.views import View
from locations.models.core.location import LocationModel
from locations.views import mage

from .city import CityCreateView, CityDetailView, CityUpdateView
from .location import LocationCreateView, LocationDetailView, LocationUpdateView


class GenericLocationDetailView(View):
    views = {
        "location": LocationDetailView,
        "city": CityDetailView,
        "node": mage.NodeDetailView,
        "sector": mage.SectorDetailView,
        "library": mage.LibraryDetailView,
        "horizon_realm": mage.RealmDetailView,
    }

    def get(self, request, *args, **kwargs):
        loc = LocationModel.objects.get(pk=kwargs["pk"])
        if loc.type in self.views:
            return self.views[loc.type].as_view()(request, *args, **kwargs)
