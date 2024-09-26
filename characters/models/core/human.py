import random
from datetime import date, timedelta

from characters.models.core.archetype import Archetype
from characters.models.core.background import Background, BackgroundRating
from characters.models.core.character import Character
from characters.models.core.derangement import Derangement
from characters.models.core.meritflaw import MeritFlaw, MeritFlawRating
from characters.models.core.specialty import Specialty
from characters.utils import random_ethnicity, random_height, random_name, random_weight
from core.models import Language
from core.utils import add_dot, weighted_choice
from django.db import models
from django.db.models import F, Q
from django.urls import reverse
from game.models import ObjectType


class Human(Character):
    type = "human"

    gameline = "wod"

    allowed_backgrounds = ["contacts", "mentor"]

    nature = models.ForeignKey(
        Archetype,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="nature_of",
    )
    demeanor = models.ForeignKey(
        Archetype,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="demeanor_of",
    )

    strength = models.IntegerField(default=1)
    dexterity = models.IntegerField(default=1)
    stamina = models.IntegerField(default=1)
    perception = models.IntegerField(default=1)
    intelligence = models.IntegerField(default=1)
    wits = models.IntegerField(default=1)
    charisma = models.IntegerField(default=1)
    manipulation = models.IntegerField(default=1)
    appearance = models.IntegerField(default=1)

    alertness = models.IntegerField(default=0)
    athletics = models.IntegerField(default=0)
    brawl = models.IntegerField(default=0)
    empathy = models.IntegerField(default=0)
    expression = models.IntegerField(default=0)
    intimidation = models.IntegerField(default=0)
    streetwise = models.IntegerField(default=0)
    subterfuge = models.IntegerField(default=0)

    crafts = models.IntegerField(default=0)
    drive = models.IntegerField(default=0)
    etiquette = models.IntegerField(default=0)
    firearms = models.IntegerField(default=0)
    melee = models.IntegerField(default=0)
    stealth = models.IntegerField(default=0)

    academics = models.IntegerField(default=0)
    computer = models.IntegerField(default=0)
    investigation = models.IntegerField(default=0)
    medicine = models.IntegerField(default=0)
    science = models.IntegerField(default=0)

    specialties = models.ManyToManyField(Specialty, blank=True)

    languages = models.ManyToManyField(Language, blank=True)

    willpower = models.IntegerField(default=3)
    derangements = models.ManyToManyField("Derangement", blank=True)

    age = models.IntegerField(blank=True, null=True)
    apparent_age = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    merits_and_flaws = models.ManyToManyField(
        MeritFlaw, blank=True, through=MeritFlawRating, related_name="flawed"
    )

    history = models.TextField(default="", blank=True, null=True)
    goals = models.TextField(default="", blank=True, null=True)
    notes = models.TextField(default="", blank=True, null=True)

    xp = models.IntegerField(default=0)
    spent_xp = models.JSONField(default=list)

    current_health_levels = models.CharField(default="", max_length=100, blank=True)
    max_health_levels = models.IntegerField(default=7)

    freebies = models.IntegerField(default=15)
    spent_freebies = models.JSONField(default=list)
    background_points = 5

    class Meta:
        verbose_name = "Human"
        verbose_name_plural = "Humans"

    def get_full_update_url(self):
        return reverse("characters:update:human_full", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("characters:update:human", kwargs={"pk": self.pk})

    @classmethod
    def get_full_creation_url(cls):
        return reverse("characters:create:human_full")

    @classmethod
    def get_creation_url(cls):
        return reverse("characters:create:human")

    def get_heading(self):
        return "wod_heading"

    def total_background_rating(self, bg_name):
        return sum(
            [
                x.rating
                for x in BackgroundRating.objects.filter(
                    bg__property_name=bg_name, char=self
                )
            ]
        )

    @property
    def contacts(self):
        return self.total_background_rating("contacts")

    @property
    def mentor(self):
        return self.total_background_rating("mentor")

    def num_languages(self):
        mf_list = self.merits_and_flaws.all().values_list("name", flat=True)
        if "Language" not in mf_list:
            return 0
        language_rating = self.mf_rating(MeritFlaw.objects.get(name="Language"))
        if "Natural Linguist" in mf_list:
            language_rating *= 2
        return language_rating

    def add_willpower(self):
        return add_dot(self, "willpower", 10)

    def has_finishing_touches(self):
        return (
            self.age is not None
            and self.date_of_birth is not None
            and self.description is not None
            and self.apparent_age is not None
        )

    def has_history(self):
        return self.history != "" and self.goals != ""

    def get_wound_penalty(self):
        health_levels = len(self.current_health_levels)
        if health_levels <= self.max_health_levels - 6:
            return 0
        if health_levels <= self.max_health_levels - 4:
            return -1
        if health_levels <= self.max_health_levels - 2:
            return -2
        if health_levels <= self.max_health_levels - 1:
            return -5
        return -1000

    def add_bashing(self):
        if len(self.current_health_levels) < self.max_health_levels:
            self.current_health_levels += "B"
        elif "B" in self.current_health_levels:
            self.current_health_levels = self.current_health_levels.replace("B", "L", 1)
        self.current_health_levels = "".join(
            sorted(self.current_health_levels, key=self.sort_damage)
        )

    @staticmethod
    def sort_damage(damage_type):
        if damage_type == "B":
            return 2
        if damage_type == "L":
            return 1
        return 0

    def add_aggravated(self):
        if len(self.current_health_levels) < self.max_health_levels:
            self.current_health_levels += "A"
        self.current_health_levels = "".join(
            sorted(self.current_health_levels, key=self.sort_damage)
        )

    def add_lethal(self):
        if len(self.current_health_levels) < self.max_health_levels:
            self.current_health_levels += "L"
        self.current_health_levels = "".join(
            sorted(self.current_health_levels, key=self.sort_damage)
        )

    def has_archetypes(self):
        return self.nature is not None and self.demeanor is not None

    def set_archetypes(self, nature, demeanor):
        self.nature = nature
        self.demeanor = demeanor
        return True

    def get_mf_and_rating_list(self):
        return [(x.name, self.mf_rating(x)) for x in self.merits_and_flaws.all()]

    def add_mf(self, mf, rating):
        if rating in mf.get_ratings():
            mfr, _ = MeritFlawRating.objects.get_or_create(character=self, mf=mf)
            mfr.rating = rating
            mfr.save()
            if mf.name in ["Language", "Natural Linguist"] and self.status == "Ran":
                num_languages = self.mf_rating(MeritFlaw.objects.get(name="Language"))
                if self.merits_and_flaws.filter(name="Natural Linguist").exists():
                    num_languages *= 2
                while self.languages.count() < num_languages:
                    self.add_random_language()
            if mf.name == "Deranged" and self.status == "Ran":
                self.random_derangement()
            return True
        return False

    def filter_mfs(self):
        character_type = self.type
        if character_type in ["fomor"]:
            character_type = "human"

        new_mfs = MeritFlaw.objects.exclude(pk__in=self.merits_and_flaws.all())

        non_max_mf = MeritFlawRating.objects.filter(character=self).exclude(
            Q(rating=F("mf__max_rating"))
        )

        had_mfs = MeritFlaw.objects.filter(pk__in=non_max_mf)
        mf = new_mfs | had_mfs
        if self.has_max_flaws():
            mf = mf.filter(max_rating__gt=0)
        character_type_object = ObjectType.objects.get(name=character_type)
        return mf.filter(allowed_types=character_type_object)

    def mf_rating(self, mf):
        if mf not in self.merits_and_flaws.all():
            return 0
        return MeritFlawRating.objects.get(character=self, mf=mf).rating

    def has_max_flaws(self):
        return self.total_flaws() <= -7

    def total_flaws(self):
        return sum(
            x.rating
            for x in MeritFlawRating.objects.filter(character=self)
            if x.rating < 0
        )

    def total_merits(self):
        return sum(
            x.rating
            for x in MeritFlawRating.objects.filter(character=self)
            if x.rating > 0
        )

    def add_derangement(self, derangement):
        if derangement in self.derangements.all():
            return False
        self.derangements.add(derangement)
        return True

    def get_specialty(self, stat):
        spec = self.specialties.filter(stat=stat).first()
        if spec is None:
            return None
        return spec.name

    def filter_specialties(self, stat=None):
        if stat is None:
            return Specialty.objects.all().exclude(pk__in=self.specialties.all())
        return Specialty.objects.filter(stat=stat).exclude(
            pk__in=self.specialties.all()
        )

    def add_attribute(self, attribute, maximum=5):
        return add_dot(self, attribute, maximum)

    def get_attributes(self):
        tmp = {}
        tmp.update(self.get_physical_attributes())
        tmp.update(self.get_mental_attributes())
        tmp.update(self.get_social_attributes())
        return tmp

    def get_physical_attributes(self):
        return {
            "strength": self.strength,
            "dexterity": self.dexterity,
            "stamina": self.stamina,
        }

    def get_social_attributes(self):
        return {
            "charisma": self.charisma,
            "manipulation": self.manipulation,
            "appearance": self.appearance,
        }

    def get_mental_attributes(self):
        return {
            "perception": self.perception,
            "intelligence": self.intelligence,
            "wits": self.wits,
        }

    def total_physical_attributes(self):
        return sum(self.get_physical_attributes().values())

    def total_social_attributes(self):
        return sum(self.get_social_attributes().values())

    def total_mental_attributes(self):
        return sum(self.get_mental_attributes().values())

    def total_attributes(self):
        return sum(self.get_attributes().values())

    def random_attributes(self, primary=7, secondary=5, tertiary=3):
        attribute_types = [primary, secondary, tertiary]
        random.shuffle(attribute_types)
        while self.total_physical_attributes() < attribute_types[0] + 3:
            attribute_choice = weighted_choice(
                self.get_physical_attributes(), floor=3, ceiling=3
            )
            add_dot(self, attribute_choice, 5)
        while self.total_social_attributes() < attribute_types[1] + 3:
            attribute_choice = weighted_choice(
                self.get_social_attributes(), floor=3, ceiling=3
            )
            add_dot(self, attribute_choice, 5)
        while self.total_mental_attributes() < attribute_types[2] + 3:
            attribute_choice = weighted_choice(
                self.get_mental_attributes(), floor=3, ceiling=3
            )
            add_dot(self, attribute_choice, 5)

    def has_attributes(self, primary=7, secondary=5, tertiary=3):
        triple = [
            self.total_physical_attributes(),
            self.total_mental_attributes(),
            self.total_social_attributes(),
        ]
        triple.sort()
        return triple == [3 + tertiary, 3 + secondary, 3 + primary]

    def filter_attributes(self, minimum=0, maximum=5):
        return {
            k: v for k, v in self.get_attributes().items() if minimum <= v <= maximum
        }

    def random_attribute(self):
        choice = weighted_choice(self.filter_attributes(maximum=4))
        self.add_attribute(choice, 5)

    def add_ability(self, ability, maximum=4):
        return add_dot(self, ability, maximum)

    def random_ability(self, maximum=4):
        choice = weighted_choice(
            self.filter_abilities(maximum=maximum), ceiling=5, floor=0
        )
        self.add_ability(choice, 5)

    def get_abilities(self):
        tmp = {}
        tmp.update(self.get_talents())
        tmp.update(self.get_skills())
        tmp.update(self.get_knowledges())
        return tmp

    def filter_abilities(self, minimum=0, maximum=5):
        return {
            k: v for k, v in self.get_abilities().items() if minimum <= v <= maximum
        }

    def get_talents(self):
        return {
            "alertness": self.alertness,
            "athletics": self.athletics,
            "brawl": self.brawl,
            "empathy": self.empathy,
            "expression": self.expression,
            "intimidation": self.intimidation,
            "streetwise": self.streetwise,
            "subterfuge": self.subterfuge,
        }

    def get_skills(self):
        return {
            "crafts": self.crafts,
            "drive": self.drive,
            "etiquette": self.etiquette,
            "firearms": self.firearms,
            "melee": self.melee,
            "stealth": self.stealth,
        }

    def get_knowledges(self):
        return {
            "academics": self.academics,
            "computer": self.computer,
            "investigation": self.investigation,
            "medicine": self.medicine,
            "science": self.science,
        }

    def total_talents(self):
        return sum(self.get_talents().values())

    def total_skills(self):
        return sum(self.get_skills().values())

    def total_knowledges(self):
        return sum(self.get_knowledges().values())

    def random_abilities(self, primary=13, secondary=9, tertiary=5):
        ability_types = [primary, secondary, tertiary]
        random.shuffle(ability_types)
        while self.total_talents() < ability_types[0]:
            ability_choice = weighted_choice(self.get_talents())
            self.add_ability(ability_choice, maximum=3)
        while self.total_skills() < ability_types[1]:
            ability_choice = weighted_choice(self.get_skills())
            self.add_ability(ability_choice, maximum=3)
        while self.total_knowledges() < ability_types[2]:
            ability_choice = weighted_choice(self.get_knowledges())
            self.add_ability(ability_choice, maximum=3)

    def total_abilities(self):
        return sum(self.get_abilities().values())

    def has_abilities(self, primary=13, secondary=9, tertiary=5):
        triple = [self.total_talents(), self.total_skills(), self.total_knowledges()]
        triple.sort()
        return triple == [tertiary, secondary, primary]

    def random_name(self, ethnicity=None):
        if self.ethnicity is None:
            ethnicity = random_ethnicity()
        sex = random.random()
        if sex < 0.495:
            self.sex = "Male"
            gender = "m"
        elif sex < 0.99:
            self.sex = "Female"
            gender = "f"
        else:
            self.sex = "Other"
            gender = "mf"
        if not self.has_name():
            name = random_name(gender, ethnicity)
            count = 0
            while Character.objects.filter(name=name).exists() and count < 20:
                self.ethnicity = random_ethnicity()
                name = random_name(gender, ethnicity)
                count += 1
            if count == 20:
                name = f"Random Name {random.randint(1, 10000000000)}"
            self.set_name(name)

    def random_archetypes(self):
        self.nature = Archetype.objects.order_by("?").first()
        self.demeanor = Archetype.objects.order_by("?").first()

    def add_specialty(self, specialty):
        if getattr(self, specialty.stat) < 4 and specialty.stat not in [
            "arts",
            "athletics",
            "crafts",
            "firearms",
            "melee",
            "academics",
            "esoterica",
            "lore",
            "politics",
            "science",
        ]:
            return False
        if specialty in self.specialties.all():
            return False
        self.specialties.add(specialty)
        return True

    def has_specialties(self):
        output = True
        for attribute in self.filter_attributes(minimum=4):
            output = output and (self.specialties.filter(stat=attribute).count() > 0)
        for ability in self.filter_abilities(minimum=4):
            output = output and (self.specialties.filter(stat=ability).count() > 0)
        for ability in [
            x
            for x in self.filter_abilities(minimum=1)
            if x
            in [
                "arts",
                "athletics",
                "crafts",
                "firearms",
                "melee",
                "academics",
                "esoterica",
                "lore",
                "politics",
                "science",
            ]
        ]:
            output = output and (self.specialties.filter(stat=ability).count() > 0)
        return output

    def random_specialty(self, stat):
        options = self.filter_specialties(stat=stat)
        return self.add_specialty(random.choice(options))

    def random_specialties(self):
        need_specialty = []
        for attribute in self.filter_attributes(minimum=4):
            if attribute not in need_specialty:
                need_specialty.append(attribute)
        for ability in self.filter_abilities(minimum=4):
            if ability not in need_specialty:
                need_specialty.append(ability)
        for ability in [
            x
            for x in self.filter_abilities(minimum=1)
            if x
            in [
                "arts",
                "athletics",
                "crafts",
                "firearms",
                "melee",
                "academics",
                "esoterica",
                "lore",
                "politics",
                "science",
            ]
        ]:
            if ability not in need_specialty:
                need_specialty.append(ability)
        for stat in need_specialty:
            self.specialties.add(random.choice(self.filter_specialties(stat=stat)))

    def get_backgrounds(self):
        return {
            "contacts": self.contacts,
            "mentor": self.mentor,
        }

    def add_background(self, background, maximum=5):
        if isinstance(background, str):
            bg = Background.objects.get(property_name=background)
            ratings = BackgroundRating.objects.filter(char=self, bg=bg)
            if ratings.filter(rating__lt=5).count() > 0:
                background = ratings.filter(rating__lt=5).first()
            else:
                background = BackgroundRating.objects.create(char=self, bg=bg)
        elif isinstance(background, Background):
            ratings = BackgroundRating.objects.filter(char=self, bg=background)
            if ratings.filter(rating__lt=5).count() > 0:
                background = ratings.filter(rating__lt=5).first()
            else:
                background = BackgroundRating.objects.create(char=self, bg=background)
        else:
            raise ValueError(
                "Must be a background name, Background object, or BackgroundRating object"
            )
        if background.rating == 5:
            return False
        background.rating += 1
        background.save()
        return True

    def total_backgrounds(self):
        return sum(self.get_backgrounds().values())

    def filter_backgrounds(self, minimum=0, maximum=5):
        return {
            k: v for k, v in self.get_backgrounds().items() if minimum <= v <= maximum
        }

    def has_backgrounds(self):
        if self.total_backgrounds() > self.background_points:
            self.freebies -= self.total_backgrounds() - self.background_points
        return self.total_backgrounds() >= self.background_points

    def random_background(self):
        choice = weighted_choice(self.get_backgrounds())
        return self.add_background(choice)

    def random_backgrounds(self, backgrounds=None):
        if backgrounds is None:
            backgrounds = {}
        for trait, value in backgrounds.items():
            setattr(self, trait, value)
        while not self.has_backgrounds():
            self.random_background()

    def add_random_language(self):
        d = {
            l.name: l.frequency
            for l in Language.objects.all()
            if l not in self.languages.all()
        }
        if len(d) == 0:
            return False
        choice = weighted_choice(d)
        choice = Language.objects.get(name=choice)
        self.languages.add(choice)
        self.save()
        return True

    def random_derangement(self):
        d = (
            Derangement.objects.exclude(pk__in=self.derangements.all())
            .order_by("?")
            .first()
        )
        return self.add_derangement(d)

    def random_birthdate(self, age):
        earliest_date = date.today() - timedelta(days=(age + 1) * 365)
        int_delta = 365 * 24 * 60 * 60
        random_second = random.randrange(int_delta)
        return earliest_date + timedelta(seconds=random_second)

    def random_finishing_touches(self):
        self.age = random.randint(18, 80)
        birthday = self.random_birthdate(self.age)
        self.date_of_birth = birthday
        self.description = "Description"
        self.apparent_age = self.age
        self.save()

    def random_history(self):
        self.history = "History"
        self.goals = "Goals"
        self.save()

    def mf_based_corrections(self):
        if self.merits_and_flaws.filter(name="Ability Deficit").exists():
            stats_to_lose = random.choice(
                [self.get_talents(), self.get_skills(), self.get_knowledges()]
            )
            total_removed = 0
            for key, value in stats_to_lose.items():
                if value > 3:
                    total_removed += value - 3
                    stats_to_lose[key] = 3
                    setattr(self, key, 3)
            while total_removed > 5:
                tmp = {k: v for k, v in stats_to_lose.item() if v < 3}
                new_stat = weighted_choice(tmp)
                if self.add_ability(new_stat):
                    stats_to_lose[new_stat] += 1
                    total_removed -= 1
            while total_removed < 5:
                new_stat = weighted_choice(stats_to_lose)
                stats_to_lose[new_stat] -= 1
                setattr(self, new_stat, stats_to_lose[new_stat])
                total_removed += 1

    def random(self, freebies=15, xp=0, ethnicity=None):
        self.update_status("Ran")
        self.freebies = freebies
        self.xp = xp
        self.random_name(ethnicity=ethnicity)
        self.random_concept()
        self.random_archetypes()
        self.random_attributes()
        self.random_abilities()
        self.random_backgrounds()
        self.mf_based_corrections()
        self.random_specialties()
        self.random_finishing_touches()
        self.random_history()

    def freebie_cost(self, trait_type):
        costs = {
            "attribute": 5,
            "ability": 2,
            "background": 1,
            "willpower": 1,
            "meritflaw": "rating",
        }
        return costs[trait_type]

    def freebie_spend_record(self, trait, trait_type, value, cost=None):
        if cost is None:
            cost = self.freebie_cost(trait_type)
        return {
            "trait": trait,
            "value": value,
            "cost": cost,
        }

    def xp_cost(self, trait_type, trait_value):
        costs = {
            "new_ability": 3,
            "attribute": 4,
            "ability": 2,
            "background": 3,
            "willpower": 1,
        }
        if trait_type == "ability" and trait_value == 0:
            return costs["new_ability"]
        return costs["trait_type"] * trait_value
