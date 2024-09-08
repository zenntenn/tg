from characters.models.core import Specialty
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView, UpdateView


class SpecialtyDetailView(DetailView):
    model = Specialty
    template_name = "characters/core/specialty/detail.html"


class SpecialtyCreateView(CreateView):
    model = Specialty
    fields = ["name", "stat"]
    template_name = "characters/core/specialty/form.html"


class SpecialtyUpdateView(UpdateView):
    model = Specialty
    fields = ["name", "stat"]
    template_name = "characters/core/specialty/form.html"


class SpecialtyListView(ListView):
    model = Specialty
    ordering = ["name"]
    template_name = "characters/core/specialty/list.html"
