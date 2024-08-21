from characters import views
from django.urls import path

# Create your URLs here
app_name = "mage:create"
urls = [
    path(
        "load_faction_details/",
        views.mage.load_factions,
        name="load_factions",
    ),
    path(
        "load_subfaction_details/",
        views.mage.load_subfactions,
        name="load_subfactions",
    ),
    path(
        "load_mf_ratings/",
        views.mage.load_mf_ratings,
        name="load_mf_ratings",
    ),
]
