from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView
from items.models.mage import Wonder, WonderResonanceRating


class WonderDetailView(DetailView):
    model = Wonder
    template_name = "items/mage/wonder/detail.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["resonance"] = "resonance": WonderResonanceRating.objects.filter(wonder=wonder).order_by(
                "resonance__name"
            )
        return context



class WonderCreateView(CreateView):
    model = Wonder
    fields = ["name", "rank", "background_cost", "quintessence_max", "description"]
    template_name = "items/mage/wonder/form.html"


class WonderUpdateView(UpdateView):
    model = Wonder
    fields = ["name", "rank", "background_cost", "quintessence_max", "description"]
    template_name = "items/mage/wonder/form.html"
