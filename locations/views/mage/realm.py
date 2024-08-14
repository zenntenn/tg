from django.views.generic import CreateView, DetailView, UpdateView
from locations.models.mage.realm import HorizonRealm


class RealmDetailView(DetailView):
    model = HorizonRealm
    template_name = "locations/mage/realm/detail.html"


class RealmCreateView(CreateView):
    model = HorizonRealm
    fields = ["name", "description", "parent"]
    template_name = "locations/mage/realm/form.html"


class RealmUpdateView(UpdateView):
    model = HorizonRealm
    fields = ["name", "description", "parent"]
    template_name = "locations/mage/realm/form.html"
