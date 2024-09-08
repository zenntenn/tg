from characters.models.changeling.house import House
from django.views.generic import CreateView, DetailView, ListView, UpdateView


class HouseDetailView(DetailView):
    model = House
    template_name = "characters/changeling/house/detail.html"


class HouseCreateView(CreateView):
    model = House
    fields = ["name", "description", "court", "boon", "flaw"]
    template_name = "characters/changeling/house/form.html"


class HouseUpdateView(UpdateView):
    model = House
    fields = ["name", "description", "court", "boon", "flaw"]
    template_name = "characters/changeling/house/form.html"


class HouseListView(ListView):
    model = House
    ordering = ["name"]
    template_name = "characters/changeling/house/list.html"
