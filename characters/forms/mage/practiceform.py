from characters.models.mage.focus import Practice
from characters.models.mage.mage import Mage, PracticeRating
from django import forms
from django.forms import inlineformset_factory


class PracticeRatingForm(forms.ModelForm):
    class Meta:
        model = PracticeRating
        fields = ["practice", "rating"]

    practice = forms.ModelChoiceField(queryset=Practice.objects.all())
    rating = forms.IntegerField(min_value=0, max_value=5, initial=0)


PracticeRatingFormSet = inlineformset_factory(
    Mage, PracticeRating, form=PracticeRatingForm, extra=1, can_delete=False
)
