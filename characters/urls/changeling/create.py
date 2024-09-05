from characters import views
from django.urls import path

urls = [
    path(
        "changeling/",
        views.changeling.ChangelingCreateView.as_view(),
        name="changeling",
    ),
    path(
        "motley/",
        views.changeling.MotleyCreateView.as_view(),
        name="motley",
    ),
    path(
        "kith/",
        views.changeling.KithCreateView.as_view(),
        name="kith",
    ),
    path(
        "house/",
        views.changeling.HouseCreateView.as_view(),
        name="house",
    ),
    path(
        "legacy/",
        views.changeling.LegacyCreateView.as_view(),
        name="legacy",
    ),
    path(
        "ctdhuman/",
        views.changeling.CtDHumanCreateView.as_view(),
        name="ctd_human",
    ),
]
