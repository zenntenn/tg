from characters.models.core import Group
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView


# Create your views here.
class GroupDetailView(DetailView):
    model = Group
    template_name = "characters/core/group/detail.html"


class GroupCreateView(CreateView):
    model = Group
    fields = ["name", "description", "members", "leader"]
    template_name = "characters/core/group/form.html"


class GroupUpdateView(UpdateView):
    model = Group
    fields = ["name", "description", "members", "leader"]
    template_name = "characters/core/group/form.html"
