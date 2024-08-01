from django.urls import path

from accounts import views

# Create your URLs here
urlpatterns = [
    path("", views.ProfileView.as_view(), name="user"),
]
