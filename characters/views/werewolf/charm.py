from characters.models.werewolf.charm import SpiritCharm
from django.views.generic import CreateView, DetailView, ListView, UpdateView


class SpiritCharmDetailView(DetailView):
    model = SpiritCharm
    template_name = "characters/werewolf/charm/detail.html"


class SpiritCharmCreateView(CreateView):
    model = SpiritCharm
    fields = ["name", "description"]
    template_name = "characters/werewolf/charm/form.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["name"].widget.attrs.update({"placeholder": "Enter name here"})
        form.fields["description"].widget.attrs.update(
            {"placeholder": "Enter description here"}
        )
        return form


class SpiritCharmUpdateView(UpdateView):
    model = SpiritCharm
    fields = ["name", "description"]
    template_name = "characters/werewolf/charm/form.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["name"].widget.attrs.update({"placeholder": "Enter name here"})
        form.fields["description"].widget.attrs.update(
            {"placeholder": "Enter description here"}
        )
        return form


class SpiritCharmListView(ListView):
    model = SpiritCharm
    ordering = ["name"]
    template_name = "characters/werewolf/charm/list.html"
