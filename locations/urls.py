from django.urls import path
from locations import views

# Create your URLs here
app_name = "locations"
urlpatterns = [
    path("<pk>/", views.GenericLocationDetailView.as_view(), name="location"),
    path(
        "location/create/",
        views.LocationCreateView.as_view(),
        name="create_location",
    ),
    path(
        "location/update/<pk>/",
        views.LocationUpdateView.as_view(),
        name="update_location",
    ),
    path(
        "city/create/",
        views.CityCreateView.as_view(),
        name="create_city",
    ),
    path(
        "city/update/<pk>/",
        views.CityUpdateView.as_view(),
        name="update_city",
    ),
]
