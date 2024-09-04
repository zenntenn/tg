from django.urls import path
from locations import views

app_name = "locations:detail"
urls = [
    path(
        "realityzone/<pk>/",
        views.mage.RealityZoneDetailView.as_view(),
        name="realityzone",
    ),
]
