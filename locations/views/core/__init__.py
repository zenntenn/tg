from core.utils import get_gameline_name, level_name, tree_sort
from core.views.generic import DictView
from django.http import Http404
from django.shortcuts import redirect, render
from django.views import View
from game.models import Chronicle, ObjectType
from locations.forms.core.location_creation import LocationCreationForm
from locations.models.core.city import City
from locations.models.core.location import LocationModel
from locations.models.mage.chantry import Chantry
from locations.models.mage.library import Library
from locations.models.mage.node import Node
from locations.models.mage.reality_zone import RealityZone
from locations.models.mage.realm import HorizonRealm
from locations.models.mage.sanctum import Sanctum
from locations.models.mage.sector import Sector
from locations.models.werewolf.caern import Caern
from locations.views import mage, werewolf

from .city import CityCreateView, CityDetailView, CityUpdateView
from .location import LocationCreateView, LocationDetailView, LocationUpdateView


class GenericLocationDetailView(DictView):
    view_mapping = {
        "location": LocationDetailView,
        "city": CityDetailView,
        "node": mage.NodeDetailView,
        "sector": mage.SectorDetailView,
        "library": mage.LibraryDetailView,
        "horizon_realm": mage.RealmDetailView,
        "caern": werewolf.CaernDetailView,
        "sanctum": mage.SanctumDetailView,
        "chantry": mage.ChantryDetailView,
    }

    model_class = LocationModel
    key_property = "type"
    default_redirect = "locations:index wod"


class LocationIndexView(View):
    locs = {
        "location": LocationModel,
        "city": City,
        "node": Node,
        "sector": Sector,
        "library": Library,
        "horizon_realm": HorizonRealm,
        "caern": Caern,
        "chantry": Chantry,
        "sanctum": Sanctum,
        "reality_zone": RealityZone,
    }

    def get(self, request, *args, **kwargs):
        context = self.get_context(kwargs)
        return render(request, "locations/index.html", context)

    def post(self, request, *args, **kwargs):
        context = self.get_context(kwargs)
        action = request.POST.get("action")
        loc_type = request.POST["loc_type"]
        gameline = kwargs["gameline"]
        if action == "create":
            if gameline == "wod":
                redi = f"locations:create:{loc_type}"
            elif gameline == "wta":
                redi = f"locations:werewolf:create:{loc_type}"
            elif gameline == "mta":
                redi = f"locations:mage:create:{loc_type}"
            return redirect(redi)
        elif action == "index":
            if gameline == "wod":
                redi = f"locations:list:{loc_type}"
            elif gameline == "wta":
                redi = f"locations:werewolf:list:{loc_type}"
            elif gameline == "mta":
                redi = f"locations:mage:list:{loc_type}"
            return redirect(redi)
        elif action == "random":
            if request.user.is_authenticated:
                user = request.user
            else:
                user = None
            try:
                loc = self.locs[request.POST["loc_type"]].objects.create(
                    name=request.POST["name"], owner=user
                )
                if "rank" in dir(loc):
                    loc.rank = int(request.POST["rank"])
                    loc.save()
            except KeyError:
                raise Http404
            if request.POST["rank"] is None:
                rank = None
            else:
                rank = int(request.POST["rank"])
            try:
                loc.random(rank=rank)
            except:
                raise Http404
            loc.save()
            return redirect(loc.get_absolute_url())
        return render(request, "locations/index.html", context)

    def get_context(self, kwargs):
        gameline = kwargs["gameline"]
        game_locations = ObjectType.objects.filter(gameline=gameline, type="loc")
        game_location_types = [x.name for x in game_locations]
        context = {
            "objects": game_locations,
            "gameline": get_gameline_name(gameline),
            "gameline_short": gameline,
        }
        chron_dict = {}
        for chron in list(Chronicle.objects.all()) + [None]:
            chron_dict[chron] = LocationModel.objects.filter(
                chronicle=chron, parent=None
            ).order_by("name")
        context["form"] = LocationCreationForm(gameline=gameline)
        context["chrondict"] = chron_dict
        return context
