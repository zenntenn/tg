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
        fields = ["preferred_heading", "theme", "discord_id", "lines", "veils"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["discord_id"].required = False
