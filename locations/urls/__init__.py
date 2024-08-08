from django.urls import include, path
from locations import views

from .core import create, detail, update

# Create your URLs here
urlpatterns = [
    path("create/", include((create.urls, "locations_create"), namespace="create")),
    path("update/", include((update.urls, "locations_update"), namespace="update")),
    path("", include(detail.urls)),
]
