from django.urls import path
from items import views

# Create your URLs here
urls = [
    path(
        "wonder/<pk>/",
        views.mage.WonderUpdateView.as_view(),
        name="wonder",
    ),
]
