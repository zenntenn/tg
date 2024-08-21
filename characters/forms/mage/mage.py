from core.models import Language
from core.widgets import AutocompleteTextInput
from django import forms
from game.models.chronicle import Chronicle
from wod.models.characters.human import Archetype, MeritFlaw, WoDSpecialty
from wod.models.characters.mage import MageFaction
from wod.models.characters.mage.focus import Instrument, Paradigm, Practice
from wod.models.characters.mage.resonance import Resonance


class MageCreationForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    concept = forms.CharField(label="Concept", max_length=100)
    chronicle = forms.ModelChoiceField(
        required=False,
        queryset=Chronicle.objects.filter(
            allowed_objects__name="Mage", allowed_objects__system="wod"
        ),
    )
    nature = forms.ModelChoiceField(queryset=Archetype.objects.all())
    demeanor = forms.ModelChoiceField(queryset=Archetype.objects.all())
    affiliation = forms.ModelChoiceField(
        queryset=MageFaction.objects.filter(parent=None)
    )
    essence = forms.CharField(
        widget=forms.Select(
            choices=[
                ("---------", "---------"),
                ("Dynamic", "Dynamic"),
                ("Pattern", "Pattern"),
                ("Primordial", "Primordial"),
                ("Questing", "Questing"),
            ]
        ),
    )
    faction = forms.ModelChoiceField(
        queryset=MageFaction.objects.none(), required=False
    )
    subfaction = forms.ModelChoiceField(
        queryset=MageFaction.objects.none(), required=False
    )

    def clean_faction(self):
        faction = self.cleaned_data.get("faction")
        if faction and not MageFaction.objects.filter(id=faction.id).exists():
            raise forms.ValidationError("Invalid faction selected")
        return faction

    def clean_subfaction(self):
        subfaction = self.cleaned_data.get("subfaction")
        if subfaction and not MageFaction.objects.filter(id=subfaction.id).exists():
            raise forms.ValidationError("Invalid subfaction selected")
        return subfaction


