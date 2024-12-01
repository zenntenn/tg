from characters.models.core.ability_block import Ability
from characters.models.mage.focus import Practice
from characters.models.mage.resonance import Resonance
from core.widgets import AutocompleteTextInput
from django import forms

from characters.forms.core.xp import CATEGORY_CHOICES, XPForm

CATEGORY_CHOICES = CATEGORY_CHOICES + [
    ("New Sphere", "New Sphere"),
    ("Sphere", "Sphere"),
    ("Affinity Sphere", "Affinity Sphere"),
    ("Rote Points", "Rote Points"),
    ("Resonance", "Resonance"),
    ("Tenet", "Tenet"),
    ("Remove Tenet", "Remove Tenet"),
    ("New Practice", "New Practice"),
    ("Practice", "Practice"),
    ("Arete", "Arete"),
    ("Rote", "Rote"),
]

class MageXPForm(XPForm):
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    resonance = forms.CharField(
        required=False, widget=AutocompleteTextInput(suggestions=[])
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        