from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, View
from items.models.mage import WonderResonanceRating
from items.models.mage.artifact import Artifact


class ArtifactDetailView(View):
    def get(self, request, *args, **kwargs):
        artifact = Artifact.objects.get(pk=kwargs["pk"])
        context = self.get_context(artifact)
        return render(request, "items/mage/artifact/detail.html", context)

    def get_context(self, artifact):
        return {
            "object": artifact,
            "resonance": WonderResonanceRating.objects.filter(wonder=artifact).order_by(
                "resonance__name"
            ),
        }


class ArtifactCreateView(CreateView):
    model = Artifact
    fields = [
        "name",
        "rank",
        "background_cost",
        "quintessence_max",
        "description",
        "power",
    ]
    template_name = "items/mage/artifact/form.html"


class ArtifactUpdateView(UpdateView):
    model = Artifact
    fields = [
        "name",
        "rank",
        "background_cost",
        "quintessence_max",
        "description",
        "power",
    ]
    template_name = "items/mage/artifact/form.html"
