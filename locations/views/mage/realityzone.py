from typing import Any

from django.views.generic import CreateView, DetailView, ListView, UpdateView
from locations.models.mage.realityzone import RealityZone, ZoneRating


class RealityZoneDetailView(DetailView):
    model = RealityZone
    template_name = "locations/mage/realityzone/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["positive_practices"] = ZoneRating.objects.filter(
            zone=self.object, rating__gt=0
        )
        context["negative_practices"] = ZoneRating.objects.filter(
            zone=self.object, rating__lt=0
        )
        return context


class RealityZoneCreateView(CreateView):
    model = RealityZone
    fields = ["name", "description", "practices"]
    template_name = "locations/mage/realityzone/form.html"


class RealityZoneUpdateView(UpdateView):
    model = RealityZone
    fields = ["name", "description", "practices"]
    template_name = "locations/mage/realityzone/form.html"


class RealityZoneListView(ListView):
    model = RealityZone
    ordering = ["name"]
    template_name = "locations/mage/realityzone/list.html"
