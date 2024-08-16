from django import forms
from game.models import ObjectType


class CharacterCreationForm(forms.Form):
    char_type = forms.ChoiceField(choices=[])
    name = forms.CharField(max_length=100, label="Name", required=False)
    rank = forms.IntegerField(initial=1, max_value=5)

    def __init__(self, *args, **kwargs):
        gameline = kwargs.pop("gameline")
        super().__init__(*args, **kwargs)
        self.fields["char_type"].choices = [
            (x.name, x.name.replace("_", " ").title())
            for x in ObjectType.objects.filter(type="char", gameline=gameline)
        ]
