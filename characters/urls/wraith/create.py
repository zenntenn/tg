from characters import views
from django.urls import path

urls = [
    path(
        "wtohuman/",
        views.wraith.WtOHumanCreateView.as_view(),
        name="wto_human",
    ),
]
