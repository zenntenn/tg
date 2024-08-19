from collections import namedtuple
from typing import Any

from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, View
from items.models.mage.grimoire import Grimoire

EmptyRote = namedtuple("EmptyRote", ["name", "spheres"])
empty_rote = EmptyRote("", "")


class GrimoireDetailView(DetailView):
    model = Grimoire
    template_name = "items/mage/grimoire/detail.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["abilities"] = "<br>".join(
            [x.name for x in self.object.abilities.all()]
        )
        context["spheres"] = "<br>".join([x.name for x in self.object.spheres.all()])
        context["practices"] = "<br>".join(
            [
                f'<a href="{x.get_absolute_url()}">{x}</a>'
                for x in self.object.practices.all()
            ]
        )
        context["instruments"] = "<br>".join(
            [
                f'<a href="{x.get_absolute_url()}">{x}</a>'
                for x in self.object.instruments.all()
            ]
        )
        context["year"] = abs(self.object.date_written)
        all_effects = list(self.object.effects.all())
        row_length = 2
        all_effects = [
            all_effects[i : i + row_length]
            for i in range(0, len(all_effects), row_length)
        ]
        if len(all_effects) != 0:
            while len(all_effects[-1]) < row_length:
                all_effects[-1].append(empty_rote)
        context["effects"] = all_effects
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
