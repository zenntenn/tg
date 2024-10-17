from accounts.forms import CustomUSerCreationForm, ProfileUpdateForm
from accounts.models import Profile
from characters.models.core import Character
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView
from game.models import Chronicle, Scene
from items.models.core import ItemModel
from locations.models.core.location import LocationModel


class SignUp(CreateView):
    """View for the Sign Up Page"""

    form_class = CustomUSerCreationForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


class ProfileView(DetailView):
    model = Profile
    template_name = "accounts/detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        if any(x.startswith("XP for") for x in request.POST.keys()):
            to_remove = [x for x in request.POST.keys() if x.startswith("XP for")][0]
            new_dict = {
                k: v
                for k, v in request.POST.items()
                if k not in [to_remove, "csrfmiddlewaretoken"]
            }
            scene_name = [x for x in request.POST.keys() if x.startswith("XP for")][
                0
            ].split("XP for ")[-1]
            scene = Scene.objects.get(name=scene_name)
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
        else:
            print(request.POST.keys())
            char = [
                x
                for x in self.object.objects_to_approve()
                if x.name in request.POST.keys()
            ][0]
            char.status = "App"
            char.save()
        return render(
            request,
            "accounts/detail.html",
            self.get_context_data(),
        )
