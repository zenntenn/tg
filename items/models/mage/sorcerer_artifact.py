from items.models.core.item import ItemModel
from django.db import models


class SorcererArtifact(ItemModel):
    type = "sorcerer_artifact"

    rank = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Artifact (Sorcerer)"
        verbose_name_plural = "Artifacts (Sorcerer)"
