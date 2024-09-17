from characters.models.mage.resonance import Resonance
from core.widgets import AutocompleteTextInput
from django import forms
from items.models.mage.wonder import Wonder, WonderResonanceRating


class WonderForm(forms.Form):
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

    def __init__(self, *args, suggestions=None, **kwargs):
        super().__init__(*args, **kwargs)
        if suggestions is None:
            suggestions = [x.name.title() for x in Resonance.objects.order_by("name")]
        self.fields["resonance"].widget.suggestions = suggestions


class BaseWonderResonanceRatingFormSet(forms.BaseInlineFormSet):
    def __init__(self, *args, suggestions=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.suggestions = suggestions or [
            x.name.title() for x in Resonance.objects.order_by("name")
        ]

    def _construct_form(self, i, **kwargs):
        # Pass suggestions to each form
        kwargs["suggestions"] = self.suggestions
        return super()._construct_form(i, **kwargs)


WonderResonancePracticeRatingFormSet = forms.inlineformset_factory(
    Wonder,
    WonderResonanceRating,
    form=WonderResonanceRatingForm,
    formset=BaseWonderResonanceRatingFormSet,
    extra=1,
    can_delete=False,
)
