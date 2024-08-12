from django.urls import path
from locations import views

# Create your URLs here
app_name = "locations:update"
urls = [
    path(
        "node/<pk>/",
        views.mage.NodeUpdateView.as_view(),
        name="node",
    ),
]
