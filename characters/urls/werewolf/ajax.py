from characters import views
from django.urls import path

app_name = "werewolf:ajax"
urls = [
    path(
        "load_wtahuman_examples/",
        views.werewolf.wtahuman.WtAHumanFreebieFormPopulationView.as_view(),
        name="load_wtahuman_examples",
    ),
]
