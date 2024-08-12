from django.db import models


class Sphere(models.Model):
    type = "sphere"

    name = models.CharField(max_length=100)
