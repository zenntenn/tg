from collections import namedtuple

from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, View
from items.models.mage.grimoire import Grimoire

EmptyRote = namedtuple("EmptyRote", ["name", "spheres"])
empty_rote = EmptyRote("", "")


class GrimoireDetailView(View):
    def get(self, request, *args, **kwargs):
        grimoire = Grimoire.objects.get(pk=kwargs["pk"])
        context = self.get_context(grimoire)
        return render(request, "items/mage/grimoire/detail.html", context)

    def get_context(self, grimoire):
        if grimoire.faction is not None:
            if grimoire.faction.parent is not None:
                if grimoire.faction.parent.parent is not None:
                    s = f"{grimoire.faction.parent} ({grimoire.faction})"
                else:
                    s = f"{grimoire.faction}"
            else:
                s = ""
        else:
            s = ""
        context = {
            "object": grimoire,
            "abilities": "<br>".join([x.name for x in grimoire.abilities.all()]),
            "spheres": "<br>".join([x.name for x in grimoire.spheres.all()]),
            "effects": "<br>".join([str(x) for x in grimoire.effects.all()]),
            "date_written": grimoire.date_written,
            "faction": s,
        }
        context["paradigms"] = "<br>".join(
            [
                f'<a href="{x.get_absolute_url()}">{x}</a>'
                for x in grimoire.paradigms.all()
            ]
        )
        context["practices"] = "<br>".join(
            [
                f'<a href="{x.get_absolute_url()}">{x}</a>'
                for x in grimoire.practices.all()
            ]
        )
        context["instruments"] = "<br>".join(
            [
                f'<a href="{x.get_absolute_url()}">{x}</a>'
                for x in grimoire.instruments.all()
            ]
        )
        all_effects = list(context["object"].effects.all())
        row_length = 2
        all_effects = [
            all_effects[i : i + row_length]
            for i in range(0, len(all_effects), row_length)
        ]
        if len(all_effects) != 0:
            while len(all_effects[-1]) < row_length:
                all_effects[-1].append(empty_rote)
        context["effects"] = all_effects
        context["year"] = abs(grimoire.date_written)
        return context


class GrimoireCreateView(CreateView):
    model = Grimoire
    fields = [
        "name",
        "description",
        "abilities",
        "spheres",
        "date_written",
        "faction",
        "paradigms",
        "practices",
        "instruments",
        "is_primer",
        "language",
        "length",
        "cover_material",
        "inner_material",
        "medium",
        "effects",
    ]
    template_name = "items/mage/grimoire/form.html"


class GrimoireUpdateView(UpdateView):
    model = Grimoire
    fields = [
        "name",
        "description",
        "abilities",
        "spheres",
        "date_written",
        "faction",
        "paradigms",
        "practices",
        "instruments",
        "is_primer",
        "language",
        "length",
        "cover_material",
        "inner_material",
        "medium",
        "effects",
    ]
    template_name = "items/mage/grimoire/form.html"
