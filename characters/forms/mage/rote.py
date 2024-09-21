from typing import Any, Mapping

from characters.models.core.ability import Ability
from characters.models.core.attribute import Attribute
from characters.models.mage.effect import Effect
from characters.models.mage.focus import Practice
from characters.models.mage.rote import Rote
from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList


class RoteCreationForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    practice = forms.ModelChoiceField(queryset=Practice.objects.none())
    attribute = forms.ModelChoiceField(queryset=Attribute.objects.all())
    ability = forms.ModelChoiceField(queryset=Ability.objects.none())
    systems = forms.CharField(widget=forms.Textarea())
    description = forms.CharField(widget=forms.Textarea())
    correspondence = forms.IntegerField(min_value=0, initial=0)
    time = forms.IntegerField(min_value=0, initial=0)
    spirit = forms.IntegerField(min_value=0, initial=0)
    matter = forms.IntegerField(min_value=0, initial=0)
    life = forms.IntegerField(min_value=0, initial=0)
    forces = forms.IntegerField(min_value=0, initial=0)
    entropy = forms.IntegerField(min_value=0, initial=0)
    mind = forms.IntegerField(min_value=0, initial=0)
    prime = forms.IntegerField(min_value=0, initial=0)

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop("instance", None)
        super().__init__(*args, **kwargs)
        self.fields["practice"].queryset = self.instance.practices.all()
        self.fields["correspondence"].widget.attrs["max"] = getattr(
            self.instance, "correspondence"
        )
        self.fields["time"].widget.attrs["max"] = getattr(self.instance, "time")
        self.fields["spirit"].widget.attrs["max"] = getattr(self.instance, "spirit")
        self.fields["matter"].widget.attrs["max"] = getattr(self.instance, "matter")
        self.fields["life"].widget.attrs["max"] = getattr(self.instance, "life")
        self.fields["forces"].widget.attrs["max"] = getattr(self.instance, "forces")
        self.fields["entropy"].widget.attrs["max"] = getattr(self.instance, "entropy")
        self.fields["mind"].widget.attrs["max"] = getattr(self.instance, "mind")
        self.fields["prime"].widget.attrs["max"] = getattr(self.instance, "prime")

    def save(self, mage):
        name = self.cleaned_data.get("name")
        practice = self.cleaned_data.get("practice")
        attribute = self.cleaned_data.get("attribute")
        ability = Ability.objects.get(pk=self.data.get("ability"))
        systems = self.cleaned_data.get("systems")
        description = self.cleaned_data.get("description")
        correspondence = self.cleaned_data.get("correspondence")
        time = self.cleaned_data.get("time")
        spirit = self.cleaned_data.get("spirit")
        matter = self.cleaned_data.get("matter")
        life = self.cleaned_data.get("life")
        forces = self.cleaned_data.get("forces")
        entropy = self.cleaned_data.get("entropy")
        mind = self.cleaned_data.get("mind")
        prime = self.cleaned_data.get("prime")
        e = Effect(
            correspondence=correspondence,
            time=time,
            spirit=spirit,
            matter=matter,
            life=life,
            forces=forces,
            entropy=entropy,
            mind=mind,
            prime=prime,
            description=systems,
            name=name,
            status="Sub",
        )
        if e.is_learnable(mage) and e.cost() <= mage.rote_points:
            e.save()
            r = Rote.objects.create(
                name=name,
                practice=practice,
                attribute=attribute,
                ability=ability,
                description=description,
                effect=e,
                status="Sub",
            )
            mage.rotes.add(r)
            mage.rote_points -= e.cost()
            mage.save()
            return True
        return False
