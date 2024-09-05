from characters.models.werewolf.tribe import Tribe
from django.views.generic import CreateView, DetailView, UpdateView


class TribeDetailView(DetailView):
    model = Tribe
    template_name = "characters/werewolf/tribe/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO: split gifts by level once implemented
        # TODO: camp list
        return context


class TribeCreateView(CreateView):
    model = Tribe
    fields = ["name", "willpower", "description"]
    template_name = "characters/werewolf/tribe/form.html"


class TribeUpdateView(UpdateView):
    model = Tribe
    fields = ["name", "willpower", "description"]
    template_name = "characters/werewolf/tribe/form.html"
