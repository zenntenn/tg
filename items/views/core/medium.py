from django.views.generic import CreateView, DetailView, UpdateView
from items.models.core import Medium


# Create your views here.
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
