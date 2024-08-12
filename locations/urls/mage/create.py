from django.urls import path
from locations import views

# Create your URLs here
app_name = "mage:create"
urls = [
    path(
        "node/",
        views.mage.NodeCreateView.as_view(),
        name="node",
    ),
]
