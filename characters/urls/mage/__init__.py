from characters import views
from characters.urls.mage import ajax, create, detail, update
from django.urls import include, path

# Create your URLs here
urls = [
    path("ajax/", include((ajax.urls, "mage_ajax"), namespace="ajax")),
    path("create/", include((create.urls, "mage_create"), namespace="create")),
    path("update/", include((update.urls, "mage_update"), namespace="update")),
    path("", include(detail.urls)),
]
