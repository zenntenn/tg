from django.db import models


class Statistic(models.Model):
    type = "statistic"

    name = models.CharField(max_length=100)
    property_name = models.CharField(max_length=100)

    def __str__(self):
        return self.property_name
