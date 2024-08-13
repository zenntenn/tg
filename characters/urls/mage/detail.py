from characters import views
from django.urls import path

# Create your URLs here
app_name = "mage:detail"
urls = [
    path(
        "effect/<pk>/",
        views.mage.EffectDetailView.as_view(),
        name="effect",
    ),
    path(
        "resonances/<pk>/",
        views.mage.ResonanceDetailView.as_view(),
        name="resonance",
    ),
    path(
        "instruments/<pk>/",
        views.mage.InstrumentDetailView.as_view(),
        name="instrument",
    ),
    path(
        "paradigms/<pk>/",
        views.mage.ParadigmDetailView.as_view(),
        name="paradigm",
    ),
    path(
        "practices/<pk>/",
        views.mage.GenericPracticeDetailView.as_view(),
        name="practice",
    ),
    path(
        "tenet/<pk>/",
        views.mage.TenetDetailView.as_view(),
        name="tenet",
    ),
]
