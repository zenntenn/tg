import random

from characters.models.core.ability import Ability
from characters.models.core.archetype import Archetype
from characters.models.core.meritflaw import MeritFlaw
from characters.models.core.specialty import Specialty
from characters.models.mage.effect import Effect
from characters.models.mage.faction import MageFaction
from characters.models.mage.focus import Instrument, Paradigm, Practice
from characters.models.mage.mtahuman import MtAHuman
from characters.tests.utils import mage_setup
from core.models import Language, Noun
from django.contrib.auth.models import User
from django.test import TestCase
from game.models import ObjectType


class TestMtAHuman(TestCase):
    def setUp(self):
        mage_setup()

        self.player = User.objects.create_user(username="Test")
        self.character = MtAHuman.objects.create(name="", owner=self.player)

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


class TestMtAHumanDetailView(TestCase):
    def setUp(self) -> None:
        self.mtahuman = MtAHuman.objects.create(name="Test MtAHuman")
        self.url = self.mtahuman.get_absolute_url()

    def test_effect_detail_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_effect_detail_view_templates(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "characters/mage/mtahuman/detail.html")


class TestMtAHumanCreateView(TestCase):
    def setUp(self):
        self.valid_data = {
            "name": "Test MtAHuman",
            "description": 0,
            "willpower": 0,
            "age": 0,
            "apparent_age": 0,
            "hair": 0,
            "eyes": 0,
            "ethnicity": 0,
            "nationality": 0,
            "height": 0,
            "weight": 0,
            "sex": 0,
            "childhood": 0,
            "history": 0,
            "goals": 0,
            "notes": 0,
            "strength": 0,
            "dexterity": 0,
            "stamina": 0,
            "perception": 0,
            "intelligence": 0,
            "wits": 0,
            "charisma": 0,
            "manipulation": 0,
            "appearance": 0,
            "awareness": 0,
            "art": 0,
            "leadership": 0,
            "animal_kinship": 0,
            "blatancy": 0,
            "carousing": 0,
            "do": 0,
            "flying": 0,
            "high_ritual": 0,
            "lucid_dreaming": 0,
            "search": 0,
            "seduction": 0,
            "martial_arts": 0,
            "meditation": 0,
            "research": 0,
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
            "cosmology": 0,
            "enigmas": 0,
            "esoterica": 0,
            "law": 0,
            "occult": 0,
            "politics": 0,
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
        }
        self.url = MtAHuman.get_creation_url()

    def test_create_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "characters/mage/mtahuman/form.html")

    def test_create_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(MtAHuman.objects.count(), 1)
        self.assertEqual(MtAHuman.objects.first().name, "Test MtAHuman")


class TestMtAHumanUpdateView(TestCase):
    def setUp(self):
        self.mtahuman = MtAHuman.objects.create(
            name="Test MtAHuman", description="Test"
        )
        self.valid_data = {
            "name": "Test MtAHuman 2",
            "description": 0,
            "willpower": 0,
            "age": 0,
            "apparent_age": 0,
            "hair": 0,
            "eyes": 0,
            "ethnicity": 0,
            "nationality": 0,
            "height": 0,
            "weight": 0,
            "sex": 0,
            "childhood": 0,
            "history": 0,
            "goals": 0,
            "notes": 0,
            "strength": 0,
            "dexterity": 0,
            "stamina": 0,
            "perception": 0,
            "intelligence": 0,
            "wits": 0,
            "charisma": 0,
            "manipulation": 0,
            "appearance": 0,
            "awareness": 0,
            "art": 0,
            "leadership": 0,
            "animal_kinship": 0,
            "blatancy": 0,
            "carousing": 0,
            "do": 0,
            "flying": 0,
            "high_ritual": 0,
            "lucid_dreaming": 0,
            "search": 0,
            "seduction": 0,
            "martial_arts": 0,
            "meditation": 0,
            "research": 0,
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
            "cosmology": 0,
            "enigmas": 0,
            "esoterica": 0,
            "law": 0,
            "occult": 0,
            "politics": 0,
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
        }
        self.url = self.mtahuman.get_update_url()

    def test_update_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_update_view_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "characters/mage/mtahuman/form.html")

    def test_update_view_successful_post(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.mtahuman.refresh_from_db()
        self.assertEqual(self.mtahuman.name, "Test MtAHuman 2")
