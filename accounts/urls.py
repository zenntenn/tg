from accounts import views
from core import views as core_views
from django.urls import path

urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("profile/<pk>/", views.ProfileView.as_view(), name="profile"),
    path("", core_views.HomeListView.as_view(), name="user"),
]
