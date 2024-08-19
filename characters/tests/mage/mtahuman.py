
import random
from django.test import TestCase

from characters.models.core.archetype import Archetype
from characters.models.core.meritflaw import MeritFlaw
from characters.models.mage.effect import Effect
from characters.models.mage.faction import MageFaction
from characters.models.mage.focus import Instrument, Paradigm, Practice
from characters.models.mage.mtahuman import MtAHuman
from characters.models.mage.resonance import Resonance
from core.models import Language, Noun


class TestMtAHuman(TestCase):
    def setUp(self):
        self.player = User.objects.create_user(username="Test")
        self.character = MtAHuman.objects.create(name="", owner=self.player)
    for i in range(10):
        Noun.objects.create(name=f"Mage Noun {i}")

    for i in range(5):
        m = Mage.objects.create(name=f"Character {i}", owner=player)

    for i in range(15):
        Instrument.objects.create(name=f"Instrument {i}")

    for i in range(5):
        practice = Practice.objects.create(
            name=f"Practice {i}", abilities=list(random.sample(ABILITY_LIST, k=4))
        )
        practice.instruments.set(Instrument.objects.all())
        practice.save()

    for i in range(3):
        paradigm = Paradigm.objects.create(name=f"Paradigm {i}")
        paradigm.practices.set(Practice.objects.all())
        paradigm.save()

    trad = MageFaction.objects.create(name="Traditions")
    MageFaction.objects.create(name="Akashayana", parent=trad)

    for faction in MageFaction.objects.exclude(parent=None):
        faction.paradigms.set(Paradigm.objects.all())
        faction.practices.set(Practice.objects.all())
        faction.save()
        MageFaction.objects.create(name=f"sub-{faction.name}", parent=faction)

    for i in range(5):
        MeritFlaw.objects.create(name=f"Merit {i}", ratings=[i], human=True, mage=True)
        MeritFlaw.objects.create(name=f"Flaw {i}", ratings=[-i], human=True, mage=True)
        MeritFlaw.objects.create(name=f"Merit2 {i}", ratings=[i], human=True, mage=True)
        MeritFlaw.objects.create(name=f"Flaw2 {i}", ratings=[-i], human=True, mage=True)
        MeritFlaw.objects.create(name=f"Merit3 {i}", ratings=[i], human=True, mage=True)
        MeritFlaw.objects.create(name=f"Flaw3 {i}", ratings=[-i], human=True, mage=True)
        NodeMeritFlaw.objects.create(name=f"Node Merit {i}", ratings=[i])
        NodeMeritFlaw.objects.create(name=f"Node Flaw {i}", ratings=[-i])

    for i in range(1, 11):
        Resonance.objects.create(name=f"Resonance {i}")

    for i in range(1, 6):
        Effect.objects.create(name=f"Correspondence {i}", correspondence=i)
        Effect.objects.create(name=f"Time {i}", time=i)
        Effect.objects.create(name=f"Spirit {i}", spirit=i)
        Effect.objects.create(name=f"Forces {i}", forces=i)
        Effect.objects.create(name=f"Matter {i}", matter=i)
        Effect.objects.create(name=f"Life {i}", life=i)
        Effect.objects.create(name=f"Entropy {i}", entropy=i)
        Effect.objects.create(name=f"Prime {i}", prime=i)
        Effect.objects.create(name=f"Mind {i}", mind=i)

    for i in range(10):
        for trait in m.get_attributes():
            WoDSpecialty.objects.create(
                name=f"{trait.replace('_', ' ').title()} {i}", stat=trait
            )

        for trait in m.get_abilities():
            WoDSpecialty.objects.create(
                name=f"{trait.replace('_', ' ').title()} {i}", stat=trait
            )

        for trait in m.get_spheres():
            WoDSpecialty.objects.create(
                name=f"{trait.replace('_', ' ').title()} {i}", stat=trait
            )
            for i in range(5):
                Resonance.objects.get_or_create(
                    name=f"{trait.title()} Resonance {i}", **{trait: True}
                )

    for i in range(20):
        Archetype.objects.create(name=f"Archetype {i}")

    for i in range(1, 11):
        Language.objects.create(name=f"Language {i}", frequency=i)

    def set_abilities(self):
        self.character.alertness = 1
        self.character.art = 2
        self.character.empathy = 3
        self.character.streetwise = 2
        self.character.firearms = 3
        self.character.melee = 4
        self.character.stealth = 2
        self.character.technology = 1
        self.character.cosmology = 3
        self.character.law = 2
        self.character.area_knowledge = 1
        self.character.belief_systems = 1
        self.character.cryptography = 1

    def test_get_abilities(self):
        self.assertEqual(
            self.character.get_abilities(),
            {
                "alertness": 0,
                "awareness": 0,
                "art": 0,
                "athletics": 0,
                "brawl": 0,
                "empathy": 0,
                "intimidation": 0,
                "leadership": 0,
                "expression": 0,
                "streetwise": 0,
                "subterfuge": 0,
                "animal_kinship": 0,
                "blatancy": 0,
                "carousing": 0,
                "do": 0,
                "flying": 0,
                "high_ritual": 0,
                "lucid_dreaming": 0,
                "search": 0,
                "seduction": 0,
                "crafts": 0,
                "drive": 0,
                "etiquette": 0,
                "firearms": 0,
                "martial_arts": 0,
                "meditation": 0,
                "melee": 0,
                "research": 0,
                "stealth": 0,
                "survival": 0,
                "technology": 0,
                "acrobatics": 0,
                "archery": 0,
                "biotech": 0,
                "energy_weapons": 0,
                "hypertech": 0,
                "jetpack": 0,
                "riding": 0,
                "torture": 0,
                "academics": 0,
                "computer": 0,
                "cosmology": 0,
                "enigmas": 0,
                "esoterica": 0,
                "investigation": 0,
                "law": 0,
                "medicine": 0,
                "occult": 0,
                "politics": 0,
                "science": 0,
                "area_knowledge": 0,
                "belief_systems": 0,
                "cryptography": 0,
                "demolitions": 0,
                "finance": 0,
                "lore": 0,
                "media": 0,
                "pharmacopeia": 0,
                "cooking": 0,
                "diplomacy": 0,
                "instruction": 0,
                "intrigue": 0,
                "intuition": 0,
                "mimicry": 0,
                "negotiation": 0,
                "newspeak": 0,
                "scan": 0,
                "scrounging": 0,
                "style": 0,
                "blind_fighting": 0,
                "climbing": 0,
                "disguise": 0,
                "elusion": 0,
                "escapology": 0,
                "fast_draw": 0,
                "fast_talk": 0,
                "fencing": 0,
                "fortune_telling": 0,
                "gambling": 0,
                "gunsmith": 0,
                "heavy_weapons": 0,
                "hunting": 0,
                "hypnotism": 0,
                "jury_rigging": 0,
                "microgravity_operations": 0,
                "misdirection": 0,
                "networking": 0,
                "pilot": 0,
                "psychology": 0,
                "security": 0,
                "speed_reading": 0,
                "swimming": 0,
                "conspiracy_theory": 0,
                "chantry_politics": 0,
                "covert_culture": 0,
                "cultural_savvy": 0,
                "helmsman": 0,
                "history_knowledge": 0,
                "power_brokering": 0,
                "propaganda": 0,
                "theology": 0,
                "unconventional_warface": 0,
                "vice": 0,
            },
        )
        self.set_abilities()
        self.assertEqual(
            self.character.get_abilities(),
            {
                "alertness": 1,
                "awareness": 0,
                "art": 2,
                "athletics": 0,
                "brawl": 0,
                "empathy": 3,
                "intimidation": 0,
                "leadership": 0,
                "expression": 0,
                "streetwise": 2,
                "subterfuge": 0,
                "animal_kinship": 0,
                "blatancy": 0,
                "carousing": 0,
                "do": 0,
                "flying": 0,
                "high_ritual": 0,
                "lucid_dreaming": 0,
                "search": 0,
                "seduction": 0,
                "crafts": 0,
                "drive": 0,
                "etiquette": 0,
                "firearms": 3,
                "martial_arts": 0,
                "meditation": 0,
                "melee": 4,
                "research": 0,
                "stealth": 2,
                "survival": 0,
                "technology": 1,
                "acrobatics": 0,
                "archery": 0,
                "biotech": 0,
                "energy_weapons": 0,
                "hypertech": 0,
                "jetpack": 0,
                "riding": 0,
                "torture": 0,
                "academics": 0,
                "computer": 0,
                "cosmology": 3,
                "enigmas": 0,
                "esoterica": 0,
                "investigation": 0,
                "law": 2,
                "medicine": 0,
                "occult": 0,
                "politics": 0,
                "science": 0,
                "area_knowledge": 1,
                "belief_systems": 1,
                "cryptography": 1,
                "demolitions": 0,
                "finance": 0,
                "lore": 0,
                "media": 0,
                "pharmacopeia": 0,
                "cooking": 0,
                "diplomacy": 0,
                "instruction": 0,
                "intrigue": 0,
                "intuition": 0,
                "mimicry": 0,
                "negotiation": 0,
                "newspeak": 0,
                "scan": 0,
                "scrounging": 0,
                "style": 0,
                "blind_fighting": 0,
                "climbing": 0,
                "disguise": 0,
                "elusion": 0,
                "escapology": 0,
                "fast_draw": 0,
                "fast_talk": 0,
                "fencing": 0,
                "fortune_telling": 0,
                "gambling": 0,
                "gunsmith": 0,
                "heavy_weapons": 0,
                "hunting": 0,
                "hypnotism": 0,
                "jury_rigging": 0,
                "microgravity_operations": 0,
                "misdirection": 0,
                "networking": 0,
                "pilot": 0,
                "psychology": 0,
                "security": 0,
                "speed_reading": 0,
                "swimming": 0,
                "conspiracy_theory": 0,
                "chantry_politics": 0,
                "covert_culture": 0,
                "cultural_savvy": 0,
                "helmsman": 0,
                "history_knowledge": 0,
                "power_brokering": 0,
                "propaganda": 0,
                "theology": 0,
                "unconventional_warface": 0,
                "vice": 0,
            },
        )

    def test_get_talents(self):
        self.assertEqual(
            self.character.get_talents(),
            {
                "alertness": 0,
                "awareness": 0,
                "art": 0,
                "athletics": 0,
                "brawl": 0,
                "empathy": 0,
                "intimidation": 0,
                "leadership": 0,
                "expression": 0,
                "streetwise": 0,
                "subterfuge": 0,
                "animal_kinship": 0,
                "blatancy": 0,
                "carousing": 0,
                "do": 0,
                "flying": 0,
                "high_ritual": 0,
                "lucid_dreaming": 0,
                "search": 0,
                "seduction": 0,
                "cooking": 0,
                "diplomacy": 0,
                "instruction": 0,
                "intrigue": 0,
                "intuition": 0,
                "mimicry": 0,
                "negotiation": 0,
                "newspeak": 0,
                "scan": 0,
                "scrounging": 0,
                "style": 0,
            },
        )
        self.set_abilities()
        self.assertEqual(
            self.character.get_talents(),
            {
                "alertness": 1,
                "awareness": 0,
                "art": 2,
                "athletics": 0,
                "brawl": 0,
                "empathy": 3,
                "intimidation": 0,
                "leadership": 0,
                "expression": 0,
                "streetwise": 2,
                "subterfuge": 0,
                "animal_kinship": 0,
                "blatancy": 0,
                "carousing": 0,
                "do": 0,
                "flying": 0,
                "high_ritual": 0,
                "lucid_dreaming": 0,
                "search": 0,
                "seduction": 0,
                "cooking": 0,
                "diplomacy": 0,
                "instruction": 0,
                "intrigue": 0,
                "intuition": 0,
                "mimicry": 0,
                "negotiation": 0,
                "newspeak": 0,
                "scan": 0,
                "scrounging": 0,
                "style": 0,
            },
        )

    def test_get_skills(self):
        self.assertEqual(
            self.character.get_skills(),
            {
                "crafts": 0,
                "drive": 0,
                "etiquette": 0,
                "firearms": 0,
                "martial_arts": 0,
                "meditation": 0,
                "melee": 0,
                "research": 0,
                "stealth": 0,
                "survival": 0,
                "technology": 0,
                "acrobatics": 0,
                "archery": 0,
                "biotech": 0,
                "energy_weapons": 0,
                "hypertech": 0,
                "jetpack": 0,
                "riding": 0,
                "torture": 0,
                "blind_fighting": 0,
                "climbing": 0,
                "disguise": 0,
                "elusion": 0,
                "escapology": 0,
                "fast_draw": 0,
                "fast_talk": 0,
                "fencing": 0,
                "fortune_telling": 0,
                "gambling": 0,
                "gunsmith": 0,
                "heavy_weapons": 0,
                "hunting": 0,
                "hypnotism": 0,
                "jury_rigging": 0,
                "microgravity_operations": 0,
                "misdirection": 0,
                "networking": 0,
                "pilot": 0,
                "psychology": 0,
                "security": 0,
                "speed_reading": 0,
                "swimming": 0,
            },
        )
        self.set_abilities()
        self.assertEqual(
            self.character.get_skills(),
            {
                "crafts": 0,
                "drive": 0,
                "etiquette": 0,
                "firearms": 3,
                "martial_arts": 0,
                "meditation": 0,
                "melee": 4,
                "research": 0,
                "stealth": 2,
                "survival": 0,
                "technology": 1,
                "acrobatics": 0,
                "archery": 0,
                "biotech": 0,
                "energy_weapons": 0,
                "hypertech": 0,
                "jetpack": 0,
                "riding": 0,
                "torture": 0,
                "blind_fighting": 0,
                "climbing": 0,
                "disguise": 0,
                "elusion": 0,
                "escapology": 0,
                "fast_draw": 0,
                "fast_talk": 0,
                "fencing": 0,
                "fortune_telling": 0,
                "gambling": 0,
                "gunsmith": 0,
                "heavy_weapons": 0,
                "hunting": 0,
                "hypnotism": 0,
                "jury_rigging": 0,
                "microgravity_operations": 0,
                "misdirection": 0,
                "networking": 0,
                "pilot": 0,
                "psychology": 0,
                "security": 0,
                "speed_reading": 0,
                "swimming": 0,
            },
        )

    def test_get_knowledges(self):
        self.assertEqual(
            self.character.get_knowledges(),
            {
                "academics": 0,
                "computer": 0,
                "cosmology": 0,
                "enigmas": 0,
                "esoterica": 0,
                "investigation": 0,
                "law": 0,
                "medicine": 0,
                "occult": 0,
                "politics": 0,
                "science": 0,
                "area_knowledge": 0,
                "belief_systems": 0,
                "cryptography": 0,
                "demolitions": 0,
                "finance": 0,
                "lore": 0,
                "media": 0,
                "pharmacopeia": 0,
                "conspiracy_theory": 0,
                "chantry_politics": 0,
                "covert_culture": 0,
                "cultural_savvy": 0,
                "helmsman": 0,
                "history_knowledge": 0,
                "power_brokering": 0,
                "propaganda": 0,
                "theology": 0,
                "unconventional_warface": 0,
                "vice": 0,
            },
        )
        self.set_abilities()
        self.assertEqual(
            self.character.get_knowledges(),
            {
                "academics": 0,
                "computer": 0,
                "cosmology": 3,
                "enigmas": 0,
                "esoterica": 0,
                "investigation": 0,
                "law": 2,
                "medicine": 0,
                "occult": 0,
                "politics": 0,
                "science": 0,
                "area_knowledge": 1,
                "belief_systems": 1,
                "cryptography": 1,
                "demolitions": 0,
                "finance": 0,
                "lore": 0,
                "media": 0,
                "pharmacopeia": 0,
                "conspiracy_theory": 0,
                "chantry_politics": 0,
                "covert_culture": 0,
                "cultural_savvy": 0,
                "helmsman": 0,
                "history_knowledge": 0,
                "power_brokering": 0,
                "propaganda": 0,
                "theology": 0,
                "unconventional_warface": 0,
                "vice": 0,
            },
        )

    def test_get_backgrounds(self):
        self.assertEqual(
            self.character.get_backgrounds(),
            {
                "contacts": 0,
                "mentor": 0,
                "allies": 0,
                "alternate_identity": 0,
                "arcane": 0,
                "avatar": 0,
                "backup": 0,
                "blessing": 0,
                "certification": 0,
                "chantry": 0,
                "cult": 0,
                "demesne": 0,
                "destiny": 0,
                "dream": 0,
                "enhancement": 0,
                "fame": 0,
                "familiar": 0,
                "influence": 0,
                "legend": 0,
                "library": 0,
                "node": 0,
                "past_lives": 0,
                "patron": 0,
                "rank": 0,
                "requisitions": 0,
                "resources": 0,
                "retainers": 0,
                "sanctum": 0,
                "secret_weapons": 0,
                "spies": 0,
                "status_background": 0,
                "totem": 0,
                "wonder": 0,
            },
        )
        self.character.mentor = 3
        self.character.chantry = 2
        self.character.fame = 1
        self.character.dream = 3
        self.assertEqual(
            self.character.get_backgrounds(),
            {
                "contacts": 0,
                "mentor": 3,
                "allies": 0,
                "alternate_identity": 0,
                "arcane": 0,
                "avatar": 0,
                "backup": 0,
                "blessing": 0,
                "certification": 0,
                "chantry": 2,
                "cult": 0,
                "demesne": 0,
                "destiny": 0,
                "dream": 3,
                "enhancement": 0,
                "fame": 1,
                "familiar": 0,
                "influence": 0,
                "legend": 0,
                "library": 0,
                "node": 0,
                "past_lives": 0,
                "patron": 0,
                "rank": 0,
                "requisitions": 0,
                "resources": 0,
                "retainers": 0,
                "sanctum": 0,
                "secret_weapons": 0,
                "spies": 0,
                "status_background": 0,
                "totem": 0,
                "wonder": 0,
            },
        )
