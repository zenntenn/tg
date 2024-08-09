from characters import views
from characters.urls.mage import create, detail, update
from django.urls import include, path

# Create your URLs here
urls = [
    path("create/", include((create.urls, "mage_create"), namespace="create")),
    path("update/", include((update.urls, "mage_update"), namespace="update")),
    path("", include(detail.urls)),
]
