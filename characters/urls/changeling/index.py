from characters import views
from django.urls import path

urls = [
    path(
        "kith/",
        views.changeling.KithListView.as_view(),
        name="kith",
    ),
    path(
        "house/",
        views.changeling.HouseListView.as_view(),
        name="house",
    ),
    path(
        "legacy/",
        views.changeling.LegacyListView.as_view(),
        name="legacy",
    ),
]
