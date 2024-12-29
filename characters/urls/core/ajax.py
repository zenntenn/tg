from characters import views
from django.urls import path

app_name = "core:create"
urls = [
    path("load_examples/", views.core.load_examples, name="load_examples"),
    path("load_values/", views.core.load_values, name="load_values"),
]
