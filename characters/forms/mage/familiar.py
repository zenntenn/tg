from characters.models.core.archetype import Archetype
from characters.models.mage.companion import Companion
from characters.models.mage.faction import MageFaction
from django import forms


class FamiliarForm(forms.ModelForm):
    class Meta:
        model = Companion
        fields = [
            "name",
            "nature",
            "demeanor",
            "affiliation",
            "concept",
            "subfaction",
            "faction",
            "image",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nature"].queryset = Archetype.objects.all().order_by("name")
        self.fields["demeanor"].queryset = Archetype.objects.all().order_by("name")
        self.fields["affiliation"].queryset = MageFaction.objects.filter(parent=None)
        self.fields["faction"].queryset = MageFaction.objects.none()
        self.fields["subfaction"].queryset = MageFaction.objects.none()
        self.fields["name"].widget.attrs.update({"placeholder": "Enter name here"})
        self.fields["concept"].widget.attrs.update(
            {"placeholder": "Enter concept here"}
        )
        self.fields["image"].required = False