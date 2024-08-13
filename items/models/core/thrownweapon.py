from django.urls import reverse
from items.models.core.weapon import Weapon

# Create your models here.


class ThrownWeapon(Weapon):
    type = "thrown_weapon"

    class Meta:
        verbose_name = "Thrown Weapon"
        verbose_name_plural = "Thrown Weapons"

    def get_update_url(self):
        return reverse("items:update:thrownweapon", args=[str(self.id)])