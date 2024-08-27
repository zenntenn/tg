from core.models import NewsItem
from django.views.generic import CreateView, DetailView, UpdateView


class NewsItemDetailView(DetailView):
    model = NewsItem
    template_name = "core/newsitem/detail.html"


class NewsItemCreateView(CreateView):
    model = NewsItem
    fields = "__all__"
    template_name = "core/newsitem/form.html"


class NewsItemUpdateView(UpdateView):
    model = NewsItem
    fields = "__all__"
    template_name = "core/newsitem/form.html"
