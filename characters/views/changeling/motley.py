from characters.models.changeling.motley import Motley
from django.views.generic import CreateView, DetailView, UpdateView


class MotleyDetailView(DetailView):
    model = Motley
    template_name = "characters/changeling/motley/detail.html"


class MotleyCreateView(CreateView):
    model = Motley
    fields = ["name", "description", "members", "leader"]
    template_name = "characters/changeling/motley/form.html"


class MotleyUpdateView(UpdateView):
    model = Motley
    fields = ["name", "description", "members", "leader"]
    template_name = "characters/changeling/motley/form.html"
