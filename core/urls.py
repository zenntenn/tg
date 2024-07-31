from django.urls import path

from core import views

# Create your URLs here
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
]
