from characters import views
from django.urls import path

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
    path(
        "wtahuman/",
        views.werewolf.WtAHumanCreateView.as_view(),
        name="wta_human",
    ),
]
