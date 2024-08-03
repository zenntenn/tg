from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from accounts.forms import CustomUSerCreationForm
from characters.models.core import CharacterModel
from items.models.core import ItemModel


# Create your views here.
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
        return render(
            request,
            "accounts/index.html",
            context,
        )

    def get_context(self, user):
        return {
            "characters": CharacterModel.objects.filter(owner=user).order_by("name"),
            "items": ItemModel.objects.filter(owner=user).order_by("name"),
        }
