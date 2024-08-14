from django.views.generic import CreateView, DetailView, UpdateView
from locations.models.mage.library import Library


class LibraryDetailView(DetailView):
    model = Library
    template_name = "locations/mage/library/detail.html"


class LibraryCreateView(CreateView):
    model = Library
    fields = ["name", "description", "parent", "rank", "faction", "books"]
    template_name = "locations/mage/library/form.html"


class LibraryUpdateView(UpdateView):
    model = Library
    fields = ["name", "description", "parent", "rank", "faction", "books"]
    template_name = "locations/mage/library/form.html"
