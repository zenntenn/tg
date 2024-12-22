from accounts.forms import (
    CustomUSerCreationForm,
    FreebieAwardForm,
    ProfileUpdateForm,
    SceneXP,
    StoryXP,
    WeeklyXP,
)
from accounts.models import Profile
from characters.models.core import Character
from characters.models.mage.rote import Rote
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView
from game.models import Chronicle, Scene, Story, Week
from items.models.core import ItemModel
from locations.models.core.location import LocationModel


class SignUp(CreateView):
    """View for the Sign Up Page"""

    form_class = CustomUSerCreationForm
    success_url = reverse_lazy("home")
    template_name = "accounts/signup.html"


class ProfileView(DetailView):
    model = Profile
    template_name = "accounts/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["scenes_waiting"] = []
        if self.object.is_st():
            context["scenes_waiting"] = Scene.objects.filter(waiting_for_st=True)
        context["scenexp_forms"] = [
            SceneXP(scene=s, prefix=f"scene_{s.pk}") for s in self.object.xp_requests()
        ]
        context["story_xp_forms"] = [
            StoryXP(story=x, prefix=f"story_{x.pk}")
            for x in Story.objects.filter(xp_given=False)
        ]
        context["weekly_xp_forms"] = [
            WeeklyXP(week=x, prefix=f"week_{x.pk}")
            for x in Week.objects.filter(xp_given=False)
        ]
        context["freebie_forms"] = [
            FreebieAwardForm(character=character)
            for character in self.object.freebies_to_approve()
        ]
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        submitted_scene_id = request.POST.get("submit_scene")
        submitted_story_id = request.POST.get("submit_story")
        submitted_week_id = request.POST.get("submit_week")
        submitted_freebies_id = request.POST.get("submit_freebies")
        approve_character_id = request.POST.get("approve_character")
        approve_location_id = request.POST.get("approve_location")
        approve_item_id = request.POST.get("approve_item")
        approve_rote_id = request.POST.get("approve_rote")
        approve_character_image_id = request.POST.get("approve_character_image")
        approve_location_image_id = request.POST.get("approve_location_image")
        approve_item_image_id = request.POST.get("approve_item_image")
        if submitted_scene_id is not None:
            scene = Scene.objects.get(pk=submitted_scene_id)
            form = SceneXP(request.POST, scene=scene)
            if form.is_valid():
                form.save()
        if submitted_story_id is not None:
            story = Story.objects.get(pk=submitted_story_id)
            form = StoryXP(request.POST, story=story)
            if form.is_valid():
                form.save()
        if submitted_week_id is not None:
            week = Week.objects.get(pk=submitted_week_id)
            form = WeeklyXP(request.POST, week=week)
            if form.is_valid():
                form.save()
        if approve_character_id is not None:
            char = Character.objects.get(pk=approve_character_id)
            char.status = "App"
            char.save()
            if hasattr(char, "group_set"):
                for g in char.group_set.all():
                    g.update_pooled_backgrounds()
        if approve_location_id is not None:
            loc = LocationModel.objects.get(pk=approve_location_id)
            loc.status = "App"
            loc.save()
        if approve_item_id is not None:
            item = ItemModel.objects.get(pk=approve_item_id)
            item.status = "App"
            item.save()
        if approve_rote_id is not None:
            rote = Rote.objects.get(pk=approve_rote_id)
            rote.status = "App"
            rote.save()
        if approve_character_image_id is not None:
            approve_character_image_id = approve_character_image_id.split("-")[-1]
            char = Character.objects.get(pk=approve_character_image_id)
            char.image_status = "App"
            char.save()
        if approve_item_image_id is not None:
            approve_item_image_id = approve_item_image_id.split("-")[-1]
            loc = LocationModel.objects.get(pk=approve_location_image_id)
            loc.image_status = "App"
            loc.save()
        if approve_item_image_id is not None:
            approve_item_image_id = approve_item_image_id.split("-")[-1]
            item = ItemModel.objects.get(pk=approve_item_image_id)
            item.image_status = "App"
            item.save()
        if submitted_freebies_id is not None:
            char = Character.objects.get(pk=submitted_freebies_id)
            form = FreebieAwardForm(request.POST, character=char)
            if form.is_valid():
                form.save()
        elif "Edit Preferences" in request.POST.keys():
            return redirect("profile_update", pk=self.object.pk)
        return render(
            request,
            "accounts/detail.html",
            self.get_context_data(),
        )


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = "accounts/form.html"


class CustomLoginView(LoginView):
    def get_success_url(self):
        return self.request.user.profile.get_absolute_url()
