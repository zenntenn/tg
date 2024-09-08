from django.urls import path
from items import views

urls = [
    path("material/", views.core.MaterialListView.as_view(), name="material"),
    path("medium/", views.core.MediumListView.as_view(), name="medium"),
]
