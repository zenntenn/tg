from characters import views
from django.urls import include, path

from . import changeling, mage, vampire, werewolf, wraith
from .core import ajax, create, detail, index, update

urlpatterns = [
    path("vampire/", include((vampire.urls, "vampire"), namespace="vampire")),
    path("werewolf/", include((werewolf.urls, "werewolf"), namespace="werewolf")),
    path("mage/", include((mage.urls, "mage"), namespace="mage")),
    path("wraith/", include((wraith.urls, "wraith"), namespace="wraith")),
    path(
        "changeling/", include((changeling.urls, "changeling"), namespace="changeling")
    ),
    path("ajax/", include((ajax.urls, "characters_ajax"), namespace="ajax")),
    path("create/", include((create.urls, "characters_create"), namespace="create")),
    path("update/", include((update.urls, "characters_update"), namespace="update")),
    path("list/", include((index.urls, "characters_list"), namespace="list")),
    path("index/<gameline>/", views.core.CharacterIndexView.as_view(), name="index"),
    path("", include(detail.urls)),
]
