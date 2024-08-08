from characters import views
from django.urls import include, path

from .core import create, detail, update

# Create your URLs here
urlpatterns = [
    path("create/", include((create.urls, "characters_create"), namespace="create")),
    path("update/", include((update.urls, "characters_update"), namespace="update")),
    path("", include(detail.urls)),
]
