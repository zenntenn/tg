from django.shortcuts import render, redirect
from items.models.core import ItemModel
from django.views.generic import DetailView, View

# Create your views here.


class ItemDetailView(DetailView):
    model = ItemModel
    template_name = "items/detail.html"

class GenericItemDetailView(View):
    views = {
        "item": ItemDetailView,
    }

    def get(self, request, *args, **kwargs):
        item = ItemModel.objects.get(pk=kwargs["pk"])
        if item.type in self.views:
            return self.views[item.type].as_view()(request, *args, **kwargs)
    