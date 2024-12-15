from accounts.models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUSerCreationForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def is_valid(self):
        if self.data["username"] == self.data["email"]:
            self.add_error(None, "Username and Email must be distinct")
            return False
        return super().is_valid()

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "preferred_heading",
            "theme",
            "discord_id",
            "lines",
            "veils",
            "discord_toggle",
            "lines_toggle",
            "veils_toggle",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["discord_id"].required = False


class SceneXP(forms.Form):
    def __init__(self, *args, **kwargs):
        self.scene = kwargs.pop("scene")
        super().__init__(*args, **kwargs)
        for character in self.scene.characters.filter(npc=False):
            self.fields[f"{character.name}"] = forms.BooleanField(required=False)

    def save(self):
        self.scene.xp_given = True
        self.scene.save()
        for char in self.cleaned_data.keys():
            if self.cleaned_data[char]:
                char.xp += 1
                char.save()

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = {
            self.scene.characters.get(name=k): v for k, v in cleaned_data.items()
        }
        for key1 in cleaned_data.keys():
            for key2 in self.data.keys():
                if key1.name in key2:
                    cleaned_data[key1] = True
        return cleaned_data
