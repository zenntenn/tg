from characters.models.werewolf.fomoripower import FomoriPower
from django.views.generic import CreateView, DetailView, ListView, UpdateView


class FomoriPowerDetailView(DetailView):
    model = FomoriPower
    template_name = "characters/werewolf/fomoripower/detail.html"


class FomoriPowerCreateView(CreateView):
    model = FomoriPower
    fields = ["name", "description"]
    template_name = "characters/werewolf/fomoripower/form.html"


class FomoriPowerUpdateView(UpdateView):
    model = FomoriPower
    fields = ["name", "description"]
    template_name = "characters/werewolf/fomoripower/form.html"


class FomoriPowerListView(ListView):
    model = FomoriPower
    ordering = ["name"]
    template_name = "characters/werewolf/fomoripower/list.html"
