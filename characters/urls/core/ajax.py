from characters import views
from django.urls import path

# Create your URLs here
app_name = "core:create"
urls = [
    path("load_examples/", views.core.human.load_examples, name="load_examples"),
    path("load_values/", views.core.human.load_values, name="load_values"),
]
