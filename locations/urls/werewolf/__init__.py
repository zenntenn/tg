from characters import views
from django.urls import include, path

from . import create, detail, update

# Create your URLs here
urls = [
    path("create/", include((create.urls, "mage_create"), namespace="create")),
    path("update/", include((update.urls, "mage_update"), namespace="update")),
    path("", include(detail.urls)),
]
