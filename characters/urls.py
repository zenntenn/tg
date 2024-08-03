from django.urls import path
from characters import views

# Create your URLs here
app_name = "characters"
urlpatterns = [
    path(
        "<pk>/", views.GenericCharacterDetailView.as_view(), name="character"
    ),
]
