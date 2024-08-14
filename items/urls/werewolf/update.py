from django.urls import path
from items import views

# Create your URLs here
urls = [
    path(
        "fetish/<pk>/",
        views.werewolf.FetishUpdateView.as_view(),
        name="fetish",
    ),
]
