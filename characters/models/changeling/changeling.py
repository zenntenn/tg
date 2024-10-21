import random
from collections import defaultdict

from characters.models.changeling.ctdhuman import CtDHuman
from characters.models.changeling.house import House
from characters.models.changeling.kith import Kith
from characters.models.changeling.legacy import Legacy
from core.utils import add_dot, weighted_choice
from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class Changeling(CtDHuman):
    type = "changeling"

    court = models.CharField(
        default="",
        max_length=20,
        choices=[("seelie", "Seelie"), ("unseelie", "Unseelie")],
    )
    seelie_legacy = models.ForeignKey(
        Legacy,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="seelie_legacy_of",
    )
    unseelie_legacy = models.ForeignKey(
        Legacy,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="unseelie_legacy_of",
    )

    kith = models.ForeignKey(Kith, null=True, blank=True, on_delete=models.SET_NULL)
    seeming = models.CharField(
        default="",
        max_length=15,
        choices=[("childling", "Childling"), ("wilder", "Wilder"), ("grump", "Grump")],
    )
    house = models.ForeignKey(House, null=True, blank=True, on_delete=models.SET_NULL)

    autumn = models.IntegerField(default=0)
    chicanery = models.IntegerField(default=0)
    chronos = models.IntegerField(default=0)
    contract = models.IntegerField(default=0)
    dragons_ire = models.IntegerField(default=0)
    legerdemain = models.IntegerField(default=0)
    metamorphosis = models.IntegerField(default=0)
    naming = models.IntegerField(default=0)
    oneiromancy = models.IntegerField(default=0)
    primal = models.IntegerField(default=0)
    pyretics = models.IntegerField(default=0)
    skycraft = models.IntegerField(default=0)
    soothsay = models.IntegerField(default=0)
    sovereign = models.IntegerField(default=0)
    spring = models.IntegerField(default=0)
    summer = models.IntegerField(default=0)
    wayfare = models.IntegerField(default=0)
    winter = models.IntegerField(default=0)

    actor = models.IntegerField(default=0)
    fae = models.IntegerField(default=0)
    nature_realm = models.IntegerField(default=0)
    prop = models.IntegerField(default=0)
    scene = models.IntegerField(default=0)
    time = models.IntegerField(default=0)

    banality = models.IntegerField(default=3)
    glamour = models.IntegerField(default=4)

    MUSING_THRESHOLDS = [
        ("inspire_creativity", "Inspire Creativity"),
        ("create_hope", "Create Hope"),
        ("create_love", "Create Love"),
        ("create_calm", "Create Calm"),
        ("foster_trust", "Foster Trust"),
        ("help_those_in_need", "Help Those In Need"),
        ("foster_dreams", "Foster Dreams"),
    ]

    RAVAGING_THRESHOLDS = [
        ("exhaust_creativity", "Exhaust Creativity"),
        ("destroy_hope", "Destroy Hope"),
        ("destroy_love", "Destroy Love"),
        ("create_anger", "Create Anger"),
        ("break_trust", "Break Trust"),
        ("exploit_dependence", "Exploit Dependence"),
        ("destroy_illusions", "Destroy Illusions"),
    ]

    musing_threshold = models.CharField(
        default="",
        max_length=20,
        choices=MUSING_THRESHOLDS,
    )
    ravaging_threshold = models.CharField(
        default="",
        max_length=20,
        choices=RAVAGING_THRESHOLDS,
    )

    antithesis = models.TextField(default="")

    true_name = models.TextField(default="")
    date_ennobled = models.DateField(blank=True, null=True)
    crysalis = models.TextField(default="")
    date_of_crysalis = models.DateField(blank=True, null=True)
    fae_mien = models.TextField(default="")

    class Meta:
        verbose_name = "Changeling"
        verbose_name_plural = "Changelings"

    def has_court(self):
        return self.court != ""

    def set_court(self, court):
        self.court = court
        return True

    def random_court(self):
        return self.set_court(random.choice(["seelie", "unseelie"]))

    def eligible_for_house(self):
        if self.kith:
            return self.title > 0 or "Sidhe" in self.kith.name
        return self.title > 0

    def has_house(self):
        if self.eligible_for_house():
            return self.house is not None
        return self.house is None

    def set_house(self, house):
        if self.eligible_for_house() and house.court == self.court:
            self.house = house
            return True
        return False

    def random_house(self):
        h = House.objects.filter(court=self.court).order_by("?").first()
        return self.set_house(h)

    def has_seelie_legacy(self):
        return self.seelie_legacy is not None

    def set_seelie_legacy(self, legacy):
        if legacy.court == "seelie":
            self.seelie_legacy = legacy
            return True
        return False

    def random_seelie_legacy(self):
        legacy = Legacy.objects.filter(court="seelie").order_by("?").first()
        return self.set_seelie_legacy(legacy)

    def has_unseelie_legacy(self):
        return self.unseelie_legacy is not None

    def set_unseelie_legacy(self, legacy):
        if legacy.court == "unseelie":
            self.unseelie_legacy = legacy
            return True
        return False

    def random_unseelie_legacy(self):
        legacy = Legacy.objects.filter(court="unseelie").order_by("?").first()
        return self.set_unseelie_legacy(legacy)

    def has_seeming(self):
        return self.seeming != ""

    def set_seeming(self, seeming):
        self.willpower = 4
        self.seeming = seeming
        if self.seeming == "childling":
            self.add_glamour()
        if self.seeming == "wilder":

            random.choice([self.add_glamour, self.add_willpower])()
        if self.seeming == "grump":
            self.add_willpower()
        return True

    def random_seeming(self):
        return self.set_seeming(random.choice(["childling", "wilder", "grump"]))

    def has_kith(self):
        return self.kith is not None

    def set_kith(self, kith):
        self.kith = kith
        return True

    def random_kith(self):
        kith = Kith.objects.order_by("?").first()
        return self.set_kith(kith)

    def add_art(self, art):
        return add_dot(self, art, 5)

    def get_arts(self):
        return {
            "autumn": self.autumn,
            "chicanery": self.chicanery,
            "chronos": self.chronos,
            "contract": self.contract,
            "dragons_ire": self.dragons_ire,
            "legerdemain": self.legerdemain,
            "metamorphosis": self.metamorphosis,
            "naming": self.naming,
            "oneiromancy": self.oneiromancy,
            "primal": self.primal,
            "pyretics": self.pyretics,
            "skycraft": self.skycraft,
            "soothsay": self.soothsay,
            "sovereign": self.sovereign,
            "spring": self.spring,
            "summer": self.summer,
            "wayfare": self.wayfare,
            "winter": self.winter,
        }

    def filter_arts(self, minimum=0, maximum=5):
        return [k for k, v in self.get_arts().items() if minimum <= v <= maximum]

    def has_arts(self):
        return self.total_arts() == 3

    def total_arts(self):
        return sum(v for v in self.get_arts().values())

    def random_art(self):
        art = weighted_choice(self.get_arts())
        return self.add_art(art)

    def random_arts(self):
        while not self.has_arts():
            self.random_art()

    def add_realm(self, realm):
        return add_dot(self, realm, 5)

    def get_realms(self):
        return {
            "actor": self.actor,
            "fae": self.fae,
            "nature_realm": self.nature_realm,
            "prop": self.prop,
            "scene": self.scene,
            "time": self.time,
        }

    def filter_realms(self, minimum=0, maximum=5):
        return [k for k, v in self.get_realms().items() if minimum <= v <= maximum]

    def has_realms(self):
        return self.total_realms() == 5

    def total_realms(self):
        return sum(v for v in self.get_realms().values())

    def random_realm(self):
        realm_dict = self.get_realms()
        if self.total_realms() < 3:
            realm_dict = {
                k: v for k, v in realm_dict.items() if k not in ["time", "scene"]
            }
        realm = weighted_choice(realm_dict)
        return self.add_art(realm)

    def random_realms(self):
        while not self.has_realms():
            self.random_realm()

    def random_background(self):
        bgs = self.get_backgrounds()
        bgs = {k: v + 2 for k, v in bgs.items()}
        if self.kith:
            if "Sidhe" not in self.kith.name:
                bgs["holdings"] -= 1
                bgs["title"] -= 2
                bgs["retinue"] -= 2
        choice = weighted_choice(bgs)
        return self.add_background(choice)

    def add_banality(self):
        return add_dot(self, "banality", 10)

    def add_glamour(self):
        return add_dot(self, "glamour", 10)

    def has_musing_threshold(self):
        return self.musing_threshold != ""

    def set_musing_threshold(self, threshold):
        self.musing_threshold = threshold
        return True

    def random_musing_threshold(self):
        threshold = random.choice(self.MUSING_THRESHOLDS)[0]
        return self.set_musing_threshold(threshold)

    def has_ravaging_threshold(self):
        return self.ravaging_threshold != ""

    def set_ravaging_threshold(self, threshold):
        self.ravaging_threshold = threshold
        return True

    def random_ravaging_threshold(self):
        threshold = random.choice(self.RAVAGING_THRESHOLDS)[0]
        return self.set_ravaging_threshold(threshold)

    def set_antithesis(self, antithesis):
        self.antithesis = antithesis
        return True

    def has_antithesis(self):
        return self.antithesis != ""

    def random_antithesis(self):
        return self.set_antithesis("Antithesis")

    def has_changeling_history(self):
        b = True
        b = b and (self.true_name != "")
        b = b and (self.date_ennobled != "")
        b = b and (self.crysalis != "")
        b = b and (self.date_of_crysalis != "")
        return b

    def set_changeling_history(
        self, true_name, date_ennobled, crysalis, date_of_crysalis
    ):
        self.true_name = true_name
        self.date_ennobled = date_ennobled
        self.crysalis = crysalis
        self.date_of_crysalis = date_of_crysalis
        return True

    def random_changeling_history(self):
        return self.set_changeling_history("True Name", now(), "Crysalis", now())

    def has_changeling_appearance(self):
        return self.fae_mien != ""

    def set_changeling_appearance(self, fae_mien):
        self.fae_mien = fae_mien
        return True

    def random_changeling_appearance(self):
        return self.set_changeling_appearance("Fae Mien")

    def birthright_correction(self):
        if self.kith.name == "Troll":
            self.add_attribute("strength", maximum=10)
            self.max_health_levels += 1
            self.save()
        if self.kith.name == "Satyr":
            self.add_attribute("stamina", maximum=10)
        if self.kith.name == "Piskey":
            self.add_attribute("dexterity", maximum=10)
        if "Sidhe" in self.kith.name:
            self.add_attribute("appearance", maximum=10)
            self.add_attribute("appearance", maximum=10)

    def random(
        self,
        freebies=15,
        xp=0,
        ethnicity=None,
    ):
        self.update_status("Ran")
        self.willpower = 4
        self.freebies = freebies
        self.xp = xp
        self.random_name(ethnicity=ethnicity)
        self.random_kith()
        self.random_concept()
        self.random_attributes()
        self.random_abilities()
        self.random_backgrounds()
        self.random_seeming()
        self.random_court()
        self.random_seelie_legacy()
        self.random_unseelie_legacy()
        self.random_arts()
        self.random_realms()
        self.random_musing_threshold()
        self.random_ravaging_threshold()
        self.random_antithesis()
        self.random_history()
        self.random_changeling_history()
        self.random_changeling_appearance()
        self.random_finishing_touches()
        self.mf_based_corrections()
        self.random_house()
        self.random_specialties()
        self.birthright_correction()
