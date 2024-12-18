from characters import views
from django.urls import include, path

from . import ajax, create, detail, index, update

urls = [
    path("create/", include((create.urls, "mage_create"), namespace="create")),
    path("update/", include((update.urls, "mage_update"), namespace="update")),
    path("list/", include((index.urls, "items_list"), namespace="list")),
    path("ajax/", include((ajax.urls, "items_ajax"), namespace="ajax")),
    path("", include(detail.urls)),
]
