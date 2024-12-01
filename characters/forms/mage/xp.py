from characters.models.core.ability_block import Ability
from characters.models.mage.focus import Practice
from characters.models.mage.resonance import Resonance
from characters.models.mage.sphere import Sphere
from core.widgets import AutocompleteTextInput
from django import forms

from characters.forms.core.xp import CATEGORY_CHOICES, XPForm

CATEGORY_CHOICES = CATEGORY_CHOICES + [
    ("Sphere", "Sphere"),
    ("Rote Points", "Rote Points"),
    ("Resonance", "Resonance"),
    ("Tenet", "Tenet"),
    ("Remove Tenet", "Remove Tenet"),
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
        if not self.spheres_valid():
            self.fields["category"].choices = [x for x in self.fields["category"].choices if x[0] != "Sphere"]
        if not self.rote_points_valid():
            self.fields["category"].choices = [x for x in self.fields["category"].choices if x[0] != "Rote Points"]
        if not self.resonance_valid():
            self.fields["category"].choices = [x for x in self.fields["category"].choices if x[0] != "Resonance"]
        if not self.add_tenet_valid():
            self.fields["category"].choices = [x for x in self.fields["category"].choices if x[0] != "Tenet"]
        if not self.remove_tenet_valid():
            self.fields["category"].choices = [x for x in self.fields["category"].choices if x[0] != "Remove Tenet"]
        if not self.practice_valid():
            self.fields["category"].choices = [x for x in self.fields["category"].choices if x[0] != "Practice"]
        if not self.arete_valid():
            self.fields["category"].choices = [x for x in self.fields["category"].choices if x[0] != "Arete"]
        if not self.rote_valid():
            self.fields["category"].choices = [x for x in self.fields["category"].choices if x[0] != "Rote"]
        
    def spheres_valid(self):
        filtered_spheres = [
                sphere
                for sphere in Sphere.objects.all()
                if getattr(self.character, sphere.property_name) < self.character.arete
            ]
        filtered_for_xp_cost = [
                x for x in filtered_spheres if self.character.xp_cost(
                    self.character.sphere_to_trait_type(x.property_name),
                    getattr(self.character, x.property_name),
                ) <= self.character.xp
            ]
        return len(filtered_for_xp_cost) > 0
    
    def rote_points_valid(self):
        return True
    
    def resonance_valid(self):
        return True
    
    def add_tenet_valid(self):
        return True
    
    def remove_tenet_valid(self):
        return True
    
    def practice_valid(self):
        return True
    
    def arete_valid(self):
        return self.character.xp_cost("arete", self.character.arete) <= self.character.xp
    
    def rote_valid(self):
        return self.character.rote_points > 0
    
