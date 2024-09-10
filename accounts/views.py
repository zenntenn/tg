from accounts.forms import CustomUSerCreationForm
from characters.models.core import CharacterModel
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from game.models import Chronicle, Scene
from items.models.core import ItemModel
from locations.models.core.location import LocationModel


class SignUp(CreateView):
    """View for the Sign Up Page"""

    form_class = CustomUSerCreationForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


class ProfileView(View):
    """View for User Profiles"""

    def get(self, request):
        if request.user.is_authenticated:
            context = self.get_context(request.user)
            return render(
                request,
                "accounts/index.html",
                context,
            )
        return redirect("/accounts/login/")

    def post(self, request):
        context = self.get_context(request.user)
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
        context = self.get_context(request.user)
        return render(
            request,
            "accounts/index.html",
            context,
        )

    def get_context(self, user):
        chronicles_sted = [
            x for x in Chronicle.objects.all() if user in x.storytellers.all()
        ]
        return {
            "characters": CharacterModel.objects.filter(owner=user).order_by("name"),
            "items": ItemModel.objects.filter(owner=user).order_by("name"),
            "xp_requests": Scene.objects.filter(
                story__chronicle__in=chronicles_sted, finished=True, xp_given=False
            ),
            "locations": LocationModel.objects.filter(owner=user).order_by("name"),
        }
