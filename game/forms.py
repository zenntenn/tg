from characters.models.core import CharacterModel
from django import forms
from locations.models.core import LocationModel


class SceneCreationForm(forms.Form):
    name = forms.CharField(max_length=100)
    location = forms.ModelChoiceField(queryset=LocationModel.objects.order_by("name"))
    date_of_scene = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        chronicle = kwargs.pop("chronicle")
        super().__init__(*args, **kwargs)
        self.fields["location"] = forms.ModelChoiceField(
            LocationModel.objects.filter(chronicle=chronicle).order_by("name")
        )


class StoryCreationForm(forms.Form):
    name = forms.CharField(max_length=100)


class AddCharForm(forms.Form):
    character_to_add = forms.ModelChoiceField(
        queryset=CharacterModel.objects.order_by("name")
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        scene = kwargs.pop("scene")
        super().__init__(*args, **kwargs)
        self.fields["character_to_add"] = forms.ModelChoiceField(
            CharacterModel.objects.filter(
                owner=user, chronicle=scene.story.chronicle
            ).exclude(pk__in=scene.characters.all())
        )


class PostForm(forms.Form):
    character = forms.ModelChoiceField(queryset=CharacterModel.objects.none())
    display_name = forms.CharField(max_length=100, required=False)
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        scene = kwargs.pop("scene")
        super().__init__(*args, **kwargs)
        self.fields["character"] = forms.ModelChoiceField(
            CharacterModel.objects.filter(
                owner=user,
                chronicle=scene.story.chronicle,
                pk__in=scene.characters.all(),
            )
        )
