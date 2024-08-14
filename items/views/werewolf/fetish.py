from django.views.generic import CreateView, DetailView, UpdateView
from items.models.werewolf.fetish import Fetish


class FetishDetailView(DetailView):
    model = Fetish
    template_name = "items/werewolf/fetish/detail.html"


class FetishCreateView(CreateView):
    model = Fetish
    fields = [
        "name",
        "rank",
        "background_cost",
        "quintessence_max",
        "description",
        "gnosis",
        "spirit",
    ]
    template_name = "items/werewolf/fetish/form.html"


class FetishUpdateView(UpdateView):
    model = Fetish
    fields = [
        "name",
        "rank",
        "background_cost",
        "quintessence_max",
        "description",
        "gnosis",
        "spirit",
    ]
    template_name = "items/werewolf/fetish/form.html"
