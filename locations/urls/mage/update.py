from django.urls import path
from locations import views

app_name = "locations:update"
urls = [
    path(
        "node/<pk>/",
        views.mage.NodeUpdateView.as_view(),
        name="node",
    ),
    path(
        "sector/<pk>/",
        views.mage.SectorUpdateView.as_view(),
        name="sector",
    ),
    path(
        "library/<pk>/",
        views.mage.LibraryUpdateView.as_view(),
        name="library",
    ),
    path(
        "realm/<pk>/",
        views.mage.RealmUpdateView.as_view(),
        name="realm",
    ),
    path(
        "chantry/<pk>/",
        views.mage.ChantryUpdateView.as_view(),
        name="chantry",
    ),
    path(
        "realityzone/<pk>/",
        views.mage.RealityZoneUpdateView.as_view(),
        name="realityzone",
    ),
]
