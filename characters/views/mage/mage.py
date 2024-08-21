from characters.models.mage.faction import MageFaction
from characters.models.mage.mage import Mage
from django.forms import formset_factory
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View


def load_factions(request):
    affiliation_id = request.GET.get("affiliation")
    factions = MageFaction.objects.filter(parent=affiliation_id).order_by("name")
    return render(
        request,
        "wod/characters/mage/mage/load_faction_dropdown_list.html",
        {"factions": factions},
    )


def load_subfactions(request):
    faction_id = request.GET.get("faction")
    subfactions = MageFaction.objects.filter(parent=faction_id).order_by("name")
    return render(
        request,
        "wod/characters/mage/mage/load_subfaction_dropdown_list.html",
        {"subfactions": subfactions},
    )


def load_mf_ratings(request):
    mf_id = request.GET.get("mf")
    ratings = MeritFlaw.objects.get(pk=mf_id).ratings
    return render(
        request,
        "wod/characters/mage/mage/load_mf_rating_dropdown_list.html",
        {"ratings": ratings},
    )


class MageCreateView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        context["form"] = MageCreationForm()
        return render(request, "wod/characters/mage/mage/create.html", context)

    def post(self, request, *args, **kwargs):
        if "Full Random" in request.POST:
            s = Mage.objects.create(owner=request.user, status="Un")
            s.random()
            return redirect(s.get_absolute_url())
        if "Random Basics" in request.POST:
            s = Mage.objects.create(owner=request.user, status="Un")
            s.random_name()
            s.random_concept()
            s.random_archetypes()
            s.random_essence()
            s.random_faction()
            s.save()
            return redirect(s.get_absolute_url())
        if "Save" in request.POST:
            form = MageCreationForm(request.POST)
            form.full_clean()
            affiliation = form.cleaned_data.get("affiliation")
            faction = form.cleaned_data.get("faction")
            subfaction = form.cleaned_data.get("subfaction")
            s = Mage.objects.create(
                name=form.data["name"],
                concept=form.data["concept"],
                demeanor=form.cleaned_data["demeanor"],
                nature=form.cleaned_data["nature"],
                owner=request.user,
                status="Un",
                chronicle=form.cleaned_data["chronicle"],
            )
            s.set_faction(affiliation, faction, subfaction=subfaction)
            return redirect(s.get_absolute_url())
        context = {}
        context["form"] = MageCreationForm()
        return render(request, "wod/characters/mage/mage/create.html", context)


class MageAbilitiesDetailView(BaseCharacterView):
    def get(self, request, *args, **kwargs):
        character = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(character)
        context["form"] = MageAbilitiesForm(character=character)
        return render(request, "wod/characters/mage/mage/2_abilities.html", context)

    def post(self, request, *args, **kwargs):
        character = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(character)
        form = MageAbilitiesForm(request.POST, character=character)
        if "Back" in form.data:
            character.prev_stage()
            return redirect(character.get_absolute_url())
        if "Random Abilities" in form.data:
            character.random_abilities()
            character.next_stage()
            return redirect(character.get_absolute_url())
        form.assign()
        if character.has_abilities():
            character.next_stage()
            return redirect(character.get_absolute_url())
        context["form"] = MageAbilitiesForm(character=character)
        return redirect(character.get_absolute_url())


class MageAdvantagesView(BaseCharacterView):
    def get(self, request, *args, **kwargs):
        character = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(character)
        context["form"] = MageAdvantagesForm(character=character)
        return render(request, "wod/characters/mage/mage/3_advantages.html", context)

    def post(self, request, *args, **kwargs):
        character = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(character)
        form = MageAdvantagesForm(request.POST, character=character)
        if "Back" in form.data:
            character.prev_stage()
            context["form"] = MageAbilitiesForm(character=character)
            return redirect(character.get_absolute_url())
        if "Random Advantages" in form.data:
            character.random_focus()
            character.random_backgrounds()
            character.random_arete()
            character.random_affinity_sphere()
            character.next_stage()
            context["resonances"] = Resonance.objects.all().order_by("name")
            context["form"] = MagePowersForm(character=character)
            return redirect(character.get_absolute_url())
        form.assign()
        if (
            character.has_backgrounds()
            and character.has_affinity_sphere()
            and character.has_focus()
        ):
            character.next_stage()
            context["resonances"] = Resonance.objects.all().order_by("name")
            context["form"] = MagePowersForm(character=character)
            return redirect(character.get_absolute_url())
        context["form"] = MageAdvantagesForm(character=character)
        return redirect(character.get_absolute_url())


class MagePowersView(BaseCharacterView):
    def get(self, request, *args, **kwargs):
        character = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(character)
        context["resonances"] = Resonance.objects.all().order_by("name")
        context["form"] = MagePowersForm(character=character)
        return render(
            request,
            "wod/characters/mage/mage/4_powers.html",
            context,
        )

    def post(self, request, *args, **kwargs):
        character = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(character)
        form = MagePowersForm(request.POST, character=character)
        if "Back" in form.data:
            character.prev_stage()
            context["form"] = MageAdvantagesForm(character=character)
            return redirect(character.get_absolute_url())
        if "Random Powers" in form.data:
            character.random_spheres()
            character.random_resonance()
            character.next_stage()
            MFFormset = formset_factory(MeritFlawForm, extra=1)
            context["formset"] = MFFormset(form_kwargs={"chartype": "mage"})
            context["form"] = MageFreebieForm(character=character)
            return redirect(character.get_absolute_url())
        form.assign()
        if character.has_spheres() and character.total_resonance() > 0:
            character.next_stage()
            MFFormset = formset_factory(MeritFlawForm, extra=1)
            context["formset"] = MFFormset(form_kwargs={"chartype": "mage"})
            context["form"] = MageFreebieForm(character=character)
            return redirect(character.get_absolute_url())
        context["resonances"] = Resonance.objects.all().order_by("name")
        context["form"] = MagePowersForm(character=character)
        return redirect(character.get_absolute_url())


