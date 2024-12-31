from characters.views.core.human import load_examples, load_values
from django.urls import path

app_name = "core:create"
urls = [
    path("load_examples/", load_examples, name="load_examples"),
    path("load_values/", load_values, name="load_values"),
]
