from characters.models.werewolf.pack import Pack
from django.views.generic import CreateView, DetailView, UpdateView


class PackDetailView(DetailView):
    model = Pack
    template_name = "characters/werewolf/pack/detail.html"


class PackCreateView(CreateView):
    model = Pack
    fields = ["name", "description", "members", "leader", "totem"]
    template_name = "characters/werewolf/pack/form.html"


class PackUpdateView(UpdateView):
    model = Pack
    fields = ["name", "description", "members", "leader", "totem"]
    template_name = "characters/werewolf/pack/form.html"
