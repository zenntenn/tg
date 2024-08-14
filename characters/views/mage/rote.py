from characters.models.mage.rote import Rote
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, UpdateView


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