class MageAbilitiesForm(forms.Form):
    alertness = forms.IntegerField(max_value=3, min_value=0)
    athletics = forms.IntegerField(max_value=3, min_value=0)
    brawl = forms.IntegerField(max_value=3, min_value=0)
    empathy = forms.IntegerField(max_value=3, min_value=0)
    expression = forms.IntegerField(max_value=3, min_value=0)
    intimidation = forms.IntegerField(max_value=3, min_value=0)
    streetwise = forms.IntegerField(max_value=3, min_value=0)
    subterfuge = forms.IntegerField(max_value=3, min_value=0)

    crafts = forms.IntegerField(max_value=3, min_value=0)
    drive = forms.IntegerField(max_value=3, min_value=0)
    etiquette = forms.IntegerField(max_value=3, min_value=0)
    firearms = forms.IntegerField(max_value=3, min_value=0)
    melee = forms.IntegerField(max_value=3, min_value=0)
    stealth = forms.IntegerField(max_value=3, min_value=0)

    academics = forms.IntegerField(max_value=3, min_value=0)
    computer = forms.IntegerField(max_value=3, min_value=0)
    investigation = forms.IntegerField(max_value=3, min_value=0)
    medicine = forms.IntegerField(max_value=3, min_value=0)
    science = forms.IntegerField(max_value=3, min_value=0)
    awareness = forms.IntegerField(max_value=3, min_value=0)
    art = forms.IntegerField(max_value=3, min_value=0)
    leadership = forms.IntegerField(max_value=3, min_value=0)
    animal_kinship = forms.IntegerField(max_value=3, min_value=0)
    blatancy = forms.IntegerField(max_value=3, min_value=0)
    carousing = forms.IntegerField(max_value=3, min_value=0)
    do = forms.IntegerField(max_value=3, min_value=0)
    flying = forms.IntegerField(max_value=3, min_value=0)
    high_ritual = forms.IntegerField(max_value=3, min_value=0)
    lucid_dreaming = forms.IntegerField(max_value=3, min_value=0)
    search = forms.IntegerField(max_value=3, min_value=0)
    seduction = forms.IntegerField(max_value=3, min_value=0)
    martial_arts = forms.IntegerField(max_value=3, min_value=0)
    meditation = forms.IntegerField(max_value=3, min_value=0)
    research = forms.IntegerField(max_value=3, min_value=0)
    survival = forms.IntegerField(max_value=3, min_value=0)
    technology = forms.IntegerField(max_value=3, min_value=0)
    acrobatics = forms.IntegerField(max_value=3, min_value=0)
    archery = forms.IntegerField(max_value=3, min_value=0)
    biotech = forms.IntegerField(max_value=3, min_value=0)
    energy_weapons = forms.IntegerField(max_value=3, min_value=0)
    hypertech = forms.IntegerField(max_value=3, min_value=0)
    jetpack = forms.IntegerField(max_value=3, min_value=0)
    riding = forms.IntegerField(max_value=3, min_value=0)
    torture = forms.IntegerField(max_value=3, min_value=0)
    cosmology = forms.IntegerField(max_value=3, min_value=0)
    enigmas = forms.IntegerField(max_value=3, min_value=0)
    esoterica = forms.IntegerField(max_value=3, min_value=0)
    law = forms.IntegerField(max_value=3, min_value=0)
    occult = forms.IntegerField(max_value=3, min_value=0)
    politics = forms.IntegerField(max_value=3, min_value=0)
    area_knowledge = forms.IntegerField(max_value=3, min_value=0)
    belief_systems = forms.IntegerField(max_value=3, min_value=0)
    cryptography = forms.IntegerField(max_value=3, min_value=0)
    demolitions = forms.IntegerField(max_value=3, min_value=0)
    finance = forms.IntegerField(max_value=3, min_value=0)
    lore = forms.IntegerField(max_value=3, min_value=0)
    media = forms.IntegerField(max_value=3, min_value=0)
    pharmacopeia = forms.IntegerField(max_value=3, min_value=0)

    cooking = forms.IntegerField(max_value=3, min_value=0)
    diplomacy = forms.IntegerField(max_value=3, min_value=0)
    instruction = forms.IntegerField(max_value=3, min_value=0)
    intrigue = forms.IntegerField(max_value=3, min_value=0)
    intuition = forms.IntegerField(max_value=3, min_value=0)
    mimicry = forms.IntegerField(max_value=3, min_value=0)
    negotiation = forms.IntegerField(max_value=3, min_value=0)
    newspeak = forms.IntegerField(max_value=3, min_value=0)
    scan = forms.IntegerField(max_value=3, min_value=0)
    scrounging = forms.IntegerField(max_value=3, min_value=0)
    style = forms.IntegerField(max_value=3, min_value=0)
    blind_fighting = forms.IntegerField(max_value=3, min_value=0)
    climbing = forms.IntegerField(max_value=3, min_value=0)
    disguise = forms.IntegerField(max_value=3, min_value=0)
    elusion = forms.IntegerField(max_value=3, min_value=0)
    escapology = forms.IntegerField(max_value=3, min_value=0)
    fast_draw = forms.IntegerField(max_value=3, min_value=0)
    fast_talk = forms.IntegerField(max_value=3, min_value=0)
    fencing = forms.IntegerField(max_value=3, min_value=0)
    fortune_telling = forms.IntegerField(max_value=3, min_value=0)
    gambling = forms.IntegerField(max_value=3, min_value=0)
    gunsmith = forms.IntegerField(max_value=3, min_value=0)
    heavy_weapons = forms.IntegerField(max_value=3, min_value=0)
    hunting = forms.IntegerField(max_value=3, min_value=0)
    hypnotism = forms.IntegerField(max_value=3, min_value=0)
    jury_rigging = forms.IntegerField(max_value=3, min_value=0)
    microgravity_operations = forms.IntegerField(max_value=3, min_value=0)
    misdirection = forms.IntegerField(max_value=3, min_value=0)
    networking = forms.IntegerField(max_value=3, min_value=0)
    pilot = forms.IntegerField(max_value=3, min_value=0)
    psychology = forms.IntegerField(max_value=3, min_value=0)
    security = forms.IntegerField(max_value=3, min_value=0)
    speed_reading = forms.IntegerField(max_value=3, min_value=0)
    swimming = forms.IntegerField(max_value=3, min_value=0)
    conspiracy_theory = forms.IntegerField(max_value=3, min_value=0)
    chantry_politics = forms.IntegerField(max_value=3, min_value=0)
    covert_culture = forms.IntegerField(max_value=3, min_value=0)
    cultural_savvy = forms.IntegerField(max_value=3, min_value=0)
    helmsman = forms.IntegerField(max_value=3, min_value=0)
    history_knowledge = forms.IntegerField(max_value=3, min_value=0)
    power_brokering = forms.IntegerField(max_value=3, min_value=0)
    propaganda = forms.IntegerField(max_value=3, min_value=0)
    theology = forms.IntegerField(max_value=3, min_value=0)
    unconventional_warface = forms.IntegerField(max_value=3, min_value=0)
    vice = forms.IntegerField(max_value=3, min_value=0)

    def __init__(self, *args, **kwargs):
        self.char = kwargs.pop("character")
        kwargs["initial"] = self.char.get_abilities()
        super().__init__(*args, **kwargs)

    def assign(self):
        self.full_clean()
        for key in (
            list(self.char.get_talents().keys())
            + list(self.char.get_skills().keys())
            + list(self.char.get_knowledges().keys())
        ):
            if key == "do" and self.char.faction.name != "Akashayana":
                pass
            else:
                setattr(self.char, key, self.cleaned_data[key])


