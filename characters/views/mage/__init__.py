from .cabal import CabalCreateView, CabalDetailView, CabalUpdateView
from .effect import EffectCreateView, EffectDetailView, EffectUpdateView
from .faction import MageFactionCreateView, MageFactionDetailView, MageFactionUpdateView
from .focus import (
    CorruptedPracticeCreateView,
    CorruptedPracticeDetailView,
    CorruptedPracticeUpdateView,
    GenericPracticeDetailView,
    InstrumentCreateView,
    InstrumentDetailView,
    InstrumentUpdateView,
    ParadigmCreateView,
    ParadigmDetailView,
    ParadigmUpdateView,
    PracticeCreateView,
    PracticeDetailView,
    PracticeUpdateView,
    SpecializedPracticeCreateView,
    SpecializedPracticeDetailView,
    SpecializedPracticeUpdateView,
    TenetCreateView,
    TenetDetailView,
    TenetUpdateView,
)
from .mage import (
    MageCreateView,
    MageDetailView,
    MageUpdateView,
    load_factions,
    load_mf_ratings,
    load_subfactions,
)
from .mtahuman import MtAHumanCreateView, MtAHumanDetailView, MtAHumanUpdateView
from .resonance import ResonanceCreateView, ResonanceDetailView, ResonanceUpdateView
from .rote import RoteCreateView, RoteDetailView, RoteUpdateView
