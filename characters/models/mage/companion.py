from characters.models.mage.mtahuman import MtAHuman
from django.db import models

from characters.models.werewolf.charm import SpiritCharm
from core.models import Model, Number

class Advantage(Model):
    type = "advantage"
    
    ratings = models.ManyToManyField(Number, blank=True)



class Companion(MtAHuman):
    type = "companion"
    
    # Concept, Affiliation/Faction/Subfaction, Type of Companion, Nature/Demeanor
    # Attributes 6/4/3
    # Abilities 11/7/4
    # 5 backgrounds, if consor 4 + mentor 1
    # Advantages start at 0
    # Willpower starts at 3
    # Essence = WP x 5 for Familiars
    # Merits and Flaws
    # Charms start with 0, familiars only
    # Freebies 15 for acolytes and backup agents, 21 for consors and skilled allies, 25 for Familiars
    # Starting Abilities and Backgruonds maxed at FOUR
    
    # advantages cost listed amount in Freebies, can't be bought with XP
    
    advantages = models.ManyToManyField(Advantage, blank=True)
    


class Familiar(Companion):
    # Must Have: Bond-Sharing + Paradox Nullification Adantages
    # Thaumivore Flaw
    type = "familiar"
    
    background_points = 5
    
    essence = models.IntegerField(default=0)
    
    # essence costs 1 freebie per dot, current x 2 XP
    # charms cost 1 pt per essence needed/5 freebies or XP
    
    charms = models.ManyToManyField(SpiritCharm, blank=True)

