from django.views.generic import CreateView, DetailView, ListView, UpdateView
from items.models.core import Medium


class MediumDetailView(DetailView):
    model = Medium
    template_name = "items/core/medium/detail.html"


class MediumCreateView(CreateView):
    model = Medium
    fields = "__all__"
    template_name = "items/core/medium/form.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["name"].widget.attrs.update(
            {"placeholder": "Enter name here", "rows": 1}
        )
        return form


class MediumUpdateView(UpdateView):
    model = Medium
    fields = "__all__"
    template_name = "items/core/medium/form.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["name"].widget.attrs.update(
            {"placeholder": "Enter name here", "rows": 1}
        )
        return form


class MediumListView(ListView):
    model = Medium
    ordering = ["name"]
    template_name = "items/core/medium/list.html"
