from characters import views
from django.urls import path

app_name = "vampire:ajax"
urls = [
    path(
        "load_vtmhuman_examples/",
        views.vampire.vtmhuman.VtMHumanFreebieFormPopulationView.as_view(),
        name="load_vtmhuman_examples",
    ),
]
