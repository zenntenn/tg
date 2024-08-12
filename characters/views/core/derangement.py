from characters.models.core import Derangement
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView


# Create your views here.
class DerangementDetailView(DetailView):
    model = Derangement
    template_name = "characters/core/derangement/detail.html"


class DerangementCreateView(CreateView):
    model = Derangement
    fields = ["name", "description"]
    template_name = "characters/core/derangement/form.html"


class DerangementUpdateView(UpdateView):
    model = Derangement
    fields = ["name", "description"]
    template_name = "characters/core/derangement/form.html"
