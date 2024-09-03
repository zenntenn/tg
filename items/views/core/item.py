from django.views.generic import CreateView, DetailView, UpdateView
from items.models.core import ItemModel


class ItemDetailView(DetailView):
    model = ItemModel
    template_name = "items/core/item/detail.html"


class ItemCreateView(CreateView):
    model = ItemModel
    fields = ["name", "description"]
    template_name = "items/core/item/form.html"


class ItemUpdateView(UpdateView):
    model = ItemModel
    fields = ["name", "description"]
    template_name = "items/core/item/form.html"
