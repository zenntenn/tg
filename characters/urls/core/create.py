from characters import views
from django.urls import path

# Create your URLs here
app_name = "characters:create"
urls = [
    path(
        "character/",
        views.core.CharacterCreateView.as_view(),
        name="character",
    ),
    path(
        "group/",
        views.core.GroupCreateView.as_view(),
        name="group",
    ),
    path(
        "human/",
        views.core.HumanBasicsView.as_view(),
        name="human",
    ),
    path(
        "human/full/",
        views.core.HumanCreateView.as_view(),
        name="human_full",
    ),
    path(
        "archetypes/",
        views.core.ArchetypeCreateView.as_view(),
        name="archetype",
    ),
    path(
        "meritflaws/",
        views.core.MeritFlawCreateView.as_view(),
        name="meritflaw",
    ),
    path(
        "specialties/",
        views.core.SpecialtyCreateView.as_view(),
        name="specialty",
    ),
    path(
        "derangement/",
        views.core.DerangementCreateView.as_view(),
        name="derangement",
    ),
]
