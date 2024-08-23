from characters import views
from django.urls import path

# Create your URLs here
urls = [
    path(
        "vtmhuman/",
        views.vampire.VtMHumanCreateView.as_view(),
        name="vtmhuman",
    ),
]
