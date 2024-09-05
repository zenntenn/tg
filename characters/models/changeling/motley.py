from characters.models.core.group import Group
from django.urls import reverse


class Motley(Group):
    type = "motley"

    class Meta:
        verbose_name = "Motley"
        verbose_name_plural = "Motleys"

    def get_heading(self):
        return "ctd_heading"

    def random(
        self,
        num_chars=None,
        new_characters=True,
        random_names=True,
        freebies=15,
        xp=0,
        user=None,
    ):
        from characters.models.changeling.changeling import Changeling

        super().random(
            num_chars=num_chars,
            new_characters=new_characters,
            random_names=random_names,
            freebies=freebies,
            xp=xp,
            user=user,
            member_type=Changeling,
            character_kwargs={},
        )

    @classmethod
    def get_creation_url(cls):
        return reverse("characters:changeling:create:motley")

    def get_update_url(self):
        return reverse("characters:changeling:update:motley", kwargs={"pk": self.pk})
