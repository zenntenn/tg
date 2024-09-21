from characters.forms.core.advancement import CATEGORY_CHOICES, AdvancementForm
from characters.models.mage.resonance import Resonance
from core.widgets import AutocompleteTextInput
from django import forms

CATEGORY_CHOICES = CATEGORY_CHOICES + [
    ("Sphere", "Sphere"),
    ("Rotes", "Rotes"),
    ("Resonance", "Resonance"),
    ("Tenet", "Tenet"),
    ("Practice", "Practice"),
    ("Arete", "Arete"),
    ("Quintessence", "Quintessence"),
]


class MageAdvancementForm(AdvancementForm):
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    resonance = forms.CharField(
        required=False, widget=AutocompleteTextInput(suggestions=[])
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["resonance"].widget.attrs.update(
            {
                "suggestions": [
                    x.name.title() for x in Resonance.objects.order_by("name")
                ],
            }
        )
        ADDITIONAL_CATS = [
            ("Sphere", "Sphere"),
            ("Rotes", "Rotes"),
            ("Resonance", "Resonance"),
            ("Tenet", "Tenet"),
            ("Practice", "Practice"),
            ("Arete", "Arete"),
            ("Quintessence", "Quintessence"),
        ]
        if self.instance.freebies < 4:
            ADDITIONAL_CATS = [x for x in ADDITIONAL_CATS if x[0] != "Arete"]
        if self.instance.freebies < 7:
            ADDITIONAL_CATS = [x for x in ADDITIONAL_CATS if x[0] != "Sphere"]
        if self.instance.freebies < 3:
            ADDITIONAL_CATS = [x for x in ADDITIONAL_CATS if x[0] != "Resonance"]
        self.fields["category"].choices += ADDITIONAL_CATS

    def save(self, *args, **kwargs):
        return self.instance
