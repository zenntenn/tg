from characters.models.werewolf.camp import Camp
from django.views.generic import CreateView, DetailView, UpdateView


class CampDetailView(DetailView):
    model = Camp
    template_name = "characters/werewolf/camp/detail.html"


class CampCreateView(CreateView):
    model = Camp
    fields = ["name", "description", "tribe", "camp_type"]
    template_name = "characters/werewolf/camp/form.html"


class CampUpdateView(UpdateView):
    model = Camp
    fields = ["name", "description", "tribe", "camp_type"]
    template_name = "characters/werewolf/camp/form.html"
