from django.views.generic import CreateView, DetailView, UpdateView
from locations.models.mage.library import Library


class LibraryDetailView(DetailView):
    model = Library
    template_name = "locations/mage/library/detail.html"


class LibraryCreateView(CreateView):
    model = Library
    fields = ["name", "description", "parent", "rank", "faction", "books"]
    template_name = "locations/mage/library/form.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["name"].widget.attrs.update({"placeholder": "Enter name here"})
        form.fields["description"].widget.attrs.update(
            {"placeholder": "Enter description here"}
        )
        return form


class LibraryUpdateView(UpdateView):
    model = Library
    fields = ["name", "description", "parent", "rank", "faction", "books"]
    template_name = "locations/mage/library/form.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["name"].widget.attrs.update({"placeholder": "Enter name here"})
        form.fields["description"].widget.attrs.update(
            {"placeholder": "Enter description here"}
        )
        return form
