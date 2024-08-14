from characters import views
from django.urls import path

# Create your URLs here
urls = [
    path(
        "charms/<pk>/",
        views.werewolf.SpiritCharmUpdateView.as_view(),
        name="charm",
    ),
    path(
        "spirits/<pk>/",
        views.werewolf.SpiritUpdateView.as_view(),
        name="spirit",
    ),
    path(
        "totems/<pk>/",
        views.werewolf.TotemUpdateView.as_view(),
        name="totem",
    ),
]
