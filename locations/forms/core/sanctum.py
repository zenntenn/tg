from django import forms
from locations.models.core.location import LocationModel
from locations.models.mage.sanctum import Sanctum


class SanctumForm(forms.Form):
    name = forms.CharField(max_length=100)
    parent = forms.ModelChoiceField(queryset=LocationModel.objects.none())
    description = forms.CharField(widget=forms.Textarea)

    def save(self, mage, reality_zone=None):
        name = self.cleaned_data.get("name", "")
        description = self.cleaned_data.get("description", "")
        parent = self.cleaned_data.get("parent", None)
        s = Sanctum.objects.create(
            name=name,
            description=description,
            owned_by=mage,
            chronicle=mage.chronicle,
            parent=parent,
            owner=mage.owner,
            status="Sub",
        )
        if reality_zone is not None:
            s.reality_zone = reality_zone
            s.save()
        return True

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop("instance", None)
        super().__init__(*args, **kwargs)
