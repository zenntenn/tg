from django.views.generic import CreateView, DetailView, UpdateView
from locations.models.mage.sector import Sector


class SectorDetailView(DetailView):
    model = Sector
    template_name = "locations/mage/sector/detail.html"


class SectorCreateView(CreateView):
    model = Sector
    fields = ["name", "description", "parent", "sector_class", "constraints"]
    template_name = "locations/mage/sector/form.html"


class SectorUpdateView(UpdateView):
    model = Sector
    fields = ["name", "description", "parent", "sector_class", "constraints"]
    template_name = "locations/mage/sector/form.html"
