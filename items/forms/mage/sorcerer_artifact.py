from characters.models.mage.resonance import Resonance
from core.widgets import AutocompleteTextInput
from django import forms
from items.models.mage import SorcererArtifact


class SorcererArtifactForm(forms.Form):
    select_or_create_artifact = forms.BooleanField(required=False)
    artifact_options = forms.ModelChoiceField(
        queryset=SorcererArtifact.objects.all(), required=False
    )
    name = forms.CharField(max_length=100, label="Name", required=False)
    description = forms.CharField(
        widget=forms.Textarea, label="Description", required=False
    )

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop("instance", None)
        self.rank = kwargs.pop("rank", 0)
        super().__init__(*args, **kwargs)
        self.fields["artifact_options"].queryset = SorcererArtifact.objects.filter(
            rank=self.rank
        )
