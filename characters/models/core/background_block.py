from characters.models.core.background import Background, BackgroundRating
from core.utils import weighted_choice
from django.db import models


class BackgroundBlock(models.Model):
    allowed_backgrounds = []
    background_points = 5

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for bg in self.allowed_backgrounds:
            if not hasattr(self.__class__, bg):
                setattr(self.__class__, bg, self._create_property(bg))

    def _create_property(self, bg):
        return property(
            lambda self: self._get_property(bg),
            lambda self, value: self._set_property(bg, value),
        )

    def _get_property(self, bg):
        return self.total_background_rating(bg)

    def _set_property(self, prop, value):
        if value != 0:
            BackgroundRating.objects.create(
                char=self, bg=Background.objects.get(property_name=prop), rating=value
            )
        else:
            BackgroundRating.objects.filter(char=self, bg__property_name=prop).delete()

    def total_background_rating(self, bg_name):
        return sum(
            [
                x.rating
                for x in BackgroundRating.objects.filter(
                    bg__property_name=bg_name, char=self
                )
            ]
        )

    def get_backgrounds(self):
        return {bg: getattr(self, bg) for bg in self.allowed_backgrounds}

    def add_background(self, background, maximum=5):
        if isinstance(background, str):
            bg = Background.objects.get(property_name=background)
            ratings = BackgroundRating.objects.filter(char=self, bg=bg)
            if ratings.filter(rating__lt=5).count() > 0:
                background = ratings.filter(rating__lt=5).first()
            else:
                background = BackgroundRating.objects.create(char=self, bg=bg)
        elif isinstance(background, Background):
            ratings = BackgroundRating.objects.filter(char=self, bg=background)
            if ratings.filter(rating__lt=5).count() > 0:
                background = ratings.filter(rating__lt=5).first()
            else:
                background = BackgroundRating.objects.create(char=self, bg=background)
        else:
            raise ValueError(
                "Must be a background name, Background object, or BackgroundRating object"
            )
        if background.rating == 5:
            return False
        background.rating += 1
        background.save()
        return True

    def total_backgrounds(self):
        return sum(self.get_backgrounds().values())

    def filter_backgrounds(self, minimum=0, maximum=5):
        return {
            k: v for k, v in self.get_backgrounds().items() if minimum <= v <= maximum
        }

    def has_backgrounds(self):
        if self.total_backgrounds() > self.background_points:
            self.freebies -= self.total_backgrounds() - self.background_points
        return self.total_backgrounds() >= self.background_points

    def random_background(self):
        choice = weighted_choice(self.get_backgrounds())
        return self.add_background(choice)

    def random_backgrounds(self, backgrounds=None):
        if backgrounds is None:
            backgrounds = {}
        for trait, value in backgrounds.items():
            setattr(self, trait, value)
        while not self.has_backgrounds():
            self.random_background()
