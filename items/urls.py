from django.urls import path
from items import views

# Create your URLs here
app_name = "items"
urlpatterns = [
    path("item/create/", views.ItemCreateView.as_view(), name="create_item"),
    path(
        "item/update/<pk>/",
        views.ItemUpdateView.as_view(),
        name="update_item",
    ),
    path(
        "weapon/create/",
        views.WeaponCreateView.as_view(),
        name="create_weapon",
    ),
    path(
        "weapon/update/<pk>/",
        views.WeaponUpdateView.as_view(),
        name="update_weapon",
    ),
    path(
        "meleeweapon/create/",
        views.MeleeWeaponCreateView.as_view(),
        name="create_meleeweapon",
    ),
    path(
        "meleeweapon/update/<pk>/",
        views.MeleeWeaponUpdateView.as_view(),
        name="update_meleeweapon",
    ),
    path(
        "rangedweapon/create/",
        views.RangedWeaponCreateView.as_view(),
        name="create_rangedweapon",
    ),
    path(
        "rangedweapon/update/<pk>/",
        views.RangedWeaponUpdateView.as_view(),
        name="update_rangedweapon",
    ),
    path(
        "thrownweapon/create/",
        views.ThrownWeaponCreateView.as_view(),
        name="create_thrownweapon",
    ),
    path(
        "thrownweapon/update/<pk>/",
        views.ThrownWeaponUpdateView.as_view(),
        name="update_thrownweapon",
    ),
    path(
        "material/create/",
        views.MaterialCreateView.as_view(),
        name="create_material",
    ),
    path(
        "material/update/<pk>/",
        views.MaterialUpdateView.as_view(),
        name="update_material",
    ),
    path("material/<pk>/", views.MaterialDetailView.as_view(), name="material"),
    path(
        "medium/create/",
        views.MediumCreateView.as_view(),
        name="create_medium",
    ),
    path(
        "medium/update/<pk>/",
        views.MediumUpdateView.as_view(),
        name="update_medium",
    ),
    path("medium/<pk>/", views.MediumDetailView.as_view(), name="medium"),
    path("<pk>/", views.GenericItemDetailView.as_view(), name="item"),
]
