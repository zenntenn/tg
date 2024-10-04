import random

from core.utils import add_dot, weighted_choice
from django.db import models


class AttributeBlock(models.Model):
    strength = models.IntegerField(default=1)
    dexterity = models.IntegerField(default=1)
    stamina = models.IntegerField(default=1)
    perception = models.IntegerField(default=1)
    intelligence = models.IntegerField(default=1)
    wits = models.IntegerField(default=1)
    charisma = models.IntegerField(default=1)
    manipulation = models.IntegerField(default=1)
    appearance = models.IntegerField(default=1)

    class Meta:
        abstract = True

    def add_attribute(self, attribute, maximum=5):
        return add_dot(self, attribute, maximum)

    def get_attributes(self):
        return {
            "strength": self.strength,
            "dexterity": self.dexterity,
            "stamina": self.stamina,
            "perception": self.perception,
            "intelligence": self.intelligence,
            "wits": self.wits,
            "charisma": self.charisma,
            "manipulation": self.manipulation,
            "appearance": self.appearance,
        }

    def get_physical_attributes(self, attribute_dict=None):
        if attribute_dict is None:
            attribute_dict = self.get_attributes()
        return {
            k: v
            for k, v in attribute_dict.items()
            if k in ["strength", "dexterity", "stamina"]
        }

    def get_social_attributes(self, attribute_dict=None):
        if attribute_dict is None:
            attribute_dict = self.get_attributes()
        return {
            k: v
            for k, v in attribute_dict.items()
            if k in ["charisma", "manipulation", "appearance"]
        }

    def get_mental_attributes(self, attribute_dict=None):
        if attribute_dict is None:
            attribute_dict = self.get_attributes()
        return {
            k: v
            for k, v in attribute_dict.items()
            if k in ["perception", "intelligence", "wits"]
        }

    def total_physical_attributes(self, attribute_dict=None):
        return sum(self.get_physical_attributes(attribute_dict=attribute_dict).values())

    def total_social_attributes(self, attribute_dict=None):
        return sum(self.get_social_attributes(attribute_dict=attribute_dict).values())

    def total_mental_attributes(self, attribute_dict=None):
        return sum(self.get_mental_attributes(attribute_dict=attribute_dict).values())

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

    def has_attributes(
        self, primary=7, secondary=5, tertiary=3, max_value=5, attribute_dict=None
    ):
        triple = [
            self.total_physical_attributes(attribute_dict=attribute_dict),
            self.total_mental_attributes(attribute_dict=attribute_dict),
            self.total_social_attributes(attribute_dict=attribute_dict),
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