class MageAdvantagesForm(forms.Form):
    allies = forms.IntegerField(max_value=5, min_value=0)
    alternate_identity = forms.IntegerField(max_value=5, min_value=0)
    arcane = forms.IntegerField(max_value=5, min_value=0)
    avatar = forms.IntegerField(max_value=5, min_value=0)
    backup = forms.IntegerField(max_value=5, min_value=0)
    blessing = forms.IntegerField(max_value=5, min_value=0)
    certification = forms.IntegerField(max_value=5, min_value=0)
    chantry = forms.IntegerField(max_value=5, min_value=0)
    contacts = forms.IntegerField(max_value=5, min_value=0)
    cult = forms.IntegerField(max_value=5, min_value=0)
    demesne = forms.IntegerField(max_value=5, min_value=0)
    destiny = forms.IntegerField(max_value=5, min_value=0)
    dream = forms.IntegerField(max_value=5, min_value=0)
    enhancement = forms.IntegerField(max_value=5, min_value=0)
    fame = forms.IntegerField(max_value=5, min_value=0)
    familiar = forms.IntegerField(max_value=5, min_value=0)
    influence = forms.IntegerField(max_value=5, min_value=0)
    legend = forms.IntegerField(max_value=5, min_value=0)
    library = forms.IntegerField(max_value=5, min_value=0)
    mentor = forms.IntegerField(max_value=5, min_value=0)
    node = forms.IntegerField(max_value=5, min_value=0)
    past_lives = forms.IntegerField(max_value=5, min_value=0)
    patron = forms.IntegerField(max_value=5, min_value=0)
    rank = forms.IntegerField(max_value=5, min_value=0)
    requisitions = forms.IntegerField(max_value=5, min_value=0)
    resources = forms.IntegerField(max_value=5, min_value=0)
    retainers = forms.IntegerField(max_value=5, min_value=0)
    sanctum = forms.IntegerField(max_value=5, min_value=0)
    secret_weapons = forms.IntegerField(max_value=5, min_value=0)
    spies = forms.IntegerField(max_value=5, min_value=0)
    status_background = forms.IntegerField(max_value=5, min_value=0)
    totem = forms.IntegerField(max_value=5, min_value=0)
    wonder = forms.IntegerField(max_value=5, min_value=0)

    arete = forms.IntegerField(max_value=3, min_value=1)

    affinity_sphere = forms.CharField(
        widget=forms.Select(choices=[("----", "----")]),
    )

    paradigms = forms.ModelMultipleChoiceField(
        required=False, queryset=Paradigm.objects.all()
    )
    practices = forms.ModelMultipleChoiceField(
        required=False, queryset=Practice.objects.all()
    )
    instruments = forms.ModelMultipleChoiceField(
        required=False, queryset=Instrument.objects.all()
    )

    def __init__(self, *args, **kwargs):
        self.char = kwargs.pop("character")
        possible_affinities = []
        for aff in [self.char.affiliation, self.char.faction, self.char.subfaction]:
            if aff is not None:
                if isinstance(aff.affinities, list):
                    possible_affinities.extend(aff.affinities)
        choices = [(x, x.title()) for x in possible_affinities]
        if len(choices) == 0:
            choices = [(x, x.title()) for x in self.char.get_spheres().keys()]
        choices = list(set(choices))
        choices.sort()
        kwargs["initial"] = self.char.get_backgrounds()
        kwargs["initial"]["arete"] = max(self.char.arete, 1)
        kwargs["initial"]["affinity_sphere"] = self.char.affinity_sphere
        kwargs["initial"]["paradigms"] = self.char.paradigms.all()
        kwargs["initial"]["practices"] = self.char.practices.all()
        kwargs["initial"]["instruments"] = self.char.instruments.all()
        super().__init__(*args, **kwargs)
        self.fields["affinity_sphere"].widget.choices += choices

    def assign(self):
        self.full_clean()
        for key in self.char.get_backgrounds().keys():
            setattr(self.char, key, self.cleaned_data[key])
        self.char.arete = self.cleaned_data["arete"]
        self.char.affinity_sphere = self.cleaned_data["affinity_sphere"]
        setattr(self.char, self.char.affinity_sphere, 1)
        self.char.paradigms.add(*list(self.cleaned_data["paradigms"]))
        self.char.practices.add(*list(self.cleaned_data["practices"]))
        self.char.instruments.add(*list(self.cleaned_data["instruments"]))


