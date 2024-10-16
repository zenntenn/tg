from characters.models.core.merit_flaw_block import MeritFlaw
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
            "parent",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["parent"].required = False


class NodeResonanceRatingForm(forms.ModelForm):
    class Meta:
        model = NodeResonanceRating
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


class BaseNodeResonanceRatingFormSet(forms.BaseInlineFormSet):
    def __init__(self, *args, suggestions=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.suggestions = suggestions or [
            x.name.title() for x in Resonance.objects.order_by("name")
        ]

    def _construct_form(self, i, **kwargs):
        # Pass suggestions to each form
        kwargs["suggestions"] = self.suggestions
        return super()._construct_form(i, **kwargs)


NodeResonancePracticeRatingFormSet = forms.inlineformset_factory(
    Node,
    NodeResonanceRating,
    form=NodeResonanceRatingForm,
    formset=BaseNodeResonanceRatingFormSet,
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
