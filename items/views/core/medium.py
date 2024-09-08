from django.views.generic import CreateView, DetailView, ListView, UpdateView
from items.models.core import Medium


class MediumDetailView(DetailView):
    model = Medium
    template_name = "items/core/medium/detail.html"


class MediumCreateView(CreateView):
    model = Medium
    fields = "__all__"
    template_name = "items/core/medium/form.html"


class MediumUpdateView(UpdateView):
    model = Medium
    fields = "__all__"
    template_name = "items/core/medium/form.html"


class MediumListView(ListView):
    model = Medium
    ordering = ["name"]
    template_name = "items/core/medium/list.html"
