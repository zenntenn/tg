from django.contrib import admin
from game.models import (
    Chronicle,
    Gameline,
    ObjectType,
    Post,
    Scene,
    SettingElement,
    STRelationship,
)

admin.site.register(Chronicle)


@admin.register(Scene)
class SceneAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "finished",
    )


admin.site.register(Post)
admin.site.register(SettingElement)
admin.site.register(ObjectType)

admin.site.register(Gameline)


@admin.register(STRelationship)
class STRelationshipAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "chronicle",
        "gameline",
    )
