from django.urls import path
from items import views

# Create your URLs here
app_name = "items:create"
urls = [
    path("item/", views.core.ItemCreateView.as_view(), name="item"),
    path(
        "weapon/",
        views.core.WeaponCreateView.as_view(),
        name="weapon",
    ),
    path(
        "meleeweapon/",
        views.core.MeleeWeaponCreateView.as_view(),
        name="meleeweapon",
    ),
    path(
        "rangedweapon/",
        views.core.RangedWeaponCreateView.as_view(),
        name="rangedweapon",
    ),
    path(
        "thrownweapon/",
        views.core.ThrownWeaponCreateView.as_view(),
        name="thrownweapon",
    ),
    path(
        "material/",
        views.core.MaterialCreateView.as_view(),
        name="material",
    ),
    path(
        "medium/",
        views.core.MediumCreateView.as_view(),
        name="medium",
    ),
]
