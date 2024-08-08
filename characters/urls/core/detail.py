from characters import views
from django.urls import path

# Create your URLs here
app_name = "characters:detail"
urls = [
    path("groups/<pk>/", views.core.GenericGroupDetailView.as_view(), name="group"),
    path(
        "archetypes/<pk>/",
        views.core.ArchetypeDetailView.as_view(),
        name="archetype",
    ),
    path(
        "meritflaws/<pk>/",
        views.core.MeritFlawDetailView.as_view(),
        name="meritflaw",
    ),
    path(
        "specialties/<pk>/",
        views.core.SpecialtyDetailView.as_view(),
        name="specialty",
    ),
    path(
        "derangement/<pk>/",
        views.core.DerangementDetailView.as_view(),
        name="derangement",
    ),
    path("<pk>/", views.core.GenericCharacterDetailView.as_view(), name="character"),
]
