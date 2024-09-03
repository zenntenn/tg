from characters import views
from django.urls import path

app_name = "characters:update"
urls = [
    path(
        "character/<pk>/",
        views.core.CharacterUpdateView.as_view(),
        name="character",
    ),
    path(
        "group/<pk>/",
        views.core.GroupUpdateView.as_view(),
        name="group",
    ),
    path(
        "human/full/<pk>/",
        views.core.HumanUpdateView.as_view(),
        name="human_full",
    ),
    path(
        "human/<pk>/",
        views.core.HumanCharacterCreationView.as_view(),
        name="human",
    ),
    path(
        "archetypes/<pk>/",
        views.core.ArchetypeUpdateView.as_view(),
        name="archetype",
    ),
    path(
        "meritflaws/<pk>/",
        views.core.MeritFlawUpdateView.as_view(),
        name="meritflaw",
    ),
    path(
        "specialties/<pk>/",
        views.core.SpecialtyUpdateView.as_view(),
        name="specialty",
    ),
    path(
        "derangement/<pk>/",
        views.core.DerangementUpdateView.as_view(),
        name="derangement",
    ),
]
