from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, View
from items.models.mage import Wonder, WonderResonanceRating


class WonderDetailView(View):
    def get(self, request, *args, **kwargs):
        wonder = Wonder.objects.get(pk=kwargs["pk"])
        context = self.get_context(wonder)
        return render(request, "items/mage/wonder/detail.html", context)

    def get_context(self, wonder):
        return {
            "object": wonder,
            "resonance": WonderResonanceRating.objects.filter(wonder=wonder).order_by(
                "resonance__name"
            ),
        }


class WonderCreateView(CreateView):
    model = Wonder
    fields = ["name", "rank", "background_cost", "quintessence_max", "description"]
    template_name = "items/mage/wonder/form.html"


class WonderUpdateView(UpdateView):
    model = Wonder
    fields = ["name", "rank", "background_cost", "quintessence_max", "description"]
    template_name = "items/mage/wonder/form.html"
