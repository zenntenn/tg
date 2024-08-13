from django.urls import reverse
from items.models.core.weapon import Weapon

# Create your models here.


class MeleeWeapon(Weapon):
    type = "melee_weapon"

    class Meta:
        verbose_name = "Melee Weapon"
        verbose_name_plural = "Melee Weapons"

    def get_update_url(self):
        return reverse("items:update:meleeweapon", args=[str(self.id)])