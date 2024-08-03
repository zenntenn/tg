from django.urls import path
from locations import views

# Create your URLs here
app_name = "locations"
urlpatterns = [
    path("<pk>/", views.GenericLocationDetailView.as_view(), name="location"),
]
