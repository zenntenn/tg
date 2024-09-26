from characters.models.core.attribute import Attribute
from characters.models.core.meritflaw import MeritFlaw
from core.models import Number
from django import forms

CATEGORY_CHOICES = [
    ("-----", "-----"),
    ("Attribute", "Attribute"),
    ("Ability", "Ability"),
    ("New Background", "New Background"),
    ("Existing Background", "Existing Background"),
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
        CATEGORY_CHOICES = [
            ("-----", "-----"),
            ("Attribute", "Attribute"),
            ("Ability", "Ability"),
            ("New Background", "New Background"),
            ("Existing Background", "Existing Background"),
            ("Willpower", "Willpower"),
            ("MeritFlaw", "MeritFlaw"),
        ]
        if self.instance.freebies < 5:
            CATEGORY_CHOICES = [x for x in CATEGORY_CHOICES if x[0] != "Attribute"]
        if self.instance.freebies < 2:
            CATEGORY_CHOICES = [x for x in CATEGORY_CHOICES if x[0] != "Ability"]
        self.fields["category"].choices = CATEGORY_CHOICES
