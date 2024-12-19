from items.models.core.meleeweapon import MeleeWeapon
from items.models.core.rangedweapon import RangedWeapon
from items.models.core.thrownweapon import ThrownWeapon

MeleeWeapon.objects.get_or_create(
    name="Sap", difficulty=4, damage=0, damage_type="B", conceal="P", display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 302)
MeleeWeapon.objects.get_or_create(
    name="Whip", difficulty=6, damage=1, damage_type="L", conceal="J", display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 302)
MeleeWeapon.objects.get_or_create(
    name="Spiked Gauntlet",
    difficulty=6,
    damage=1,
    damage_type="L",
    conceal="J",
    display=False,
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 302)
MeleeWeapon.objects.get_or_create(
    name="Broken Bottle",
    difficulty=6,
    damage=1,
    damage_type="L",
    conceal="P",
    display=False,
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 302)
MeleeWeapon.objects.get_or_create(
    name="Chair", difficulty=7, damage=2, damage_type="B", conceal="N", display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 302)
MeleeWeapon.objects.get_or_create(
    name="Table", difficulty=8, damage=3, damage_type="B", conceal="N", display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 302)
MeleeWeapon.objects.get_or_create(
    name="Chain", difficulty=5, damage=0, damage_type="B", conceal="J", display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 302)
MeleeWeapon.objects.get_or_create(
    name="Staff", difficulty=5, damage=1, damage_type="B", conceal="N", display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 302)
MeleeWeapon.objects.get_or_create(
    name="Mace", difficulty=6, damage=2, damage_type="L", conceal="N", display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 302)
MeleeWeapon.objects.get_or_create(
    name="Baseball Bat",
    difficulty=5,
    damage=2,
    damage_type="B",
    conceal="T",
    display=False,
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 302)
MeleeWeapon.objects.get_or_create(
    name="Spiked Club",
    difficulty=6,
    damage=2,
    damage_type="L",
    conceal="T",
    display=False,
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 302)
MeleeWeapon.objects.get_or_create(
    name="Huge Spiked Club",
    difficulty=7,
    damage=4,
    damage_type="L",
    conceal="N",
    display=False,
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 302)
MeleeWeapon.objects.get_or_create(
    name="Knife", difficulty=4, damage=1, damage_type="L", conceal="P", display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 302)
MeleeWeapon.objects.get_or_create(
    name="Sword", difficulty=6, damage=2, damage_type="L", conceal="T", display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 302)
# MeleeWeapon.objects.get_or_create(name="Klaive", difficulty=6, damage=2, damage_type="A", conceal="J", display=False)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 302)
# MeleeWeapon.objects.get_or_create(name="Grand Klaive", difficulty=7, damage=5, damage_type="A", conceal="T", display=False)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 302)
MeleeWeapon.objects.get_or_create(
    name="Great Sword",
    difficulty=7,
    damage=6,
    damage_type="L",
    conceal="N",
    display=False,
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 302)
MeleeWeapon.objects.get_or_create(
    name="Axe", difficulty=7, damage=3, damage_type="L", conceal="T", display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 302)
MeleeWeapon.objects.get_or_create(
    name="Great Axe",
    difficulty=7,
    damage=6,
    damage_type="L",
    conceal="N",
    display=False,
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 302)
MeleeWeapon.objects.get_or_create(
    name="Polearm", difficulty=7, damage=3, damage_type="L", conceal="N", display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 302)
MeleeWeapon.objects.get_or_create(
    name="Chainsaw", difficulty=8, damage=7, damage_type="L", conceal="N", display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 302)


ThrownWeapon.objects.get_or_create(
    name="Throwing Knife",
    difficulty=6,
    damage=0,
    damage_type="L",
    conceal="P",
    display=False,
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 302)
ThrownWeapon.objects.get_or_create(
    name="Shuriken", difficulty=7, damage=3, damage_type="L", conceal="P", display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 302)
ThrownWeapon.objects.get_or_create(
    name="Spear", difficulty=6, damage=1, damage_type="L", conceal="N", display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 302)
