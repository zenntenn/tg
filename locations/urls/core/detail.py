from django.urls import path
from locations import views

# Create your URLs here
app_name = "locations:detail"
urls = [
    path("<pk>/", views.core.GenericLocationDetailView.as_view(), name="location"),
]
