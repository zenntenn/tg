from django.shortcuts import redirect, render
from django.views.generic import DetailView, View

from items.models.core import ItemModel, Weapon


# Create your views here.
class ItemDetailView(DetailView):
    model = ItemModel
    template_name = "items/detail.html"


class WeaponDetailView(DetailView):
    model = Weapon
    template_name = "items/weapon/detail.html"


class GenericItemDetailView(View):
    views = {
        "item": ItemDetailView,
        "weapon": WeaponDetailView,
    }

    def get(self, request, *args, **kwargs):
        item = ItemModel.objects.get(pk=kwargs["pk"])
        if item.type in self.views:
            return self.views[item.type].as_view()(request, *args, **kwargs)
