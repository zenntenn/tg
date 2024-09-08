from django.urls import path
from locations import views

app_name = "locations:detail"
urls = [
    path(
        "reality_zone/<pk>/",
        views.mage.RealityZoneDetailView.as_view(),
        name="reality_zone",
    ),
]