class MagePowersForm(forms.Form):
    correspondence = forms.IntegerField(max_value=5, min_value=0)
    time = forms.IntegerField(max_value=5, min_value=0)
    spirit = forms.IntegerField(max_value=5, min_value=0)
    mind = forms.IntegerField(max_value=5, min_value=0)
    entropy = forms.IntegerField(max_value=5, min_value=0)
    prime = forms.IntegerField(max_value=5, min_value=0)
    forces = forms.IntegerField(max_value=5, min_value=0)
    matter = forms.IntegerField(max_value=5, min_value=0)
    life = forms.IntegerField(max_value=5, min_value=0)

    resonance = forms.CharField(
        required=False,
        widget=AutocompleteTextInput(suggestions=[]),
    )

    def __init__(self, *args, **kwargs):
        self.char = kwargs.pop("character")

        kwargs["initial"] = self.char.get_spheres()
        kwargs["initial"]["resonance"] = self.char.filter_resonance(minimum=1).first()
        self.char.subtract_resonance(kwargs["initial"]["resonance"])

        super().__init__(*args, **kwargs)
        for sphere in [
            "correspondence",
            "time",
            "spirit",
            "mind",
            "entropy",
            "prime",
            "forces",
            "matter",
            "life",
        ]:
            self.fields[sphere] = forms.IntegerField(
                max_value=self.char.arete, min_value=0
            )
        self.fields[self.char.affinity_sphere] = forms.IntegerField(
            max_value=self.char.arete, min_value=1
        )
        self.fields["resonance"].widget.suggestions = [
            x.name.title() for x in Resonance.objects.order_by("name")
        ]

    def assign(self):
        self.full_clean()
        for key in self.char.get_spheres().keys():
            setattr(self.char, key, self.cleaned_data[key])
        res = self.cleaned_data["resonance"]
        self.char.add_resonance(res)


