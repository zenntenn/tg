from characters import views
from django.urls import include, path

from . import create, detail, index, update, ajax

urls = [
    path("ajax/", include((ajax.urls, "werewolf_ajax"), namespace="ajax")),
    path("create/", include((create.urls, "werewolf_create"), namespace="create")),
    path("update/", include((update.urls, "werewolf_update"), namespace="update")),
    path("list/", include((index.urls, "werewolf_list"), namespace="list")),
    path("", include(detail.urls)),
]
