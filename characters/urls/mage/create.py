from characters import views
from django.urls import path

# Create your URLs here
app_name = "mage:create"
urls = [
    path(
        "effect/",
        views.mage.EffectCreateView.as_view(),
        name="effect",
    ),
    path(
        "resonance/",
        views.mage.ResonanceCreateView.as_view(),
        name="resonance",
    ),
    path(
        "instruments/",
        views.mage.InstrumentCreateView.as_view(),
        name="instrument",
    ),
    path(
        "paradigms/",
        views.mage.ParadigmCreateView.as_view(),
        name="paradigm",
    ),
    path(
        "practices/",
        views.mage.PracticeCreateView.as_view(),
        name="practice",
    ),
    path(
        "specialized_practices/",
        views.mage.SpecializedPracticeCreateView.as_view(),
        name="specialized_practice",
    ),
    path(
        "corrupted_practices/",
        views.mage.CorruptedPracticeCreateView.as_view(),
        name="corrupted_practice",
    ),
    path(
        "tenet/",
        views.mage.TenetCreateView.as_view(),
        name="tenet",
    ),
    path(
        "magefaction/",
        views.mage.MageFactionCreateView.as_view(),
        name="magefaction",
    ),
    path(
        "rotes/",
        views.mage.RoteCreateView.as_view(),
        name="rote",
    ),
]
