from characters.models.core.meritflaw import MeritFlaw, MeritFlawRating
from django.db import models
from django.db.models import F, Q
from game.models import ObjectType


class MeritFlawBlock(models.Model):
    merits_and_flaws = models.ManyToManyField(
        MeritFlaw, blank=True, through=MeritFlawRating, related_name="flawed"
    )

    class Meta:
        abstract = True

    def num_languages(self):
        mf_list = self.merits_and_flaws.all().values_list("name", flat=True)
        if "Language" not in mf_list:
            return 0
        language_rating = self.mf_rating(MeritFlaw.objects.get(name="Language"))
        if "Natural Linguist" in mf_list:
            language_rating *= 2
        return language_rating

    def get_mf_and_rating_list(self):
        return [(x.name, self.mf_rating(x)) for x in self.merits_and_flaws.all()]

    def add_mf(self, mf, rating):
        if rating in mf.get_ratings():
            mfr, _ = MeritFlawRating.objects.get_or_create(character=self, mf=mf)
            mfr.rating = rating
            mfr.save()
            if mf.name in ["Language", "Natural Linguist"] and self.status == "Ran":
                num_languages = self.mf_rating(MeritFlaw.objects.get(name="Language"))
                if self.merits_and_flaws.filter(name="Natural Linguist").exists():
                    num_languages *= 2
                while self.languages.count() < num_languages:
                    self.add_random_language()
            if mf.name == "Deranged" and self.status == "Ran":
                self.random_derangement()
            return True
        return False

    def filter_mfs(self):
        character_type = self.type
        if character_type in ["fomor"]:
            character_type = "human"

        new_mfs = MeritFlaw.objects.exclude(pk__in=self.merits_and_flaws.all())

        non_max_mf = MeritFlawRating.objects.filter(character=self).exclude(
            Q(rating=F("mf__max_rating"))
        )

        had_mfs = MeritFlaw.objects.filter(pk__in=non_max_mf)
        mf = new_mfs | had_mfs
        if self.has_max_flaws():
            mf = mf.filter(max_rating__gt=0)
        character_type_object = ObjectType.objects.get(name=character_type)
        return mf.filter(allowed_types=character_type_object)

    def mf_rating(self, mf):
        if mf not in self.merits_and_flaws.all():
            return 0
        return MeritFlawRating.objects.get(character=self, mf=mf).rating

    def has_max_flaws(self):
        return self.total_flaws() <= -7

    def total_flaws(self):
        return sum(
            x.rating
            for x in MeritFlawRating.objects.filter(character=self)
            if x.rating < 0
        )

    def total_merits(self):
        return sum(
            x.rating
            for x in MeritFlawRating.objects.filter(character=self)
            if x.rating > 0
        )
