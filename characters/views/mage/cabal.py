from characters.models.mage.cabal import Cabal
from django.views.generic import CreateView, DetailView, UpdateView


class CabalDetailView(DetailView):
    model = Cabal
    template_name = "characters/mage/cabal/detail.html"


class CabalCreateView(CreateView):
    model = Cabal
    fields = ["name", "description", "members", "leader", "chronicle", "public_info"]
    template_name = "characters/mage/cabal/form.html"


class CabalUpdateView(UpdateView):
    model = Cabal
    fields = ["name", "description", "members", "leader", "chronicle", "public_info"]
    template_name = "characters/mage/cabal/form.html"
