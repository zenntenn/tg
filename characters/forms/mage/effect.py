from characters.models.mage.effect import Effect
from django import forms


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


EffectFormSet = forms.formset_factory(form=EffectForm, extra=1, can_delete=False)
