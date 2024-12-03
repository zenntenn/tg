from characters.models.core.attribute_block import Attribute
from characters.models.core.merit_flaw_block import MeritFlaw
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


class FreebiesForm(forms.Form):
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    example = forms.ModelChoiceField(queryset=Attribute.objects.none(), required=False)
    value = forms.ModelChoiceField(queryset=Number.objects.none(), required=False)
    note = forms.CharField(max_length=300, required=False)
    pooled = forms.BooleanField(required=False)

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
        self.fields["category"].choices = [
            x for x in self.fields["category"].choices if self.validator(x[0])
        ]

    def validator(self, trait_type):
        trait_type = trait_type.lower().split(" ")[-1]
        if not isinstance(self.instance.freebie_cost(trait_type), int):
            return True
        if self.instance.freebie_cost(trait_type) == 10000:
            return True
        if self.instance.freebie_cost(trait_type) <= self.instance.freebies:
            return True
        return False
