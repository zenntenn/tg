from characters.models.mage.sorcerer import LinearMagicPath, LinearMagicRitual
from django.views.generic import DetailView


class PathDetailView(DetailView):
    model = LinearMagicPath
    template_name = "characters/mage/linear_magic_path/detail.html"


class RitualDetailView(DetailView):
    model = LinearMagicRitual
    template_name = "characters/mage/linear_magic_ritual/detail.html"