class MageFreebiesView(BaseCharacterView):
    def get(self, request, *args, **kwargs):
        character = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(character)
        MFFormset = formset_factory(MeritFlawForm, extra=1)
        context["formset"] = MFFormset(form_kwargs={"chartype": "mage"})
        context["form"] = MageFreebieForm(character=character)
        return render(request, "wod/characters/mage/mage/5_freebies.html", context)

    def post(self, request, *args, **kwargs):
        character = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(character)
        form = MageFreebieForm(request.POST, character=character)
        if "Back" in form.data:
            character.prev_stage()
            context["resonances"] = Resonance.objects.all().order_by("name")
            context["form"] = MagePowersForm(character=character)
            return redirect(character.get_absolute_url())
        if "Random Freebies" in form.data:
            character.random_freebies()
            character.next_stage()
            context["form"] = MageDescriptionForm(character=character)
            return redirect(character.get_absolute_url())
        form.full_clean()
        if form.total_cost_freebies() == character.freebies:
            form.assign()
            character.next_stage()
            context["form"] = MageDescriptionForm(character=character)
            return redirect(character.get_absolute_url())
        MFFormset = formset_factory(MeritFlawForm, extra=1)
        context["formset"] = MFFormset(form_kwargs={"chartype": "mage"})
        context["form"] = MageFreebieForm(character=character)
        return redirect(character.get_absolute_url())


class MageDescriptionView(BaseCharacterView):
    def get(self, request, *args, **kwargs):
        character = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(character)
        context["form"] = MageDescriptionForm(character=character)
        return render(request, "wod/characters/mage/mage/6_description.html", context)

    def post(self, request, *args, **kwargs):
        character = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(character)
        form = MageDescriptionForm(request.POST, character=character)
        if "Back" in form.data:
            character.prev_stage()
            MFFormset = formset_factory(MeritFlawForm, extra=1)
            context["formset"] = MFFormset(form_kwargs={"chartype": "mage"})
            context["form"] = MageFreebieForm(character=character)
            return redirect(character.get_absolute_url())
        if "Random Description" in form.data:
            character.random_history()
            character.random_mage_history()
            character.random_finishing_touches()
            character.mf_based_corrections()
            character.next_stage()
            return redirect(character.get_absolute_url())
        form.full_clean()
        if form.complete():
            for key, value in form.cleaned_data.items():
                setattr(character, key, value)
            character.next_stage()
            return redirect(character.get_absolute_url())
        context["form"] = MageDescriptionForm(character=character)
        return redirect(character.get_absolute_url())


class MageSpecialtiesView(BaseCharacterView):
    def get(self, request, *args, **kwargs):
        character = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(character)
        context["form"] = MageSpecialtiesForm(character=character)
        return render(request, "wod/characters/mage/mage/7_specialties.html", context)

    def post(self, request, *args, **kwargs):
        character = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(character)
        form = MageSpecialtiesForm(request.POST, character=character)
        if "Back" in form.data:
            character.prev_stage()
            context["form"] = MageDescriptionForm(character=character)
            return redirect(character.get_absolute_url())
        if "Random Specialties" in form.data:
            character.random_specialties()
            character.update_status("Sub")
            character.next_stage()
            return redirect(character.get_absolute_url())
        form.full_clean()
        if form.complete():
            for stat, spec_name in form.cleaned_data.items():
                spec, _ = WoDSpecialty.objects.get_or_create(stat=stat, name=spec_name)
                character.add_specialty(spec)
            character.next_stage()
            character.update_status("Sub")
            return redirect(character.get_absolute_url())
        context["form"] = MageSpecialtiesForm(character=character)
        return redirect(character.get_absolute_url())


class MageDetailView(BaseCharacterView):
    stage_views = {
        1: AttributeDetailView,
        2: MageAbilitiesDetailView,
        3: MageAdvantagesView,
        4: MagePowersView,
        5: MageFreebiesView,
        6: MageDescriptionView,
        7: MageSpecialtiesView,
    }

    def get(self, request, *args, **kwargs):
        char = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(char)
        if char.status != "Un":
            return render(
                request,
                "wod/characters/mage/mage/detail.html",
                context,
            )
        if char.creation_status in self.stage_views.keys():
            return self.stage_views[char.creation_status].as_view()(
                request, *args, **kwargs
            )
        return render(
            request,
            "wod/characters/mage/mage/detail.html",
            context,
        )

    def post(self, request, *args, **kwargs):
        char = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(char)
        if char.creation_status in self.stage_views.keys():
            return self.stage_views[char.creation_status].as_view()(
                request, *args, **kwargs
            )
        return render(
            request,
            "wod/characters/mage/mage/detail.html",
            context,
        )

    def get_context(self, character):
        context = super().get_context(character)
        context["resonance"] = ResRating.objects.filter(
            mage=character, rating__gte=1
        ).order_by("resonance__name")
        all_effects = list(Rote.objects.filter(mage=context["object"]))
        row_length = 2
        all_effects = [
            all_effects[i : i + row_length]
            for i in range(0, len(all_effects), row_length)
        ]
        context["rotes"] = all_effects
        return context


class MageUpdateView(UpdateView):
    model = Mage
    fields = "__all__"
    template_name = "wod/characters/mage/mage/form.html"
