from characters import views
from django.urls import path

# Create your URLs here
app_name = "characters"
urlpatterns = [
    path(
        "character/create/",
        views.CharacterCreateView.as_view(),
        name="create_character",
    ),
    path(
        "character/update/<pk>/",
        views.CharacterUpdateView.as_view(),
        name="update_character",
    ),
    path(
        "group/create/",
        views.GroupCreateView.as_view(),
        name="create_group",
    ),
    path(
        "group/update/<pk>/",
        views.GroupUpdateView.as_view(),
        name="update_group",
    ),
    path("groups/<pk>/", views.GenericGroupDetailView.as_view(), name="group"),
    path(
        "human/create/",
        views.HumanCreateView.as_view(),
        name="create_human",
    ),
    path(
        "human/update/<pk>/",
        views.HumanUpdateView.as_view(),
        name="update_human",
    ),
    path(
        "archetypes/create/",
        views.ArchetypeCreateView.as_view(),
        name="create_archetype",
    ),
    path(
        "archetypes/update/<pk>/",
        views.ArchetypeUpdateView.as_view(),
        name="update_archetype",
    ),
    path(
        "archetypes/<pk>/",
        views.ArchetypeDetailView.as_view(),
        name="archetype",
    ),
    path(
        "meritflaws/create/",
        views.MeritFlawCreateView.as_view(),
        name="create_meritflaw",
    ),
    path(
        "meritflaws/update/<pk>/",
        views.MeritFlawUpdateView.as_view(),
        name="update_meritflaw",
    ),
    path(
        "meritflaws/<pk>/",
        views.MeritFlawDetailView.as_view(),
        name="meritflaw",
    ),
    path(
        "specialties/create/",
        views.SpecialtyCreateView.as_view(),
        name="create_specialty",
    ),
    path(
        "specialties/update/<pk>/",
        views.SpecialtyUpdateView.as_view(),
        name="update_specialty",
    ),
    path(
        "specialties/<pk>/",
        views.SpecialtyDetailView.as_view(),
        name="specialty",
    ),
    path(
        "derangement/create/",
        views.DerangementCreateView.as_view(),
        name="create_derangement",
    ),
    path(
        "derangement/update/<pk>/",
        views.DerangementUpdateView.as_view(),
        name="update_derangement",
    ),
    path(
        "derangement/<pk>/",
        views.DerangementDetailView.as_view(),
        name="derangement",
    ),
    path("<pk>/", views.GenericCharacterDetailView.as_view(), name="character"),
]
