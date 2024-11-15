from typing import Any

from characters.forms.core.ally import AllyForm
from characters.forms.mage.effect import EffectForm, EffectFormSet
from characters.forms.mage.enhancements import EnhancementForm
from characters.forms.mage.familiar import FamiliarForm
from characters.models.core.background_block import Background, BackgroundRating
from characters.models.core.human import Human
from characters.models.core.merit_flaw_block import MeritFlaw
from characters.models.mage.companion import Companion
from characters.models.mage.effect import Effect
from characters.models.mage.faction import MageFaction
from characters.models.mage.focus import Practice
from characters.models.mage.mage import Mage
from characters.models.mage.mtahuman import MtAHuman
from characters.models.mage.resonance import Resonance
from characters.models.mage.sphere import Sphere
from characters.models.werewolf.spirit_character import SpiritCharacter
from core.views.approved_user_mixin import SpecialUserMixin
from core.views.generic import MultipleFormsetsMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, FormView
from items.forms.mage.wonder import WonderForm
from items.models.mage.artifact import Artifact
from items.models.mage.charm import Charm
from items.models.mage.talisman import Talisman
from items.models.mage.wonder import WonderResonanceRating
from locations.forms.core.sanctum import SanctumForm
from locations.forms.mage.node import (
    NodeForm,
    NodeMeritFlawForm,
    NodeMeritFlawFormSet,
    NodeResonancePracticeRatingFormSet,
    NodeResonanceRatingForm,
)
from locations.forms.mage.reality_zone import (
    RealityZonePracticeRatingForm,
    RealityZonePracticeRatingFormSet,
)
from locations.models.core.location import LocationModel
from locations.models.mage.library import Library
from locations.models.mage.node import Node, NodeMeritFlawRating, NodeResonanceRating
from locations.models.mage.reality_zone import RealityZone, ZoneRating
from locations.models.mage.sanctum import Sanctum


