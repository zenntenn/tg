from characters import views
from django.urls import path

app_name = "mage:ajax"
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
    path(
        "load_companion_examples/",
        views.mage.companion.LoadExamplesView.as_view(),
        name="load_companion_examples",
    ),
    path(
        "load_advantage_values/",
        views.mage.companion.load_companion_values,
        name="load_advantage_values",
    ),
    path(
        "get_abilities/",
        views.mage.mage.get_abilities,
        name="get_abilities",
    ),
]
