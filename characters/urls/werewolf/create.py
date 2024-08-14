from characters import views
from django.urls import path

# Create your URLs here
urls = [
    path(
        "charms/",
        views.werewolf.SpiritCharmCreateView.as_view(),
        name="charm",
    ),
    path(
        "spirits/",
        views.werewolf.SpiritCreateView.as_view(),
        name="spirit",
    ),
    path(
        "totems/",
        views.werewolf.TotemCreateView.as_view(),
        name="totem",
    ),
]
