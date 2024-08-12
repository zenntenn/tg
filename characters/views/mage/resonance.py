from characters.models.mage import Resonance
from django.views.generic import CreateView, DetailView, UpdateView


class ResonanceDetailView(DetailView):
    model = Resonance
    template_name = "characters/mage/resonance/detail.html"


class ResonanceCreateView(CreateView):
    model = Resonance
    fields = [
        "name",
        "correspondence",
        "life",
        "prime",
        "entropy",
        "matter",
        "spirit",
        "forces",
        "mind",
        "time",
    ]
    template_name = "characters/mage/resonance/form.html"


class ResonanceUpdateView(UpdateView):
    model = Resonance
    fields = [
        "name",
        "correspondence",
        "life",
        "prime",
        "entropy",
        "matter",
        "spirit",
        "forces",
        "mind",
        "time",
    ]
    template_name = "characters/mage/resonance/form.html"
