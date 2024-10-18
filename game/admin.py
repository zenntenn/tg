from django.contrib import admin
from game.models import (
    Chronicle,
    Gameline,
    ObjectType,
    Post,
    Scene,
    SettingElement,
    Story,
    STRelationship,
)

admin.site.register(Chronicle)


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Scene)
class SceneAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "story",
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
