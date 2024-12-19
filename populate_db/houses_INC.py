from characters.models.changeling.house import House
from characters.models.changeling.house_faction import HouseFaction

h = House.objects.get_or_create(
    name="House Aesin",
    court="unseelie",
    boon="Speak with forest animals",
    flaw="Cannot gain Glamour through Rapture",
)[0].add_source("Changeling: the Dreaming 20th Anniversary Edition", 119)

hf = HouseFaction.objects.get_or_create(name="The Virtue Council")[0]
h.factions.add(hf)
hf = HouseFaction.objects.get_or_create(name="The Berserkers")[0]
h.factions.add(hf)

h = House.objects.get_or_create(
    name="House Ailil",
    court="unseelie",
    boon="-1 diff on manipulation",
    flaw="Willpower roll to admit being wrong, and +1 penalty to all Social rolls when they've lost face",
)[0].add_source("Changeling: the Dreaming 20th Anniversary Edition", 120)

hf = HouseFaction.objects.get_or_create(name="The Guardians of the Silver Dragon")[0]
h.factions.add(hf)
hf = HouseFaction.objects.get_or_create(name="Les Amoureux")[0]
h.factions.add(hf)
hf = HouseFaction.objects.get_or_create(name="The Disinherited")[0]
h.factions.add(hf)
hf = HouseFaction.objects.get_or_create(name="The Lock-Keepers")[0]
h.factions.add(hf)


h = House.objects.get_or_create(
    name="House Balor",
    court="unseelie",
    boon="No Glamour loss from cold iron, can soak cold iron damage at diff 10.",
    flaw="Deformed",
)[0].add_source("Changeling: the Dreaming 20th Anniversary Edition", 122)

hf = HouseFaction.objects.get_or_create(name="The Eyes of Balor")[0]
h.factions.add(hf)
hf = HouseFaction.objects.get_or_create(name="Masters of the Dance")[0]
h.factions.add(hf)
hf = HouseFaction.objects.get_or_create(name="The Old Firm")[0]
h.factions.add(hf)
hf = HouseFaction.objects.get_or_create(name="The Guardians of the Gates")[0]
h.factions.add(hf)
hf = HouseFaction.objects.get_or_create(name="The Riders of the Fell")[0]
h.factions.add(hf)
hf = HouseFaction.objects.get_or_create(name="Scarlet Eye Solutions")[0]
h.factions.add(hf)

# TODO: Finish Houses and House Factions
House.objects.get_or_create(name="House Beaumayn", court="seelie", boon="", flaw="",)[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 123)
House.objects.get_or_create(name="House Danaan", court="unseelie", boon="", flaw="",)[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 124)
House.objects.get_or_create(name="House Daireann", court="unseelie", boon="", flaw="",)[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 126)
House.objects.get_or_create(name="House Dougal", court="seelie", boon="", flaw="",)[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 127)
House.objects.get_or_create(name="House Eiluned", court="seelie", boon="", flaw="",)[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 128)
House.objects.get_or_create(name="House Fiona", court="seelie", boon="", flaw="",)[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 129)
House.objects.get_or_create(name="House Gwydion", court="seelie", boon="", flaw="",)[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 131)
House.objects.get_or_create(name="House Leanhaun", court="unseelie", boon="", flaw="",)[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 132)
House.objects.get_or_create(name="House Liam", court="seelie", boon="", flaw="",)[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 133)
House.objects.get_or_create(name="House Scathach", court="seelie", boon="", flaw="",)[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 135)
House.objects.get_or_create(name="House Varich", court="unseelie", boon="", flaw="",)[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 136)
