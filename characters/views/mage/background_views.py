from typing import Any

from characters.forms.core.ally import AllyForm
from characters.forms.mage.enhancements import EnhancementForm
from characters.forms.mage.familiar import FamiliarForm
from characters.models.core.background_block import Background, BackgroundRating
from characters.models.core.human import Human
from characters.models.mage.companion import Companion
from characters.models.mage.mage import Mage
from characters.models.mage.mtahuman import MtAHuman
from characters.models.werewolf.spirit_character import SpiritCharacter
from core.views.approved_user_mixin import SpecialUserMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import FormView


class MtAFamiliarView(SpecialUserMixin, FormView):
    form_class = FamiliarForm
    template_name = "characters/mage/mage/chargen.html"
    potential_skip = [
        "wonder",
        "enhancement",
        "sanctum",
        "allies",
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = get_object_or_404(Human, pk=self.kwargs.get("pk"))
        context["is_approved_user"] = self.check_if_special_user(
            context["object"], self.request.user
        )
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        obj = context["object"]

        c = Companion(
            name=form.cleaned_data["name"],
            nature=form.cleaned_data["nature"],
            demeanor=form.cleaned_data["demeanor"],
            companion_type="familiar",
            concept=form.cleaned_data["concept"],
            chronicle=obj.chronicle,
            owner=obj.owner,
            npc=True,
            companion_of=obj,
        )
        x = BackgroundRating.objects.filter(
            char=obj,
            bg=Background.objects.get(property_name="familiar"),
            complete=False,
        ).first()
        c.freebies = 10 * x.rating
        c.save()
        x.url = c.get_absolute_url()
        x.complete = True
        x.note = c.name
        x.save()
        if (
            BackgroundRating.objects.filter(
                char=obj,
                bg=Background.objects.get(property_name="familiar"),
                complete=False,
            ).count()
            == 0
        ):
            obj.creation_status += 1
            obj.save()
            for step in self.potential_skip:
                if (
                    BackgroundRating.objects.filter(
                        bg=Background.objects.get(property_name=step),
                        char=obj,
                        complete=False,
                    ).count()
                    == 0
                ):
                    obj.creation_status += 1
                else:
                    obj.save()
                    break
            obj.save()
        return HttpResponseRedirect(obj.get_absolute_url())

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["name"].initial = (
            BackgroundRating.objects.filter(
                char=get_object_or_404(Human, pk=self.kwargs.get("pk")),
                bg=Background.objects.get(property_name="familiar"),
                complete=False,
            )
            .first()
            .note
        )
        return form


class MtAEnhancementView(SpecialUserMixin, FormView):
    form_class = EnhancementForm
    template_name = "characters/mage/mage/chargen.html"

    potential_skip = [
        "sanctum",
        "allies",
    ]

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        obj = Human.objects.get(id=self.kwargs["pk"])
        self.current_enhancement = BackgroundRating.objects.filter(
            char=obj,
            bg=Background.objects.get(property_name="enhancement"),
            complete=False,
        ).first()
        kwargs["rank"] = self.current_enhancement.rating
        return kwargs

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        obj = get_object_or_404(Human, pk=self.kwargs.get("pk"))
        self.current_enhancement = BackgroundRating.objects.filter(
            char=obj,
            bg=Background.objects.get(property_name="enhancement"),
            complete=False,
        ).first()
        return form

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["object"] = Human.objects.get(id=self.kwargs["pk"])
        context["is_approved_user"] = self.check_if_special_user(
            context["object"], self.request.user
        )
        context["current_enhancement"] = self.current_enhancement
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        obj = context["object"]
        # Check Data Valid
        if form.save(char=obj):
            if (
                BackgroundRating.objects.filter(
                    char=obj,
                    bg=Background.objects.get(property_name="enhancement"),
                    complete=False,
                ).count()
                == 0
            ):
                obj.creation_status += 1
                obj.save()
                for step in self.potential_skip:
                    if (
                        BackgroundRating.objects.filter(
                            bg=Background.objects.get(property_name=step),
                            char=obj,
                            complete=False,
                        ).count()
                        == 0
                    ):
                        obj.creation_status += 1
                    else:
                        obj.save()
                        break
                obj.save()
            return HttpResponseRedirect(obj.get_absolute_url())
        return super().form_invalid(form)


class MtAAlliesView(SpecialUserMixin, FormView):
    form_class = AllyForm
    template_name = "characters/mage/mage/chargen.html"

    ally_types = {"human": MtAHuman, "mage": Mage, "spirit": SpiritCharacter}

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["object"] = Human.objects.get(id=self.kwargs["pk"])
        context["is_approved_user"] = self.check_if_special_user(
            context["object"], self.request.user
        )
        context["current_ally"] = self.current_ally
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        obj = context["object"]
        char_class = self.ally_types[form.cleaned_data["ally_type"]]
        a = char_class.objects.create(
            name=form.cleaned_data["name"],
            concept=form.cleaned_data["name"],
            notes=form.cleaned_data["name"]
            + f"<br> Rank {self.current_ally.rating} Ally for {obj.name}",
            chronicle=obj.chronicle,
            npc=True,
            status="Un",
        )
        obj.allied_characters.add(a)

        self.current_ally.note = a.name
        self.current_ally.url = a.get_absolute_url()
        self.current_ally.complete = True
        self.current_ally.save()

        if (
            BackgroundRating.objects.filter(
                char=obj,
                bg=Background.objects.get(property_name="allies"),
                complete=False,
            ).count()
            == 0
        ):
            obj.creation_status += 1
            obj.save()
        return HttpResponseRedirect(obj.get_absolute_url())

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        obj = get_object_or_404(Human, pk=self.kwargs.get("pk"))
        self.current_ally = BackgroundRating.objects.filter(
            char=obj, bg=Background.objects.get(property_name="allies"), complete=False
        ).first()
        form.fields["name"].initial = self.current_ally.note
        return form
