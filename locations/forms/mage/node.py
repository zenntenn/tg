from characters.models.core.meritflaw import MeritFlaw
from characters.models.mage.resonance import Resonance
from core.models import Number
from core.widgets import AutocompleteTextInput
from django import forms
from game.models import ObjectType
from locations.models.mage import Node
from locations.models.mage.node import NodeMeritFlawRating, NodeResonanceRating


class NodeForm(forms.ModelForm):
    class Meta:
        model = Node
        fields = (
            "name",
            "description",
            "ratio",
            "size",
            "quintessence_form",
            "tass_form",
        )


class NodeResonanceRatingForm(forms.ModelForm):
    class Meta:
        model = NodeResonanceRating
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


NodeResonancePracticeRatingFormSet = forms.inlineformset_factory(
    Node,
    NodeResonanceRating,
    form=NodeResonanceRatingForm,
    extra=1,
    can_delete=False,
)


class NodeMeritFlawForm(forms.ModelForm):
    class Meta:
        model = NodeMeritFlawRating
        fields = ["mf", "rating"]

    rating = forms.ModelChoiceField(queryset=Number.objects.none(), required=False)
    mf = forms.ModelChoiceField(queryset=MeritFlaw.objects.none())

    def __init__(self, *args, **kwargs):
        n = ObjectType.objects.get_or_create(name="node")[0]
        super().__init__(*args, **kwargs)
        self.fields["mf"].queryset = MeritFlaw.objects.filter(allowed_types__in=[n])


NodeMeritFlawFormSet = forms.inlineformset_factory(
    Node,
    NodeMeritFlawRating,
    form=NodeMeritFlawForm,
    extra=1,
    can_delete=False,
)
