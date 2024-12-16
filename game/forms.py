from characters.models.core import CharacterModel
from django import forms
from game.models import Journal, JournalEntry, Story
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


class AddCharForm(forms.Form):
    character_to_add = forms.ModelChoiceField(
        queryset=CharacterModel.objects.none(), empty_label="Add Character"
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        scene = kwargs.pop("scene")
        super().__init__(*args, **kwargs)
        self.fields["character_to_add"].queryset = CharacterModel.objects.filter(
            owner=user, chronicle=scene.chronicle
        ).exclude(pk__in=scene.characters.all())


class PostForm(forms.Form):
    character = forms.ModelChoiceField(
        queryset=CharacterModel.objects.none(), empty_label="Character Select"
    )
    display_name = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.Textarea(
            attrs={"placeholder": "Display Name (Optional)", "rows": 1, "cols": 25}
        ),
    )
    message = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Message"}))

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        scene = kwargs.pop("scene")
        super().__init__(*args, **kwargs)
        self.fields["character"].queryset = CharacterModel.objects.filter(
            owner=user,
            chronicle=scene.chronicle,
            pk__in=scene.characters.all(),
        )

    def clean(self):
        cleaned_data = super().clean()

        if "character" in self.errors.keys():
            del self.errors["character"]

        message = cleaned_data.get("message")

        # Validate the message content (example: no prohibited words or empty message)
        if not message or len(message.strip()) == 0:
            raise forms.ValidationError("The message cannot be empty.")
        return cleaned_data


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ("name",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"placeholder": "Story Name"})


class JournalEntryForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Message"}))

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop("instance")
        super().__init__(*args, **kwargs)
        self.fields["message"].widget.attrs.update({"placeholder": "Journal Entry"})

    def save(self, commit=True):
        return self.instance.add_post(
            self.cleaned_data["date"], self.cleaned_data["message"]
        )


class STResponseForm(forms.Form):
    st_message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Message"})
    )

    def __init__(self, *args, **kwargs):
        self.entry = kwargs.pop("entry")
        super().__init__(*args, **kwargs)
        self.fields["st_message"].widget.attrs.update(
            {"placeholder": "Journal Response"}
        )

    def save(self, commit=True):
        self.entry.st_message = self.cleaned_data["st_message"]
        self.entry.save()
