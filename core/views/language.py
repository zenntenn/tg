from core.models import Language
from django.views.generic import CreateView, DetailView, UpdateView


class LanguageDetailView(DetailView):
    model = Language
    template_name = "core/language/detail.html"


class LanguageCreateView(CreateView):
    model = Language
    fields = "__all__"
    template_name = "core/language/form.html"


class LanguageUpdateView(UpdateView):
    model = Language
    fields = "__all__"
    template_name = "core/language/form.html"