class MageFreebieForm(forms.Form):
    strength = forms.IntegerField(max_value=5, min_value=1)
    dexterity = forms.IntegerField(max_value=5, min_value=1)
    stamina = forms.IntegerField(max_value=5, min_value=1)
    charisma = forms.IntegerField(max_value=5, min_value=1)
    manipulation = forms.IntegerField(max_value=5, min_value=1)
    appearance = forms.IntegerField(max_value=5, min_value=1)
    perception = forms.IntegerField(max_value=5, min_value=1)
    intelligence = forms.IntegerField(max_value=5, min_value=1)
    wits = forms.IntegerField(max_value=5, min_value=1)
    alertness = forms.IntegerField(max_value=3, min_value=0)
    athletics = forms.IntegerField(max_value=3, min_value=0)
    brawl = forms.IntegerField(max_value=3, min_value=0)
    empathy = forms.IntegerField(max_value=3, min_value=0)
    expression = forms.IntegerField(max_value=3, min_value=0)
    intimidation = forms.IntegerField(max_value=3, min_value=0)
    streetwise = forms.IntegerField(max_value=3, min_value=0)
    subterfuge = forms.IntegerField(max_value=3, min_value=0)

    crafts = forms.IntegerField(max_value=3, min_value=0)
    drive = forms.IntegerField(max_value=3, min_value=0)
    etiquette = forms.IntegerField(max_value=3, min_value=0)
    firearms = forms.IntegerField(max_value=3, min_value=0)
    melee = forms.IntegerField(max_value=3, min_value=0)
    stealth = forms.IntegerField(max_value=3, min_value=0)

    academics = forms.IntegerField(max_value=3, min_value=0)
    computer = forms.IntegerField(max_value=3, min_value=0)
    investigation = forms.IntegerField(max_value=3, min_value=0)
    medicine = forms.IntegerField(max_value=3, min_value=0)
    science = forms.IntegerField(max_value=3, min_value=0)
    awareness = forms.IntegerField(max_value=3, min_value=0)
    art = forms.IntegerField(max_value=3, min_value=0)
    leadership = forms.IntegerField(max_value=3, min_value=0)
    animal_kinship = forms.IntegerField(max_value=3, min_value=0)
    blatancy = forms.IntegerField(max_value=3, min_value=0)
    carousing = forms.IntegerField(max_value=3, min_value=0)
    do = forms.IntegerField(max_value=3, min_value=0)
    flying = forms.IntegerField(max_value=3, min_value=0)
    high_ritual = forms.IntegerField(max_value=3, min_value=0)
    lucid_dreaming = forms.IntegerField(max_value=3, min_value=0)
    search = forms.IntegerField(max_value=3, min_value=0)
    seduction = forms.IntegerField(max_value=3, min_value=0)
    martial_arts = forms.IntegerField(max_value=3, min_value=0)
    meditation = forms.IntegerField(max_value=3, min_value=0)
    research = forms.IntegerField(max_value=3, min_value=0)
    survival = forms.IntegerField(max_value=3, min_value=0)
    technology = forms.IntegerField(max_value=3, min_value=0)
    acrobatics = forms.IntegerField(max_value=3, min_value=0)
    archery = forms.IntegerField(max_value=3, min_value=0)
    biotech = forms.IntegerField(max_value=3, min_value=0)
    energy_weapons = forms.IntegerField(max_value=3, min_value=0)
    hypertech = forms.IntegerField(max_value=3, min_value=0)
    jetpack = forms.IntegerField(max_value=3, min_value=0)
    riding = forms.IntegerField(max_value=3, min_value=0)
    torture = forms.IntegerField(max_value=3, min_value=0)
    cosmology = forms.IntegerField(max_value=3, min_value=0)
    enigmas = forms.IntegerField(max_value=3, min_value=0)
    esoterica = forms.IntegerField(max_value=3, min_value=0)
    law = forms.IntegerField(max_value=3, min_value=0)
    occult = forms.IntegerField(max_value=3, min_value=0)
    politics = forms.IntegerField(max_value=3, min_value=0)
    area_knowledge = forms.IntegerField(max_value=3, min_value=0)
    belief_systems = forms.IntegerField(max_value=3, min_value=0)
    cryptography = forms.IntegerField(max_value=3, min_value=0)
    demolitions = forms.IntegerField(max_value=3, min_value=0)
    finance = forms.IntegerField(max_value=3, min_value=0)
    lore = forms.IntegerField(max_value=3, min_value=0)
    media = forms.IntegerField(max_value=3, min_value=0)
    pharmacopeia = forms.IntegerField(max_value=3, min_value=0)

    cooking = forms.IntegerField(max_value=3, min_value=0)
    diplomacy = forms.IntegerField(max_value=3, min_value=0)
    instruction = forms.IntegerField(max_value=3, min_value=0)
    intrigue = forms.IntegerField(max_value=3, min_value=0)
    intuition = forms.IntegerField(max_value=3, min_value=0)
    mimicry = forms.IntegerField(max_value=3, min_value=0)
    negotiation = forms.IntegerField(max_value=3, min_value=0)
    newspeak = forms.IntegerField(max_value=3, min_value=0)
    scan = forms.IntegerField(max_value=3, min_value=0)
    scrounging = forms.IntegerField(max_value=3, min_value=0)
    style = forms.IntegerField(max_value=3, min_value=0)
    blind_fighting = forms.IntegerField(max_value=3, min_value=0)
    climbing = forms.IntegerField(max_value=3, min_value=0)
    disguise = forms.IntegerField(max_value=3, min_value=0)
    elusion = forms.IntegerField(max_value=3, min_value=0)
    escapology = forms.IntegerField(max_value=3, min_value=0)
    fast_draw = forms.IntegerField(max_value=3, min_value=0)
    fast_talk = forms.IntegerField(max_value=3, min_value=0)
    fencing = forms.IntegerField(max_value=3, min_value=0)
    fortune_telling = forms.IntegerField(max_value=3, min_value=0)
    gambling = forms.IntegerField(max_value=3, min_value=0)
    gunsmith = forms.IntegerField(max_value=3, min_value=0)
    heavy_weapons = forms.IntegerField(max_value=3, min_value=0)
    hunting = forms.IntegerField(max_value=3, min_value=0)
    hypnotism = forms.IntegerField(max_value=3, min_value=0)
    jury_rigging = forms.IntegerField(max_value=3, min_value=0)
    microgravity_operations = forms.IntegerField(max_value=3, min_value=0)
    misdirection = forms.IntegerField(max_value=3, min_value=0)
    networking = forms.IntegerField(max_value=3, min_value=0)
    pilot = forms.IntegerField(max_value=3, min_value=0)
    psychology = forms.IntegerField(max_value=3, min_value=0)
    security = forms.IntegerField(max_value=3, min_value=0)
    speed_reading = forms.IntegerField(max_value=3, min_value=0)
    swimming = forms.IntegerField(max_value=3, min_value=0)
    conspiracy_theory = forms.IntegerField(max_value=3, min_value=0)
    chantry_politics = forms.IntegerField(max_value=3, min_value=0)
    covert_culture = forms.IntegerField(max_value=3, min_value=0)
    cultural_savvy = forms.IntegerField(max_value=3, min_value=0)
    helmsman = forms.IntegerField(max_value=3, min_value=0)
    history_knowledge = forms.IntegerField(max_value=3, min_value=0)
    power_brokering = forms.IntegerField(max_value=3, min_value=0)
    propaganda = forms.IntegerField(max_value=3, min_value=0)
    theology = forms.IntegerField(max_value=3, min_value=0)
    unconventional_warface = forms.IntegerField(max_value=3, min_value=0)
    vice = forms.IntegerField(max_value=3, min_value=0)
    allies = forms.IntegerField(max_value=5, min_value=0)
    alternate_identity = forms.IntegerField(max_value=5, min_value=0)
    arcane = forms.IntegerField(max_value=5, min_value=0)
    avatar = forms.IntegerField(max_value=5, min_value=0)
    backup = forms.IntegerField(max_value=5, min_value=0)
    blessing = forms.IntegerField(max_value=5, min_value=0)
    certification = forms.IntegerField(max_value=5, min_value=0)
    chantry = forms.IntegerField(max_value=5, min_value=0)
    contacts = forms.IntegerField(max_value=5, min_value=0)
    cult = forms.IntegerField(max_value=5, min_value=0)
    demesne = forms.IntegerField(max_value=5, min_value=0)
    destiny = forms.IntegerField(max_value=5, min_value=0)
    dream = forms.IntegerField(max_value=5, min_value=0)
    enhancement = forms.IntegerField(max_value=5, min_value=0)
    fame = forms.IntegerField(max_value=5, min_value=0)
    familiar = forms.IntegerField(max_value=5, min_value=0)
    influence = forms.IntegerField(max_value=5, min_value=0)
    legend = forms.IntegerField(max_value=5, min_value=0)
    library = forms.IntegerField(max_value=5, min_value=0)
    mentor = forms.IntegerField(max_value=5, min_value=0)
    node = forms.IntegerField(max_value=5, min_value=0)
    past_lives = forms.IntegerField(max_value=5, min_value=0)
    patron = forms.IntegerField(max_value=5, min_value=0)
    rank = forms.IntegerField(max_value=5, min_value=0)
    requisitions = forms.IntegerField(max_value=5, min_value=0)
    resources = forms.IntegerField(max_value=5, min_value=0)
    retainers = forms.IntegerField(max_value=5, min_value=0)
    sanctum = forms.IntegerField(max_value=5, min_value=0)
    secret_weapons = forms.IntegerField(max_value=5, min_value=0)
    spies = forms.IntegerField(max_value=5, min_value=0)
    status_background = forms.IntegerField(max_value=5, min_value=0)
    totem = forms.IntegerField(max_value=5, min_value=0)
    wonder = forms.IntegerField(max_value=5, min_value=0)

    arete = forms.IntegerField(max_value=3, min_value=1)

    correspondence = forms.IntegerField(max_value=5, min_value=0)
    time = forms.IntegerField(max_value=5, min_value=0)
    spirit = forms.IntegerField(max_value=5, min_value=0)
    mind = forms.IntegerField(max_value=5, min_value=0)
    entropy = forms.IntegerField(max_value=5, min_value=0)
    prime = forms.IntegerField(max_value=5, min_value=0)
    forces = forms.IntegerField(max_value=5, min_value=0)
    matter = forms.IntegerField(max_value=5, min_value=0)
    life = forms.IntegerField(max_value=5, min_value=0)

    willpower = forms.IntegerField(max_value=10, min_value=5)

    native_language = forms.ModelChoiceField(queryset=Language.objects.all())
    languages = forms.ModelMultipleChoiceField(
        queryset=Language.objects.all(), required=False
    )

    def __init__(self, *args, **kwargs):
        self.char = kwargs.pop("character")

        kwargs["initial"] = self.char.get_attributes()
        kwargs["initial"].update(self.char.get_abilities())
        kwargs["initial"].update(self.char.get_backgrounds())
        kwargs["initial"].update(self.char.get_spheres())
        kwargs["initial"]["willpower"] = 5
        kwargs["initial"]["native_language"] = Language.objects.get(name="English")

        super().__init__(*args, **kwargs)
        for sphere in self.char.get_spheres().keys():
            self.fields[sphere] = forms.IntegerField(
                max_value=self.char.arete, min_value=getattr(self.char, sphere)
            )
        for attribute in self.char.get_attributes().keys():
            self.fields[attribute] = forms.IntegerField(
                max_value=5, min_value=getattr(self.char, attribute)
            )
        for ability in self.char.get_abilities().keys():
            self.fields[ability] = forms.IntegerField(
                max_value=5, min_value=getattr(self.char, ability)
            )
        for bg in self.char.get_backgrounds().keys():
            self.fields[bg] = forms.IntegerField(
                max_value=5, min_value=getattr(self.char, bg)
            )
        self.fields["arete"] = forms.IntegerField(
            max_value=3, min_value=self.char.arete
        )

    def total_cost_freebies(self):
        self.full_clean()
        total = 0
        attr_total = 0
        for key, value in self.char.get_attributes().items():
            attr_total += self.cleaned_data[key] - value
        total += 5 * attr_total
        abb_total = 0
        for key, value in self.char.get_abilities().items():
            if self.char.faction.name == "Akashayana" or key != "do":
                abb_total += self.cleaned_data[key] - value
        total += 2 * abb_total
        total += 4 * (self.char.arete - 1)
        sphere_total = 0
        for key, value in self.char.get_spheres().items():
            sphere_total += self.cleaned_data[key] - value
        total += 7 * sphere_total
        bg_total = 0
        for key, value in self.char.get_backgrounds().items():
            bg_total += self.cleaned_data[key] - value
            if key in ["totem", "enhancement", "sanctum"]:
                bg_total += self.cleaned_data[key] - value
        total += 1 * bg_total
        total += self.cleaned_data["willpower"] - 5
        mf_keys = [
            x
            for x in self.data.keys()
            if x.startswith("form-") and (x.endswith("-mf") or x.endswith("-rating"))
            if self.data[x] not in ["", "---"]
        ]
        mf_values = [int(self.data[x]) for x in mf_keys]
        mfs = dict(zip(mf_keys, mf_values))
        values = [v for k, v in mfs.items() if "-rating" in k]
        flaw_total = sum(x for x in values if x < 0)
        merit_total = sum(x for x in values if x > 0)
        if flaw_total < -7:
            return False
        total += merit_total
        total += flaw_total
        if "languages" in self.cleaned_data:
            total += self.cleaned_data["languages"].count()
        return total

    def assign(self):
        self.full_clean()
        for key in list(self.char.get_attributes().keys()):
            setattr(self.char, key, self.cleaned_data[key])
        for key in (
            list(self.char.get_talents().keys())
            + list(self.char.get_skills().keys())
            + list(self.char.get_knowledges().keys())
        ):
            if self.char.faction.name == "Akashayana" or key != "do":
                setattr(self.char, key, self.cleaned_data[key])
        for key in list(self.char.get_spheres().keys()):
            setattr(self.char, key, self.cleaned_data[key])
        for key in list(self.char.get_backgrounds().keys()):
            setattr(self.char, key, self.cleaned_data[key])
        self.char.willpower = self.data["willpower"]
        mf_keys = [
            x
            for x in self.data.keys()
            if x.startswith("form-") and (x.endswith("-mf") or x.endswith("-rating"))
            if self.data[x] not in ["", "---"]
        ]
        mf_values = [int(self.data[x]) for x in mf_keys]
        mfs = dict(zip(mf_keys, mf_values))
        num_mf = len(mfs) // 2
        new_mfs = {}
        for i in range(num_mf):
            new_mfs[mfs[f"form-{i}-mf"]] = mfs[f"form-{i}-rating"]
        for key, value in new_mfs.items():
            self.char.add_mf(MeritFlaw.objects.get(pk=key), value)
        self.char.languages.add(self.data["native_language"])
        if "languages" in self.data:
            self.char.languages.add(*self.data["languages"])


