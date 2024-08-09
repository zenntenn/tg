from characters import views
from django.urls import path

# Create your URLs here
app_name = "mage:detail"
urls = [
    path(
        "effect/<pk>/",
        views.mage.EffectDetailView.as_view(),
        name="effect",
    ),
]
