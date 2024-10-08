from django.db import models
from polymorphic.models import PolymorphicModel


class Statistic(PolymorphicModel):
    type = "statistic"

    name = models.CharField(max_length=100)
    property_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
