from django.urls import reverse
from items.models.core.weapon import Weapon


class MeleeWeapon(Weapon):
    type = "melee_weapon"

    class Meta:
        verbose_name = "Melee Weapon"
        verbose_name_plural = "Melee Weapons"

    def get_update_url(self):
        return reverse("items:update:meleeweapon", args=[str(self.id)])

    @classmethod
    def get_creation_url(cls):
        return reverse("items:create:meleeweapon")
