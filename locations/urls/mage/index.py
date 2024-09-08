from django.urls import path
from locations import views

urls = [
    path(
        "realityzone/",
        views.mage.RealityZoneListView.as_view(),
        name="realityzone",
    ),
]
