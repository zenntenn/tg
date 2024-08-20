from django.views.generic import CreateView, DetailView, UpdateView
from locations.models.werewolf.caern import Caern


class CaernDetailView(DetailView):
    model = Caern
    template_name = "locations/werewolf/caern/detail.html"


class CaernCreateView(CreateView):
    model = Caern
    fields = [
        "name",
        "description",
        "rank",
        "caern_type",
    ]
    template_name = "locations/werewolf/caern/form.html"


class CaernUpdateView(UpdateView):
    model = Caern
    fields = [
        "name",
        "description",
        "rank",
        "caern_type",
    ]
    template_name = "locations/werewolf/caern/form.html"
