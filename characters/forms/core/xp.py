from django import forms
from characters.models.core.attribute_block import Attribute
from core.models import Number

CATEGORY_CHOICES = [
    ("-----", "-----"),
    ("Image", "Image"),
    ("Attribute", "Attribute"),
    ("New Ability", "New Ability"),
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
