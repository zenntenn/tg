import re

from core.utils import dice
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class ObjectType(models.Model):
    name = models.CharField(max_length=100, default="")
    type = models.CharField(
        default="",
        max_length=100,
        choices=[
            ("char", "Character"),
            ("loc", "Location"),
            ("obj", "Item"),
        ],
    )
    gameline = models.CharField(
        default="",
        max_length=100,
        choices=[
            ("wod", "World of Darkness"),
            ("vtm", "Vampire: the Masquerade"),
            ("wta", "Werewolf: the Apocalypse"),
            ("mta", "Mage: the Ascension"),
            ("wto", "Wraith: the Oblivion"),
            ("ctd", "Changeling: the Dreaming"),
        ],
    )

    class Meta:
        verbose_name = "Object Type"
        verbose_name_plural = "Object Types"
        ordering = ["type", "gameline", "name"]

    def __str__(self):
        return (
            self.get_gameline_display()
            + "/"
            + self.get_type_display()
            + "/"
            + self.name
        )


class SettingElement(models.Model):
    name = models.CharField(max_length=100, default="")
    description = models.TextField(default="")

    def __str__(self):
        return self.name


class Gameline(models.Model):
    name = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name


class Chronicle(models.Model):
    name = models.CharField(max_length=100, default="")
    storytellers = models.ManyToManyField(User, blank=True, through="STRelationship")
    theme = models.CharField(max_length=200, default="")
    mood = models.CharField(max_length=200, default="")
    common_knowledge_elements = models.ManyToManyField(SettingElement, blank=True)
    year = models.IntegerField(default=2022)

    headings = models.CharField(
        default="",
        max_length=100,
        choices=[
            ("vtm_heading", "Vampire: the Masquerade"),
            ("wta_heading", "Werewolf: the Apocalypse"),
            ("mta_heading", "Mage: the Ascension"),
            ("ctd_heading", "Changeling: the Dreaming"),
            ("wto_heading", "Wraith: the Oblivion"),
            ("wod_heading", "World of Darkness"),
        ],
    )

    allowed_objects = models.ManyToManyField(ObjectType, blank=True)

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

    def get_scenes_url(self):
        return reverse("game:chronicle_scenes", kwargs={"pk": self.pk})

    def add_setting_element(self, name, description):
        se = SettingElement.objects.get_or_create(name=name, description=description)[0]
        self.common_knowledge_elements.add(se)


