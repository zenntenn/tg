import re
from datetime import timedelta

from core.utils import dice
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Max, OuterRef, Subquery
from django.urls import reverse
from django.utils.timezone import (  # ensure timezone-aware now if using TIME_ZONE settings
    now,
)


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

    def get_scenes(self):
        return Scene.objects.filter(chronicle=self)

    def get_active_scenes(self):
        return Scene.objects.filter(chronicle=self, finished=False)

    def get_absolute_url(self):
        return reverse("game:chronicle", kwargs={"pk": self.pk})

    def storyteller_list(self):
        return ", ".join([x.username for x in self.storytellers.all()])

    def get_scenes_url(self):
        return reverse("game:chronicle_scenes", kwargs={"pk": self.pk})

    def add_setting_element(self, name, description):
        se = SettingElement.objects.get_or_create(name=name, description=description)[0]
        self.common_knowledge_elements.add(se)

    def total_scenes(self):
        return Scene.objects.filter(chronicle=self).count()

    def add_scene(self, name, location, date_of_scene=None):
        if isinstance(location, str):
            from locations.models import LocationModel

            location = LocationModel.objects.get(name=location)
        if Scene.objects.filter(name=name, chronicle=self, location=location).exists():
            return Scene.objects.filter(
                name=name, chronicle=self, location=location
            ).first()
        s = Scene.objects.create(
            name=name,
            chronicle=self,
            location=location,
            date_of_scene=date_of_scene,
        )
        self.save()
        return s


