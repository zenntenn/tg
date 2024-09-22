from characters.models.mage.focus import Practice
from django import forms
from django.forms import inlineformset_factory
from locations.models.mage.reality_zone import RealityZone, ZoneRating


class RealityZonePracticeRatingForm(forms.ModelForm):
    class Meta:
        model = ZoneRating
        fields = ["practice", "rating"]

    practice = forms.ModelChoiceField(
        queryset=Practice.objects.exclude(
            polymorphic_ctype__model="specializedpractice"
        ).exclude(polymorphic_ctype__model="corruptedpractice")
    )
    rating = forms.IntegerField(min_value=-5, max_value=5, initial=0)


RealityZonePracticeRatingFormSet = inlineformset_factory(
    RealityZone,
    ZoneRating,
    form=RealityZonePracticeRatingForm,
    extra=1,
    can_delete=False,
)
