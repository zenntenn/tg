import cProfile
import pstats
import random
from pstats import SortKey
from time import time


def add_dot(character, trait, maximum):
    trait_value = getattr(character, trait, None)
    if trait_value is not None and trait_value < maximum:
        setattr(character, trait, trait_value + 1)
        character.save()
        return True
    return False


def check_floor_ceiling(x, floor, ceiling):
    if x < floor:
        return floor
    if x > ceiling:
        return ceiling
    return x


def weighted_choice(dictionary, floor=0, ceiling=5):
    d = {
        k: check_floor_ceiling(v, floor=floor, ceiling=ceiling)
        for k, v in dictionary.items()
    }
    l = []
    for key, value in d.items():
        for _ in range(value + 1):
            for __ in range(value + 1):
                l.append(key)
    return random.choice(l)


def dice(dicepool, difficulty=6, specialty=False):
    dice_list = [random.randint(1, 10) for _ in range(dicepool)]
    ones = len([x for x in dice_list if x == 1])
    tens = len([x for x in dice_list if x == 10])
    successes = len([x for x in dice_list if x >= difficulty])
    total = successes - ones
    if successes == 0:
        return dice_list, total
    if specialty:
        total += tens
    return dice_list, max([total, 0])


def compute_level(x, level=0):
    if x.parent is None:
        return level
    return compute_level(x.parent, level=level + 1)


def level_name(x):
    return (compute_level(x) * "&emsp;&emsp;") + x.name


def tree_sort(x, l=None):
    if l is None:
        l = []
    l.append(x)
    for y in x.children.order_by("name"):
        tree_sort(y, l=l)
    return l


def filepath(instance, filename):
    s = str(instance.__class__).split(" ")[-1][:-1][1:-1]
    s = "/".join([x for x in s.split(".") if x != "models"])
    s += "/" + instance.name
    s += "." + filename.split(".")[-1]
    s = s.lower().replace(" ", "_")
    return s


def get_gameline_name(s):
    if s == "wod":
        return "World of Darkness"
    elif s == "vtm":
        return "Vampire: the Masquerade"
    elif s == "wta":
        return "Werewolf: the Apocalypse"
    elif s == "mta":
        return "Mage: the Ascension"
    elif s == "wto":
        return "Wraith: the Oblivion"
    elif s == "cta":
        return "Changeling: the Dreaming"


def fast_selector(cls):
    max_value = cls.objects.last().id
    index = random.randint(1, max_value)
    while not cls.objects.filter(pk=index).exists():
        index = random.randint(1, max_value)
    return cls.objects.get(pk=index)


def time_test(cls, player, character=True, xp=0, random_name=True):
    start = time()
    for _ in range(10):
        create(cls, player, character=character, xp=xp, random_name=random_name)
    avg_time = (time() - start) / 10
    print(f"Average Random {cls.__name__} Time:", avg_time)
    return avg_time


def create(cls, player, character=True, xp=0, random_name=True):
    if random_name:
        name = ""
    else:
        name = f"{cls.__name__} {cls.objects.count()}"
    obj = cls.objects.create(name=name, owner=player)
    if character:
        obj.random(xp=xp)
    else:
        obj.random()
    obj.save()


def profile(cls, player, character=True, num_rows=10, xp=0):
    cProfile.run(
        f"create({cls.__name__}, player, character={character}, xp={xp})", "tmp"
    )
    p = pstats.Stats("tmp")
    p.sort_stats(SortKey.CUMULATIVE).print_stats(num_rows)


def display_queryset(prop):
    return "<br>".join([f'<a href="{x.get_absolute_url()}">{x}</a>' for x in prop])
