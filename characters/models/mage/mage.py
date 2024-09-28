import random
from collections import defaultdict

from characters.models.mage.effect import Effect
from characters.models.mage.faction import MageFaction
from characters.models.mage.focus import (
    Instrument,
    Paradigm,
    Practice,
    SpecializedPractice,
    Tenet,
)
from characters.models.mage.mtahuman import MtAHuman
from characters.models.mage.resonance import Resonance
from characters.models.mage.rote import Rote
from characters.models.mage.sphere import Sphere
from core.utils import add_dot, weighted_choice
from django.db import models
from django.db.models import Q
from django.urls import reverse
from locations.models.mage.library import Library
from locations.models.mage.node import Node


class Mage(MtAHuman):
    type = "mage"

    gameline = "mta"

    affiliation = models.ForeignKey(
        MageFaction,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="affiliations",
    )
    faction = models.ForeignKey(
        MageFaction,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="factions",
    )
    subfaction = models.ForeignKey(
        MageFaction,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="subfactions",
    )

    essence = models.CharField(
        default="",
        max_length=100,
        choices=[
            ("Dynamic", "Dynamic"),
            ("Pattern", "Pattern"),
            ("Primordial", "Primordial"),
            ("Questing", "Questing"),
        ],
    )

    correspondence = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    spirit = models.IntegerField(default=0)
    mind = models.IntegerField(default=0)
    entropy = models.IntegerField(default=0)
    prime = models.IntegerField(default=0)
    forces = models.IntegerField(default=0)
    matter = models.IntegerField(default=0)
    life = models.IntegerField(default=0)

    metaphysical_tenet = models.ForeignKey(
        Tenet,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="metaphysical_tenet_of",
    )
    personal_tenet = models.ForeignKey(
        Tenet,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="personal_tenet_of",
    )
    ascension_tenet = models.ForeignKey(
        Tenet,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="ascension_tenet_of",
    )

    other_tenets = models.ManyToManyField(Tenet, blank=True)
    practices = models.ManyToManyField(Practice, blank=True, through="PracticeRating")
    instruments = models.ManyToManyField(Instrument, blank=True)

    arete = models.IntegerField(default=0)

    affinity_sphere = models.ForeignKey(
        Sphere,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    CORR_NAMES = [("correspondence", "Correspondence"), ("data", "Data")]
    PRIME_NAMES = [("prime", "Prime"), ("primal_utility", "Primal Utility")]
    SPIRIT_NAMES = [
        ("spirit", "Spirit"),
        ("dimensional_science", "Dimensional Science"),
    ]

    corr_name = models.CharField(
        default="correspondence",
        choices=CORR_NAMES,
        max_length=100,
    )
    prime_name = models.CharField(
        default="prime",
        choices=PRIME_NAMES,
        max_length=100,
    )
    spirit_name = models.CharField(
        default="spirit",
        choices=SPIRIT_NAMES,
        max_length=100,
    )

    age_of_awakening = models.IntegerField(default=0)
    avatar_description = models.TextField(default="")

    resonance = models.ManyToManyField("Resonance", through="ResRating")

    rote_points = models.IntegerField(default=6)
    rotes = models.ManyToManyField(Rote, blank=True)

    quintessence = models.IntegerField(default=0)
    paradox = models.IntegerField(default=0)

    quiet = models.IntegerField(default=0)
    quiet_type = models.CharField(
        default="none",
        max_length=10,
        choices=[
            ("none", "None"),
            ("denial", "Denial"),
            ("madness", "Madness"),
            ("morbidity", "Morbidity"),
        ],
    )

    background_points = 7

    class Meta:
        verbose_name = "Mage"
        verbose_name_plural = "Mages"

    def get_update_url(self):
        return reverse("characters:mage:update:mage", kwargs={"pk": self.pk})

    def get_full_update_url(self):
        return reverse("characters:mage:update:mage_full", kwargs={"pk": self.pk})

    @classmethod
    def get_creation_url(cls):
        return reverse("characters:mage:create:mage")

    @classmethod
    def get_full_creation_url(cls):
        return reverse("characters:mage:create:mage_full")

    def add_ability(self, ability, maximum=5):
        return add_dot(self, ability, maximum)

    @staticmethod
    def get_paradox_wheel():
        return list(range(20))

    def get_inverted_paradox(self):
        return 19 - self.paradox

    def get_spheres(self):
        return {
            "correspondence": self.correspondence,
            "time": self.time,
            "spirit": self.spirit,
            "mind": self.mind,
            "entropy": self.entropy,
            "prime": self.prime,
            "forces": self.forces,
            "matter": self.matter,
            "life": self.life,
        }

    def has_faction(self):
        return self.faction is not None

    def set_faction(self, affiliation, faction, subfaction=None):
        if faction is not None:
            if faction.parent != affiliation:
                return False
        if subfaction is not None:
            if subfaction.parent != faction:
                return False
        self.affiliation = affiliation
        self.faction = faction
        self.subfaction = subfaction
        self.save()
        if affiliation is not None:
            if affiliation.name == "Marauders":
                self.random_quiet()
        return True

    def get_affiliation_weights(self):
        affiliation_weights = defaultdict(int)
        for faction in MageFaction.objects.filter(parent=None):
            if faction.name == "Traditions":
                affiliation_weights[faction] = 40
            elif faction.name == "Technocratic Union":
                affiliation_weights[faction] = 40
            elif faction.name == "The Disparate Alliance":
                affiliation_weights[faction] = 10
            elif faction.name == "Nephandi":
                affiliation_weights[faction] = 5
            elif faction.name == "Marauders":
                affiliation_weights[faction] = 5
            else:
                affiliation_weights[faction] = 1
        return affiliation_weights

    def random_faction(self, affiliation=None, faction=None, subfaction=None):
        if affiliation is None:
            affiliation_weights = self.get_affiliation_weights()
            affiliation = weighted_choice(affiliation_weights, ceiling=100)
            if subfaction is not None:
                faction = subfaction.parent
            if faction is not None:
                affiliation = faction.parent
        if faction is None:
            faction = (
                MageFaction.objects.filter(parent=affiliation).order_by("?").first()
            )
            if subfaction is not None:
                faction = subfaction.parent
        if subfaction is None:
            if (
                random.random() < 0.25
                or faction.name == "Order of Hermes"
                or affiliation.name == "Technocratic Union"
            ):
                if MageFaction.objects.filter(parent=faction).exists():
                    subfaction = (
                        MageFaction.objects.filter(parent=faction).order_by("?").first()
                    )
        return self.set_faction(affiliation, faction, subfaction=subfaction)

    def set_quiet_type(self, quiet_type):
        self.quiet_type = quiet_type
        return True

    def set_quiet_rating(self, quiet_rating):
        self.quiet = quiet_rating
        return True

    def random_quiet(self):
        return self.set_quiet_rating(random.randint(1, 5)) and self.set_quiet_type(
            random.choice(["denial", "madness", "morbidity"])
        )

    def has_focus(self):
        return (
            self.metaphysical_tenet
            and self.personal_tenet
            and self.ascension_tenet
            and self.total_practices() == self.arete
        )

    def set_focus(self, tenets, practices):
        for tenet in tenets:
            self.add_tenet(tenet)
        for prac in practices:
            self.add_practice(prac)
        return True

    def random_focus(self):
        self.metaphysical_tenet = (
            Tenet.objects.filter(tenet_type="met").order_by("?").first()
        )
        self.ascension_tenet = (
            Tenet.objects.filter(tenet_type="asc").order_by("?").first()
        )
        self.personal_tenet = (
            Tenet.objects.filter(tenet_type="per").order_by("?").first()
        )
        while (
            random.random() < 0.1 and Tenet.objects.filter(tenet_type="oth").count() > 0
        ):
            self.other_tenets.add(
                Tenet.objects.filter(tenet_type="oth")
                .exclude(pk__in=self.other_tenets.all())
                .order_by("?")
                .first()
            )
        practices = {
            x: 1
            for x in Practice.objects.exclude(
                polymorphic_ctype__model="specializedpractice"
            ).exclude(polymorphic_ctype__model="corruptedpractice")
        }
        if self.affiliation:
            for practice in self.affiliation.practices.all():
                practices[practice] += 1
        if self.faction:
            for practice in self.faction.practices.all():
                practices[practice] += 1
        if self.subfaction:
            for practice in self.subfaction.practices.all():
                practices[practice] += 1
        for tenet in (
            Tenet.objects.filter(
                pk__in=[
                    self.metaphysical_tenet.id,
                    self.ascension_tenet.id,
                    self.personal_tenet.id,
                ]
            )
            | self.other_tenets.all()
        ):
            for practice in tenet.associated_practices.all():
                practices[practice] += 1
            for practice in tenet.limited_practices.all():
                practices[practice] -= 1
        if SpecializedPractice.objects.filter(faction=self.faction).count() == 1:
            specialized_practice = SpecializedPractice.objects.get(faction=self.faction)
            practices[specialized_practice] = (
                10 + practices[specialized_practice.parent_practice]
            )
            practices = {
                k: v
                for k, v in practices.items()
                if k != specialized_practice.parent_practice and v > 0
            }
        min_key = min([x for x in practices.values()])
        if set([x for x in practices.values()]) != {min_key}:
            practices = {k: v for k, v in practices.items() if v > min_key}
        while self.total_practices() < self.arete:
            prac = weighted_choice(practices, ceiling=1000)
            self.add_practice(prac)
            practices[prac] += 1
        self.save()

    def add_background(self, background, maximum=5):
        if background in ["requisitions", "secret_weapons"]:
            if self.affiliation is not None:
                if self.affiliation.name != "Technocratic Union":
                    return False
                return add_dot(self, background, maximum)
            return False
        return add_dot(self, background, maximum)

    def total_backgrounds(self):
        return (
            super().total_backgrounds() + self.enhancement + self.sanctum + self.totem
        )

    def add_sphere(self, sphere):
        if self.faction is not None:
            if self.faction.name == "Ahl-i-Batin" and sphere == "entropy":
                return False
        return add_dot(self, sphere, min(self.arete, 5))

    def filter_spheres(self, minimum=0, maximum=5):
        return {k: v for k, v in self.get_spheres().items() if minimum <= v <= maximum}

    def total_spheres(self):
        return sum(self.get_spheres().values())

    def has_spheres(self):
        if self.affinity_sphere is not None:
            aff_flag = getattr(self, self.affinity_sphere.property_name) > 0
        else:
            aff_flag = False
        total = self.total_spheres() == 6
        return aff_flag and total

    def set_affinity_sphere(self, affinity):
        self.affinity_sphere = Sphere.objects.get(property_name=affinity)
        self.add_sphere(affinity)
        return True

    def get_affinity_sphere_options(self):
        q = Sphere.objects.none()
        if self.affiliation is not None:
            q |= self.affiliation.affinities.all()
        if self.faction is not None:
            q |= self.faction.affinities.all()
        if self.subfaction is not None:
            q |= self.subfaction.affinities.all()
        q = q.distinct()
        if q.count() == 0:
            return Sphere.objects.all()
        return q

    def has_affinity_sphere(self):
        return self.affinity_sphere is not None

    def random_affinity_sphere(self):
        self.set_affinity_sphere(random.choice(list(self.get_spheres().keys())))

    def random_sphere(self):
        max_sphere = min(
            [self.arete, max([self.practice_rating(x) for x in self.practices.all()])]
        )
        if len(self.filter_spheres(maximum=self.arete - 1).keys()) != 0:
            choice = weighted_choice(self.filter_spheres(maximum=max_sphere - 1))
            self.add_sphere(choice)
        else:
            raise ValueError(f"All Spheres Maxed out at Arete {self.arete}")

    def random_spheres(self):
        if self.affinity_sphere is None:
            self.random_affinity_sphere()
        while self.total_spheres() < 6:
            self.random_sphere()

    def set_corr_name(self, name):
        if name not in [x[0] for x in self.CORR_NAMES]:
            raise ValueError("Unknown Sphere Name")
        self.corr_name = name
        self.save()
        return True

    def set_prime_name(self, name):
        if name not in [x[0] for x in self.PRIME_NAMES]:
            raise ValueError("Unknown Sphere Name")
        self.prime_name = name
        self.save()
        return True

    def set_spirit_name(self, name):
        if name not in [x[0] for x in self.SPIRIT_NAMES]:
            raise ValueError("Unknown Sphere Name")
        self.spirit_name = name
        self.save()
        return True

    def add_arete(self, freebies=False):
        if freebies:
            cap = 3
        else:
            cap = 10
        return add_dot(self, "arete", cap)

    def random_arete(self):
        target = random.randint(1, 3)
        self.arete = target
        for i in range(target - 1):
            self.spent_freebies.append(
                self.freebie_spend_record("Arete", "arete", i + 2)
            )
        self.save()

    def has_essence(self):
        return self.essence != ""

    def set_essence(self, essence):
        self.essence = essence
        return True

    def random_essence(self):
        options = ["Dynamic", "Pattern", "Primordial", "Questing"]
        choice = random.choice(options)
        self.set_essence(choice)

    def add_resonance(self, resonance):
        if isinstance(resonance, str):
            resonance, _ = Resonance.objects.get_or_create(name=resonance)
        r, _ = ResRating.objects.get_or_create(resonance=resonance, mage=self)
        if r.rating == 5:
            return False
        r.rating += 1
        r.save()
        return True

    def subtract_resonance(self, resonance):
        if isinstance(resonance, str):
            resonance, _ = Resonance.objects.get_or_create(name=resonance)
        r, _ = ResRating.objects.get_or_create(resonance=resonance, mage=self)
        if r.rating == 0:
            return False
        r.rating -= 1
        r.save()
        for rr in ResRating.objects.filter(mage=self):
            if rr.rating == 0:
                rr.delete()
        return True

    def total_resonance(self):
        return sum(x.rating for x in ResRating.objects.filter(mage=self))

    def resonance_rating(self, resonance):
        if resonance not in self.resonance.all():
            return 0
        return ResRating.objects.get(mage=self, resonance=resonance).rating

    def filter_resonance(self, minimum=0, maximum=5):
        if minimum > 0:
            all_res = Resonance.objects.filter(mage__name__contains=self.name)
        else:
            all_res = Resonance.objects.all()

        maxed_resonance = [
            x.id for x in ResRating.objects.filter(mage=self, rating__gt=maximum)
        ]
        mined_resonance = [
            x.id for x in ResRating.objects.filter(mage=self, rating__lt=minimum)
        ]
        all_res = all_res.exclude(pk__in=maxed_resonance)
        all_res = all_res.exclude(pk__in=mined_resonance)
        if minimum > 0:
            all_res = all_res.filter(
                pk__in=[
                    x.resonance.id
                    for x in ResRating.objects.filter(mage=self, rating__gt=0)
                ]
            )
        return all_res

    def random_resonance(self):
        choice = self.choose_random_resonance()
        return self.add_resonance(choice)

    def choose_random_resonance(self):
        if random.random() < 0.7:
            possible = self.filter_resonance(minimum=1, maximum=4)
            if len(possible) > 0:
                choice = random.choice(possible)
                return choice
        while True:
            index = random.randint(1, Resonance.objects.last().id)
            if Resonance.objects.filter(pk=index).exists():
                choice = Resonance.objects.get(pk=index)
                if self.resonance_rating(choice) < 5:
                    return choice

    def random_ability(self, maximum=4):
        PRACTICE_ABILITY_WEIGHTING = 5
        PRIMARY_ABILITY_WEIGHTING = 5

        possibilities = self.filter_abilities(maximum=maximum)
        for practice in self.practices.all():
            for ability in practice.abilities.all():
                if ability.property_name in possibilities:
                    possibilities[ability.property_name] += PRACTICE_ABILITY_WEIGHTING
        for ability in possibilities:
            if ability in self.primary_abilities:
                possibilities[ability] *= PRIMARY_ABILITY_WEIGHTING
        choice = weighted_choice(possibilities, ceiling=100)
        self.add_ability(choice, 5)

    def random_abilities(self):
        ability_types = [13, 9, 5]
        random.shuffle(ability_types)
        while self.total_talents() < ability_types[0]:
            possibilities = self.get_talents()
            for practice in self.practices.all():
                for ability in practice.abilities.all():
                    if ability.property_name in possibilities:
                        possibilities[ability.property_name] += 3
            ability_choice = weighted_choice(possibilities, ceiling=100)
            self.add_ability(ability_choice, maximum=3)
        while self.total_skills() < ability_types[1]:
            possibilities = self.get_skills()
            for practice in self.practices.all():
                for ability in practice.abilities.all():
                    if ability.property_name in possibilities:
                        possibilities[ability.property_name] += 3
            ability_choice = weighted_choice(possibilities, ceiling=100)
            self.add_ability(ability_choice, maximum=3)
        while self.total_knowledges() < ability_types[2]:
            possibilities = self.get_knowledges()
            for practice in self.practices.all():
                for ability in practice.abilities.all():
                    if ability.property_name in possibilities:
                        possibilities[ability.property_name] += 3
            ability_choice = weighted_choice(possibilities, ceiling=100)
            self.add_ability(ability_choice, maximum=3)

    def add_effect(self, effect):
        if effect.is_learnable(self):
            r = Rote.objects.create(effect=effect)
            r.random(mage=self)
            self.rote_points -= effect.cost()
            self.rotes.add(r)
            return True
        return False

    def has_effects(self):
        return self.rote_points == 0

    def filter_effects(self, max_cost=100):
        effects = Effect.objects.filter(rote_cost__lte=max_cost)

        spheres = self.get_spheres()
        spheres = {k + "__lte": v for k, v in spheres.items()}
        q = Q(**spheres)
        return effects.filter(q)

    def random_effect(self):
        options = self.filter_effects(max_cost=self.rote_points)
        effect = random.choice(options)
        self.add_effect(effect)

    def random_effects(self):
        while self.rote_points > 0:
            self.random_effect()

    def total_effects(self):
        return sum(x.effect.cost() for x in self.rotes.all())

    def has_specialties(self):
        output = super().has_specialties()
        for sphere in self.filter_spheres(minimum=4):
            output = output and (self.specialties.filter(stat=sphere).count() > 0)
        return output

    def random_specialties(self):
        super().random_specialties()
        for sphere in self.filter_spheres(minimum=4):
            self.specialties.add(random.choice(self.filter_specialties(stat=sphere)))

    def has_mage_history(self):
        return self.age_of_awakening != 0 and self.avatar_description != ""

    def random_mage_history(self):
        self.awakening = "A thing that happened"
        self.seekings = "None"
        self.quiets = "None"
        self.age_of_awakening = 15
        self.avatar_description = "An Avatar"

    def xp_frequencies(self):
        return {
            "attribute": 16,
            "ability": 20,
            "background": 13,
            "willpower": 1,
            "sphere": 37,
            "arete": 10,
            "rote points": 2,
        }

    def random_xp_functions(self):
        return {
            "attribute": self.random_xp_attributes,
            "ability": self.random_xp_abilities,
            "background": self.random_xp_background,
            "willpower": self.random_xp_willpower,
            "sphere": self.random_xp_sphere,
            "arete": self.random_xp_arete,
            "rote points": self.random_xp_rote_points,
        }

    def random_xp_sphere(self):
        trait = weighted_choice(self.get_spheres())
        return self.spend_xp(trait)

    def random_xp_arete(self):
        return self.spend_xp("arete")

    def random_xp_rote_points(self):
        return self.spend_xp("rote points")

    def spend_xp(self, trait):
        output = super().spend_xp(trait)
        if output in [True, False]:
            return output
        if trait == "arete":
            cost = self.xp_cost("arete") * getattr(self, trait)
            if cost <= self.xp:
                if self.add_arete():
                    self.xp -= cost
                    self.add_to_spend(trait, getattr(self, trait), cost)
                    return True
                return False
            return False
        if trait in self.get_spheres():
            if self.affinity_sphere == trait:
                cost = self.xp_cost("affinity sphere") * getattr(self, trait)
            else:
                cost = self.xp_cost("sphere") * getattr(self, trait)
            if cost == 0:
                cost = 10
            if self.merits_and_flaws.filter(
                name=f"Sphere Natural - {trait.title()}"
            ).exists():
                cost *= 0.7
                if cost % 1 != 0:
                    cost += 1
                cost = int(cost)
            if self.merits_and_flaws.filter(
                name=f"Sphere Inept - {trait.title()}"
            ).exists():
                cost *= 1.3
                if cost % 1 != 0:
                    cost += 1
                cost = int(cost)
            if cost <= self.xp:
                if self.add_sphere(trait):
                    self.xp -= cost
                    self.add_to_spend(trait, getattr(self, trait), cost)
                    return True
                return False
            return False
        if trait == "rote points":
            cost = self.xp_cost("rote points")
            if cost <= self.xp:
                self.rote_points += 3
                self.xp -= cost
                self.add_to_spend(trait, getattr(self, trait.replace(" ", "_")), cost)
                return True
            return False
        return trait

    def xp_cost(self, trait):
        cost = super().xp_cost(trait)
        if cost != 10000:
            return cost
        costs = defaultdict(
            lambda: 10000,
            {
                "affinity sphere": 7,
                "new sphere": 10,
                "sphere": 8,
                "arete": 8,
                "rote points": 1,
            },
        )
        return costs[trait]

    def freebie_frequencies(self):
        return {
            "attribute": 15,
            "ability": 8,
            "background": 10,
            "willpower": 1,
            "meritflaw": 20,
            "sphere": 25,
            "arete": 5,
            "quintessence": 1,
            "rote points": 5,
            "resonance": 10,
        }

    def random_freebie_functions(self):
        return {
            "attribute": self.random_freebies_attributes,
            "ability": self.random_freebies_abilities,
            "background": self.random_freebies_background,
            "willpower": self.random_freebies_willpower,
            "meritflaw": self.random_freebies_meritflaw,
            "sphere": self.random_freebies_sphere,
            "arete": self.random_freebies_arete,
            "quintessence": self.random_freebies_quintessence,
            "rote points": self.random_freebies_rote_points,
            "resonance": self.random_freebies_resonance,
        }

    def freebie_cost(self, trait):
        cost = super().freebie_cost(trait)
        if cost != 10000:
            return cost
        costs = defaultdict(
            lambda: 10000,
            {
                "sphere": 7,
                "arete": 4,
                "quintessence": 1,
                "rote points": 1,
                "resonance": 3,
            },
        )
        return costs[trait]

    def spend_freebies(self, trait):
        output = super().spend_freebies(trait)
        if output in [True, False]:
            return output
        if trait in self.get_spheres():
            cost = self.freebie_cost("sphere")
            if cost <= self.freebies:
                if self.add_sphere(trait):
                    self.freebies -= cost
                    return True
                return False
            return False
        if trait == "arete":
            cost = self.freebie_cost("arete")
            if cost <= self.freebies:
                if self.add_arete(freebies=True):
                    self.freebies -= cost
                    return True
                return False
            return False
        if trait == "quintessence":
            cost = self.freebie_cost("quintessence")
            if cost <= self.freebies:
                if self.quintessence < 17:
                    self.quintessence += 4
                    self.freebies -= cost
                    return True
                return False
            return False
        if trait == "rote points":
            cost = self.freebie_cost("rote points")
            if cost <= self.freebies:
                self.rote_points += 4
                self.freebies -= cost
                return True
            return False
        if Resonance.objects.filter(name=trait).exists():
            cost = self.freebie_cost("resonance") * (self.total_resonance())
            if cost <= self.freebies:
                if self.add_resonance(trait):
                    self.freebies -= cost
                    return True
                return False
            return False
        return trait

    def random_freebies_sphere(self):
        trait = weighted_choice(self.get_spheres())
        return self.spend_freebies(trait)

    def random_freebies_arete(self):
        return self.spend_freebies("arete")

    def random_freebies_quintessence(self):
        return self.spend_freebies("quintessence")

    def random_freebies_rote_points(self):
        return self.spend_freebies("rote points")

    def random_freebies_resonance(self):
        trait = self.choose_random_resonance()
        return self.spend_freebies(trait)

    def has_library(self):
        return (
            sum([x.rank for x in Library.objects.filter(owned_by=self)]) == self.library
        )

    def random_library(self):
        if self.library > 0:
            l = Library.objects.create(
                name=f"{self.name}'s Library",
                rank=self.library,
                owner=self.owner,
                chronicle=self.chronicle,
                owned_by=self,
            )
            l.random(faction=self.faction)
            l.save()
            self.library_owned = l
            self.save()

    def has_node(self):
        return sum([x.rank for x in Node.objects.filter(owned_by=self)]) == self.node

    def random_node(self, favored_list=None):
        if self.node > 0:
            n = Node.objects.create(
                name="", owner=self.owner, chronicle=self.chronicle, owned_by=self
            )
            n.random(rank=self.node, favored_list=favored_list)
            if not n.has_name():
                n.set_name(f"{self.name}'s Node")
            n.save()
            self.node_owned = n
            self.save()

    def random(
        self,
        freebies=15,
        xp=0,
        ethnicity=None,
        affiliation=None,
        faction=None,
        subfaction=None,
        backgrounds=None,
    ):
        self.update_status("Ran")
        self.willpower = 5
        if backgrounds is None:
            backgrounds = {}
        self.freebies = freebies
        self.xp = xp
        self.random_arete()
        self.random_name(ethnicity=ethnicity)
        self.random_concept()
        self.random_archetypes()
        self.random_essence()
        self.random_faction(
            affiliation=affiliation, faction=faction, subfaction=subfaction
        )
        self.random_focus()
        self.random_attributes()
        self.random_abilities()
        self.random_backgrounds(backgrounds)
        self.random_affinity_sphere()
        self.random_spheres()
        self.random_history()
        self.random_resonance()
        self.random_finishing_touches()
        self.random_mage_history()
        self.mf_based_corrections()
        self.random_effects()
        self.random_specialties()
        self.random_node(favored_list=self.resonance.all())
        self.random_library()

    def freebie_cost(self, trait_type):
        mage_costs = {
            "sphere": 7,
            "arete": 4,
            "quintessence": 1,
            "tenet": 0,
            "practice": 1,
            "rotes": 1,
            "resonance": 3,
        }
        if trait_type in mage_costs.keys():
            return mage_costs[trait_type]
        return super().freebie_cost(trait_type)

    def xp_cost(self, trait_type, trait_value):
        mage_costs = {
            "new_sphere": 10,
            "affinity_sphere": 7,
            "sphere": 8,
            "arete": 8,
            "tenet": 0,
            "remove_tenet": 1,
            "new_practice": 3,
            "practice": 1,
            "rotes": 1,
        }
        if trait_type == "sphere" and trait_value == 0:
            return mage_costs["new_sphere"]
        if trait_type == "practice" and trait_value == 0:
            return mage_costs["new_practice"]
        elif trait_type in mage_costs.keys():
            return mage_costs[trait_type] * trait_value
        return super().xp_cost(trait_type, trait_value)

    def add_tenet(self, tenet):
        if tenet.tenet_type not in ["met", "asc", "per"]:
            self.other_tenets.add(tenet)
        if tenet.tenet_type == "met" and self.metaphysical_tenet is None:
            self.metaphysical_tenet = tenet
        elif tenet.tenet_type == "per" and self.personal_tenet is None:
            self.personal_tenet = tenet
        elif tenet.tenet_type == "asc" and self.ascension_tenet is None:
            self.ascension_tenet = tenet
        else:
            self.other_tenets.add(tenet)
        return True

    def add_practice(self, practice):
        pr = PracticeRating.objects.get_or_create(mage=self, practice=practice)[0]
        pr.rating += 1
        pr.save()
        return True

    def practice_rating(self, practice):
        prs = PracticeRating.objects.filter(mage=self)
        if practice not in [x.practice for x in prs]:
            return 0
        return PracticeRating.objects.get(mage=self, practice=practice).rating

    def total_practices(self):
        return sum([self.practice_rating(x) for x in Practice.objects.all()])


class ResRating(models.Model):
    mage = models.ForeignKey("Mage", on_delete=models.SET_NULL, null=True)
    resonance = models.ForeignKey(Resonance, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Mage Resonance Rating"
        verbose_name_plural = "Mage Resonance Ratings"


class PracticeRating(models.Model):
    mage = models.ForeignKey(Mage, on_delete=models.SET_NULL, null=True)
    practice = models.ForeignKey(Practice, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.mage.name}: {self.practice}: {self.rating}"
