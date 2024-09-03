from accounts import views
from django.urls import path

urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("", views.ProfileView.as_view(), name="user"),
]
