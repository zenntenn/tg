from core.models import Book
from django.views.generic import DetailView


class BookDetailView(DetailView):
    model = Book
    template_name = "core/book/detail.html"
