from typing import Any

from core.models import Book, Language, NewsItem
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView


# Create your views here.
class HomeView(View):
    """This View controls the main landing page for the site"""

    def get(self, request):
        context = {"user": request.user}
        context["news"] = NewsItem.objects.order_by("-date")
        return render(request, "core/index.html", context=context)


class BookDetailView(DetailView):
    model = Book
    template_name = "core/book/detail.html"


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
