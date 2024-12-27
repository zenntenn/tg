from characters.models.werewolf.charm import SpiritCharm
from characters.models.werewolf.spirit_character import SpiritCharacter

x = SpiritCharacter.objects.get_or_create(
    name="Deer", willpower=4, rage=4, gnosis=6, essence=14, display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 368)
x.display = False
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Falcon", willpower=8, rage=6, gnosis=5, essence=19, display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 368)
x.charms.set(SpiritCharm.objects.filter(name__in=["Swift Flight"]))
x.display = False
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Snake", willpower=5, rage=6, gnosis=8, essence=19, display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 368)
x.charms.set(SpiritCharm.objects.filter(name__in=["Paralyzing Stare"]))
x.display = False
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Wolf", willpower=6, rage=7, gnosis=5, essence=18, display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 368)
x.charms.set(SpiritCharm.objects.filter(name__in=["Tracking"]))
x.display = False
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Glade Child (Sapling)",
    willpower=7,
    rage=3,
    gnosis=8,
    essence=20,
    display=False,
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 368)
x.charms.set(SpiritCharm.objects.filter(name__in=["Cleanse the Blight", "Realm Sense"]))
x.display = False
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Glade Child (Mature)",
    willpower=7,
    rage=3,
    gnosis=8,
    essence=35,
    display=False,
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 368)
x.charms.set(SpiritCharm.objects.filter(name__in=["Cleanse the Blight", "Realm Sense"]))
x.display = False
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Glade Child (Ancient)",
    willpower=7,
    rage=3,
    gnosis=8,
    essence=50,
    display=False,
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 368)
x.charms.set(SpiritCharm.objects.filter(name__in=["Cleanse the Blight", "Realm Sense"]))
x.display = False
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Lune", willpower=8, rage=4, gnosis=7, essence=19, display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 369)
x.charms.set(SpiritCharm.objects.filter(name__in=["Open Moon Bridge"]))
x.display = False
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Stormcrows", willpower=9, rage=7, gnosis=6, essence=22, display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 369)
x.charms.set(SpiritCharm.objects.filter(name__in=["Create Wind", "Tracking"]))
x.display = False
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="The Wendigo", willpower=7, rage=10, gnosis=5, essence=32, display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 369)
x.charms.set(
    SpiritCharm.objects.filter(
        name__in=["Blast", "Create Wind", "Freeze", "Materialize", "Tracking"]
    )
)
x.display = False
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="The Wild Hunt (Huntsman)",
    willpower=10,
    rage=10,
    gnosis=5,
    essence=40,
    display=False,
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 369)
x.charms.set(SpiritCharm.objects.filter(name__in=["Armor", "Materialize", "Tracking"]))
x.display = False
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="The Wild Hunt (The Hounds)",
    willpower=6,
    rage=7,
    gnosis=2,
    essence=18,
    display=False,
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 369)
x.charms.set(SpiritCharm.objects.filter(name__in=["Materialize", "Tracking"]))
x.display = False
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Ancestor Spirit", willpower=6, rage=8, gnosis=7, essence=21, display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 370)
x.charms.set(SpiritCharm.objects.filter(name__in=[]))
x.display = False
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Earth Elemental", willpower=9, rage=4, gnosis=5, essence=20, display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 370)
x.charms.set(
    SpiritCharm.objects.filter(name__in=["Armor", "Materialize", "Umbraquake"])
)
x.display = False
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Air Elemental", willpower=3, rage=8, gnosis=7, essence=18, display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 370)
x.charms.set(SpiritCharm.objects.filter(name__in=["Create Wind", "Updraft"]))
x.display = False
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Fire Elemental", willpower=5, rage=10, gnosis=5, essence=20, display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 370)
x.charms.set(SpiritCharm.objects.filter(name__in=["Blast", "Create Fires"]))
x.display = False
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Water Elemental", willpower=6, rage=4, gnosis=10, essence=20, display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 370)
x.charms.set(
    SpiritCharm.objects.filter(name__in=["Cleanse the Blight", "Flood", "Healing"])
)
x.display = False
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Glass Elemental", willpower=4, rage=7, gnosis=7, essence=18, display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 370)
x.charms.set(
    SpiritCharm.objects.filter(name__in=["Blast", "Materialize", "Shatter Glass"])
)
x.display = False
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Electricity Elemental",
    willpower=6,
    rage=7,
    gnosis=5,
    essence=18,
    display=False,
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 370)
x.charms.set(
    SpiritCharm.objects.filter(
        name__in=["Blast", "Control Electrical Systems", "Short Out"]
    )
)
x.display = False
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Chimerling", willpower=3, rage=5, gnosis=10, essence=18, display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 371)
x.charms.set(SpiritCharm.objects.filter(name__in=["Shapeshift"]))
x.display = False
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Engling", willpower=5, rage=1, gnosis=10, essence=16, display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 371)
x.charms.set(SpiritCharm.objects.filter(name__in=[]))
x.display = False
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Curiosi", willpower=5, rage=3, gnosis=9, essence=17, display=False
)[0].add_source("Werewolf: the Apocalypse 20th Anniversary Edition", 371)
x.charms.set(SpiritCharm.objects.filter(name__in=["Illuminate"]))
x.display = False
x.save()

for spirit in SpiritCharacter.objects.all():
    for x in SpiritCharm.objects.filter(
        name__in=[
            "Airt Sense",
            "Materialize",
            "Realm Sense",
            "Re-Form",
        ]
    ):
        spirit.charms.add(x)
