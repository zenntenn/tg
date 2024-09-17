from characters.models.werewolf.spirit_character import SpiritCharacter
from core.views.approved_user_mixin import SpecialUserMixin
from django.views.generic import CreateView, DetailView, UpdateView


class SpiritDetailView(SpecialUserMixin, DetailView):
    model = SpiritCharacter
    template_name = "characters/werewolf/spirit/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context


class SpiritCreateView(CreateView):
    model = SpiritCharacter
    fields = ["name", "description", "willpower", "rage", "gnosis", "essence", "owner"]
    template_name = "characters/werewolf/spirit/form.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["name"].widget.attrs.update({"placeholder": "Enter name here"})
        form.fields["description"].widget.attrs.update(
            {"placeholder": "Enter description here"}
        )
        return form


class SpiritUpdateView(SpecialUserMixin, UpdateView):
    model = SpiritCharacter
    fields = ["name", "description", "willpower", "rage", "gnosis", "essence", "owner"]
    template_name = "characters/werewolf/spirit/form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["name"].widget.attrs.update({"placeholder": "Enter name here"})
        form.fields["description"].widget.attrs.update(
            {"placeholder": "Enter description here"}
        )
        return form
