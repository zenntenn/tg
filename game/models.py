from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Chronicle(models.Model):
    name = models.CharField(max_length=100, default="")
    storytellers = models.ManyToManyField(User, blank=True)
    theme = models.CharField(max_length=200, default="")
    mood = models.CharField(max_length=200, default="")
    common_knowledge_elements = models.TextField(default="")
    year = models.IntegerField(default=2022)

    headings = models.CharField(
        default="",
        max_length=100,
        choices=[
            ("vtm_heading", "Vampire: the Masquerade"),
            ("wta_heading", "Werewolf: the Apocalypse"),
            ("mtas_heading", "Mage: the Ascension"),
            ("ctd_heading", "Changeling: the Dreaming"),
            ("wto_heading", "Wraith: the Oblivion"),
            ("wod_heading", "World of Darkness"),
        ],
    )

    class Meta:
        verbose_name = "Chronicle"
        verbose_name_plural = "Chronicles"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("game:chronicle", kwargs={"pk": self.pk})

    def storyteller_list(self):
        return ", ".join([x.username for x in self.storytellers.all()])

    def total_stories(self):
        return Story.objects.filter(chronicle=self).count()

    def add_story(self, name):
        if Story.objects.filter(name=name, chronicle=self).exists():
            return Story.objects.filter(name=name, chronicle=self).first()
        return Story.objects.create(name=name, chronicle=self)


class Story(models.Model):
    name = models.CharField(max_length=100, default="")
    pcs = models.ManyToManyField(
        "characters.CharacterModel", blank=True, related_name="pc_in"
    )
    key_npcs = models.ManyToManyField(
        "characters.CharacterModel", blank=True, related_name="npc_in"
    )
    plot_summary = models.TextField(default="")
    key_locations = models.ManyToManyField("locations.LocationModel", blank=True)
    chronicle = models.ForeignKey(
        "game.Chronicle", null=True, blank=True, on_delete=models.SET_NULL
    )
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Story"
        verbose_name_plural = "Stories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("game:story", kwargs={"pk": self.pk})

    def total_locations(self):
        return self.key_locations.count()

    def total_pcs(self):
        return self.pcs.count()

    def total_npcs(self):
        return self.key_npcs.count()
