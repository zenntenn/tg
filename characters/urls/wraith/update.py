from characters import views
from django.urls import path

# Create your URLs here
urls = [
    path(
        "wtohuman/<pk>/",
        views.wraith.WtOHumanUpdateView.as_view(),
        name="wtohuman",
    ),
]
