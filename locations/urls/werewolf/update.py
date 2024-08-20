from django.urls import path
from locations import views

# Create your URLs here
app_name = "locations:update"
urls = [
    path(
        "caern/<pk>/",
        views.werewolf.CaernUpdateView.as_view(),
        name="caern",
    ),
]
