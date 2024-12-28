from typing import Any

from characters.models.core import MeritFlaw
from django.views.generic import CreateView, DetailView, ListView, UpdateView


class MeritFlawDetailView(DetailView):
    model = MeritFlaw
    template_name = "characters/core/meritflaw/detail.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        mf_ratings = list(self.object.ratings.values_list("value", flat=True))
        mf_ratings.sort()
        context["ratings"] = ", ".join([str(x) for x in mf_ratings])
        return context


class MeritFlawCreateView(CreateView):
    model = MeritFlaw
    fields = ["name", "description", "ratings", "allowed_types"]
    template_name = "characters/core/meritflaw/form.html"


class MeritFlawUpdateView(UpdateView):
    model = MeritFlaw
    fields = ["name", "description", "ratings", "allowed_types"]
    template_name = "characters/core/meritflaw/form.html"


class MeritFlawListView(ListView):
    model = MeritFlaw
    ordering = ["name"]
    template_name = "characters/core/meritflaw/list.html"
