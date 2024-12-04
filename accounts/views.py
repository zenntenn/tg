from accounts.forms import CustomUSerCreationForm, ProfileUpdateForm
from accounts.models import Profile
from characters.models.core import Character
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView
from game.models import Chronicle, Scene
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
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        if any(x.startswith("XP for") for x in request.POST.keys()):
            to_remove = [x for x in request.POST.keys() if x.startswith("XP for")][0]
            new_dict = {
                "-".join(k.split("-")[1:]): v
                for k, v in request.POST.items()
                if (k not in [to_remove, "csrfmiddlewaretoken"] and v != "")
            }
            scene_name = [x for x in request.POST.keys() if x.startswith("XP for")][
                0
            ].split("XP for ")[-1]
            scene = Scene.objects.get(id=scene_name.split("-")[-1])
            for char in scene.characters.all():
                if char.name in new_dict.keys():
                    char.xp += int(new_dict[char.name])
                    char.save()
            scene.xp_given = True
            scene.save()
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
