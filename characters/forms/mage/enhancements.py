from characters.models.core.attribute_block import Attribute
from characters.models.core.background_block import Background
from characters.models.core.merit_flaw_block import MeritFlaw, MeritFlawRating
from characters.models.mage.effect import Effect
from characters.models.mage.resonance import Resonance
from core.widgets import AutocompleteTextInput
from django import forms
from game.models import ObjectType
from items.forms.mage.wonder import WonderForm
from items.models.mage.artifact import Artifact
from items.models.mage.talisman import Talisman
from items.models.mage.wonder import Wonder, WonderResonanceRating


class EnhancementForm(forms.Form):
    enhancement_style = forms.ChoiceField(
        choices=[
            ("Cybernetics", "Cybernetics"),
            ("Biomods", "Biomods"),
            ("Genegineering", "Genegineering"),
        ],
        required=False,
    )
    enhancement_type = forms.ChoiceField(
        choices=[
            ("Attributes", "Attributes"),
            ("Existing Device", "Existing Device"),
            ("New Device", "New Device"),
            ("Health", "Health"),
        ],
        required=False,
    )

    new_device_new_power_option = forms.ChoiceField(
        choices=[
            ("New Effect", "New Effect"),
            ("Existing Effect", "Existing Effect"),
        ],
        required=False,
    )

    new_device_resonance = forms.CharField(
        required=False, widget=AutocompleteTextInput(suggestions=[])
    )

    new_device_effect = forms.ModelChoiceField(
        queryset=Effect.objects.none(), required=False
    )

    new_device_new_effect_name = forms.CharField(max_length=100, required=False)
    new_device_new_effect_description = forms.CharField(
        widget=forms.Textarea(), required=False
    )
    new_device_new_effect_correspondence = forms.IntegerField(
        min_value=0, max_value=5, initial=0, required=False
    )
    new_device_new_effect_time = forms.IntegerField(
        min_value=0, max_value=5, initial=0, required=False
    )
    new_device_new_effect_spirit = forms.IntegerField(
        min_value=0, max_value=5, initial=0, required=False
    )
    new_device_new_effect_matter = forms.IntegerField(
        min_value=0, max_value=5, initial=0, required=False
    )
    new_device_new_effect_life = forms.IntegerField(
        min_value=0, max_value=5, initial=0, required=False
    )
    new_device_new_effect_forces = forms.IntegerField(
        min_value=0, max_value=5, initial=0, required=False
    )
    new_device_new_effect_entropy = forms.IntegerField(
        min_value=0, max_value=5, initial=0, required=False
    )
    new_device_new_effect_mind = forms.IntegerField(
        min_value=0, max_value=5, initial=0, required=False
    )
    new_device_new_effect_prime = forms.IntegerField(
        min_value=0, max_value=5, initial=0, required=False
    )

    device = forms.ModelChoiceField(queryset=Wonder.objects.none(), required=False)
    flaw = forms.ModelChoiceField(queryset=MeritFlaw.objects.none(), required=False)

    def __init__(self, *args, **kwargs):
        self.rank = kwargs.pop("rank", 0)
        suggestions = kwargs.pop("suggestions", None)
        super().__init__(*args, **kwargs)
        if suggestions is None:
            suggestions = [x.name.title() for x in Resonance.objects.order_by("name")]
        self.fields["new_device_resonance"].widget.suggestions = suggestions

        embedded_form = WonderForm()
        for field_name, field in embedded_form.fields.items():
            self.fields["new_device_" + field_name] = field
            self.fields["new_device_" + field_name].label = f"New Device {field.label}"
            self.fields["new_device_" + field_name].required = False
        self.fields["new_device_wonder_type"].choices = [
            ("artifact", "Artifact"),
            ("talisman", "Talisman"),
        ]
        self.fields["new_device_effect"].queryset = Effect.objects.filter(
            rote_cost__lte=2 * self.rank
        )

        for i in range(self.rank):
            self.fields[f"attribute_{i}"] = forms.ModelChoiceField(
                queryset=Attribute.objects.filter(
                    property_name__in=[
                        "strength",
                        "dexterity",
                        "stamina",
                        "appearance",
                        "perception",
                        "intelligence",
                    ]
                ),
                required=False,
            )
        self.fields["flaw"].queryset = MeritFlaw.objects.filter(
            ratings__value__in=[-self.rank],
            allowed_types__in=[ObjectType.objects.get(name="mage")],
        )
        self.fields["device"].queryset = Wonder.objects.filter(rank=self.rank).exclude(
            polymorphic_ctype__model="charm"
        )

    def save(self, *args, **kwargs):
        char = kwargs.pop("char", None)
        if char is None:
            raise ValueError("Form requires char keyword")

        note = []

        if self.cleaned_data["enhancement_type"] == "Attributes":
            for i in range(self.rank):
                att = self.cleaned_data[f"attribute_{i}"]
                note.append(att.name)
                char.add_attribute(att.property_name, maximum=10)
            url = ""
        elif self.cleaned_data["enhancement_type"] == "Existing Device":
            char.enhancement_devices.add(self.cleaned_data["device"])
            note.append(self.cleaned_data["device"].name)
            url = self.cleaned_data["device"].get_absolute_url()
        elif self.cleaned_data["enhancement_type"] == "New Device":
            wonder_dict = {
                "artifact": Artifact,
                "talisman": Talisman,
            }
            wonder = wonder_dict[self.cleaned_data["new_device_wonder_type"]]

            if self.cleaned_data["new_device_new_power_option"] == "New Effect":
                effect = Effect(
                    name=self.cleaned_data["new_device_new_effect_name"],
                    description=self.cleaned_data["new_device_new_effect_description"],
                    correspondence=self.cleaned_data[
                        "new_device_new_effect_correspondence"
                    ],
                    time=self.cleaned_data["new_device_new_effect_time"],
                    spirit=self.cleaned_data["new_device_new_effect_spirit"],
                    matter=self.cleaned_data["new_device_new_effect_matter"],
                    life=self.cleaned_data["new_device_new_effect_life"],
                    forces=self.cleaned_data["new_device_new_effect_forces"],
                    entropy=self.cleaned_data["new_device_new_effect_entropy"],
                    mind=self.cleaned_data["new_device_new_effect_mind"],
                    prime=self.cleaned_data["new_device_new_effect_prime"],
                )
                if effect.cost() > 2 * self.rank:
                    return False
                effect.save()
            elif self.cleaned_data["new_device_new_power_option"] == "Existing Effect":
                effect = self.cleaned_data["new_device_effect"]

            wonder_kwargs = {
                "name": "",
                "description": "",
                "rank": self.rank,
                "background_cost": 2 * self.rank,
                "quintessence_max": 5 * self.rank,
            }
            if self.cleaned_data["new_device_winder_type"] == "artifact":
                wonder_kwargs.update({"power": effect})
            elif self.cleaned_data["new_device_winder_type"] == "talisman":
                wonder_kwargs.update({"arete": self.rank})

            w = wonder.objects.create(**wonder_kwargs)
            if self.cleaned_data["new_device_winder_type"] == "talisman":
                w.powers.add(effect)

            WonderResonanceRating.objects.create(
                wonder=w,
                resonance=Resonance.objects.get_or_create(
                    name=self.cleaned_data["new_device_resonance"], rating=self.rank
                )[0],
            )

            note.append(w.name)
            url = w.get_absolute_url()
        elif self.cleaned_data["enhancement_type"] == "Health":
            char.max_health_levels += self.rank
            for _ in range(self.rank):
                note.append("Health")
            url = ""

        if self.cleaned_data["flaw"] is not None:
            MeritFlawRating.objects.create(
                character=char, mf=self.cleaned_data["flaw"], rating=-self.rank
            )
            note.append(self.cleaned_data["flaw"].name)
        else:
            char.paradox += self.rank
            note.append(f"{self.rank} Permanent Paradox")

        note = ", ".join(note)
        # url

        bgr = char.backgrounds.filter(
            bg=Background.objects.get(property_name="enhancement"),
            rating=self.rank,
            complete=False,
        ).first()

        bgr.note = note
        bgr.url = url
        bgr.complete = True
        bgr.save()

        return True
