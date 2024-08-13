from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, View
from items.models.mage import Charm, WonderResonanceRating


class CharmDetailView(View):
    def get(self, request, *args, **kwargs):
        charm = Charm.objects.get(pk=kwargs["pk"])
        context = self.get_context(charm)
        return render(request, "items/mage/charm/detail.html", context)

    def get_context(self, charm):
        return {
            "object": charm,
            "resonance": WonderResonanceRating.objects.filter(wonder=charm).order_by(
                "resonance__name"
            ),
        }


class CharmCreateView(CreateView):
    model = Charm
    fields = [
        "name",
        "rank",
        "background_cost",
        "quintessence_max",
        "description",
        "power",
        "arete",
    ]
    template_name = "items/mage/charm/form.html"


class CharmUpdateView(UpdateView):
    model = Charm
    fields = [
        "name",
        "rank",
        "background_cost",
        "quintessence_max",
        "description",
        "power",
        "arete",
    ]
    template_name = "items/mage/charm/form.html"