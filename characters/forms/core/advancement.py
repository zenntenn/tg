from characters.models.core.attribute import Attribute
from characters.models.core.meritflaw import MeritFlaw
from core.models import Number
from django import forms

CATEGORY_CHOICES = [
    ("-----", "-----"),
    ("Attribute", "Attribute"),
    ("Ability", "Ability"),
    ("Background", "Background"),
    ("Willpower", "Willpower"),
    ("MeritFlaw", "MeritFlaw"),
]


class AdvancementForm(forms.Form):
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    example = forms.ModelChoiceField(queryset=Attribute.objects.none(), required=False)
    value = forms.ModelChoiceField(queryset=Number.objects.none(), required=False)

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop("instance", None)
        super().__init__(*args, **kwargs)
