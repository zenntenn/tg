from django.shortcuts import redirect, render
from django.views import View
from game.models import Chronicle, Story
from locations.models.core import LocationModel


# Create your views here.
class ChronicleDetailView(View):
    def get_context(self, pk):
        chronicle = Chronicle.objects.get(pk=pk)
        return {
            "object": chronicle,
            "stories": Story.objects.filter(chronicle=chronicle).order_by("start_date"),
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
