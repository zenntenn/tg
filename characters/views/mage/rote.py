from characters.models.mage.rote import Rote
from django.views.generic import CreateView, DetailView, ListView, UpdateView


class RoteDetailView(DetailView):
    model = Rote
    template_name = "characters/mage/rote/detail.html"


class RoteCreateView(CreateView):
    model = Rote
    fields = ["name", "description", "effect", "practice", "attribute", "ability"]
    template_name = "characters/mage/rote/form.html"


class RoteUpdateView(UpdateView):
    model = Rote
    fields = ["name", "description", "effect", "practice", "attribute", "ability"]
    template_name = "characters/mage/rote/form.html"


class RoteListView(ListView):
    model = Rote
    ordering = ["name"]
    template_name = "characters/mage/rote/list.html"
