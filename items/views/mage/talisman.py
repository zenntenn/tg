from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, View
from items.models.mage import WonderResonanceRating
from items.models.mage.talisman import Talisman


class TalismanDetailView(View):
    def get(self, request, *args, **kwargs):
        talisman = Talisman.objects.get(pk=kwargs["pk"])
        context = self.get_context(talisman)
        return render(request, "items/mage/talisman/detail.html", context)

    def get_context(self, talisman):
        return {
            "object": talisman,
            "resonance": WonderResonanceRating.objects.filter(wonder=talisman).order_by(
                "resonance__name"
            ),
        }


class TalismanCreateView(CreateView):
    model = Talisman
    fields = [
        "name",
        "rank",
        "background_cost",
        "quintessence_max",
        "description",
        "powers",
    ]
    template_name = "items/mage/talisman/form.html"


class TalismanUpdateView(UpdateView):
    model = Talisman
    fields = [
        "name",
        "rank",
        "background_cost",
        "quintessence_max",
        "description",
        "powers",
    ]
    template_name = "items/mage/talisman/form.html"
