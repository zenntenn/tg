from characters.models.mage.resonance import Resonance
from core.widgets import AutocompleteTextInput
from django import forms
from items.models.mage.wonder import Wonder, WonderResonanceRating


class WonderForm(forms.Form):
    # powers
    # quintessence <- 5xArete
    # rank <- rating on character sheet
    # background cost <- derived from type and rank
    # owned_by <- character
    # owner <- derived from character
    # chronicle <- derived from character
    WONDER_CHOICES = [
        ("charm", "Charm"),
        ("artifact", "Artifact"),
        ("talisman", "Talisman"),
    ]

    wonder_type = forms.ChoiceField(choices=WONDER_CHOICES, label="Wonder Type")
    name = forms.CharField(max_length=100, label="Name")
    description = forms.CharField(widget=forms.Textarea, label="Description")
    arete = forms.IntegerField(label="Arete")


class WonderResonanceRatingForm(forms.ModelForm):
    class Meta:
        model = WonderResonanceRating
        fields = ["resonance", "rating"]

    rating = forms.IntegerField(min_value=0, max_value=5, initial=0)
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


WonderResonancePracticeRatingFormSet = forms.inlineformset_factory(
    Wonder,
    WonderResonanceRating,
    form=WonderResonanceRatingForm,
    extra=1,
    can_delete=False,
)
