from characters.models.mage.focus import Practice
from characters.models.mage.sorcerer import (
    LinearMagicPath,
    LinearMagicRitual,
    PathRating,
    Sorcerer,
)
from django import forms
from django.db.models import Q


class NuminaPathForm(forms.ModelForm):
    class Meta:
        model = PathRating
        fields = ["path", "rating", "practice", "ability"]

    path = forms.ModelChoiceField(
        queryset=LinearMagicPath.objects.all(), empty_label="Choose a Path"
    )
    rating = forms.IntegerField(min_value=0, max_value=5, initial=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["practice"].queryset = Practice.objects.exclude(
            polymorphic_ctype__model="specializedpractice"
        ).exclude(polymorphic_ctype__model="corruptedpractice")


class BaseNuminaPathRatingFormSet(forms.BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for form in self.forms:
            form.fields["path"].queryset = LinearMagicPath.objects.all()


NuminaPathRatingFormSet = forms.inlineformset_factory(
    Sorcerer,
    PathRating,
    form=NuminaPathForm,
    extra=1,
    can_delete=False,
    formset=BaseNuminaPathRatingFormSet,
)


class NuminaRitualForm(forms.ModelForm):
    select_or_create = forms.BooleanField(required=False)
    select_ritual = forms.ModelChoiceField(queryset=LinearMagicRitual.objects.all())

    class Meta:
        model = LinearMagicRitual
        fields = ["name", "description", "path", "level"]

    def __init__(self, *args, **kwargs):
        pk = kwargs.pop("pk")
        self.sorcerer = Sorcerer.objects.get(pk=pk)
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False

        self.fields["name"].required = False

        self.fields["name"].widget.attrs.update({"placeholder": "Enter name here"})
        self.fields["description"].widget.attrs.update(
            {"placeholder": "Enter description here"}
        )

        self.fields["path"].queryset = self.sorcerer.paths.all()

        rituals = Q()

        for path in self.sorcerer.pathrating_set.all():
            rituals |= Q(**{"path": path.path, "level__lte": path.rating})

        self.fields["select_ritual"].queryset = LinearMagicRitual.objects.filter(
            rituals
        ).exclude(id__in=[x.id for x in self.sorcerer.rituals.all()])
