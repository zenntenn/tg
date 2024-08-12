from characters.models.core import MeritFlaw
from django.shortcuts import redirect, render
from django.views.generic import CreateView, UpdateView, View


# Create your views here.
class MeritFlawDetailView(View):
    def get(self, request, *args, **kwargs):
        mf = MeritFlaw.objects.get(pk=kwargs["pk"])
        context = self.get_context(mf)
        return render(request, "characters/core/meritflaw/detail.html", context)

    def get_context(self, mf):
        context = {}
        context["object"] = mf
        mf_ratings = list(mf.ratings.values_list("value", flat=True))
        mf_ratings.sort()
        context["ratings"] = ", ".join([str(x) for x in mf_ratings])
        return context


class MeritFlawCreateView(CreateView):
    model = MeritFlaw
    fields = ["name", "description", "ratings", "allowed_types"]
    template_name = "characters/core/meritflaw/form.html"


class MeritFlawUpdateView(UpdateView):
    model = MeritFlaw
    fields = ["name", "description", "ratings", "allowed_types"]
    template_name = "characters/core/meritflaw/form.html"
