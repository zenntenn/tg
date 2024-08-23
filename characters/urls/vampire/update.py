from characters import views
from django.urls import path

# Create your URLs here
urls = [
    path(
        "vtmhuman/<pk>/",
        views.vampire.VtMHumanUpdateView.as_view(),
        name="vtmhuman",
    ),
]
