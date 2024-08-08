from django.urls import path
from locations import views

# Create your URLs here
app_name = "locations:update"
urls = [
    path(
        "location/<pk>/",
        views.core.LocationUpdateView.as_view(),
        name="location",
    ),
    path(
        "city/<pk>/",
        views.core.CityUpdateView.as_view(),
        name="city",
    ),
]
