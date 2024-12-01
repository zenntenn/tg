from django import forms
from characters.models.core.ability_block import Ability
from characters.models.core.attribute_block import Attribute
from characters.models.core.merit_flaw_block import MeritFlaw
from core.models import Number
from game.models import ObjectType

CATEGORY_CHOICES = [
    ("-----", "-----"),
    ("Image", "Image"),
    ("Attribute", "Attribute"),
    ("Ability", "Ability"),
    ("New Background", "New Background"),
    ("Existing Background", "Existing Background"),
    ("Willpower", "Willpower"),
    ("MeritFlaw", "MeritFlaw"),
]

class XPForm(forms.Form):
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    example = forms.ModelChoiceField(queryset=Attribute.objects.none(), required=False)
    value = forms.ModelChoiceField(queryset=Number.objects.none(), required=False)
    note = forms.CharField(max_length=300, required=False)
    pooled = forms.BooleanField(required=False)
    image_field = forms.ImageField(required=False)
    
    def __init__(self, *args, **kwargs):
        self.character = kwargs.pop("character", None)
        super().__init__(*args, **kwargs)
        
        if not self.image_valid():
            self.fields["category"].choices = [x for x in self.fields["category"].choices if x[0] != "Image"]
        if not self.attribute_valid():
            self.fields["category"].choices = [x for x in self.fields["category"].choices if x[0] != "Attribute"]
        if not self.ability_valid():
            self.fields["category"].choices = [x for x in self.fields["category"].choices if x[0] != "Ability"]
        if not self.new_bg_valid():
            self.fields["category"].choices = [x for x in self.fields["category"].choices if x[0] != "New Background"]
        if not self.existing_bg_valid():
            self.fields["category"].choices = [x for x in self.fields["category"].choices if x[0] != "Existing Background"]
        if not self.willpower_valid():
            self.fields["category"].choices = [x for x in self.fields["category"].choices if x[0] != "Willpower"]
        if not self.mf_valid():
            self.fields["category"].choices = [x for x in self.fields["category"].choices if x[0] != "MeritFlaw"]

    def image_valid(self):
        if self.character.image and self.character.image.storage.exists(self.character.image.name):
            return False
        else:
            return True

    def attribute_valid(self):
        filtered_attributes = [
                attribute
                for attribute in Attribute.objects.all()
                if getattr(self.character, attribute.property_name) < 5
        ]
        filtered_for_xp_cost = [
                x for x in filtered_attributes if self.character.xp_cost(
                    "attribute",
                    getattr(self.character, x.property_name),
                ) <= self.character.xp
        ]
        return len(filtered_for_xp_cost) > 0

    def ability_valid(self):
        filtered_abilities = [
                ability
                for ability in Ability.objects.filter(property_name__in=self.character.talents + self.character.skills + self.character.knowledges)
                if getattr(self.character, ability.property_name) < 5
            ]
        filtered_for_xp_cost = [
                x for x in filtered_abilities if self.character.xp_cost(
                    "ability",
                    getattr(self.character, x.property_name),
                ) <= self.character.xp
            ]
        return len(filtered_for_xp_cost) > 0

    def new_bg_valid(self):
        return self.character.xp >= 5

    def existing_bg_valid(self):
        bgs = self.character.backgrounds.filter(rating__lt=5)
        filtered_for_xp_cost = [
                x for x in bgs if self.character.xp_cost(
                    "background",
                    x.rating,
                ) <= self.character.xp
            ]
        return len(filtered_for_xp_cost) > 0

    def willpower_valid(self):
        return self.character.xp_cost("willpower", self.character.willpower) <= self.character.xp

    def mf_valid(self):
        return self.character.xp >= 3
