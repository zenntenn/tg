from characters.models.werewolf.gift import Gift
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView


class GiftDetailView(DetailView):
    model = Gift
    template_name = "characters/werewolf/gift/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allowed"] = []
        for key, value in self.object.allowed.items():
            value = sorted(value)
            context["allowed"].append(
                f"{key.title()}: {', '.join([x.title() for x in value])}"
            )
        return context


class GiftCreateView(CreateView):
    model = Gift
    fields = ["name", "rank", "description"]
    template_name = "characters/werewolf/gift/form.html"


class GiftUpdateView(UpdateView):
    model = Gift
    fields = ["name", "rank", "description"]
    template_name = "characters/werewolf/gift/form.html"
