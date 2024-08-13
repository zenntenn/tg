from django.urls import path
from items import views

# Create your URLs here
urls = [
    path(
        "wonder/<pk>/",
        views.mage.WonderUpdateView.as_view(),
        name="wonder",
    ),
    path(
        "charm//<pk>/",
        views.mage.CharmUpdateView.as_view(),
        name="charm",
    ),
    path(
        "artifact/<pk>/",
        views.mage.ArtifactUpdateView.as_view(),
        name="artifact",
    ),
]
