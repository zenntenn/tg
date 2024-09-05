from characters import views
from django.urls import path

urls = [
    path(
        "kith/<pk>/",
        views.changeling.KithDetailView.as_view(),
        name="kith",
    ),
    path(
        "house/<pk>/",
        views.changeling.HouseDetailView.as_view(),
        name="house",
    ),
    path(
        "legacy/<pk>/",
        views.changeling.LegacyDetailView.as_view(),
        name="legacy",
    ),
]
