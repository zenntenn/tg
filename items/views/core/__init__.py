from collections import defaultdict

from core.utils import get_gameline_name
from core.views.generic import DictView
from django.http import Http404
from django.shortcuts import redirect, render
from django.views import View
from game.models import Chronicle, ObjectType
from items.forms.core.item_creation import ItemCreationForm
from items.models.core.item import ItemModel
from items.models.core.material import Material
from items.models.core.medium import Medium
from items.models.core.meleeweapon import MeleeWeapon
from items.models.core.rangedweapon import RangedWeapon
from items.models.core.thrownweapon import ThrownWeapon
from items.models.core.weapon import Weapon
from items.models.mage.artifact import Artifact
from items.models.mage.charm import Charm
from items.models.mage.grimoire import Grimoire
from items.models.mage.talisman import Talisman
from items.models.mage.wonder import Wonder
from items.models.werewolf.fetish import Fetish
from items.views import mage, werewolf

from .item import ItemCreateView, ItemDetailView, ItemUpdateView
from .material import MaterialCreateView, MaterialDetailView, MaterialUpdateView
from .medium import MediumCreateView, MediumDetailView, MediumUpdateView
from .meleeweapon import (
    MeleeWeaponCreateView,
    MeleeWeaponDetailView,
    MeleeWeaponUpdateView,
)
from .rangedweapon import (
    RangedWeaponCreateView,
    RangedWeaponDetailView,
    RangedWeaponUpdateView,
)
from .thrownweapon import (
    ThrownWeaponCreateView,
    ThrownWeaponDetailView,
    ThrownWeaponUpdateView,
)
from .weapon import WeaponCreateView, WeaponDetailView, WeaponUpdateView


class GenericItemDetailView(DictView):
    view_mapping = {
        "item": ItemDetailView,
        "weapon": WeaponDetailView,
        "melee_weapon": MeleeWeaponDetailView,
        "thrown_weapon": ThrownWeaponDetailView,
        "ranged_weapon": RangedWeaponDetailView,
        "wonder": mage.WonderDetailView,
        "charm": mage.CharmDetailView,
        "artifact": mage.ArtifactDetailView,
        "talisman": mage.TalismanDetailView,
        "grimoire": mage.GrimoireDetailView,
        "fetish": werewolf.FetishDetailView,
    }
    model_class = ItemModel
    key_property = "type"
    default_redirect = "items:index wod"


class ItemIndexView(View):
    items = {
        "item": ItemModel,
        "weapon": Weapon,
        "melee_weapon": MeleeWeapon,
        "thrown_weapon": ThrownWeapon,
        "ranged_weapon": RangedWeapon,
        "wonder": Wonder,
        "charm": Charm,
        "artifact": Artifact,
        "talisman": Talisman,
        "grimoire": Grimoire,
        "fetish": Fetish,
        "material": Material,
        "medium": Medium,
    }

    def get(self, request, *args, **kwargs):
        context = self.get_context(kwargs)
        return render(request, "items/index.html", context)

    def post(self, request, *args, **kwargs):
        context = self.get_context(kwargs)
        action = request.POST.get("action")
        item_type = request.POST["item_type"]
        gameline = kwargs["gameline"]
        if action == "create":
            if gameline == "wod":
                redi = f"items:create:{item_type}"
            elif gameline == "wta":
                redi = f"items:werewolf:create:{item_type}"
            elif gameline == "mta":
                redi = f"items:mage:create:{item_type}"
            return redirect(redi)
        elif action == "random":
            if request.user.is_authenticated:
                user = request.user
            else:
                user = None
            item = self.items[request.POST["item_type"]].objects.create(
                name=request.POST["name"], owner=user
            )
            if request.POST["rank"] is None:
                rank = None
            else:
                rank = int(request.POST["rank"])
            try:
                item.random(rank=rank)
            except:
                raise Http404
            item.save()
            return redirect(item.get_absolute_url())
        return render(request, "items/index.html", context)

    def get_context(self, kwargs):
        gameline = kwargs["gameline"]
        game_items = ObjectType.objects.filter(gameline=gameline, type="obj")
        game_items_types = [x.name for x in game_items]
        context = {"objects": game_items, "gameline": get_gameline_name(gameline)}

        chron_dict = {}
        for chron in list(Chronicle.objects.all()) + [None]:
            c = ItemModel.objects.filter(chronicle=chron).order_by("name")
            items = [x for x in c if x.type in game_items_types]

            c = ItemModel.objects.filter(
                id__in=[x.id for x in items], chronicle=chron
            ).order_by("name")
            chron_dict[chron] = c

        context["chron_dict"] = chron_dict
        context["form"] = ItemCreationForm(gameline=gameline)
        return context