class STRelationship(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    chronicle = models.ForeignKey(Chronicle, on_delete=models.SET_NULL, null=True)
    gameline = models.ForeignKey(Gameline, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["gameline__id"]


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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if Scene.objects.filter(story=self).exists():
            self.start_date = min(
                x.date_of_scene for x in Scene.objects.filter(story=self)
            )
            self.end_date = max(
                x.date_of_scene for x in Scene.objects.filter(story=self)
            )
            super().save()

    def total_scenes(self):
        return Scene.objects.filter(story=self).count()

    def add_scene(self, name, location, date_played=None, date_of_scene=None):
        if isinstance(location, str):
            from locations.models import LocationModel

            location = LocationModel.objects.get(name=location)
        if Scene.objects.filter(name=name, story=self, location=location).exists():
            return Scene.objects.filter(
                name=name, story=self, location=location
            ).first()
        s = Scene.objects.create(
            name=name,
            story=self,
            location=location,
            date_played=date_played,
            date_of_scene=date_of_scene,
        )
        self.key_locations.add(location)
        self.save()
        return s


class Scene(models.Model):
    name = models.CharField(max_length=100, default="")
    story = models.ForeignKey("game.Story", on_delete=models.SET_NULL, null=True)
    date_played = models.DateField(null=True, blank=True)
    characters = models.ManyToManyField(
        "characters.CharacterModel", related_name="scenes", blank=True
    )
    location = models.ForeignKey(
        "locations.LocationModel", on_delete=models.SET_NULL, null=True
    )
    finished = models.BooleanField(default=False)
    xp_given = models.BooleanField(default=False)
    date_of_scene = models.DateField(default=now, null=True, blank=True)

    class Meta:
        verbose_name = "Scene"
        verbose_name_plural = "Scenes"

    def __str__(self):
        if self.name not in ["", "''"]:
            return self.name
        return str(self.location) + " " + str(self.date)

    def get_absolute_url(self):
        return reverse("game:scene", kwargs={"pk": self.pk})

    def close(self):
        self.finished = True
        self.save()

    def total_characters(self):
        return self.characters.count()

    def add_character(self, character):
        if isinstance(character, str):
            from characters.models.core import CharacterModel

            character = CharacterModel.objects.get(name=character)
        self.characters.add(character)
        if character.npc:
            self.story.key_npcs.add(character)
        else:
            self.story.pcs.add(character)
        return character

    def total_posts(self):
        return Post.objects.filter(scene=self).count()

    def add_post(self, character, display, message):
        if character not in self.characters.all():
            self.add_character(character)
        if display == "":
            display = character.name
        post = Post.objects.create(
            character=character, message=message, display_name=display, scene=self
        )
        if message.startswith("/rolls"):
            pattern = r"^/rolls\s+(?P<num_rolls>\d+)\s+rolls\s+@\s+(?P<num_dice>\d+)\s+difficulty\s+(?P<difficulty>\d+)\s+(?P<specialty>\S+)$"
            message = message.strip()
            # Perform the regex matching (case-insensitive for specialty if needed)
            match = re.match(pattern, message, re.IGNORECASE)

            if not match:
                raise ValueError("Command does not match the expected format.")

            try:
                num_rolls = int(match.group("num_rolls"))
                num_dice = int(match.group("num_dice"))
                difficulty = int(match.group("difficulty"))
                specialty_input = match.group("specialty")
            except (ValueError, AttributeError) as e:
                raise ValueError("Error parsing numerical values.") from e

            specialty_lower = specialty_input.lower()
            specialty = True if specialty_lower == "true" else False
            post.rolls(num_rolls, num_dice, difficulty, specialty)
        elif message.startswith("/roll"):
            pattern = r"^/roll\s+(\d+)\s+difficulty\s+(\d+)\s+(\S+)$"

            match = re.match(pattern, message, re.IGNORECASE)

            if not match:
                raise ValueError("Command does not match the expected format.")

            num_dice = int(match.group(1))
            difficulty = int(match.group(2))
            specialty_str = match.group(3).lower()
            specialty = True if specialty_str == "true" else False
            post.roll(num_dice, difficulty=difficulty, specialty=specialty)
        return post


class Post(models.Model):
    character = models.ForeignKey(
        "characters.CharacterModel", on_delete=models.SET_NULL, null=True
    )
    display_name = models.CharField(max_length=100)
    scene = models.ForeignKey("game.Scene", on_delete=models.SET_NULL, null=True)
    message = models.TextField(default="")
    datetime_created = models.DateTimeField(default=now)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        if self.display_name:
            return self.display_name + ": " + self.message
        return self.character.name + ": " + self.message

    def roll(self, number_of_dice, difficulty=6, specialty=False):
        roll, success_count = dice(
            number_of_dice, difficulty=difficulty, specialty=specialty
        )
        roll = ", ".join(map(str, roll))
        self.message = f"{roll}: <b>{success_count}</b>"
        self.save()

    def rolls(self, num_rolls, num_dice, difficulty, specialty):
        roll_list = []
        successes = []
        difficulties = []
        for _ in range(num_rolls):
            difficulties.append(difficulty)
            roll, success_count = dice(
                num_dice, difficulty=difficulty, specialty=specialty
            )
            roll = ", ".join(map(str, roll))
            roll_list.append(roll)
            successes.append(success_count)
            if success_count == 0:
                difficulty += 1
            if success_count < 0:
                break
        message = "Rolls:<br>"
        join_list = []
        for roll, suxx, diff in zip(roll_list, successes, difficulties):
            join_list.append(f"{roll}: <b>{suxx}</b>")
            if suxx == 0:
                join_list[-1] = join_list[-1] + f": difficulty increased to {diff + 1}"
        self.message = message + "<br>".join(join_list)
        self.save()
