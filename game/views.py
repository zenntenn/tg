import itertools

from characters.models.core import CharacterModel
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
            "items": ItemModel.objects.filter(chronicle=chronicle).order_by("name"),
            "form": SceneCreationForm(chronicle=chronicle),
            "top_locations": top_locations,
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
            "post_form": PostForm(user=user, scene=scene),
            "add_char_form": a,
            "num_chars": num_chars,
            "num_logged_in_chars": scene.characters.filter(owner=user).count(),
            "first_char": scene.characters.filter(owner=user).first(),
        }

    def get(self, request, *args, **kwargs):
        context = self.get_context(kwargs["pk"], request.user)
        return render(request, "game/scene/detail.html", context)

    def post(self, request, *args, **kwargs):
        context = self.get_context(kwargs["pk"], request.user)
        if "close_scene" in request.POST.keys():
            context["object"].close()
        elif "character_to_add" in request.POST.keys():
            c = CharacterModel.objects.get(pk=request.POST["character_to_add"])
            context["object"].add_character(c)
        elif "message" in request.POST.keys():
            if context["num_logged_in_chars"] == 1:
                character = context["first_char"]
            else:
                character = CharacterModel.objects.get(pk=request.POST["character"])
            context["object"].add_post(
                character, request.POST["display_name"], request.POST["message"]
            )
        return render(request, "game/scene/detail.html", context)


class ChronicleScenesDetailView(View):
    def get(self, request, *args, **kwargs):
        chronicle = get_object_or_404(Chronicle, pk=kwargs["pk"])
        scenes = Scene.objects.filter(chronicle=chronicle).order_by("-date_of_scene")

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
