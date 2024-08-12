from django.views.generic import CreateView, DetailView, UpdateView
from items.models.core import Material

# Create your views here.


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
