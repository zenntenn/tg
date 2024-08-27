from core.models import NewsItem
from django.views.generic import ListView


class HomeListView(ListView):
    model = NewsItem
    template_name = "home.html"
    context_object_name = "news"
    ordering = ["-date"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context
