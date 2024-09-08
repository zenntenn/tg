from django.urls import path
from locations import views

urls = [
    path(
        "reality_zone/",
        views.mage.RealityZoneListView.as_view(),
        name="reality_zone",
    ),
]
