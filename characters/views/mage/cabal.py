from django.views.generic import CreateView, DetailView, UpdateView

from characters.models.mage.cabal import Cabal

class CabalDetailView(DetailView):
    model = Cabal
    template_name = "characters/mage/cabal/detail.html"


class CabalCreateView(CreateView):
    model = Cabal
    fields = "__all__"
    template_name = "characters/mage/cabal/form.html"


class CabalUpdateView(UpdateView):
    model = Cabal
    fields = "__all__"
    template_name = "characters/mage/cabal/form.html"
