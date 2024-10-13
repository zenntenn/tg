from characters.models.mage.companion import Advantage
from django.views.generic import DetailView


class AdvantageDetailView(DetailView):
    model = Advantage
    template_name = "characters/mage/advantage/detail.html"
