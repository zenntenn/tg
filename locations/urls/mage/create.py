from django.urls import path
from locations import views

app_name = "mage:create"
urls = [
    path(
        "node/",
        views.mage.NodeCreateView.as_view(),
        name="node",
    ),
    path(
        "sector/",
        views.mage.SectorCreateView.as_view(),
        name="sector",
    ),
    path(
        "realm/create/",
        views.mage.RealmCreateView.as_view(),
        name="realm",
    ),
    path(
        "library/",
        views.mage.LibraryCreateView.as_view(),
        name="library",
    ),
    path(
        "chantry/",
        views.mage.ChantryCreateView.as_view(),
        name="chantry",
    ),
    path(
        "realityzone/",
        views.mage.RealityZoneCreateView.as_view(),
        name="realityzone",
    ),
]
