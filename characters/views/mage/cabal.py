from characters.forms.mage.cabal import CabalForm
from characters.models.core.human import Human
from characters.models.mage.cabal import Cabal
from django import forms
from django.http import JsonResponse
from django.views.generic import CreateView, DetailView, UpdateView


class CabalDetailView(DetailView):
    model = Cabal
    template_name = "characters/mage/cabal/detail.html"


class CabalCreateView(CreateView):
    model = Cabal
    form_class = CabalForm
    template_name = "characters/mage/cabal/form.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        leader = form.cleaned_data.get("leader")
        if leader:
            self.object.members.add(leader)
        return response

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class CabalUpdateView(UpdateView):
    model = Cabal
    form_class = CabalForm
    template_name = "characters/mage/cabal/form.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        # Add a new field to add a new character (a Human object)
        options = Human.objects.filter(chronicle=self.object.chronicle)
        options = options.filter(group__isnull=True)

        form.fields["new_character"] = forms.ModelChoiceField(
            queryset=options,
            required=False,
            label="Add New Member",
            help_text="Select a character to add to this cabal.",
        )
        return form

    def form_valid(self, form):
        # Handle adding the new character to the cabal
        response = super().form_valid(form)
        new_char = form.cleaned_data.get("new_character")
        if new_char:
            self.object.members.add(new_char)
        return response

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs
