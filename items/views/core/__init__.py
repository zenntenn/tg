from core.utils import get_gameline_name
from django.shortcuts import render
from django.views import View
from game.models import Chronicle, ObjectType
from items.models.core.item import ItemModel
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


class GenericItemDetailView(View):
    views = {
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

    def get(self, request, *args, **kwargs):
        item = ItemModel.objects.get(pk=kwargs["pk"])
        if item.type in self.views:
            return self.views[item.type].as_view()(request, *args, **kwargs)


class ItemIndexView(View):
    def get(self, request, *args, **kwargs):
        context = self.get_context(kwargs)
        return render(request, "items/index.html", context)

    def post(self, request, *args, **kwargs):
        context = self.get_context(kwargs)
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

        return context

        items = ItemModel.objects.filter(chronicle=None).order_by("name")
        context = {}
        context["items"] = items
        # context["form"] = RandomItemForm
        return context
