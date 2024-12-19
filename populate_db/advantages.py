from characters.models.mage.companion import Advantage

a = Advantage.objects.get_or_create(name="Alacrity")[0].add_source(
    "Gods and Monsters", 201
)
a.add_ratings([2, 4, 6])
a = Advantage.objects.get_or_create(name="Armor")[0].add_source(
    "Gods and Monsters", 201
)
a.add_ratings([1, 2, 3, 4, 5])
a = Advantage.objects.get_or_create(name="Armor (Soak Aggravated)")[0].add_source(
    "Gods and Monsters", 201
)
a.add_ratings([2, 4, 6, 8, 10])
a = Advantage.objects.get_or_create(name="Aura")[0].add_source("Gods and Monsters", 202)
a.add_ratings([3])
a = Advantage.objects.get_or_create(name="Aww!")[0].add_source("Gods and Monsters", 202)
a.add_ratings([1, 2, 3, 4])
a = Advantage.objects.get_or_create(name="Bare Necessities")[0].add_source(
    "Gods and Monsters", 202
)
a.add_ratings([1, 3])
a = Advantage.objects.get_or_create(name="Bioluminescence")[0].add_source(
    "Gods and Monsters", 202
)
a.add_ratings([1, 2, 3])
a = Advantage.objects.get_or_create(name="Blending")[0].add_source(
    "Gods and Monsters", 203
)
a.add_ratings([1])
a = Advantage.objects.get_or_create(name="Bond-Sharing")[0].add_source(
    "Gods and Monsters", 203
)
a.add_ratings([4, 5, 6])
a = Advantage.objects.get_or_create(name="Claws, Fangs, or Horns")[0].add_source(
    "Gods and Monsters", 203
)
a.add_ratings([3, 5, 7])
a = Advantage.objects.get_or_create(name="Cause Insanity")[0].add_source(
    "Gods and Monsters", 203
)
a.add_ratings([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
a = Advantage.objects.get_or_create(name="Deadly Demise")[0].add_source(
    "Gods and Monsters", 204
)
a.add_ratings([2, 4, 6])
a = Advantage.objects.get_or_create(name="Elemental Touch")[0].add_source(
    "Gods and Monsters", 204
)
a.add_ratings([3, 5, 7, 10, 15])
a = Advantage.objects.get_or_create(name="Empathic Bond")[0].add_source(
    "Gods and Monsters", 205
)
a.add_ratings([2])
a = Advantage.objects.get_or_create(name="Extra Heads")[0].add_source(
    "Gods and Monsters", 205
)
a.add_ratings([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
a = Advantage.objects.get_or_create(name="Extra Limbs")[0].add_source(
    "Gods and Monsters", 205
)
a.add_ratings([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
a = Advantage.objects.get_or_create(name="Ferocity")[0].add_source(
    "Gods and Monsters", 205
)
a.add_ratings([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
a = Advantage.objects.get_or_create(name="Flexibility")[0].add_source(
    "Gods and Monsters", 206
)
a.add_ratings([2])
a = Advantage.objects.get_or_create(name="Dominance")[0].add_source(
    "Gods and Monsters", 204
)
a.add_ratings([1])
a = Advantage.objects.get_or_create(name="Earthbond")[0].add_source(
    "Gods and Monsters", 204
)
a.add_ratings([2])
a = Advantage.objects.get_or_create(name="Hazardous Breath")[0].add_source(
    "Gods and Monsters", 206
)
a.add_ratings([5, 10, 15, 20, 25, 30])
a = Advantage.objects.get_or_create(name="Hazardous Breath (Aggravated)")[0].add_source(
    "Gods and Monsters", 206
)
a.add_ratings([10, 20, 30, 40, 50, 60])
a = Advantage.objects.get_or_create(name="Hazardous Breath (Caustic)")[0].add_source(
    "Gods and Monsters", 206
)
a.add_ratings([7, 14, 21, 28, 35, 42])
a = Advantage.objects.get_or_create(name="Hazardous Breath (Caustic, Aggravated)")[
    0
].add_source("Gods and Monsters", 206)
a.add_ratings([14, 28, 42, 56, 70, 84])
a = Advantage.objects.get_or_create(name="Healing Lick")[0].add_source(
    "Gods and Monsters", 206
)
a.add_ratings([3, 6])
a = Advantage.objects.get_or_create(name="Homing Instinct")[0].add_source(
    "Gods and Monsters", 206
)
a.add_ratings([2, 4])
a = Advantage.objects.get_or_create(name="Human Guise")[0].add_source(
    "Gods and Monsters", 206
)
a.add_ratings([2, 4])
a = Advantage.objects.get_or_create(name="Human Speech")[0].add_source(
    "Gods and Monsters", 207
)
a.add_ratings([1])
a = Advantage.objects.get_or_create(name="Information Fount")[0].add_source(
    "Gods and Monsters", 207
)
a.add_ratings([5])
a = Advantage.objects.get_or_create(name="Intangibility")[0].add_source(
    "Gods and Monsters", 207
)
a.add_ratings([8, 10])
a = Advantage.objects.get_or_create(name="Mesemerism")[0].add_source(
    "Gods and Monsters", 207
)
a.add_ratings([3, 6])
a = Advantage.objects.get_or_create(name="Musical Influence")[0].add_source(
    "Gods and Monsters", 208
)
a.add_ratings([6])
a = Advantage.objects.get_or_create(name="Musk")[0].add_source("Gods and Monsters", 208)
a.add_ratings([3])
a = Advantage.objects.get_or_create(name="Mystic Shield")[0].add_source(
    "Gods and Monsters", 208
)
a.add_ratings([2, 4, 6, 8, 10])
a = Advantage.objects.get_or_create(name="Needleteeth")[0].add_source(
    "Gods and Monsters", 209
)
a.add_ratings([3])
a = Advantage.objects.get_or_create(name="Nightsight")[0].add_source(
    "Gods and Monsters", 209
)
a.add_ratings([3])
a = Advantage.objects.get_or_create(name="Omega Status")[0].add_source(
    "Gods and Monsters", 209
)
a.add_ratings([4])
a = Advantage.objects.get_or_create(name="Paradox Nullification")[0].add_source(
    "Gods and Monsters", 209
)
a.add_ratings([2, 3, 4, 5, 6])
a = Advantage.objects.get_or_create(name="Quills")[0].add_source(
    "Gods and Monsters", 209
)
a.add_ratings([2, 4])
a = Advantage.objects.get_or_create(name="Rapid Healing")[0].add_source(
    "Gods and Monsters", 210
)
a.add_ratings([2, 4, 6, 8, 10])
a = Advantage.objects.get_or_create(name="Razorskin")[0].add_source(
    "Gods and Monsters", 210
)
a.add_ratings([3])
a = Advantage.objects.get_or_create(name="Read and Write")[0].add_source(
    "Gods and Monsters", 210
)
a.add_ratings([1])
a = Advantage.objects.get_or_create(name="Regrowth")[0].add_source(
    "Gods and Monsters", 210
)
a.add_ratings([2, 4, 6])
a = Advantage.objects.get_or_create(name="Shapechanger")[0].add_source(
    "Gods and Monsters", 210
)
a.add_ratings([3, 5, 8])
a = Advantage.objects.get_or_create(name="Size")[0].add_source("Gods and Monsters", 34)
a.add_ratings([3, 5, 8])
a = Advantage.objects.get_or_create(name="Soak Lethal Damage")[0].add_source(
    "Gods and Monsters", 211
)
a.add_ratings([3])
a = Advantage.objects.get_or_create(name="Soak Aggravated Damage")[0].add_source(
    "Gods and Monsters", 211
)
a.add_ratings([5])
a = Advantage.objects.get_or_create(name="Soul-Sense/Death-Sense")[0].add_source(
    "Gods and Monsters", 211
)
a.add_ratings([2, 3])
a = Advantage.objects.get_or_create(name="Speed")[0].add_source(
    "Gods and Monsters", 211
)
a.add_ratings([2, 4, 6, 8, 10])
a = Advantage.objects.get_or_create(name="Spirit Vision")[0].add_source(
    "Gods and Monsters", 212
)
a.add_ratings([3])
a = Advantage.objects.get_or_create(name="Spirit Travel")[0].add_source(
    "Gods and Monsters", 211
)
a.add_ratings([8, 10, 16])
a = Advantage.objects.get_or_create(name="Telepathy")[0].add_source(
    "Gods and Monsters", 212
)
a.add_ratings([2, 4, 6])
a = Advantage.objects.get_or_create(name="Telekinesis")[0].add_source(
    "Gods and Monsters", 212
)
a.add_ratings([3, 5, 8, 12])
a = Advantage.objects.get_or_create(name="Tides of Fortune")[0].add_source(
    "Gods and Monsters", 213
)
a.add_ratings([5])
a = Advantage.objects.get_or_create(name="Tunneling")[0].add_source(
    "Gods and Monsters", 213
)
a.add_ratings([3])
a = Advantage.objects.get_or_create(name="Unaging")[0].add_source(
    "Gods and Monsters", 213
)
a.add_ratings([5])
a = Advantage.objects.get_or_create(name="Universal Translator")[0].add_source(
    "Gods and Monsters", 213
)
a.add_ratings([5])
a = Advantage.objects.get_or_create(name="Venom (Injury)")[0].add_source(
    "Gods and Monsters", 213
)
a.add_ratings([3, 6, 9, 12, 15, 18, 21])
a = Advantage.objects.get_or_create(name="Venom (Contact)")[0].add_source(
    "Gods and Monsters", 213
)
a.add_ratings([5, 10, 15, 20, 25, 30])
a = Advantage.objects.get_or_create(name="Wall-Crawling")[0].add_source(
    "Gods and Monsters", 213
)
a.add_ratings([3])
a = Advantage.objects.get_or_create(name="Water-Breathing")[0].add_source(
    "Gods and Monsters", 214
)
a.add_ratings([2, 5])
a = Advantage.objects.get_or_create(name="Webbing")[0].add_source(
    "Gods and Monsters", 214
)
a.add_ratings([5])
a = Advantage.objects.get_or_create(name="Wings")[0].add_source(
    "Gods and Monsters", 214
)
a.add_ratings([3, 5])
