from django import forms


class AllyForm(forms.Form):
    ALLY_TYPE_CHOICES = [("human", "Human"), ("mage", "Mage"), ("spirit", "Spirit")]

    ally_type = forms.ChoiceField(choices=ALLY_TYPE_CHOICES, label="Ally Type")
    name = forms.CharField(
        max_length=100,
        label="Name",
        widget=forms.TextInput(attrs={"placeholder": "Name"}),
    )
    concept = forms.CharField(
        max_length=100,
        label="Concept",
        widget=forms.TextInput(attrs={"placeholder": "Concept"}),
    )
    note = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Note", "rows": 4}), label="Note"
    )