class STRelationship(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    chronicle = models.ForeignKey(Chronicle, on_delete=models.SET_NULL, null=True)
    gameline = models.ForeignKey(Gameline, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["gameline__id"]


class Story(models.Model):
    name = models.CharField(max_length=100, default="")
    xp_given = models.BooleanField(default=False)


class Week(models.Model):
    end_date = models.DateField()
    xp_given = models.BooleanField(default=False)

    @property
    def start_date(self):
        return self.end_date - timedelta(days=7)

    def finished_scenes(self):
        # Subquery to get the most recent datetime_created for each Scene
        recent_post_subquery = (
            Post.objects.filter(scene=OuterRef("pk"))
            .values("scene")
            .annotate(latest_dt=Max("datetime_created"))
            .values("latest_dt")
        )

        # Annotate each Scene with latest_post_date (datetime)
        # and then filter by conditions:
        # 1) Scene is finished
        # 2) The date portion of latest_post_date is between start_date and end_date
        return Scene.objects.annotate(
            latest_post_date=Subquery(recent_post_subquery)
        ).filter(
            finished=True,
            latest_post_date__date__gte=self.start_date,
            latest_post_date__date__lte=self.end_date,
        )

    def weekly_characters(self):
        from characters.models.core.human import Human

        scenes = self.finished_scenes()
        q = Human.objects.none()
        for scene in scenes:
            q |= scene.characters.filter(npc=False)
        q = q.distinct()
        q = q.order_by("name")
        return q


class Scene(models.Model):
    name = models.CharField(max_length=100, default="")
    chronicle = models.ForeignKey(
        "game.Chronicle", on_delete=models.SET_NULL, null=True
    )
    date_played = models.DateField(auto_now_add=True)
    characters = models.ManyToManyField(
        "characters.CharacterModel", related_name="scenes", blank=True
    )
    location = models.ForeignKey(
        "locations.LocationModel", on_delete=models.SET_NULL, null=True
    )
    finished = models.BooleanField(default=False)
    xp_given = models.BooleanField(default=False)
    waiting_for_st = models.BooleanField(default=False)
    st_message = models.CharField(max_length=300, default="")
    date_of_scene = models.DateField(default=now, null=True, blank=True)

    class Meta:
        verbose_name = "Scene"
        verbose_name_plural = "Scenes"
        ordering = ["-date_of_scene", "-date_played"]

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
        return character

    def total_posts(self):
        return Post.objects.filter(scene=self).count()

    def add_post(self, character, display, message):
        if character not in self.characters.all():
            self.add_character(character)
        if display == "":
            display = character.name
        if message.lower().startswith("@storyteller"):
            self.waiting_for_st = True
            self.st_message = message[len("@storyteller ") :]
            self.save()
            return None
        if self.waiting_for_st and character.owner.profile.is_st():
            self.waiting_for_st = False
            self.save()
        try:
            message = message_processing(character, message)
        except ValueError:
            return
        post = Post.objects.create(
            character=character, message=message, display_name=display, scene=self
        )

        return post

    def most_recent_post(self):
        return Post.objects.filter(scene=self).order_by("-datetime_created").first()


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


class JournalEntry(models.Model):
    journal = models.ForeignKey("Journal", on_delete=models.SET_NULL, null=True)
    message = models.TextField(default="")
    st_message = models.TextField(default="")
    date = models.DateTimeField()
    datetime_created = models.DateTimeField(default=now)

    class Meta:
        ordering = ["-date"]


class Journal(models.Model):
    character = models.OneToOneField(
        "characters.CharacterModel", on_delete=models.CASCADE
    )

    def add_post(self, date, message):
        try:
            message = message_processing(self.character, message)
        except ValueError:
            return
        je = JournalEntry.objects.create(journal=self, message=message, date=date)
        return je

    def get_absolute_url(self):
        return reverse("game:journal", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.character.name}'s Journal"

    def all_entries(self):
        return JournalEntry.objects.filter(journal=self)


def message_processing(character, message):
    temporary_point_regex = re.compile(r"#WP|#Q(-?\d+)|#P(-?\d+)|#(-?\d+)(B|L|A)")
    wp_spend = False
    expenditures = []

    for match in temporary_point_regex.finditer(message):
        full_match = match.group(0)
        if full_match == "#WP":
            character.temporary_willpower -= 1
            wp_spend = True
            expenditures.append("WP")
            character.save()
        elif match.group(1):
            if hasattr(character, "quintessence"):
                character.quintessence -= int(match.group(1))
                expenditures.append(f"{int(match.group(1))}Q")
                character.save()
        elif match.group(2):
            if hasattr(character, "paradox"):
                character.paradox += int(match.group(2))
                expenditures.append(f"{int(match.group(2))}P")
                character.save()
        elif match.group(3):
            damage_type = match.group(4)
            damage_amount = int(match.group(3))
            expenditures.append(f"{damage_amount}{damage_type}")
            if damage_type == "B":
                for _ in range(damage_amount):
                    character.add_bashing()
            if damage_type == "L":
                for _ in range(damage_amount):
                    character.add_lethal()
            if damage_type == "A":
                for _ in range(damage_amount):
                    character.add_aggravated()
            character.save()

    expenditures = ", ".join(["#" + x for x in expenditures])
    if "/rolls" in message:
        text, roll = message.split("/rolls")
        text = text.strip()
        roll = roll.strip()
        if match := re.match(
            r"^(?P<num_rolls>\d+)\s+rolls\s+@\s+(?P<num_dice>\d+)(?:\s+difficulty\s+(?P<difficulty>\d+))?(?:\s+(?P<specialty>\S+))?",
            roll,
            re.IGNORECASE,
        ):
            num_rolls = int(match.group("num_rolls"))
            num_dice = int(match.group("num_dice"))
            difficulty = (
                int(match.group("difficulty")) if match.group("difficulty") else 6
            )
            specialty_str = match.group("specialty")
            specialty = specialty_str.lower() == "true" if specialty_str else False
            r = rolls(
                num_rolls,
                num_dice,
                difficulty=difficulty,
                specialty=specialty,
            )
            roll_description = (
                f"{num_rolls} rolls of {num_dice} dice at difficulty {difficulty}"
            )
            if specialty:
                roll_description += " with relevant specialty"
            m = ""
            if text:
                m += text + ": "
            if expenditures:
                m += expenditures + ": "
            m += roll_description + ": " + r
            message = m
        else:
            raise ValueError("Command does not match the expected format.")
    elif "/roll" in message:
        text, roll = message.split("/roll")
        text = text.strip()
        roll = roll.strip()
        # Full Pattern
        if match := re.match(
            r"^(?P<num_dice>\d+)(?:\s+difficulty\s+(?P<difficulty>\d+))?(?:\s+(?P<specialty>\S+))?",
            roll,
            re.IGNORECASE,
        ):
            num_dice = int(match.group("num_dice"))
            difficulty = (
                int(match.group("difficulty")) if match.group("difficulty") else 6
            )
            specialty_str = match.group("specialty")
            specialty = specialty_str.lower() == "true" if specialty_str else False
            r = roll_once(
                num_dice,
                difficulty=difficulty,
                specialty=specialty,
                willpower=wp_spend,
            )
            roll_description = f"roll of {num_dice} dice at difficulty {difficulty}"
            if specialty:
                roll_description += " with relevant specialty"
            m = ""
            if text:
                m += text + ": "
            if expenditures:
                m += expenditures + ": "
            m += roll_description + ": " + r
            message = m
        else:
            raise ValueError("Command does not match the expected format.")
    return message


def roll_once(number_of_dice, difficulty=6, specialty=False, willpower=False):
    roll, success_count = dice(
        number_of_dice, difficulty=difficulty, specialty=specialty
    )
    if willpower:
        success_count += 1
        if success_count < 0:
            success_count = 0
    roll = ", ".join(map(str, roll))
    return f"{roll}: <b>{success_count}</b>"


def rolls(num_rolls, num_dice, difficulty, specialty):
    roll_list = []
    successes = []
    difficulties = []
    for _ in range(num_rolls):
        difficulties.append(difficulty)
        roll, success_count = dice(num_dice, difficulty=difficulty, specialty=specialty)
        roll = ", ".join(map(str, roll))
        roll_list.append(roll)
        successes.append(success_count)
        if success_count == 0:
            difficulty += 1
        if success_count < 0:
            break
    join_list = []
    for roll, suxx, diff in zip(roll_list, successes, difficulties):
        join_list.append(f"{roll}: <b>{suxx}</b>")
        if suxx == 0:
            join_list[-1] = join_list[-1] + f": difficulty increased to {diff + 1}"
    return "Rolls:<br>" + f"<br>".join(join_list)
