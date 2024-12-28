from characters.models.mage.faction import MageFaction
from characters.models.mage.mage import Mage
from django import forms


class MageCreationForm(forms.ModelForm):
    class Meta:
        model = Mage
        fields = [
            "name",
            "nature",
            "demeanor",
            "concept",
            "affiliation",
            "faction",
            "subfaction",
            "essence",
            "chronicle",
            "image",
            "npc",
        ]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super().__init__(*args, **kwargs)

        self.fields["affiliation"].queryset = MageFaction.objects.filter(parent=None)
        self.fields["faction"].queryset = MageFaction.objects.none()
        self.fields["subfaction"].queryset = MageFaction.objects.none()
        self.fields["name"].widget.attrs.update({"placeholder": "Enter name here"})
        self.fields["concept"].widget.attrs.update(
            {"placeholder": "Enter concept here"}
        )
        self.fields["image"].required = False
        if self.user is not None:
            if not self.user.profile.is_st():
                self.fields["affiliation"].queryset = self.fields[
                    "affiliation"
                ].queryset.exclude(name__in=["Nephandi", "Marauders"])

        if self.is_bound:
            self.fields["faction"].queryset = MageFaction.objects.all()
            self.fields["subfaction"].queryset = MageFaction.objects.all()

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:  # If we have a user
            instance.owner = self.user
        if commit:
            instance.save()
        return instance
