from characters import views as char_views
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
    path(
        "chronicle/<pk>/retired/",
        char_views.core.RetiredCharacterIndex.as_view(),
        name="retired",
    ),
    path(
        "chronicle/<pk>/deceased/",
        char_views.core.DeceasedCharacterIndex.as_view(),
        name="deceased",
    ),
    path(
        "chronicle/<pk>/npc/", char_views.core.NPCCharacterIndex.as_view(), name="npc"
    ),
    path("scene/<pk>", views.SceneDetailView.as_view(), name="scene"),
    path("commands/", views.CommandsView.as_view(), name="commands"),
    path("journal/<pk>", views.JournalDetailView.as_view(), name="journal"),
]
