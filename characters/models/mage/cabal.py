from characters.models.core.group import Group
from characters.models.mage.faction import MageFaction
from characters.models.mage.mage import Mage
from core.utils import weighted_choice
from django.urls import reverse


class Cabal(Group):
    type = "cabal"

    class Meta:
        verbose_name = "Cabal"
        verbose_name_plural = "Cabals"

    def get_heading(self):
        return "mtas_heading"

    def random(
        self,
        num_chars=None,
        new_characters=True,
        random_names=True,
        freebies=15,
        xp=0,
        user=None,
        faction=None,
        chantry=0,
    ):
        faction_probs = {}
        if faction is None:
            for faction in MageFaction.objects.all():
                if faction.parent is None:
                    faction_probs[faction] = 30
                elif faction.parent.parent is None:
                    faction_probs[faction] = 10
                elif faction.parent.parent.parent is None:
                    faction_probs[faction] = 1
                else:
                    faction_probs[faction] = 0
            mage_faction = weighted_choice(faction_probs, ceiling=100)
        else:
            mage_faction = faction
        affiliation = None
        faction = None
        subfaction = None
        if mage_faction.parent is None:
            affiliation = mage_faction
        elif mage_faction.parent.parent is None:
            faction = mage_faction
        else:
            subfaction = mage_faction
        super().random(
            num_chars=num_chars,
            new_characters=new_characters,
            random_names=random_names,
            freebies=freebies,
            xp=xp,
            user=user,
            member_type=Mage,
            character_kwargs={
                "affiliation": affiliation,
                "faction": faction,
                "subfaction": subfaction,
                "backgrounds": {"chantry": chantry},
            },
        )

    def get_update_url(self):
        return reverse("characters:mage:update:cabal", kwargs={"pk": self.pk})

    @classmethod
    def get_creation_url(cls):
        return reverse("characters:mage:create:cabal")
