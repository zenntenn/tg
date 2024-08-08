from django.urls import path
from locations import views

# Create your URLs here
app_name = "locations:create"
urls = [
    path(
        "location/",
        views.core.LocationCreateView.as_view(),
        name="location",
    ),
    path(
        "city/",
        views.core.CityCreateView.as_view(),
        name="city",
    ),
]
