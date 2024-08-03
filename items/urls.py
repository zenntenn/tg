from django.urls import path
from items import views

# Create your URLs here
app_name = "items"
urlpatterns = [
    path("<pk>/", views.GenericItemDetailView.as_view(), name="item"),
    path("medium/<pk>/", views.MediumDetailView.as_view(), name="medium"),
]
