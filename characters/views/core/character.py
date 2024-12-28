from typing import Any

from characters.models.core import Character
from core.views.approved_user_mixin import SpecialUserMixin
from django.views.generic import CreateView, DetailView, UpdateView
from game.models import Scene


class CharacterDetailView(SpecialUserMixin, DetailView):
    model = Character
    template_name = "characters/core/character/detail.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["scenes"] = Scene.objects.filter(characters=context["object"]).order_by(
            "-date_of_scene"
        )
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context


class CharacterCreateView(CreateView):
    model = Character
    fields = "__all__"
    template_name = "characters/core/character/form.html"


class CharacterUpdateView(SpecialUserMixin, UpdateView):
    model = Character
    fields = "__all__"
    template_name = "characters/core/character/form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_approved_user"] = self.check_if_special_user(
            self.object, self.request.user
        )
        return context
