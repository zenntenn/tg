from django.views.generic import CreateView, DetailView, ListView, UpdateView
from items.models.core import Material


class MaterialDetailView(DetailView):
    model = Material
    template_name = "items/core/material/detail.html"


class MaterialCreateView(CreateView):
    model = Material
    fields = "__all__"
    template_name = "items/core/material/form.html"


class MaterialUpdateView(UpdateView):
    model = Material
    fields = "__all__"
    template_name = "items/core/material/form.html"


class MaterialListView(ListView):
    model = Material
    ordering = ["name"]
    template_name = "items/core/material/list.html"
