from characters import views
from django.urls import path

# Create your URLs here
urls = [
    path(
        "wtohuman/",
        views.wraith.WtOHumanCreateView.as_view(),
        name="wto_human",
    ),
]
