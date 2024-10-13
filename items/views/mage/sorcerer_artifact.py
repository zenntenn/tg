from django.views.generic import DetailView
from items.models.mage.sorcerer_artifact import SorcererArtifact


class SorcererArtifactDetailView(DetailView):
    model = SorcererArtifact
    template_name = "items/mage/sorcerer_artifact/detail.html"
