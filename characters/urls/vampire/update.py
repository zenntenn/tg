from characters import views
from django.urls import path

urls = [
    path(
        "vtmhuman/<pk>/",
        views.vampire.VtMHumanUpdateView.as_view(),
        name="vtm_human",
    ),
    path(
        "vtm_human/full/<pk>/",
        views.vampire.VtMHumanUpdateView.as_view(),
        name="vtm_human_full",
    ),
]
