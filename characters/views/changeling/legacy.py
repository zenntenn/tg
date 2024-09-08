from characters.models.changeling.legacy import Legacy
from django.views.generic import CreateView, DetailView, ListView, UpdateView


class LegacyDetailView(DetailView):
    model = Legacy
    template_name = "characters/changeling/legacy/detail.html"


class LegacyCreateView(CreateView):
    model = Legacy
    fields = ["name", "description", "court"]
    template_name = "characters/changeling/legacy/form.html"


class LegacyUpdateView(UpdateView):
    model = Legacy
    fields = ["name", "description", "court"]
    template_name = "characters/changeling/legacy/form.html"


class LegacyListView(ListView):
    model = Legacy
    ordering = ["name"]
    template_name = "characters/changeling/legacy/list.html"
