from django.urls import path
from items import views

# Create your URLs here
app_name = "items:detail"
urls = [
    path("material/<pk>/", views.core.MaterialDetailView.as_view(), name="material"),
    path("medium/<pk>/", views.core.MediumDetailView.as_view(), name="medium"),
    path("<pk>/", views.core.GenericItemDetailView.as_view(), name="item"),
]
