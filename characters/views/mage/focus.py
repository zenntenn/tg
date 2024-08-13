from characters.models.mage.focus import (
    CorruptedPractice,
    Instrument,
    Paradigm,
    Practice,
    SpecializedPractice,
    Tenet,
)
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView


class InstrumentDetailView(DetailView):
    model = Instrument
    template_name = "characters/mage/instrument/detail.html"


class InstrumentCreateView(CreateView):
    model = Instrument
    fields = ["name", "description"]
    template_name = "characters/mage/instrument/form.html"


class InstrumentUpdateView(UpdateView):
    model = Instrument
    fields = ["name", "description"]
    template_name = "characters/mage/instrument/form.html"


class ParadigmDetailView(DetailView):
    model = Paradigm
    template_name = "characters/mage/paradigm/detail.html"


class ParadigmCreateView(CreateView):
    model = Paradigm
    fields = ["name", "tenets", "description"]
    template_name = "characters/mage/paradigm/form.html"


class ParadigmUpdateView(UpdateView):
    model = Paradigm
    fields = ["name", "tenets", "description"]
    template_name = "characters/mage/paradigm/form.html"


class PracticeDetailView(DetailView):
    model = Practice
    template_name = "characters/mage/practice/detail.html"


class PracticeCreateView(CreateView):
    model = Practice
    fields = [
        "name",
        "abilities",
        "instruments",
        "common_resonance_traits",
        "benefit",
        "penalty",
        "description",
    ]
    template_name = "characters/mage/practice/form.html"


class PracticeUpdateView(UpdateView):
    model = Practice
    fields = [
        "name",
        "abilities",
        "instruments",
        "common_resonance_traits",
        "benefit",
        "penalty",
        "description",
    ]
    template_name = "characters/mage/practice/form.html"


class CorruptedPracticeDetailView(DetailView):
    model = CorruptedPractice
    template_name = "characters/mage/corrupted_practice/detail.html"


class CorruptedPracticeCreateView(CreateView):
    model = CorruptedPractice
    fields = [
        "name",
        "abilities",
        "instruments",
        "common_resonance_traits",
        "benefit",
        "penalty",
        "extra_benefit",
        "price",
        "description",
    ]
    template_name = "characters/mage/corrupted_practice/form.html"


class CorruptedPracticeUpdateView(UpdateView):
    model = CorruptedPractice
    fields = [
        "name",
        "abilities",
        "instruments",
        "common_resonance_traits",
        "benefit",
        "penalty",
        "extra_benefit",
        "price",
        "description",
    ]
    template_name = "characters/mage/corrupted_practice/form.html"


class SpecializedPracticeDetailView(DetailView):
    model = SpecializedPractice
    template_name = "characters/mage/specialized_practice/detail.html"


class SpecializedPracticeCreateView(CreateView):
    model = SpecializedPractice
    fields = [
        "name",
        "abilities",
        "instruments",
        "common_resonance_traits",
        "benefit",
        "penalty",
        "extra_benefit",
        "description",
    ]
    template_name = "characters/mage/specialized_practice/form.html"


class SpecializedPracticeUpdateView(UpdateView):
    model = SpecializedPractice
    fields = [
        "name",
        "abilities",
        "instruments",
        "common_resonance_traits",
        "benefit",
        "penalty",
        "extra_benefit",
        "description",
    ]
    template_name = "characters/mage/specialized_practice/form.html"


class TenetDetailView(DetailView):
    model = Tenet
    template_name = "characters/mage/tenet/detail.html"


class TenetCreateView(CreateView):
    model = Tenet
    fields = [
        "name",
        "tenet_type",
        "associated_practices",
        "limited_practices",
        "description",
    ]
    template_name = "characters/mage/tenet/form.html"


class TenetUpdateView(UpdateView):
    model = Tenet
    fields = [
        "name",
        "tenet_type",
        "associated_practices",
        "limited_practices",
        "description",
    ]
    template_name = "characters/mage/tenet/form.html"


class GenericPracticeDetailView(View):
    practice_views = {
        "practice": PracticeDetailView,
        "specialized_practice": SpecializedPracticeDetailView,
        "corrupted_practice": CorruptedPracticeDetailView,
    }

    def get(self, request, *args, **kwargs):
        p = Practice.objects.get(pk=kwargs["pk"])
        if p.type in self.practice_views:
            return self.practice_views[p.type].as_view()(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        p = Practice.objects.get(pk=kwargs["pk"])
        if p.type in self.practice_views:
            return self.practice_views[p.type].as_view()(request, *args, **kwargs)
