import random
from characters.models.core import MeritFlaw
from characters.models.mage.resonance import Resonance
from core.models import Model, Noun
from core.utils import weighted_choice
from django.db import models
from django.db.models import F, Q
from django.urls import reverse
from game.models import ObjectType
from locations.models.core import LocationModel


# Create your models here.
class SizeChoices(models.IntegerChoices):
    TINY = -2, "Household Object"
    SMALL = -1, "Small Room"
    NORMAL = 0, "Average Room"
    LARGE = 1, "Small Building"
    HUGE = 2, "Large Building"


class RatioChoices(models.IntegerChoices):
    TINY = -2, "0.0"
    SMALL = -1, "0.25"
    NORMAL = 0, "0.5"
    LARGE = 1, "0.75"
    HUGE = 2, "1.0"


class Node(LocationModel):
    type = "node"

    rank = models.IntegerField(default=0)

    size = models.IntegerField(default=SizeChoices.NORMAL, choices=SizeChoices.choices)
    ratio = models.IntegerField(
        default=RatioChoices.NORMAL, choices=RatioChoices.choices
    )

    points = models.IntegerField(default=0)
    merits_and_flaws = models.ManyToManyField(
        MeritFlaw, blank=True, through="NodeMeritFlawRating"
    )
    resonance = models.ManyToManyField(
        "characters.Resonance", blank=True, through="NodeResonanceRating"
    )

    quintessence_per_week = models.IntegerField(default=0)
    tass_per_week = models.IntegerField(default=0)
    tass_form = models.CharField(default="", max_length=100)
    quintessence_form = models.CharField(default="", max_length=100)

    class Meta:
        verbose_name = "Node"
        verbose_name_plural = "Nodes"

    def get_update_url(self):
        return reverse("locations:mage:update:node", args=[str(self.id)])

    @classmethod
    def get_creation_url(cls):
        return reverse("locations:mage:create:node")

    def get_heading(self):
        return "mtas_heading"

    def set_rank(self, rank):
        self.rank = rank
        self.points = 3 * self.rank
        return True

    def add_mf(self, mf, rating):
        node = ObjectType.objects.get_or_create(
            name="node", type="loc", gameline="mta"
        )[0]
        if not node in mf.allowed_types.all():
            return False
        if not mf.ratings.filter(value=rating).exists():
            return False
        if mf in self.merits_and_flaws.all():
            current_rating = NodeMeritFlawRating.objects.get(node=self, mf=mf).rating
            if 0 < current_rating < rating:
                x = NodeMeritFlawRating.objects.get(node=self, mf=mf)
                x.rating = rating
                x.save()
                return True
            if 0 > current_rating > rating:
                x = NodeMeritFlawRating.objects.get(node=self, mf=mf)
                x.rating = rating
                x.save()
                return True
            return False
        NodeMeritFlawRating.objects.create(node=self, mf=mf, rating=rating)
        return True

    def total_mf(self):
        return sum(x.rating for x in NodeMeritFlawRating.objects.filter(node=self))

    def filter_mf(self, minimum=-10, maximum=10):
        node = ObjectType.objects.get_or_create(
            name="node", type="loc", gameline="mta"
        )[0]

        new_mfs = MeritFlaw.objects.filter(allowed_types__in=[node.pk]).exclude(
            pk__in=self.merits_and_flaws.all()
        )
        had_mf_ratings = NodeMeritFlawRating.objects.all()
        had_mf_ratings = had_mf_ratings.filter(rating__lt=F("mf__max_rating"))

        had_mfs = MeritFlaw.objects.filter(
            pk__in=had_mf_ratings.values_list("mf", flat=True)
        )
        q = new_mfs | had_mfs

        q = q.filter(max_rating__lte=maximum)
        q = q.filter(min_rating__gte=minimum)

        return q

    def mf_rating(self, mf):
        if mf not in self.merits_and_flaws.all():
            return 0
        return NodeMeritFlawRating.objects.get(node=self, mf=mf).rating

    def add_resonance(self, resonance):
        r, _ = NodeResonanceRating.objects.get_or_create(resonance=resonance, node=self)
        if r.rating == 5:
            return False
        r.rating += 1
        r.save()
        return True

    def resonance_rating(self, resonance):
        if resonance in self.resonance.all():
            return NodeResonanceRating.objects.get(
                node=self, resonance=resonance
            ).rating
        return 0

    def filter_resonance(self, minimum=0, maximum=5, sphere=None):
        all_res = Resonance.objects.all()
        if sphere is None:
            q = Q()
        else:
            q = Q(**{sphere: True})
        all_res = all_res.filter(q)

        maxed_resonance = [
            x.resonance.id
            for x in NodeResonanceRating.objects.filter(node=self, rating__gt=maximum)
        ]
        mined_resonance = [
            x.resonance.id
            for x in NodeResonanceRating.objects.filter(node=self, rating__lt=minimum)
        ]
        all_res = all_res.exclude(pk__in=maxed_resonance)
        all_res = all_res.exclude(pk__in=mined_resonance)
        if minimum > 0:
            all_res = all_res.filter(
                pk__in=[
                    x.resonance.id
                    for x in NodeResonanceRating.objects.filter(node=self, rating__gt=0)
                ]
            )
        return all_res

    def total_resonance(self):
        return sum(x.rating for x in NodeResonanceRating.objects.filter(node=self))

    def check_resonance(self, resonance, sphere=None):
        if self.resonance_rating(resonance) < 5:
            if sphere is None:
                return True
            return getattr(resonance, sphere)
        return False

    def resonance_postprocessing(self):
        if "Corrupted" in [x.name for x in self.merits_and_flaws.all()]:
            res, _ = Resonance.objects.get_or_create(name="Corrupted")
            self.add_resonance(res)
            self.add_resonance(res)
        # if "Sphere Attuned" in [x.name for x in self.merits_and_flaws.all()]:
        #     sphere = Sphere.objects.order_by("?").first()
        #     self.random_resonance(sphere=sphere)

    def has_resonance(self):
        return self.total_resonance() >= self.rank

    def has_output_forms(self):
        return self.quintessence_form != "" and self.tass_form != ""

    def set_output_forms(self, quint_form, tass_form):
        self.quintessence_form = quint_form
        self.tass_form = tass_form
        return True

    def has_output(self):
        return self.quintessence_per_week != 0 or self.tass_per_week != 0

    def set_ratio(self, ratio):
        self.ratio = ratio
        return True

    def set_size(self, size):
        self.size = size
        return True

    def update_output(self):
        self.quintessence_per_week = int(self.points * float(self.get_ratio_display()))
        self.tass_per_week = self.points - self.quintessence_per_week
        return True

    def random_rank(self, rank=None):
        if rank is None:
            rank = random.randint(1, 5)
        self.set_rank(rank)

    def random_mf(self, minimum=-10, maximum=10):
        possibility = self.filter_mf(minimum=minimum, maximum=maximum)
        choice = random.choice(possibility)
        possible_ratings = choice.ratings.all()
        possible_ratings = [
            x.value for x in possible_ratings if minimum <= x.value <= maximum
        ]
        r = 0
        if self.mf_rating(choice) < 0:
            possible_ratings = [
                x for x in possible_ratings if x < self.mf_rating(choice)
            ]
        if self.mf_rating(choice) > 0:
            possible_ratings = [
                x for x in possible_ratings if x > self.mf_rating(choice)
            ]
        if len(possible_ratings) == 0:
            return False
        r = random.choice(possible_ratings)
        return self.add_mf(choice, r)

    def random_resonance(self, sphere=None, favored_list=None):
        if random.random() < 0.7:
            possible = self.filter_resonance(minimum=1, maximum=4, sphere=sphere)
            if len(possible) > 0:
                choice = random.choice(possible)
                if self.add_resonance(choice):
                    return True
        while True:
            if favored_list is not None:
                choices = {i: 1 for i in range(1, Resonance.objects.last().id + 1)}
                for resonance in favored_list:
                    choices[resonance.id] += 100
            else:
                choices = {i: 1 for i in range(1, Resonance.objects.last().id + 1)}
            index = weighted_choice(choices, floor=1, ceiling=1000000)
            if Resonance.objects.filter(pk=index).exists():
                choice = Resonance.objects.get(pk=index)
                if self.check_resonance(choice, sphere=sphere):
                    if self.add_resonance(choice):
                        return True

    def random_forms(self):
        quintessence, tass = Noun.objects.order_by("?")[:2]
        self.set_output_forms(quintessence.name.title(), tass.name.title())

    def random_ratio(self):
        choice = random.choice([-2, -1, -1, 0, 0, 0, 1, 1, 2])
        self.set_ratio(choice)
        self.points -= self.ratio

    def random_size(self):
        choice = random.choice([-2, -1, -1, 0, 0, 0, 1, 1, 2])
        self.set_size(choice)
        self.points -= self.size

    def random_name(self):
        if not self.has_name():
            if NodeResonanceRating.objects.filter(node=self).count() > 0:
                highest_res_rating = (
                    NodeResonanceRating.objects.filter(node=self)
                    .order_by("-rating")
                    .first()
                ).resonance.name.title()
            else:
                highest_res_rating = ""
            n = Noun.objects.order_by("?").first()
            name = f"{highest_res_rating} {n.name.title()}".strip()
            return self.set_name(name)
        return True

    def random(self, rank=None, favored_list=None):
        self.update_status("Ran")
        self.gauntlet = 3
        self.random_rank(rank=rank)
        while not self.has_resonance():
            self.random_resonance(favored_list=favored_list)
        self.random_ratio()
        self.random_size()
        self.random_forms()
        while random.random() < 0.2 and self.points > 1:
            self.random_resonance(favored_list=favored_list)
        while random.random() < 0.4 and self.points > 1:
            current = self.total_mf()
            self.random_mf(maximum=self.points - 1)
            new = self.total_mf()
            self.points -= new - current
        self.resonance_postprocessing()
        self.update_output()
        self.points = 0
        self.random_name()


class NodeMeritFlawRating(models.Model):
    node = models.ForeignKey(Node, on_delete=models.SET_NULL, null=True)
    mf = models.ForeignKey(MeritFlaw, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Node Merit or Flaw Rating"
        verbose_name_plural = "Node Merits and Flaws Rating"


class NodeResonanceRating(models.Model):
    node = models.ForeignKey(Node, on_delete=models.SET_NULL, null=True)
    resonance = models.ForeignKey(Resonance, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Node Resonance Rating"
        verbose_name_plural = "Node Resonance Ratings"
