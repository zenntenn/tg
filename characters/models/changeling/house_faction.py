from core.models import Model


class HouseFaction(Model):
    type = "house_faction"

    class Meta:
        verbose_name = "House Faction"
        verbose_name_plural = "House Factions"
