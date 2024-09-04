from typing import Any

from django.views.generic import CreateView, DetailView, UpdateView
from locations.models.mage.realityzone import RealityZone, ZoneRating


class RealityZoneDetailView(DetailView):
    model = RealityZone
    template_name = "locations/mage/realityzone/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["practices"] = ZoneRating.objects.filter(zone=self.object)
        return context


class RealityZoneCreateView(CreateView):
    model = RealityZone
    fields = ["name", "description", "practices"]
    template_name = "locations/mage/realityzone/form.html"


class RealityZoneUpdateView(UpdateView):
    model = RealityZone
    fields = ["name", "description", "practices"]
    template_name = "locations/mage/realityzone/form.html"
