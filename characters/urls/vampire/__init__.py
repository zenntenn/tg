from characters import views
from django.urls import include, path

from . import create, detail, index, update, ajax

urls = [
    path("ajax/", include((ajax.urls, "vampire_ajax"), namespace="ajax")),
    path("create/", include((create.urls, "vampire_create"), namespace="create")),
    path("update/", include((update.urls, "vampire_update"), namespace="update")),
    path("list/", include((index.urls, "vampire_list"), namespace="list")),
    path("", include(detail.urls)),
]
