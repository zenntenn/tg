from django.urls import include, path
from items import views

from . import mage
from .core import create, detail, update

# Create your URLs here
urlpatterns = [
    path("mage/", include((mage.urls, "mage"), namespace="mage")),
    path("create/", include((create.urls, "items_create"), namespace="create")),
    path("update/", include((update.urls, "items_update"), namespace="update")),
    path("", include(detail.urls)),
]
