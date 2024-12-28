from characters.models.werewolf.gift import Gift
from django.views.generic import CreateView, DetailView, ListView, UpdateView


class GiftDetailView(DetailView):
    model = Gift
    template_name = "characters/werewolf/gift/detail.html"


class GiftCreateView(CreateView):
    model = Gift
    fields = ["name", "rank", "description"]
    template_name = "characters/werewolf/gift/form.html"


class GiftUpdateView(UpdateView):
    model = Gift
    fields = ["name", "rank", "description"]
    template_name = "characters/werewolf/gift/form.html"


class GiftListView(ListView):
    model = Gift
    ordering = ["name"]
    template_name = "characters/werewolf/gift/list.html"
