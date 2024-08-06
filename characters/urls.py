from characters import views
from django.urls import path

# Create your URLs here
app_name = "characters"
urlpatterns = [
    path("<pk>/", views.GenericCharacterDetailView.as_view(), name="character"),
    path(
        "archetypes/<pk>/",
        views.ArchetypeDetailView.as_view(),
        name="archetype",
    ),
    path(
        "meritflaws/<pk>/",
        views.MeritFlawDetailView.as_view(),
        name="meritflaw",
    ),
    path(
        "derangement/<pk>/",
        views.DerangementDetailView.as_view(),
        name="derangement",
    ),
    path("groups/<pk>/", views.GenericGroupDetailView.as_view(), name="group"),
    path(
        "specialties/<pk>/",
        views.SpecialtyDetailView.as_view(),
        name="specialty",
    ),
]
