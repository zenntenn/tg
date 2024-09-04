from characters import views
from django.urls import path

urls = [
    path(
        "charms/<pk>/",
        views.werewolf.SpiritCharmDetailView.as_view(),
        name="charm",
    ),
    path(
        "spirits/<pk>/",
        views.werewolf.SpiritDetailView.as_view(),
        name="spirit",
    ),
    path(
        "totems/<pk>/",
        views.werewolf.TotemDetailView.as_view(),
        name="totem",
    ),
    path("rites/<pk>/", views.werewolf.RiteDetailView.as_view(), name="rite"),
]
