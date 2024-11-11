from django import forms
from game.models import ObjectType


class CharacterCreationForm(forms.Form):
    char_type = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user is not None:
            if user.profile.is_st():
                self.fields["char_type"].choices = [
                    (x.name, x.name.replace("_", " ").title())
                    for x in ObjectType.objects.filter(type="char")
                ]
            else:
                self.fields["char_type"].choices = [
                    (x.name, x.name.replace("_", " ").title())
                    for x in ObjectType.objects.filter(type="char")
                    if x.name in ["mage", "cabal", "sorcerer"]
                ]
