from characters.models.core.background import Background, BackgroundRating
from characters.models.core.human import Human
from django import forms
from django.forms import BaseInlineFormSet, inlineformset_factory


class BackgroundRatingForm(forms.ModelForm):
    class Meta:
        model = BackgroundRating
        fields = ["bg", "rating", "note"]

    bg = forms.ModelChoiceField(
        queryset=Background.objects.all(), empty_label="Choose a Background"
    )
    rating = forms.IntegerField(min_value=0, max_value=5, initial=0)
    pooled = forms.BooleanField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["bg"].queryset = Background.objects.all().order_by("name")
        self.fields["note"].required = False


class BaseBackgroundRatingFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.forms:
            form.fields["bg"].queryset = Background.objects.all().order_by("name")


BackgroundRatingFormSet = inlineformset_factory(
    Human,
    BackgroundRating,
    form=BackgroundRatingForm,
    extra=1,
    can_delete=False,
    formset=BaseBackgroundRatingFormSet,
)
