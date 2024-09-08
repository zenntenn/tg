from characters import views
from django.urls import path

app_name = "characters:detail"
urls = [
    path(
        "archetypes/",
        views.core.ArchetypeListView.as_view(),
        name="archetype",
    ),
    path(
        "meritflaws/",
        views.core.MeritFlawListView.as_view(),
        name="meritflaw",
    ),
    path(
        "specialties/",
        views.core.SpecialtyListView.as_view(),
        name="specialty",
    ),
    path(
        "derangement/",
        views.core.DerangementListView.as_view(),
        name="derangement",
    ),
]
