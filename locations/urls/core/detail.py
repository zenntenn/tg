from django.urls import path
from locations import views

app_name = "locations:detail"
urls = [
    path("<pk>/", views.core.GenericLocationDetailView.as_view(), name="location"),
]
