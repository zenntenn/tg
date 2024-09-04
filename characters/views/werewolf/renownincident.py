from characters.models.werewolf.renownincident import RenownIncident
from django.views.generic import CreateView, DetailView, UpdateView


class RenownIncidentDetailView(DetailView):
    model = RenownIncident
    template_name = "characters/werewolf/renownincident/detail.html"


class RenownIncidentCreateView(CreateView):
    model = RenownIncident
    fields = [
        "name",
        "description",
        "glory",
        "honor",
        "wisdom",
        "posthumous",
        "only_once",
        "breed",
        "rite",
    ]
    template_name = "characters/werewolf/renownincident/form.html"


class RenownIncidentUpdateView(UpdateView):
    model = RenownIncident
    fields = [
        "name",
        "description",
        "glory",
        "honor",
        "wisdom",
        "posthumous",
        "only_once",
        "breed",
        "rite",
    ]
    template_name = "characters/werewolf/renownincident/form.html"
