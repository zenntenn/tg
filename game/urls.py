from django.urls import path
from game import views

# Create your URLs here
app_name = "game"
urlpatterns = [
    path("chronicle/<pk>", views.ChronicleDetailView.as_view(), name="chronicle"),
    path("story/<pk>", views.StoryDetailView.as_view(), name="story"),
]
