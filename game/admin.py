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
        "chronicle",
        "location",
        "finished",
        "xp_given",
        "waiting_for_st",
        "num_pcs",
        "total_posts",
    )
    list_filter = ("chronicle", "finished", "xp_given", "waiting_for_st")

    def num_pcs(self, obj):
        return obj.characters.filter(npc=False).count()

    def total_posts(self, obj):
        return obj.total_posts()


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
