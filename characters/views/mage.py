from characters.models.mage import Effect
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
