from characters.models.core import CharacterModel
from django.shortcuts import redirect, render
from django.views import View
from game.models import Chronicle, Scene, Story
from items.models.core import ItemModel
from locations.models.core import LocationModel


# Create your views here.
class ChronicleDetailView(View):
    def get_context(self, pk):
        chronicle = Chronicle.objects.get(pk=pk)
        return {
            "object": chronicle,
            "stories": Story.objects.filter(chronicle=chronicle).order_by("start_date"),
            "characters": CharacterModel.objects.filter(chronicle=chronicle).order_by(
                "name"
            ),
            "locations": LocationModel.objects.filter(chronicle=chronicle).order_by(
                "name"
            ),
            "items": ItemModel.objects.filter(chronicle=chronicle).order_by("name"),
        }

    def get(self, request, *args, **kwargs):
        context = self.get_context(kwargs["pk"])
        return render(request, "game/chronicle/detail.html", context)

    def post(self, request, *args, **kwargs):
        context = self.get_context(kwargs["pk"])
        return redirect(context["object"].add_story(request.POST["name"]))


class StoryDetailView(View):
    def get_context(self, pk):
        story = Story.objects.get(pk=pk)
        return {
            "object": story,
            "scenes": Scene.objects.filter(story=story),
        }

    def get(self, request, *args, **kwargs):
        context = self.get_context(kwargs["pk"])
        return render(request, "game/story/detail.html", context)

    def post(self, request, *args, **kwargs):
        context = self.get_context(kwargs["pk"])
        loc = LocationModel.objects.get(pk=request.POST["location"])
        return redirect(
            context["object"].add_scene(
                request.POST["name"], loc, date_of_scene=request.POST["date_of_scene"]
            )
        )


class SceneDetailView(View):
    def get_context(self, pk, user):
        if not user.is_authenticated:
            user = None
        scene = Scene.objects.get(pk=pk)
        return {
            "object": scene,
        }

    def get(self, request, *args, **kwargs):
        context = self.get_context(kwargs["pk"], request.user)
        return render(request, "game/scene/detail.html", context)

    def post(self, request, *args, **kwargs):
        context = self.get_context(kwargs["pk"], request.user)
        if "close_scene" in request.POST.keys():
            context["object"].close()
        return render(request, "game/scene/detail.html", context)


class ChronicleScenesDetailView(View):
    def get(self, request, *args, **kwargs):
        chronicle = Chronicle.objects.get(pk=kwargs["pk"])
        context = {
            "chronicle": chronicle,
            "scenes": Scene.objects.filter(story__chronicle=chronicle).order_by(
                "date_of_scene"
            ),
        }
        return render(request, "game/scenes/detail.html", context)
