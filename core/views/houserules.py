from typing import Any

from core.models import HouseRule
from core.utils import get_gameline_name
from django.views.generic import ListView
from game.models import Chronicle


class HouseRulesIndexView(ListView):
    model = HouseRule
    template_name = "core/houserules/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["chronicles"] = list(Chronicle.objects.all()) + [None]
        context["gameline_code"] = self.kwargs["gameline"]
        context["gameline"] = get_gameline_name(self.kwargs["gameline"])
        context["gameline_short"] = self.kwargs["gameline"]
        return context
