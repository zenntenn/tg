from accounts import views
from django.urls import path

urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("profile/<pk>/", views.ProfileView.as_view(), name="profile"),
]
