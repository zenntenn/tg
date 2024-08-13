from django.urls import path
from items import views

# Create your URLs here
urls = [
    path(
        "wonder/",
        views.mage.WonderCreateView.as_view(),
        name="wonder",
    ),
    path(
        "charm/",
        views.mage.CharmCreateView.as_view(),
        name="charm",
    ),
    path(
        "artifact/",
        views.mage.ArtifactCreateView.as_view(),
        name="artifact",
    ),
    path(
        "talisman/",
        views.mage.TalismanCreateView.as_view(),
        name="talisman",
    ),
]
