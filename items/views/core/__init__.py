from django.views import View
from items.models.core.item import ItemModel
from items.views import mage

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
    }

    def get(self, request, *args, **kwargs):
        item = ItemModel.objects.get(pk=kwargs["pk"])
        if item.type in self.views:
            return self.views[item.type].as_view()(request, *args, **kwargs)
