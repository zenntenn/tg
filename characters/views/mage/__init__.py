from .cabal import CabalCreateView, CabalDetailView, CabalUpdateView
from .effect import EffectCreateView, EffectDetailView, EffectListView, EffectUpdateView
from .faction import (
    MageFactionCreateView,
    MageFactionDetailView,
    MageFactionListView,
    MageFactionUpdateView,
)
from .focus import (
    CorruptedPracticeCreateView,
    CorruptedPracticeDetailView,
    CorruptedPracticeUpdateView,
    GenericPracticeDetailView,
    InstrumentCreateView,
    InstrumentDetailView,
    InstrumentListView,
    InstrumentUpdateView,
    ParadigmCreateView,
    ParadigmDetailView,
    ParadigmListView,
    ParadigmUpdateView,
    PracticeCreateView,
    PracticeDetailView,
    PracticeListView,
    PracticeUpdateView,
    SpecializedPracticeCreateView,
    SpecializedPracticeDetailView,
    SpecializedPracticeUpdateView,
    TenetCreateView,
    TenetDetailView,
    TenetListView,
    TenetUpdateView,
)
from .mage import (
    MageBasicsView,
    MageCharacterCreationView,
    MageCreateView,
    MageDetailView,
    MageUpdateView,
    load_factions,
    load_mf_ratings,
    load_subfactions,
)
from .mtahuman import (
    MtAHumanAbilityView,
    MtAHumanCreateView,
    MtAHumanDetailView,
    MtAHumanUpdateView,
)
from .resonance import (
    ResonanceCreateView,
    ResonanceDetailView,
    ResonanceListView,
    ResonanceUpdateView,
)
from .rote import RoteCreateView, RoteDetailView, RoteListView, RoteUpdateView