class MtANodeView(SpecialUserMixin, MultipleFormsetsMixin, FormView):
    form_class = NodeForm
    template_name = "characters/mage/mage/chargen.html"
    formsets = {
        "rz_form": RealityZonePracticeRatingFormSet,
        "resonance_form": NodeResonancePracticeRatingFormSet,
        "mf_form": NodeMeritFlawFormSet,
    }
    potential_skip = [
        "library",
        "familiar",
        "wonder",
        "enhancement",
        "sanctum",
        "allies",
    ]

    def form_valid(self, form):
        context = self.get_context_data()
        obj = context["object"]

        n = Node(
            name=form.cleaned_data["name"],
            description=form.cleaned_data["description"],
            ratio=form.cleaned_data["ratio"],
            size=form.cleaned_data["size"],
            quintessence_form=form.cleaned_data["quintessence_form"],
            tass_form=form.cleaned_data["tass_form"],
            gauntlet=3,
            owned_by=obj,
            chronicle=obj.chronicle,
            owner=obj.owner,
            status="Sub",
        )
        n.set_rank(self.current_node.rating)
        n.points -= form.cleaned_data["ratio"]
        n.points -= form.cleaned_data["size"]

        resonance_data = self.get_form_data("resonance_form")
        for res in resonance_data:
            res["resonance"] = Resonance.objects.get_or_create(name=res["resonance"])[0]
            res["rating"] = int(res["rating"])
            if res["rating"] > 5:
                form.add_error(
                    None,
                    "Resonance may not be higher than 5",
                )
                return self.form_invalid(form)
        total_resonance = sum([x["rating"] for x in resonance_data])

        mf_data = self.get_form_data("mf_form")
        for res in mf_data:
            res["mf"] = MeritFlaw.objects.get(id=res["mf"])
            res["rating"] = int(res["rating"])
        total_mfs = sum([x["rating"] for x in mf_data])

        rz_data = self.get_form_data("rz_form")
        for res in rz_data:
            res["practice"] = Practice.objects.get(id=res["practice"])
            res["rating"] = int(res["rating"])
        total_rz = sum([x["rating"] for x in rz_data])
        total_positive = sum([x["rating"] for x in rz_data if x["rating"] > 0])
        if total_rz != 0:
            form.add_error(None, "Ratings must total 0")
            return super().form_invalid(form)
        if total_positive != self.current_node.rating:
            form.add_error(None, "Positive Ratings must equal Node rating")
            return super().form_invalid(form)

        if total_resonance < n.rank:
            form.add_error(None, "Resonance total must match or exceed rank")
            return self.form_invalid(form)
        n.points -= total_resonance - n.rank
        n.points -= total_mfs
        if n.points < 0:
            form.add_error(
                None,
                "Node invalid: spend fewer points on merits/flaws, resonance, size, or ratio",
            )
            return self.form_invalid(form)
        n.update_output()
        n.save()

        self.current_node.note = n.name
        self.current_node.url = n.get_absolute_url()
        self.current_node.complete = True
        self.current_node.save()

        for resonance in resonance_data:
            NodeResonanceRating.objects.create(
                node=n, resonance=resonance["resonance"], rating=resonance["rating"]
            )

        for mf in mf_data:
            NodeMeritFlawRating.objects.create(node=n, mf=mf["mf"], rating=mf["rating"])

        rzone = RealityZone.objects.create(name="{n.name} Reality Zone")
        n.reality_zone = rzone
        n.save()
        for rz in rz_data:
            ZoneRating.objects.create(
                zone=rzone, practice=rz["practice"], rating=rz["rating"]
            )

        if (
            BackgroundRating.objects.filter(
                char=obj,
                bg=Background.objects.get(property_name="node"),
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = get_object_or_404(Human, pk=self.kwargs.get("pk"))
        context["is_approved_user"] = self.check_if_special_user(
            context["object"], self.request.user
        )
        context["points"] = 3 * self.current_node.rating
        context["current_node"] = self.current_node
        return context

    def get_form(self, form_class=None):
        obj = get_object_or_404(Human, pk=self.kwargs.get("pk"))
        self.current_node = BackgroundRating.objects.filter(
            char=obj, bg=Background.objects.get(property_name="node"), complete=False
        ).first()
        form = super().get_form(form_class)
        form.fields["name"].initial = self.current_node.note
        form.fields["quintessence_form"].widget.attrs.update(
            {"placeholder": "Enter quintessence form here"}
        )
        form.fields["tass_form"].widget.attrs.update(
            {"placeholder": "Enter tass form here"}
        )
        form.fields["description"].widget.attrs.update(
            {"placeholder": "Enter description here"}
        )
        return form


class MtALibraryView(SpecialUserMixin, CreateView):
    model = Library
    fields = ["name", "description", "parent"]
    template_name = "characters/mage/mage/chargen.html"
    potential_skip = [
        "familiar",
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
        context["current_library"] = self.current_library
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        obj = context["object"]
        if hasattr(obj, "faction"):
            l = Library(
                **form.cleaned_data,
                owned_by=obj,
                owner=obj.owner,
                chronicle=obj.chronicle,
                faction=obj.faction,
                rank=self.current_library.rating,
                status="Sub",
            )
        else:
            l = Library(
                **form.cleaned_data,
                owned_by=obj,
                owner=obj.owner,
                chronicle=obj.chronicle,
                rank=self.current_library.rating,
                status="Sub",
            )
        l.save()
        for _ in range(l.rank):
            l.random_book()

        self.current_library.note = l.name
        self.current_library.url = l.get_absolute_url()
        self.current_library.complete = True
        self.current_library.save()

        if (
            BackgroundRating.objects.filter(
                char=obj,
                bg=Background.objects.get(property_name="library"),
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
        obj = get_object_or_404(Human, pk=self.kwargs.get("pk"))
        self.current_library = BackgroundRating.objects.filter(
            char=obj, bg=Background.objects.get(property_name="library"), complete=False
        ).first()
        form.fields["name"].initial = (
            self.current_library.note or f"{obj.name}'s Library"
        )
        form.fields["parent"].empty_label = "Choose a Parent Location"
        form.fields["description"].widget.attrs.update(
            {"placeholder": "Enter description here"}
        )
        return form


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


class MtAWonderView(SpecialUserMixin, MultipleFormsetsMixin, FormView):
    form_class = WonderForm
    formsets = {
        "effects_form": EffectFormSet,
        "resonance_form": NodeResonancePracticeRatingFormSet,
    }
    template_name = "characters/mage/mage/chargen.html"

    wonder_classes = {
        "charm": Charm,
        "artifact": Artifact,
        "talisman": Talisman,
    }

    potential_skip = [
        "enhancement",
        "sanctum",
        "allies",
    ]

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["object"] = Human.objects.get(id=self.kwargs["pk"])
        context["is_approved_user"] = self.check_if_special_user(
            context["object"], self.request.user
        )
        context["points"] = 3 * context["object"].wonder
        context["current_wonder"] = self.current_wonder
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        obj = context["object"]
        if form.cleaned_data["select_or_create_wonder"]:
            del form.cleaned_data["select_or_create_wonder"]
            del form.cleaned_data["wonder_options"]
            if form.cleaned_data["wonder_type"] == "artifact":
                del form.cleaned_data["arete"]
            wonder_type = form.cleaned_data["wonder_type"]
            del form.cleaned_data["wonder_type"]
            w = self.wonder_classes[wonder_type](
                **form.cleaned_data,
                rank=self.current_wonder.rating,
                chronicle=obj.chronicle,
                owner=obj.owner,
                status="Sub",
            )
            w.owned_by.add(obj)
            points = 3 * w.rank

            resonance_data = self.get_form_data("resonance_form")
            for res in resonance_data:
                res["resonance"] = Resonance.objects.get_or_create(
                    name=res["resonance"]
                )[0]
                res["rating"] = int(res["rating"])
                if res["rating"] > 5:
                    form.add_error(
                        None,
                        "Resonance may not be higher than 5",
                    )
                    return self.form_invalid(form)
            total_resonance = sum([x["rating"] for x in resonance_data])
            if total_resonance < w.rank:
                form.add_error(None, "Resonance must be at least rank")
                return self.form_invalid(form)
            if wonder_type == "charm":
                max_cost = w.rank
            else:
                max_cost = 2 * w.rank

            effects = []
            total_effect_cost = 0
            effects_data = self.get_form_data("effects_form")
            if wonder_type == "charm" and len(effects_data) > 1:
                form.add_error(None, "Charms can only have one power")
                return self.form_invalid(form)
            elif wonder_type == "artifact" and len(effects_data) > 1:
                form.add_error(None, "Artifacts can only have one power")
                return self.form_invalid(form)
            elif wonder_type == "talisman" and len(effects_data) > w.rank:
                form.add_error(None, "Talismans may up to their rank in effects")
                return self.form_invalid(form)
            for effect in effects_data:
                for sphere in Sphere.objects.all():
                    effect[sphere.property_name] = int(effect[sphere.property_name])
                e = Effect(**effect)
                effects.append(e)
                total_effect_cost += e.cost()
                if total_effect_cost > max_cost:
                    form.add_error(
                        None,
                        "Effects cost more than allowed: rank for Charms, twice rank for Artifacts and Talismans",
                    )
                    return self.form_invalid(form)
            cost = (total_resonance - w.rank) + total_effect_cost
            if wonder_type != "artifact":
                cost += w.arete - w.rank
            if cost > points:
                form.add_error(
                    None,
                    "Extra Resonance, Arete, and Effects must be less than 3 times the rank of the Wonder",
                )
                return self.form_invalid(form)

            w.save()
            for e in effects:
                e.save()
                if wonder_type in ["charm", "artifact"]:
                    w.power = e
                else:
                    w.powers.add(e)
            w.save()

            for resonance in resonance_data:
                WonderResonanceRating.objects.create(
                    wonder=None,
                    resonance=resonance["resonance"],
                    rating=resonance["rating"],
                )
        else:
            w = form.cleaned_data["wonder_options"]
            w.owned_by.add(obj)
            w.save()

        w.display = True
        w.save()
        self.current_wonder.note = w.name
        self.current_wonder.url = w.get_absolute_url()
        self.current_wonder.complete = True
        self.current_wonder.save()

        if (
            BackgroundRating.objects.filter(
                char=obj,
                bg=Background.objects.get(property_name="wonder"),
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
        obj = get_object_or_404(Human, pk=self.kwargs.get("pk"))
        self.current_wonder = BackgroundRating.objects.filter(
            char=obj, bg=Background.objects.get(property_name="wonder"), complete=False
        ).first()
        form.fields["name"].initial = self.current_wonder.note
        form.fields["description"].widget.attrs.update(
            {"placeholder": "Enter description here"}
        )
        return form

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        obj_id = self.kwargs.get("pk")
        obj = Human.objects.get(pk=obj_id)
        kwargs["instance"] = obj
        bgr = BackgroundRating.objects.filter(
            char=obj, bg=Background.objects.get(property_name="wonder"), complete=False
        ).first()
        kwargs["rank"] = bgr.rating
        return kwargs


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


class MtASanctumView(SpecialUserMixin, MultipleFormsetsMixin, CreateView):
    model = Sanctum
    form_class = SanctumForm
    template_name = "characters/mage/mage/chargen.html"
    potential_skip = [
        "allies",
    ]
    formsets = {
        "rz_form": RealityZonePracticeRatingFormSet,
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj_id = self.kwargs.get("pk")
        context["object"] = Human.objects.get(id=obj_id)
        # context["rz_form"] = RealityZonePracticeRatingForm()
        context["form"].fields["name"].initial = f"{context['object']}'s Sanctum"
        context["is_approved_user"] = self.check_if_special_user(
            context["object"], self.request.user
        )
        context["current_sanctum"] = self.current_sanctum
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        obj = context["object"]

        rz_data = self.get_form_data("rz_form")
        for res in rz_data:
            res["practice"] = Practice.objects.get(id=res["practice"])
            res["rating"] = int(res["rating"])
        total_rz = sum([x["rating"] for x in rz_data])
        total_positive = sum([x["rating"] for x in rz_data if x["rating"] > 0])
        if total_rz != 0:
            form.add_error(None, "Ratings must total 0")
            return super().form_invalid(form)
        if total_positive != self.current_sanctum.rating:
            form.add_error(None, "Positive Ratings must equal Sanctum rating")
            return super().form_invalid(form)

        rzone = RealityZone.objects.create(name="{obj.name} Reality Zone")
        obj.reality_zone = rzone
        obj.save()
        for rz in rz_data:
            ZoneRating.objects.create(
                zone=rzone, practice=rz["practice"], rating=rz["rating"]
            )

        s = form.save(obj, reality_zone=rzone)

        self.current_sanctum.note = s.name
        self.current_sanctum.url = s.get_absolute_url()
        self.current_sanctum.complete = True
        self.current_sanctum.save()
        if s:
            if (
                BackgroundRating.objects.filter(
                    char=obj,
                    bg=Background.objects.get(property_name="sanctum"),
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

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        obj = get_object_or_404(Human, pk=self.kwargs.get("pk"))
        self.current_sanctum = BackgroundRating.objects.filter(
            char=obj, bg=Background.objects.get(property_name="sanctum"), complete=False
        ).first()
        form.fields["name"].initial = self.current_sanctum.note
        form.fields["description"].widget.attrs.update(
            {"placeholder": "Enter description here"}
        )
        form.fields["parent"].queryset = LocationModel.objects.filter(
            chronicle=obj.chronicle
        )
        return form


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
