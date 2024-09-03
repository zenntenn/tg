from characters import views
from django.urls import path

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
    path(
        "load_examples/",
        views.mage.mage.LoadExamplesView.as_view(),
        name="load_examples",
    ),
]
