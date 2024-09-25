from characters.models.core.background import Background, BackgroundRating
from characters.models.core.human import Human
from django import forms
from django.forms import BaseInlineFormSet, inlineformset_factory


class BackgroundRatingForm(forms.ModelForm):
    class Meta:
        model = BackgroundRating
        fields = ["bg", "rating"]

    bg = forms.ModelChoiceField(
        queryset=Background.objects.all(), empty_label="Choose a Background"
    )
    rating = forms.IntegerField(min_value=0, max_value=5, initial=0)

    def __init__(self, *args, **kwargs):
        char = kwargs.pop("char", None)
        super().__init__(*args, **kwargs)
        if char:
            q = Background.objects.all().order_by("name")
            q = q.filter(property_name__in=char.allowed_backgrounds)
            self.fields["bg"].queryset = q
        else:
            self.fields["bg"].queryset = Background.objects.all().order_by("name")


class BaseBackgroundRatingFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        self.char = kwargs.pop("char", None)
        super().__init__(*args, **kwargs)

        for form in self.forms:
            form.fields["bg"].queryset = self.get_practice_queryset()

    def get_practice_queryset(self):
        if self.char:
            q = Background.objects.all()
            return q.order_by("name")
        return Background.objects.all()


BackgroundRatingFormSet = inlineformset_factory(
    Human,
    BackgroundRating,
    form=BackgroundRatingForm,
    extra=1,
    can_delete=False,
    formset=BaseBackgroundRatingFormSet,
)
