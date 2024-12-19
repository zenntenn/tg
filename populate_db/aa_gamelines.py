from game.models import Gameline

wod = Gameline.objects.get_or_create(name="World of Darkness")[0]
vtm = Gameline.objects.get_or_create(name="Vampire: the Masquerade")[0]
wta = Gameline.objects.get_or_create(name="Werewolf: the Apocalypse")[0]
mta = Gameline.objects.get_or_create(name="Mage: the Ascension")[0]
ctd = Gameline.objects.get_or_create(name="Changeling: the Dreaming")[0]
wto = Gameline.objects.get_or_create(name="Wraith: the Oblivion")[0]
htr = Gameline.objects.get_or_create(name="Hunter: the Reckoning")[0]
mtr = Gameline.objects.get_or_create(name="Mummy: the Resurrection")[0]
dtf = Gameline.objects.get_or_create(name="Demon: the Fallen")[0]
