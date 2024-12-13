from characters.models.core.human import Human
from core.views.approved_user_mixin import SpecialUserMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import FormView


class GenericBackgroundView(SpecialUserMixin, FormView):
    primary_object_class = Human
    background_name = ""
    potential_skip = []
    multiple_ownership = False

    def form_valid(self, form):
        content = self.get_context_data()
        primary_object = content["object"]
        background_object = form.save()
        if self.multiple_ownership:
            background_object.owned_by.add(primary_object)
        else:
            background_object.owned_by = primary_object
        background_object.owner = primary_object.owner
        background_object.chronicle = primary_object.chronicle
        background_object.status = "Sub"
        background_object.save()

        self.current_background.note = background_object.name
        self.current_background.url = background_object.get_absolute_url()
        self.current_background.complete = True
        self.current_background.save()

        if (
            primary_object.backgrounds.filter(
                bg__property_name=self.background_name, complete=False
            ).count()
            == 0
        ):
            primary_object.creation_status += 1
            primary_object.save()
            for step in self.potential_skip:
                if (
                    primary_object.backgrounds.filter(
                        bg__property_name=step, complete=False
                    ).count()
                    == 0
                ):
                    primary_object.creation_status += 1
                else:
                    primary_object.save()
                    break
            primary_object.save()
        return HttpResponseRedirect(primary_object.get_absolute_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = get_object_or_404(
            self.primary_object_class, pk=self.kwargs.get("pk")
        )
        context["is_approved_user"] = self.check_if_special_user(
            context["object"], self.request.user
        )
        context["curreng_background"] = (
            context["object"]
            .backgrounds.filter(bg__property_name=self.background_name, complete=False)
            .first()
        )
        return context

    def get_form(self, form_class=None):
        obj = get_object_or_404(self.primary_object_class, pk=self.kwargs.get("pk"))
        self.current_background = obj.backgrounds.filter(
            bg__property_name=self.background_name, complete=False
        ).first()
        form = super().get_form(form_class)
        form.fields["rank"].initial = self.current_background.rating
        form.fields["rank"].widget.attrs.update(
            {
                "min": self.current_background.rating,
                "max": self.current_background.rating,
            }
        )
        return form