class MageDescriptionForm(forms.Form):
    age_of_awakening = forms.IntegerField(required=False)
    age = forms.IntegerField(required=False)
    apparent_age = forms.IntegerField(required=False)
    date_of_birth = forms.DateField(widget=forms.DateInput(), required=False)
    hair = forms.CharField(required=False)
    eyes = forms.CharField(required=False)
    ethnicity = forms.CharField(required=False)
    nationality = forms.CharField(required=False)
    height = forms.CharField(required=False)
    weight = forms.CharField(required=False)
    sex = forms.CharField(required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)

    childhood = forms.CharField(widget=forms.Textarea, required=False)
    history = forms.CharField(widget=forms.Textarea, required=False)
    goals = forms.CharField(widget=forms.Textarea, required=False)
    notes = forms.CharField(widget=forms.Textarea, required=False)

    awakening = forms.CharField(widget=forms.Textarea, required=False)
    seekings = forms.CharField(widget=forms.Textarea, required=False)
    quiets = forms.CharField(widget=forms.Textarea, required=False)
    avatar_description = forms.CharField(widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        self.char = kwargs.pop("character")
        super().__init__(*args, **kwargs)

    def complete(self):
        self.full_clean()
        if self.cleaned_data["age_of_awakening"] is None:
            return False
        if self.cleaned_data["age"] is None:
            return False
        if self.cleaned_data["apparent_age"] is None:
            return False
        if self.cleaned_data["date_of_birth"] is None:
            return False
        if self.cleaned_data["hair"] is None:
            return False
        if self.cleaned_data["eyes"] is None:
            return False
        if self.cleaned_data["ethnicity"] is None:
            return False
        if self.cleaned_data["nationality"] is None:
            return False
        if self.cleaned_data["height"] is None:
            return False
        if self.cleaned_data["weight"] is None:
            return False
        if self.cleaned_data["sex"] is None:
            return False
        if self.cleaned_data["description"] is None:
            return False
        if self.cleaned_data["childhood"] is None:
            return False
        if self.cleaned_data["history"] is None:
            return False
        if self.cleaned_data["goals"] is None:
            return False
        if self.cleaned_data["notes"] is None:
            return False
        if self.cleaned_data["awakening"] is None:
            return False
        if self.cleaned_data["seekings"] is None:
            return False
        if self.cleaned_data["quiets"] is None:
            return False
        if self.cleaned_data["avatar_description"] is None:
            return False
        return True


class MageSpecialtiesForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.char = kwargs.pop("character")
        super().__init__(*args, **kwargs)
        for key in {k: v for k, v in self.char.get_attributes().items() if v >= 4}:
            self.fields[key] = forms.CharField(
                required=False,
                widget=AutocompleteTextInput(
                    suggestions=[
                        x.name
                        for x in WoDSpecialty.objects.filter(stat=key).order_by("name")
                    ]
                ),
            )
        d = self.char.get_abilities()
        for key in [
            "art",
            "athletics",
            "crafts",
            "firearms",
            "martial_arts",
            "melee",
            "academics",
            "esoterica",
            "lore",
            "politics",
            "science",
        ]:
            if d[key] > 0:
                self.fields[key] = forms.CharField(
                    required=False,
                    widget=AutocompleteTextInput(
                        suggestions=[
                            x.name
                            for x in WoDSpecialty.objects.filter(stat=key).order_by(
                                "name"
                            )
                        ]
                    ),
                )
        for key in {k: v for k, v in d.items() if v >= 4}:
            self.fields[key] = forms.CharField(
                required=False,
                widget=AutocompleteTextInput(
                    suggestions=[
                        x.name
                        for x in WoDSpecialty.objects.filter(stat=key).order_by("name")
                    ]
                ),
            )
        for key in {k: v for k, v in self.char.get_spheres().items() if v >= 4}:
            self.fields[key] = forms.CharField(
                required=False,
                widget=AutocompleteTextInput(
                    suggestions=[
                        x.name
                        for x in WoDSpecialty.objects.filter(stat=key).order_by("name")
                    ]
                ),
            )

    def complete(self):
        complete = True
        self.full_clean()
        for field in self.fields:
            if field not in self.cleaned_data:
                complete = False
        return complete
