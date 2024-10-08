from characters.models.mage import Effect
from django.views.generic import CreateView, DetailView, ListView, UpdateView


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


class EffectListView(ListView):
    model = Effect
    ordering = ["name"]
    template_name = "characters/mage/effect/list.html"
