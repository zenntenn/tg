from django.views.generic import CreateView, DetailView, UpdateView
from locations.models.mage.sanctum import Sanctum


class SanctumDetailView(DetailView):
    model = Sanctum
    template_name = "locations/mage/sanctum/detail.html"


class SanctumCreateView(CreateView):
    model = Sanctum
    fields = ["name", "description", "parent"]
    template_name = "locations/mage/sanctum/form.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["name"].widget.attrs.update({"placeholder": "Enter name here"})
        form.fields["description"].widget.attrs.update(
            {"placeholder": "Enter description here"}
        )
        form.fields["parent"].empty_label = "Parent Location"
        return form


class SanctumUpdateView(UpdateView):
    model = Sanctum
    fields = ["name", "description", "parent"]
    template_name = "locations/mage/sanctum/form.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["name"].widget.attrs.update({"placeholder": "Enter name here"})
        form.fields["description"].widget.attrs.update(
            {"placeholder": "Enter description here"}
        )
        form.fields["parent"].empty_label = "Parent Location"
        return form