ThrownWeapon.objects.get_or_create(
    name="Stone", difficulty=5, damage=0, damage_type="B", conceal="N", display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 302)
ThrownWeapon.objects.get_or_create(
    name="Stone, head-sized",
    difficulty=6,
    damage=3,
    damage_type="B",
    conceal="N",
    display=False,
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 302)
ThrownWeapon.objects.get_or_create(
    name="Tomahawk", difficulty=6, damage=1, damage_type="L", conceal="J", display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 302)

RangedWeapon.objects.get_or_create(
    name="Revolver, Lt.", damage=4, range=12, rate=3, clip=6, conceal="P", display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 303)
RangedWeapon.objects.get_or_create(
    name="Revolver, Hvy.",
    damage=6,
    range=35,
    rate=2,
    clip=6,
    conceal="J",
    display=False,
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 303)
RangedWeapon.objects.get_or_create(
    name="Semi-Automatic Pistol, Lt.",
    damage=4,
    range=20,
    rate=4,
    clip=18,
    conceal="P",
    display=False,
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 303)
RangedWeapon.objects.get_or_create(
    name="Semi-Automatic Pistol, Hvy.",
    damage=5,
    range=25,
    rate=3,
    clip=14,
    conceal="J",
    display=False,
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 303)
RangedWeapon.objects.get_or_create(
    name="Rifle", damage=8, range=200, rate=1, clip=6, conceal="N", display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 303)
RangedWeapon.objects.get_or_create(
    name="SMG, Small", damage=4, range=25, rate=3, clip=31, conceal="J", display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 303)
RangedWeapon.objects.get_or_create(
    name="SMG, Large", damage=4, range=50, rate=3, clip=31, conceal="T", display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 303)
RangedWeapon.objects.get_or_create(
    name="Assault Rifle",
    damage=7,
    range=150,
    rate=3,
    clip=31,
    conceal="N",
    display=False,
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 303)
RangedWeapon.objects.get_or_create(
    name="Shotgun, Sawed-Off",
    damage=8,
    range=10,
    rate=2,
    clip=2,
    conceal="J",
    display=False,
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 303)
RangedWeapon.objects.get_or_create(
    name="Shotgun", damage=8, range=20, rate=1, clip=6, conceal="T", display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 303)
RangedWeapon.objects.get_or_create(
    name="Shotgun, Semi-Automatic",
    damage=8,
    range=25,
    rate=3,
    clip=7,
    conceal="T",
    display=False,
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 303)
RangedWeapon.objects.get_or_create(
    name="Shotgun, Assault",
    damage=8,
    range=50,
    rate=0,
    clip=33,
    conceal="N",
    display=False,
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 303)
RangedWeapon.objects.get_or_create(
    name="Short Bow", damage=4, range=60, rate=1, clip=1, conceal="N", display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 303)
RangedWeapon.objects.get_or_create(
    name="Hunting Bow", damage=5, range=100, rate=1, clip=1, conceal="N", display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 303)
RangedWeapon.objects.get_or_create(
    name="Long Bow", damage=5, range=120, rate=1, clip=1, conceal="N", display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 303)
RangedWeapon.objects.get_or_create(
    name="Crossbow, Commando",
    damage=3,
    range=20,
    rate=1,
    clip=1,
    conceal="J",
    display=False,
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 303)
RangedWeapon.objects.get_or_create(
    name="Crossbow", damage=5, range=90, rate=1, clip=1, conceal="T", display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 303)
RangedWeapon.objects.get_or_create(
    name="Crossbow, Hvy.",
    damage=6,
    range=100,
    rate=1,
    clip=1,
    conceal="N",
    display=False,
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 303)
RangedWeapon.objects.get_or_create(
    name="Taser", damage=5, range=5, rate=1, clip=1, conceal="P", display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 303)
RangedWeapon.objects.get_or_create(
    name="Tear Gas", damage=3, range=3, rate=1, clip=5, conceal="P", display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 303)
RangedWeapon.objects.get_or_create(
    name="Bear Mace", damage=4, range=3, rate=1, clip=3, conceal="P", display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 303)
