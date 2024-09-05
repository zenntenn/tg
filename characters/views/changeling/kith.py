from characters.models.changeling.kith import Kith
from django.views.generic import CreateView, DetailView, UpdateView


class KithDetailView(DetailView):
    model = Kith
    template_name = "characters/changeling/kith/detail.html"


class KithCreateView(CreateView):
    model = Kith
    fields = ["name", "description", "affinity", "frailty"]
    template_name = "characters/changeling/kith/form.html"


class KithUpdateView(UpdateView):
    model = Kith
    fields = ["name", "description", "affinity", "frailty"]
    template_name = "characters/changeling/kith/form.html"
