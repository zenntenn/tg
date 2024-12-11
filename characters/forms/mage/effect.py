from characters.models.mage.effect import Effect
from django import forms
from django.forms import modelformset_factory


class EffectForm(forms.ModelForm):
    class Meta:
        model = Effect
        fields = [
            "name",
            "description",
            "correspondence",
            "time",
            "spirit",
            "matter",
            "life",
            "forces",
            "entropy",
            "mind",
            "prime",
        ]


EffectFormSet = modelformset_factory(Effect, form=EffectForm, extra=1, can_delete=False)


class EffectCreateOrSelectForm(forms.ModelForm):
    select_or_create = forms.BooleanField(required=False)
    select = forms.ModelChoiceField(queryset=Effect.objects.all(), required=False)

    class Meta:
        model = Effect
        fields = [
            "select_or_create",
            "select",
            "name",
            "description",
            "correspondence",
            "time",
            "spirit",
            "matter",
            "life",
            "forces",
            "entropy",
            "mind",
            "prime",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].required = False

    def clean(self):
        cleaned_data = super().clean()
        select_or_create = cleaned_data.get("select_or_create")
        select = cleaned_data.get("select")

        # If not creating a new one, user must have selected an existing effect.
        if not select_or_create and not select:
            self.add_error(
                "select",
                "You must either select an existing effect or choose to create a new one.",
            )
        return cleaned_data

    def save(self, commit=True):
        """
        Custom save logic:
        - If select_or_create is False and an existing effect is chosen, return that existing effect.
        - Otherwise, create a new effect using the provided fields.
        """
        select_or_create = self.cleaned_data.get("select_or_create")
        select = self.cleaned_data.get("select")

        if not select_or_create and select:
            # User chose an existing effect
            # Return the existing effect without creating a new one.
            return select

        # Otherwise, create a new effect by calling the super save method
        # Note: This will create a new Effect instance with the data from the form
        return super().save(commit=commit)

    def cost(self):
        cleaned_data = super().clean()
        if cleaned_data.get("select"):
            return cleaned_data.get("select").cost()
        return (
            cleaned_data.get("correspondence", 0)
            + cleaned_data.get("time", 0)
            + cleaned_data.get("spirit", 0)
            + cleaned_data.get("matter", 0)
            + cleaned_data.get("life", 0)
            + cleaned_data.get("forces", 0)
            + cleaned_data.get("entropy", 0)
            + cleaned_data.get("mind", 0)
            + cleaned_data.get("prime", 0)
        )


EffectCreateOrSelectFormSet = modelformset_factory(
    Effect, form=EffectCreateOrSelectForm, extra=1, can_delete=False
)
