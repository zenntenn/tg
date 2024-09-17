from characters.models.core import CharacterModel
from django import forms
from locations.models.core import LocationModel


class SceneCreationForm(forms.Form):
    name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"placeholder": "Scene Title"})
    )
    location = forms.ModelChoiceField(
        queryset=LocationModel.objects.order_by("name"), empty_label="Scene Location"
    )
    date_of_scene = forms.CharField(
        max_length=100, widget=forms.DateInput(attrs={"type": "date"})
    )

    def __init__(self, *args, **kwargs):
        chronicle = kwargs.pop("chronicle")
        super().__init__(*args, **kwargs)
        self.fields["location"].queryset = LocationModel.objects.filter(
            chronicle=chronicle
        ).order_by("name")


class StoryCreationForm(forms.Form):
    name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"placeholder": "Story Name"})
    )


class AddCharForm(forms.Form):
    character_to_add = forms.ModelChoiceField(
        queryset=CharacterModel.objects.none(), empty_label="Add Character"
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        scene = kwargs.pop("scene")
        super().__init__(*args, **kwargs)
        self.fields["character_to_add"].queryset = CharacterModel.objects.filter(
            owner=user, chronicle=scene.story.chronicle
        ).exclude(pk__in=scene.characters.all())


class PostForm(forms.Form):
    character = forms.ModelChoiceField(
        queryset=CharacterModel.objects.none(), empty_label="Character Select"
    )
    display_name = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.Textarea(
            attrs={"placeholder": "Display Name", "rows": 1, "cols": 25}
        ),
    )
    message = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Message"}))

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        scene = kwargs.pop("scene")
        super().__init__(*args, **kwargs)
        self.fields["character"].queryset = CharacterModel.objects.filter(
            owner=user,
            chronicle=scene.story.chronicle,
            pk__in=scene.characters.all(),
        )
