from django.urls import include, path
from items import views

from . import mage, werewolf
from .core import create, detail, update

urlpatterns = [
    path("werewolf/", include((werewolf.urls, "werewolf"), namespace="werewolf")),
    path("mage/", include((mage.urls, "mage"), namespace="mage")),
    path("create/", include((create.urls, "items_create"), namespace="create")),
    path("update/", include((update.urls, "items_update"), namespace="update")),
    path("index/<gameline>/", views.core.ItemIndexView.as_view(), name="index"),
    path("", include(detail.urls)),
]
