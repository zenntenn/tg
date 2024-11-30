import itertools

from characters.models.core import CharacterModel
from characters.models.core.group import Group
from core.utils import level_name, tree_sort
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.timezone import datetime, localtime
from django.views import View
from game.forms import AddCharForm, PostForm, SceneCreationForm
from game.models import Chronicle, Post, Scene
from items.models.core import ItemModel
from locations.models.core import LocationModel


class ChronicleDetailView(View):
    def get_context(self, pk):
        chronicle = Chronicle.objects.get(pk=pk)
        top_locations = LocationModel.objects.filter(
            chronicle=chronicle, parent=None
        ).order_by("name")

        return {
            "object": chronicle,
            "characters": CharacterModel.objects.filter(chronicle=chronicle).order_by(
                "name"
            ),
            "groups": Group.objects.filter(chronicle=chronicle).order_by("name"),
            "items": ItemModel.objects.filter(chronicle=chronicle).order_by("name"),
            "form": SceneCreationForm(chronicle=chronicle),
            "top_locations": top_locations,
            "active_scenes": Scene.objects.filter(chronicle=chronicle, finished=False),
        }

    def get(self, request, *args, **kwargs):
        context = self.get_context(kwargs["pk"])
        return render(request, "game/chronicle/detail.html", context)

    def post(self, request, *args, **kwargs):
        context = self.get_context(kwargs["pk"])
        return redirect(
            context["object"].add_scene(
                request.POST["name"],
                LocationModel.objects.get(pk=request.POST["location"]),
                date_of_scene=request.POST["date_of_scene"],
            )
        )


class SceneDetailView(View):
    def get_context(self, pk, user):
        if not user.is_authenticated:
            user = None
        scene = Scene.objects.get(pk=pk)
        a = AddCharForm(user=user, scene=scene)
        num_chars = (a.fields["character_to_add"].queryset).count()
        return {
            "object": scene,
            "posts": Post.objects.filter(scene=scene),
            "post_form": PostForm,
            "add_char_form": a,
            "num_chars": num_chars,
            "num_logged_in_chars": scene.characters.filter(owner=user).count(),
            "first_char": scene.characters.filter(owner=user).first(),
        }

    def get(self, request, *args, **kwargs):
        context = self.get_context(kwargs["pk"], request.user)
        context["post_form"] = context["post_form"](
            user=request.user, scene=context["object"]
        )
        return render(request, "game/scene/detail.html", context)

    def post(self, request, *args, **kwargs):
        context = self.get_context(kwargs["pk"], request.user)
        if "close_scene" in request.POST.keys():
            context["post_form"] = context["post_form"](
                user=request.user, scene=context["object"]
            )
            context["object"].close()
        elif "character_to_add" in request.POST.keys():
            c = CharacterModel.objects.get(pk=request.POST["character_to_add"])
            context["post_form"] = context["post_form"](
                user=request.user, scene=context["object"]
            )
            context["object"].add_character(c)
        elif "message" in request.POST.keys():
            context["post_form"] = context["post_form"](
                request.POST, user=request.user, scene=context["object"]
            )
            if context["post_form"].is_valid():
                if context["num_logged_in_chars"] == 1:
                    character = context["first_char"]
                else:
                    character = CharacterModel.objects.get(pk=request.POST["character"])
                try:
                    context["object"].add_post(
                        character, request.POST["display_name"], request.POST["message"]
                    )
                    context["post_form"] = PostForm(
                        user=request.user, scene=context["object"]
                    )
                except ValueError:
                    context["post_form"].add_error(
                        None, "Command does not match the expected format."
                    )
        return render(request, "game/scene/detail.html", context)


class ChronicleScenesDetailView(View):
    def get(self, request, *args, **kwargs):
        chronicle = get_object_or_404(Chronicle, pk=kwargs["pk"])
        scenes = Scene.objects.filter(chronicle=chronicle)

        # Group scenes by year and month
        scenes_grouped = [
            (datetime(year=year, month=month, day=1), list(scenes_in_month))
            for (year, month), scenes_in_month in itertools.groupby(
                scenes, key=lambda x: (x.date_of_scene.year, x.date_of_scene.month)
            )
        ]

        context = {
            "chronicle": chronicle,
            "scenes_grouped": scenes_grouped,
        }
        return render(request, "game/scenes/detail.html", context)
