import random

from characters.models.core.human import Human
from characters.models.mage.resonance import Resonance
from core.utils import add_dot, weighted_choice
from django.db import models
from django.urls import reverse
from locations.models.core.location import LocationModel
from locations.models.mage.library import Library
from locations.models.mage.node import Node
from locations.models.mage.realityzone import RealityZone


class Chantry(LocationModel):
    type = "chantry"

    faction = models.ForeignKey(
        "characters.MageFaction", blank=True, null=True, on_delete=models.SET_NULL
    )

    LEADERSHIP_CHOICES = [
        ("panel", "Panel of Cabal Leaders"),
        ("teachers", "Teachers"),
        ("triumvirate", "Triumvirate"),
        ("democracy", "Democracy"),
        ("anarchy", "Anarchy"),
        ("single_deacon", "Single Deacon"),
        ("council_of_elders", "Council of Elders"),
        ("meritocracy", "Meritocracy"),
    ]

    leadership_type = models.CharField(
        max_length=20, null=True, choices=LEADERSHIP_CHOICES
    )
    leaders = models.ManyToManyField(
        Human, blank=True, related_name="chantry_leader_at"
    )

    SEASONS = [
        ("spring", "Spring"),
        ("winter", "Winter"),
        ("summer", "Summer"),
        ("autumn", "Autumn"),
    ]

    season = models.CharField(
        max_length=100,
        null=True,
        choices=SEASONS,
    )

    CHANTRY_TYPES = [
        ("exploration", "Exploration"),
        ("ancestral", "Ancestral"),
        ("hereditary", "Hereditary"),
        ("college", "College"),
        ("squatter", "Squatter"),
        ("war", "War"),
        ("library", "Library"),
        ("healing", "Healing"),
        ("research", "Research"),
        ("fortress", "Fortress"),
        ("diplomatic", "Diplomatic"),
    ]

    chantry_type = models.CharField(
        max_length=100,
        null=True,
        choices=CHANTRY_TYPES,
    )

    rank = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    allies = models.IntegerField(default=0)
    arcane = models.IntegerField(default=0)
    backup = models.IntegerField(default=0)
    cult = models.IntegerField(default=0)
    elders = models.IntegerField(default=0)
    integrated_effects = models.IntegerField(default=0)
    retainers = models.IntegerField(default=0)
    spies = models.IntegerField(default=0)
    resources = models.IntegerField(default=0)
    enhancement = models.IntegerField(default=0)
    requisitions = models.IntegerField(default=0)
    reality_zone_rating = models.IntegerField(default=0)
    node_rating = models.IntegerField(default=0)
    library_rating = models.IntegerField(default=0)

    chantry_library = models.ForeignKey(
        Library, on_delete=models.SET_NULL, blank=True, null=True
    )
    nodes = models.ManyToManyField(Node, blank=True)
    reality_zone = models.ForeignKey(
        RealityZone, blank=True, null=True, on_delete=models.SET_NULL
    )

    members = models.ManyToManyField(Human, blank=True, related_name="member_of")
    cabals = models.ManyToManyField("characters.Cabal", blank=True)

    ambassador = models.ForeignKey(
        Human,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="ambassador_from",
    )
    node_tender = models.ForeignKey(
        Human,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="tends_node_at",
    )
    investigator = models.ManyToManyField(
        Human, blank=True, related_name="investigator_at"
    )
    guardian = models.ManyToManyField(Human, blank=True, related_name="guardian_of")
    teacher = models.ManyToManyField(Human, blank=True, related_name="teacher_at")

    factional_names = {
        "Akashayana": [
            "Monastery",
            "Torii",
            "Pagoda",
            "Bodhimandala",
            "Tao Chang",
            "Dojo",
            "Dojang",
            "Xiudaoyuan",
        ],
        "Celestial Chorus": ["Chapel", "Covenant", "Sanctuary", "Adytum", "Temple"],
        "Cult of Ecstasy": ["Pleasuredome"],
        "Dreamspeakers": ["Lodge"],
        "Euthanatos": ["Marabout"],
        "Order of Hermes": ["Covenant", "Chantry"],
        "Hollow Ones": ["Hideout", "Hole", "Crashspace", "Haunt"],
        "Society of Ether": ["Laboratory"],
        "Verbena": ["Covenhouse", "Circle", "Great Hall"],
        "Virtual Adepts": ["Epicenter", "Fortress", "Net"],
        "Traditions": ["Chantry"],
        "Technocratic Union": ["Construct"],
        "Kopa Loei": ["He'iau"],
    }

    class Meta:
        verbose_name = "Chantry"
        verbose_name_plural = "Chantries"

    def get_update_url(self):
        return reverse("locations:mage:update:chantry", args=[str(self.id)])

    @classmethod
    def get_creation_url(cls):
        return reverse("locations:mage:create:chantry")

    def get_heading(self):
        return "mta_heading"

    def random_name(self, name=None):
        if name is not None:
            return self.set_name(name)
        options = []
        current = self.faction
        while current is not None:
            if current.name in self.factional_names:
                options.extend(self.factional_names[current.name])
            current = current.parent
        if len(options) == 0:
            choice = "Chantry"
        else:
            choice = random.choice(options)
        adjective = Resonance.objects.order_by("?").first().name
        adjective = adjective.title()
        return self.set_name(f"{adjective} {choice}")

    def has_season(self):
        return self.season is not None

    def set_season(self, season):
        self.season = season
        self.save()
        return True

    def random_season(self, season=None):
        if season is None:
            season = random.choice(self.SEASONS)[0]
        return self.set_season(season)

    def has_chantry_type(self):
        return self.chantry_type is not None

    def set_chantry_type(self, chantry_type):
        self.chantry_type = chantry_type
        if chantry_type == "library":
            self.library_rating = 3
        self.save()
        return True

    def random_chantry_type(self, chantry_type=None):
        if chantry_type is None:
            chantry_type = random.choice(self.CHANTRY_TYPES)[0]
        return self.set_chantry_type(chantry_type)

    def trait_cost(self, trait):
        if trait in [
            "allies",
            "arcane",
            "backup",
            "cult",
            "elders",
            "integrated_effects",
            "library_rating",
            "retainers",
            "spies",
        ]:
            return 2
        if trait in ["node_rating", "resources"]:
            return 3
        if trait in ["enhancement", "requisitions"]:
            return 4
        if trait in ["reality_zone_rating"]:
            return 5
        return 1000

    def points_spent(self):
        return (
            2
            * (
                self.allies
                + self.arcane
                + self.backup
                + self.cult
                + self.elders
                + self.integrated_effects
                + self.library_rating
                + self.retainers
                + self.spies
            )
            + 3 * (self.node_rating + self.resources)
            + 4 * (self.enhancement + self.requisitions)
            + 5 * (self.reality_zone_rating)
        )

    def has_node(self):
        return self.total_node() == self.node_rating

    def add_node(self, node):
        self.nodes.add(node)
        self.save()

    def create_nodes(self, list_of_nodes=None):
        if list_of_nodes is not None:
            for node in list_of_nodes:
                self.add_node(node)
            return True
        node_ranks = []
        while sum(node_ranks) < self.node_rating:
            x = random.randint(1, min(5, self.node_rating - sum(node_ranks)))
            node_ranks.append(x)

        for i, rank in enumerate(node_ranks):
            n = Node.objects.create(name="", parent=self, owner=self.owner)
            n.random(rank=rank)
            if not n.has_name():
                n.set_name(f"{self.name}'s Node {i}")
            n.save()
            self.add_node(n)
        return True

    def total_node(self):
        return sum(x.rank for x in self.nodes.all())

    def has_library(self):
        if self.chantry_library is not None:
            return self.chantry_library.rank == self.chantry_library.num_books()
        return False

    def set_library(self, library):
        self.chantry_library = library
        library.parent = self
        library.save()
        return True

    def create_library(self, library=None):
        if library is not None:
            return self.set_library(library)
        l, _ = Library.objects.get_or_create(
            name=f"{self.name} Library", owner=self.owner
        )
        l.rank = self.library_rating
        while l.num_books() < l.rank:
            l.random_book()
        return self.set_library(l)

    def random_points(self, rank=None):
        if rank is None:
            rank = self.rank
        if rank == 1:
            self.points = random.randint(10, 20)
        if rank == 2:
            self.points = random.randint(21, 30)
        if rank == 3:
            self.points = random.randint(31, 70)
        if rank == 4:
            self.points = random.randint(71, 100)
        if rank == 5:
            self.points = random.randint(101, 200)

    def random_rank(self, rank=None):
        if rank is None:
            rank = random.randint(1, 5)
        self.set_rank(rank)

    def set_rank(self, rank):
        self.rank = rank
        self.random_points(rank=rank)
        return True

    def random_populate(self):
        from characters.models.mage.cabal import Cabal

        while sum(x.chantry for x in self.members.all()) < self.points:
            c = Cabal.objects.create(
                name=f"{self.name} Cabal {self.cabals.count()}", owner=self.owner
            )
            modifier = random.randint(-1, 1)
            c.random(
                num_chars=5 + modifier,
                xp=50 + modifier * 50,
                faction=self.faction,
                chantry=3 + modifier,
                user=self.owner,
            )
            self.cabals.add(c)
            for member in c.members.all():
                self.members.add(member)
        all_characters = self.members.all()
        self.ambassador = max(all_characters, key=lambda x: x.charisma + x.expression)
        self.node_tender = max(all_characters, key=lambda x: x.prime)
        self.investigator.add(
            max(all_characters, key=lambda x: x.perception + x.investigation)
        )
        self.guardian.add(max(all_characters, key=lambda x: x.dexterity + x.firearms))
        self.teacher.add(
            max(all_characters, key=lambda x: x.manipulation + x.instruction)
        )
        if self.leadership_type == "panel":
            for cabal in self.cabals.all():
                self.leaders.add(cabal.leader)
        elif self.leadership_type == "triumvirate":
            all_characters = list(all_characters)
            all_characters.sort(key=lambda x: -x.arete)
            self.leaders.set(all_characters[:3])
        elif self.leadership_type == "single_deacon":
            all_characters = list(all_characters)
            all_characters.sort(key=lambda x: -x.arete)
            max_arete_chars = [
                x for x in all_characters if x.arete == all_characters[0].arete
            ]
            self.leaders.add(random.choice(max_arete_chars))
        self.save()

    def random_leadership_type(self, leadership_type=None):
        if leadership_type is not None:
            self.leadership_type = leadership_type
        else:
            self.leadership_type = random.choice(self.LEADERSHIP_CHOICES)[0]
        return True

    def random(
        self,
        rank=None,
        leadership_type=None,
        name=None,
        season=None,
        chantry_type=None,
        faction=None,
    ):
        self.update_status("Ran")
        self.random_leadership_type(leadership_type=leadership_type)
        self.random_faction(faction=faction)
        self.random_name(name=name)
        self.random_season(season=season)
        self.random_chantry_type(chantry_type=chantry_type)
        self.random_rank(rank=rank)
        self.random_populate()
        tmp = self.faction
        f = [tmp.name]
        while tmp.parent is not None:
            tmp = tmp.parent
            f.append(tmp.name)
        while self.points - self.points_spent() > 1:
            d = self.get_traits()
            if "Technocratic Union" not in f:
                d = {
                    k: v
                    for k, v in d.items()
                    if k not in ["requisitions", "enhancement"]
                }
            choice = weighted_choice(d)
            if self.trait_cost(choice) <= self.points - self.points_spent():
                if choice != "node_rating":
                    add_dot(self, choice, maximum=10)
                else:
                    add_dot(self, choice, maximum=100)
        self.create_nodes()
        self.create_library()

    def get_traits(self):
        return {
            "allies": self.allies,
            "arcane": self.arcane,
            "backup": self.backup,
            "cult": self.cult,
            "elders": self.elders,
            "integrated_effects": self.integrated_effects,
            "retainers": self.retainers,
            "spies": self.spies,
            "resources": self.resources,
            "enhancement": self.enhancement,
            "requisitions": self.requisitions,
            "reality_zone": self.reality_zone_rating,
            "node_rating": self.node_rating,
            "library_rating": self.library_rating,
        }

    def set_faction(self, faction):
        self.faction = faction
        return True

    def has_faction(self):
        return self.faction is not None

    def random_faction(self, faction=None):
        from characters.models.mage.faction import MageFaction

        if faction is None:
            faction_probs = {}
            for faction in MageFaction.objects.all():
                if faction.parent is None:
                    faction_probs[faction] = 30
                elif faction.parent.parent is None:
                    faction_probs[faction] = 10
                elif faction.parent.parent.parent is None:
                    faction_probs[faction] = 1
                else:
                    faction_probs[faction] = 0
                faction = weighted_choice(faction_probs, ceiling=100)
        return self.set_faction(faction)
