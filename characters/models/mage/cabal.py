from django.urls import reverse

from characters.models.core.group import Group



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

        if faction is None:
            mage_faction = weighted_random_faction()
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
        return reverse("wod:characters:mage:update_cabal", kwargs={"pk": self.pk})
