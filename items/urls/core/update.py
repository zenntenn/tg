from django.urls import path
from items import views

# Create your URLs here
app_name = "items:update"
urls = [
    path(
        "item/<pk>/",
        views.core.ItemUpdateView.as_view(),
        name="item",
    ),
    path(
        "weapon/<pk>/",
        views.core.WeaponUpdateView.as_view(),
        name="weapon",
    ),
    path(
        "meleeweapon/<pk>/",
        views.core.MeleeWeaponUpdateView.as_view(),
        name="meleeweapon",
    ),
    path(
        "rangedweapon/<pk>/",
        views.core.RangedWeaponUpdateView.as_view(),
        name="rangedweapon",
    ),
    path(
        "thrownweapon/<pk>/",
        views.core.ThrownWeaponUpdateView.as_view(),
        name="thrownweapon",
    ),
    path(
        "material/<pk>/",
        views.core.MaterialUpdateView.as_view(),
        name="material",
    ),
    path(
        "medium/<pk>/",
        views.core.MediumUpdateView.as_view(),
        name="medium",
    ),
]
