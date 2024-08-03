from characters import views
from django.urls import path

# Create your URLs here
app_name = "characters"
urlpatterns = [
    path("<pk>/", views.GenericCharacterDetailView.as_view(), name="character"),
]
