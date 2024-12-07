from django.urls import path
from game import views

app_name = "game"
urlpatterns = [
    path("chronicle/<pk>", views.ChronicleDetailView.as_view(), name="chronicle"),
    path(
        "chronicle/<pk>/scenes/",
        views.ChronicleScenesDetailView.as_view(),
        name="chronicle_scenes",
    ),
    path("scene/<pk>", views.SceneDetailView.as_view(), name="scene"),
    path("commands/", views.CommandsView.as_view(), name="commands"),
]
