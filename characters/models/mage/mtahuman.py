from characters.models.core.character import Character
from characters.models.core.human import Human
from django.db import models
from django.urls import reverse
from items.models.mage.wonder import Wonder


class MtAHuman(Human):
    type = "mta_human"

    allowed_backgrounds = [
        "contacts",
        "mentor",
        "allies",
        "alternate_identity",
        "arcane",
        "backup",
        "blessing",
        "certification",
        "chantry",
        "cult",
        "demesne",
        "destiny",
        "dream",
        "enhancement",
        "fame",
        "familiar",
        "influence",
        "legend",
        "library",
        "node",
        "past_lives",
        "patron",
        "rank",
        "requisitions",
        "resources",
        "retainers",
        "sanctum",
        "secret_weapons",
        "spies",
        "status_background",
        "totem",
        "wonder",
    ]

    gameline = "mta"

    primary_abilities = [
        "awareness",
        "art",
        "leadership",
        "larceny" "meditation",
        "research",
        "survival",
        "technology",
        "cosmology",
        "enigmas",
        "finance",
        "law",
        "occult",
        "politics",
        "alertness",
        "athletics",
        "brawl",
        "empathy",
        "expression",
        "intimidation",
        "streetwise",
        "subterfuge",
        "crafts",
        "drive",
        "etiquette",
        "firearms",
        "melee",
        "stealth",
        "academics",
        "computer",
        "investigation",
        "medicine",
        "science",
    ]

    awareness = models.IntegerField(default=0)
    art = models.IntegerField(default=0)
    leadership = models.IntegerField(default=0)
    animal_kinship = models.IntegerField(default=0)
    blatancy = models.IntegerField(default=0)
    carousing = models.IntegerField(default=0)
    do = models.IntegerField(default=0)
    flying = models.IntegerField(default=0)
    high_ritual = models.IntegerField(default=0)
    lucid_dreaming = models.IntegerField(default=0)
    search = models.IntegerField(default=0)
    seduction = models.IntegerField(default=0)
    larceny = models.IntegerField(default=0)
    meditation = models.IntegerField(default=0)
    research = models.IntegerField(default=0)
    survival = models.IntegerField(default=0)
    technology = models.IntegerField(default=0)
    acrobatics = models.IntegerField(default=0)
    archery = models.IntegerField(default=0)
    biotech = models.IntegerField(default=0)
    energy_weapons = models.IntegerField(default=0)
    jetpack = models.IntegerField(default=0)
    riding = models.IntegerField(default=0)
    torture = models.IntegerField(default=0)
    cosmology = models.IntegerField(default=0)
    enigmas = models.IntegerField(default=0)
    finance = models.IntegerField(default=0)
    law = models.IntegerField(default=0)
    occult = models.IntegerField(default=0)
    politics = models.IntegerField(default=0)
    area_knowledge = models.IntegerField(default=0)
    belief_systems = models.IntegerField(default=0)
    cryptography = models.IntegerField(default=0)
    demolitions = models.IntegerField(default=0)
    lore = models.IntegerField(default=0)
    media = models.IntegerField(default=0)
    pharmacopeia = models.IntegerField(default=0)

    cooking = models.IntegerField(default=0)
    diplomacy = models.IntegerField(default=0)
    instruction = models.IntegerField(default=0)
    intrigue = models.IntegerField(default=0)
    intuition = models.IntegerField(default=0)
    mimicry = models.IntegerField(default=0)
    negotiation = models.IntegerField(default=0)
    newspeak = models.IntegerField(default=0)
    scan = models.IntegerField(default=0)
    scrounging = models.IntegerField(default=0)
    style = models.IntegerField(default=0)
    blind_fighting = models.IntegerField(default=0)
    climbing = models.IntegerField(default=0)
    disguise = models.IntegerField(default=0)
    elusion = models.IntegerField(default=0)
    escapology = models.IntegerField(default=0)
    fast_draw = models.IntegerField(default=0)
    fast_talk = models.IntegerField(default=0)
    fencing = models.IntegerField(default=0)
    fortune_telling = models.IntegerField(default=0)
    gambling = models.IntegerField(default=0)
    gunsmith = models.IntegerField(default=0)
    heavy_weapons = models.IntegerField(default=0)
    hunting = models.IntegerField(default=0)
    hypnotism = models.IntegerField(default=0)
    jury_rigging = models.IntegerField(default=0)
    microgravity_operations = models.IntegerField(default=0)
    misdirection = models.IntegerField(default=0)
    networking = models.IntegerField(default=0)
    pilot = models.IntegerField(default=0)
    psychology = models.IntegerField(default=0)
    security = models.IntegerField(default=0)
    speed_reading = models.IntegerField(default=0)
    swimming = models.IntegerField(default=0)
    conspiracy_theory = models.IntegerField(default=0)
    chantry_politics = models.IntegerField(default=0)
    covert_culture = models.IntegerField(default=0)
    cultural_savvy = models.IntegerField(default=0)
    helmsman = models.IntegerField(default=0)
    history_knowledge = models.IntegerField(default=0)
    power_brokering = models.IntegerField(default=0)
    propaganda = models.IntegerField(default=0)
    theology = models.IntegerField(default=0)
    unconventional_warface = models.IntegerField(default=0)
    vice = models.IntegerField(default=0)

    allied_characters = models.ManyToManyField(Character, blank=True)
    enhancement_devices = models.ManyToManyField(Wonder, blank=True)

    background_points = 7

    class Meta:
        verbose_name = "Human (Mage)"
        verbose_name_plural = "Humans (Mage)"

    def get_heading(self):
        return "mta_heading"

    def get_secondaries_for_display(self):
        secondary_talents = {
            k: v
            for k, v in self.get_talents().items()
            if k not in self.primary_abilities and v != 0
        }
        secondary_skills = {
            k: v
            for k, v in self.get_skills().items()
            if k not in self.primary_abilities and v != 0
        }
        secondary_knowledges = {
            k: v
            for k, v in self.get_knowledges().items()
            if k not in self.primary_abilities and v != 0
        }

        if "History Knowledge" in secondary_knowledges:
            secondary_knowledges["History"] = secondary_knowledges.pop(
                "History Knowledge"
            )

        secondary_talents = list(secondary_talents.items())
        secondary_skills = list(secondary_skills.items())
        secondary_knowledges = list(secondary_knowledges.items())

        secondary_talents = [
            (k.replace("_", " ").title(), v, k) for k, v in secondary_talents
        ]
        secondary_skills = [
            (k.replace("_", " ").title(), v, k) for k, v in secondary_skills
        ]
        secondary_knowledges = [
            (k.replace("_", " ").title(), v, k) for k, v in secondary_knowledges
        ]

        secondary_talents.sort(key=lambda x: x[0])
        secondary_skills.sort(key=lambda x: x[0])
        secondary_knowledges.sort(key=lambda x: x[0])

        num_sec_tal = len(secondary_talents)
        num_sec_ski = len(secondary_skills)
        num_sec_kno = len(secondary_knowledges)
        m = max(num_sec_tal, num_sec_ski, num_sec_kno)
        for _ in range(m - num_sec_tal):
            secondary_talents.append(("", 0, ""))
        for _ in range(m - num_sec_ski):
            secondary_skills.append(("", 0, ""))
        for _ in range(m - num_sec_kno):
            secondary_knowledges.append(("", 0, ""))
        return list(zip(secondary_talents, secondary_skills, secondary_knowledges))

    def get_talents(self):
        tmp = super().get_talents()
        tmp.update(
            {
                "awareness": self.awareness,
                "art": self.art,
                "leadership": self.leadership,
                "animal_kinship": self.animal_kinship,
                "blatancy": self.blatancy,
                "carousing": self.carousing,
                "do": self.do,
                "flying": self.flying,
                "high_ritual": self.high_ritual,
                "lucid_dreaming": self.lucid_dreaming,
                "search": self.search,
                "seduction": self.seduction,
                "cooking": self.cooking,
                "diplomacy": self.diplomacy,
                "instruction": self.instruction,
                "intrigue": self.intrigue,
                "intuition": self.intuition,
                "mimicry": self.mimicry,
                "negotiation": self.negotiation,
                "newspeak": self.newspeak,
                "scan": self.scan,
                "scrounging": self.scrounging,
                "style": self.style,
            }
        )
        return tmp

    def get_skills(self):
        tmp = super().get_skills()
        tmp.update(
            {
                "larceny": self.larceny,
                "meditation": self.meditation,
                "research": self.research,
                "survival": self.survival,
                "technology": self.technology,
                "acrobatics": self.acrobatics,
                "archery": self.archery,
                "biotech": self.biotech,
                "energy_weapons": self.energy_weapons,
                "jetpack": self.jetpack,
                "riding": self.riding,
                "torture": self.torture,
                "blind_fighting": self.blind_fighting,
                "climbing": self.climbing,
                "disguise": self.disguise,
                "elusion": self.elusion,
                "escapology": self.escapology,
                "fast_draw": self.fast_draw,
                "fast_talk": self.fast_talk,
                "fencing": self.fencing,
                "fortune_telling": self.fortune_telling,
                "gambling": self.gambling,
                "gunsmith": self.gunsmith,
                "heavy_weapons": self.heavy_weapons,
                "hunting": self.hunting,
                "hypnotism": self.hypnotism,
                "jury_rigging": self.jury_rigging,
                "microgravity_operations": self.microgravity_operations,
                "misdirection": self.misdirection,
                "networking": self.networking,
                "pilot": self.pilot,
                "psychology": self.psychology,
                "security": self.security,
                "speed_reading": self.speed_reading,
                "swimming": self.swimming,
            }
        )
        return tmp

    def get_knowledges(self):
        tmp = super().get_knowledges()
        tmp.update(
            {
                "cosmology": self.cosmology,
                "enigmas": self.enigmas,
                "finance": self.finance,
                "law": self.law,
                "occult": self.occult,
                "politics": self.politics,
                "area_knowledge": self.area_knowledge,
                "belief_systems": self.belief_systems,
                "cryptography": self.cryptography,
                "demolitions": self.demolitions,
                "lore": self.lore,
                "media": self.media,
                "pharmacopeia": self.pharmacopeia,
                "conspiracy_theory": self.conspiracy_theory,
                "chantry_politics": self.chantry_politics,
                "covert_culture": self.covert_culture,
                "cultural_savvy": self.cultural_savvy,
                "helmsman": self.helmsman,
                "history_knowledge": self.history_knowledge,
                "power_brokering": self.power_brokering,
                "propaganda": self.propaganda,
                "theology": self.theology,
                "unconventional_warface": self.unconventional_warface,
                "vice": self.vice,
            }
        )
        return tmp

    def get_backgrounds(self):
        tmp = super().get_backgrounds()
        tmp.update(
            {
                "allies": self.allies,
                "alternate_identity": self.alternate_identity,
                "arcane": self.arcane,
                "avatar": self.avatar,
                "backup": self.backup,
                "blessing": self.blessing,
                "certification": self.certification,
                "chantry": self.chantry,
                "cult": self.cult,
                "demesne": self.demesne,
                "destiny": self.destiny,
                "dream": self.dream,
                "enhancement": self.enhancement,
                "fame": self.fame,
                "familiar": self.familiar,
                "influence": self.influence,
                "legend": self.legend,
                "library": self.library,
                "node": self.node,
                "past_lives": self.past_lives,
                "patron": self.patron,
                "rank": self.rank,
                "requisitions": self.requisitions,
                "resources": self.resources,
                "retainers": self.retainers,
                "sanctum": self.sanctum,
                "secret_weapons": self.secret_weapons,
                "spies": self.spies,
                "status_background": self.status_background,
                "totem": self.totem,
                "wonder": self.wonder,
            }
        )
        return tmp

    def get_update_url(self):
        return reverse("characters:mage:update:mtahuman", kwargs={"pk": self.pk})

    @classmethod
    def get_creation_url(cls):
        return reverse("characters:mage:create:mtahuman")
