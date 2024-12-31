from characters import views
from django.urls import path

app_name = "wraith:ajax"
urls = [
    path(
        "load_wtohuman_examples/",
        views.wraith.wtohuman.WtOHumanFreebieFormPopulationView.as_view(),
        name="load_wtohuman_examples",
    ),
]
