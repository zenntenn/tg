from characters.forms.mage.effect import EffectCreateOrSelectForm
from characters.models.core.background_block import Background
from characters.models.mage.effect import Effect
from django import forms
from locations.models.mage import Chantry
from locations.models.mage.chantry import ChantryBackgroundRating


class ChantryPointForm(forms.Form):
    INTEGRATED_EFFECTS_NUMBERS = {
        0: 0,
        1: 4,
        2: 8,
        3: 15,
        4: 20,
        5: 25,
        6: 35,
        7: 45,
        8: 55,
        9: 70,
        10: 90,
    }

    category = forms.ChoiceField(
        choices=[
            ("-----", "-----"),
            ("Integrated Effects", "Integrated Effects"),
            ("New Background", "New Background"),
            ("Existing Background", "Existing Background"),
        ]
    )
    example = forms.ModelChoiceField(queryset=Background.objects.none(), required=False)
    note = forms.CharField(max_length=300, required=False)
    display_alt_name = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        pk = kwargs.pop("pk")
        self.object = Chantry.objects.get(pk=pk)
        super().__init__(*args, **kwargs)
        if self.object.backgrounds.count() == 0:
            self.fields["category"].choices = [
                ("-----", "-----"),
                ("Integrated Effects", "Integrated Effects"),
                ("New Background", "New Background"),
            ]

        if self.object.integrated_effects_score == 10:
            self.fields["category"].choices = [
                x
                for x in self.fields["category"].choices
                if x[0] != "Integrated Effects"
            ]

        category = self.data.get("category")
        if category == "New Background":
            self.fields["example"].queryset = Background.objects.all()
        if category == "Existing Background":
            self.fields["example"].queryset = self.object.backgrounds.all()

    def is_valid(self):
        valid = super().is_valid()
        category = self.cleaned_data["category"]
        if category == "New Background":
            if self.cleaned_data["example"] is None:
                raise forms.ValidationError("Need to choose a Background")
        if category == "Existing Background":
            if self.cleaned_data["example"] is None:
                raise forms.ValidationError("Need to choose a Background")
        return valid

    def save(self, commit=True):
        category = self.cleaned_data["category"]
        if category == "Integrated Effects":
            self.object.integrated_effects_score += 1
            self.object.save()
        elif "New Background" == category:
            ChantryBackgroundRating.objects.create(
                bg=self.cleaned_data["example"],
                note=self.cleaned_data["note"],
                chantry=self.object,
                display_alt_name=self.cleaned_data["display_alt_name"],
                rating=1,
            )
        elif "Existing Background" == category:
            x = self.cleaned_data["example"]
            x.rating += 1
            x.save()
        else:
            pass


# Form for choosing effects
class ChantryEffectsForm(EffectCreateOrSelectForm):
    def __init__(self, *args, **kwargs):
        pk = kwargs.pop("pk")
        self.object = Chantry.objects.get(pk=pk)
        super().__init__(*args, **kwargs)
        q = Effect.objects.filter(max_sphere__lte=self.object.rank)
        q = q.exclude(pk__in=self.object.integrated_effects.all())
        q = q.exclude(rote_cost__gt=self.object.current_ie_points())
        self.fields["select"].queryset = q

    def save(self, commit=True):
        effect = super().save(commit=commit)
        self.object.integrated_effects.add(effect)
