from characters.models.mage import Effect, Resonance
from django.views.generic import CreateView, DetailView, UpdateView, View


class EffectDetailView(DetailView):
    model = Effect
    template_name = "characters/mage/effect/detail.html"


class EffectCreateView(CreateView):
    model = Effect
    fields = [
        "name",
        "description",
        "correspondence",
        "time",
        "spirit",
        "matter",
        "life",
        "forces",
        "entropy",
        "mind",
        "prime",
    ]
    template_name = "characters/mage/effect/form.html"


class EffectUpdateView(UpdateView):
    model = Effect
    fields = [
        "name",
        "description",
        "correspondence",
        "time",
        "spirit",
        "matter",
        "life",
        "forces",
        "entropy",
        "mind",
        "prime",
    ]
    template_name = "characters/mage/effect/form.html"


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
