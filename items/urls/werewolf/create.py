from django.urls import path
from items import views

# Create your URLs here
urls = [
    path(
        "fetish/",
        views.werewolf.FetishCreateView.as_view(),
        name="fetish",
    ),
]
