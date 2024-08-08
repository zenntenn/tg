from django.urls import include, path
from items import views

from .core import create, detail, update

# Create your URLs here
urlpatterns = [
    path("create/", include((create.urls, "items_create"), namespace="create")),
    path("update/", include((update.urls, "items_update"), namespace="update")),
    path("", include(detail.urls)),
]
