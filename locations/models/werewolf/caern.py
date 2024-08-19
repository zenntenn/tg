class Caern(Location):
    type = "caern"

    rank = models.IntegerField(default=0)

    TYPES = [
        ("enigmas", "Enigmas"),
        ("gnosis", "Gnosis"),
        ("healing", "Healing"),
        ("leadership", "Leadership"),
        ("rage", "Rage"),
        ("stamina", "Stamina"),
        ("strength", "Strength"),
        ("urban", "Urban"),
        ("visions", "Visions"),
        ("will", "Will"),
        ("wisdom", "Wisdom"),
        ("wyld", "Wyld"),
    ]

    caern_type = models.CharField(default="", choices=TYPES, max_length=15)

    class Meta:
        verbose_name = "Caern"
        verbose_name_plural = "Caerns"

    def get_update_url(self):
        return reverse("wod:locations:werewolf:update_caern", args=[str(self.id)])

    def get_heading(self):
        return "wta_heading"

    def save(self, *args, **kwargs):
        if "gauntlet" not in kwargs:
            if self.rank < 3:
                self.gauntlet = 4
            elif self.rank < 5:
                self.gauntlet = 3
            else:
                self.gauntlet = 2
        return super().save(*args, **kwargs)
