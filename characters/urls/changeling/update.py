from characters import views
from django.urls import path

urls = [
    path(
        "changeling/<pk>/",
        views.changeling.ChangelingUpdateView.as_view(),
        name="changeling",
    ),
    path(
        "motley/<pk>/",
        views.changeling.MotleyUpdateView.as_view(),
        name="motley",
    ),
    path(
        "kith/<pk>/",
        views.changeling.KithUpdateView.as_view(),
        name="kith",
    ),
    path(
        "house/<pk>/",
        views.changeling.HouseUpdateView.as_view(),
        name="house",
    ),
    path(
        "legacy/<pk>/",
        views.changeling.LegacyUpdateView.as_view(),
        name="legacy",
    ),
    path(
        "ctdhuman/<pk>/",
        views.changeling.CtDHumanUpdateView.as_view(),
        name="ctd_human",
    ),
]
