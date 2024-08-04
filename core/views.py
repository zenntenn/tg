from core.models import Book, Language
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView


# Create your views here.
class HomeView(View):
    """This View controls the main landing page for the site"""

    def get(self, request):
        return render(request, "core/index.html", context={})


class BookDetailView(DetailView):
    model = Book
    template_name = "core/book/detail.html"


class LanguageDetailView(DetailView):
    model = Language
    template_name = "core/language/detail.html"
