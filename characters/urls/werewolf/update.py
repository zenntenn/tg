from characters import views
from django.urls import path

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
    path(
        "wtahuman/<pk>/",
        views.werewolf.WtAHumanUpdateView.as_view(),
        name="wta_human",
    ),
    path(
        "rites/<pk>/",
        views.werewolf.RiteUpdateView.as_view(),
        name="rite",
    ),
]
