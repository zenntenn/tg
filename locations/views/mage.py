from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, UpdateView
from locations.models.mage import Node, NodeMeritFlawRating, NodeResonanceRating


class NodeDetailView(View):
    def get(self, request, *args, **kwargs):
        node = Node.objects.get(pk=kwargs["pk"])
        context = self.get_context(node)
        return render(request, "locations/mage/node/detail.html", context)

    def get_context(self, node):
        return {
            "object": node,
            "resonance": NodeResonanceRating.objects.filter(node=node).order_by(
                "resonance__name"
            ),
            "merits_and_flaws": NodeMeritFlawRating.objects.filter(node=node).order_by(
                "mf__name"
            ),
        }


class NodeCreateView(CreateView):
    model = Node
    fields = [
        "name",
        "parent",
        "reality_zone",
        "description",
        "rank",
        "size",
        "quintessence_per_week",
        "quintessence_form",
        "tass_per_week",
        "tass_form",
        "merits_and_flaws",
        "resonance",
    ]
    template_name = "locations/mage/node/form.html"


class NodeUpdateView(UpdateView):
    model = Node
    fields = [
        "name",
        "parent",
        "reality_zone",
        "description",
        "rank",
        "size",
        "quintessence_per_week",
        "quintessence_form",
        "tass_per_week",
        "tass_form",
        "merits_and_flaws",
        "resonance",
    ]
    template_name = "locations/mage/node/form.html"
