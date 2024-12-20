from accounts.forms import (
    CustomUSerCreationForm,
    ProfileUpdateForm,
    SceneXP,
    StoryXP,
    WeeklyXP,
)
from accounts.models import Profile
from characters.models.core import Character
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
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        submitted_scene_id = request.POST.get("submit_scene")
        submitted_story_id = request.POST.get("submit_story")
        submitted_week_id = request.POST.get("submit_week")
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
        elif any(x.startswith("image") for x in request.POST.keys()):
            char = [
                x
                for x in self.object.image_to_approve()
                if "image " + x.name in request.POST.keys()
            ][0]
            char.image_status = "app"
            char.save()
        elif "Edit Preferences" in request.POST.keys():
            return redirect("profile_update", pk=self.object.pk)
        elif len([x for x in request.POST.keys() if x.endswith("_approve")]):
            approved = [
                x.replace("_approve", "")
                for x in request.POST.keys()
                if x.endswith("_approve")
            ][0]
            approved = [
                x for x in self.object.objects_to_approve() if x.name == approved
            ][0]
            approved.status = "App"
            approved.save()
            if hasattr(approved, "group_set"):
                for g in approved.group_set.all():
                    g.update_pooled_backgrounds()
        elif len([x for x in request.POST.keys() if x.endswith("_edit")]):
            to_edit = [
                x.replace("_edit", "")
                for x in request.POST.keys()
                if x.endswith("_edit")
            ][0]
            to_edit = [
                x for x in self.object.objects_to_approve() if x.name == to_edit
            ][0]
            return redirect(to_edit.get_update_url())
        elif len([x for x in request.POST.keys() if x.endswith("_freebies")]):
            to_approve = [
                x.replace("_freebies", "")
                for x in request.POST.keys()
                if x.endswith("_freebies")
            ][0]
            to_approve = [
                x for x in self.object.freebies_to_approve() if x.name == to_approve
            ][0]
            num_to_add = int(request.POST[f"{ to_approve.name }_freebiesField"])
            to_approve.freebies += num_to_add
            if f"{to_approve.name}_checkbox" in request.POST.keys():
                to_approve.freebies += 15
            to_approve.freebies_approved = True
            to_approve.save()
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
