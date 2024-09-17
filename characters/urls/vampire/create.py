from characters import views
from django.urls import path

urls = [
    path(
        "vtmhuman/",
        views.vampire.VtMHumanCreateView.as_view(),
        name="vtm_human",
    ),
]
