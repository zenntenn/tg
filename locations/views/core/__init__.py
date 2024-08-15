from core.utils import get_gameline_name, level_name, tree_sort
from django.shortcuts import render
from django.views import View
from game.models import Chronicle, ObjectType
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


class LocationIndexView(View):
    def get(self, request, *args, **kwargs):
        context = self.get_context(kwargs)
        return render(request, "locations/index.html", context)

    def post(self, request, *args, **kwargs):
        context = self.get_context(kwargs)
        return render(request, "locations/index.html", context)

    def get_context(self, kwargs):
        gameline = kwargs["gameline"]
        game_locations = ObjectType.objects.filter(gameline=gameline, type="loc")
        game_location_types = [x.name for x in game_locations]
        context = {"objects": game_locations, "gameline": get_gameline_name(gameline)}
        chron_dict = {}
        for chron in list(Chronicle.objects.all()) + [None]:
            locations = LocationModel.objects.filter(chronicle=chron).order_by("name")
            locations = [x for x in locations if x.type in game_location_types]
            # context["form"] = RandomLocationForm
            L1 = []
            L2 = []
            for x in LocationModel.objects.filter(
                parent=None, id__in=[x.id for x in locations], chronicle=chron
            ).order_by("name"):
                L1.extend([level_name(y) for y in tree_sort(x)])
                L2.extend(tree_sort(x))
            if len(L1) != 0:
                names_dict = dict(zip(L1, L2))
                chron_dict[chron] = names_dict.items()

        context["chrondict"] = chron_dict
        return context
