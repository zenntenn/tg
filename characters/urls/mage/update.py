from characters import views
from django.urls import path

# Create your URLs here
app_name = "mage:update"
urls = [
    path(
        "effect/<pk>/",
        views.mage.EffectUpdateView.as_view(),
        name="effect",
    ),
]
