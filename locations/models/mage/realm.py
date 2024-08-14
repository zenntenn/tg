from django.urls import reverse
from locations.models.core.location import LocationModel


class HorizonRealm(LocationModel):
    type = "horizon_realm"

    class Meta:
        verbose_name = "Horizon Realm"
        verbose_name_plural = "Horizon Realms"

    def get_update_url(self):
        return reverse("locations:mage:update:realm", args=[str(self.id)])

    def get_heading(self):
        return "mtas_heading"
