from characters.models.changeling.kith import Kith

Kith.objects.get_or_create(
    name="Boggan",
    affinity="actor",
    birthrights=["Craftwork", "Social Dynamics"],
    frailty="Call of the Needy",
)[0].add_source("Changeling: the Dreaming 20th Anniversary Edition", 88)
Kith.objects.get_or_create(
    name="Clurichaun",
    affinity="actor",
    birthrights=["Twinkling of an Eye", "Fighting Words"],
    frailty="Hoard",
)[0].add_source("Changeling: the Dreaming 20th Anniversary Edition", 90)
Kith.objects.get_or_create(
    name="Eshu",
    affinity="scene",
    birthrights=["Serendipity", "Talecraft"],
    frailty="Recklessness",
)[0].add_source("Changeling: the Dreaming 20th Anniversary Edition", 92)
Kith.objects.get_or_create(
    name="Nocker",
    affinity="prop",
    birthrights=["Make it Work", "Fix-It"],
    frailty="Perfect is the Enemy of Done",
)[0].add_source("Changeling: the Dreaming 20th Anniversary Edition", 94)
Kith.objects.get_or_create(
    name="Piskey",
    affinity="actor",
    birthrights=["Nimble", "Blending In"],
    frailty="Light-Fingers",
)[0].add_source("Changeling: the Dreaming 20th Anniversary Edition", 96)
Kith.objects.get_or_create(
    name="Pooka",
    affinity="nature",
    birthrights=["Shapechanging", "Confidante"],
    frailty="Untruths",
)[0].add_source("Changeling: the Dreaming 20th Anniversary Edition", 98)
Kith.objects.get_or_create(
    name="Redcap",
    affinity="nature",
    birthrights=["Dark Appetite", "Bully Browbeat"],
    frailty="Bad Attitude",
)[0].add_source("Changeling: the Dreaming 20th Anniversary Edition", 100)
Kith.objects.get_or_create(
    name="Satyr",
    affinity="fae",
    birthrights=["Gift of Pan", "Physical Prowess"],
    frailty="Passion's Curse",
)[0].add_source("Changeling: the Dreaming 20th Anniversary Edition", 102)
Kith.objects.get_or_create(
    name="Selkie",
    affinity="nature",
    birthrights=["Seal Form", "Ocean's Grace"],
    frailty="Seal Coat",
)[0].add_source("Changeling: the Dreaming 20th Anniversary Edition", 104)
Kith.objects.get_or_create(
    name="Arcadian Sidhe",
    affinity="time",
    birthrights=["Unearthly Beauty", "Noble Bearing"],
    frailty="Curse of Banality",
)[0].add_source("Changeling: the Dreaming 20th Anniversary Edition", 106)
Kith.objects.get_or_create(
    name="Autumn Sidhe",
    affinity="fae",
    birthrights=["Unearthly Beauty", "Noble Bearing"],
    frailty="Adoration",
)[0].add_source("Changeling: the Dreaming 20th Anniversary Edition", 108)
Kith.objects.get_or_create(
    name="Sluagh",
    affinity="prop",
    birthrights=["Squirm", "Sharpened Senses"],
    frailty="Curse of Silence",
)[0].add_source("Changeling: the Dreaming 20th Anniversary Edition", 110)
Kith.objects.get_or_create(
    name="Troll",
    affinity="fae",
    birthrights=["Titan's Power", "Strong of Will and Body"],
    frailty="Bond of Duty",
)[0].add_source("Changeling: the Dreaming 20th Anniversary Edition", 112)
