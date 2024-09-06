from django.views.generic import CreateView, DetailView, UpdateView
from locations.models.mage.sanctum import Sanctum


class SanctumDetailView(DetailView):
    model = Sanctum
    template_name = "locations/mage/sanctum/detail.html"


class SanctumCreateView(CreateView):
    model = Sanctum
    fields = ["name", "description", "parent"]
    template_name = "locations/mage/sanctum/form.html"


class SanctumUpdateView(UpdateView):
    model = Sanctum
    fields = ["name", "description", "parent"]
    template_name = "locations/mage/sanctum/form.html"
