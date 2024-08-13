from characters.models.mage.faction import MageFaction
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, View


class MageFactionDetailView(View):
    def get(self, request, *args, **kwargs):
        magefaction = MageFaction.objects.get(pk=kwargs["pk"])
        context = self.get_context(magefaction)
        return render(request, "characters/mage/magefaction/detail.html", context)

    def get_context(self, magefaction):
        context = {}
        context["object"] = magefaction
        context["languages"] = ", ".join([str(x) for x in magefaction.languages.all()])
        context["affinities"] = ", ".join([x.title() for x in magefaction.affinities])
        context["paradigms"] = ", ".join(
            [
                f'<a href="{x.get_absolute_url()}">{x}</a>'
                for x in magefaction.paradigms.all()
            ]
        )
        context["practices"] = ", ".join(
            [
                f'<a href="{x.get_absolute_url()}">{x}</a>'
                for x in magefaction.practices.all()
            ]
        )
        context["media"] = ", ".join(
            [
                f'<a href="{x.get_absolute_url()}">{x}</a>'
                for x in magefaction.media.all()
            ]
        )
        context["materials"] = ", ".join(
            [
                f'<a href="{x.get_absolute_url()}">{x}</a>'
                for x in magefaction.materials.all()
            ]
        )
        context["year"] = abs(magefaction.founded)
        context["subfactions"] = ", ".join(
            [
                f'<a href="{x.get_absolute_url()}">{x}</a>'
                for x in MageFaction.objects.filter(parent=magefaction)
            ]
        )
        return context


class MageFactionCreateView(CreateView):
    model = MageFaction
    fields = "__all__"
    template_name = "characters/mage/faction/form.html"


class MageFactionUpdateView(UpdateView):
    model = MageFaction
    fields = "__all__"
    template_name = "characters/mage/faction/form.html"
