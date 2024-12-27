from datetime import date, timedelta

from game.models import Week

week = timedelta(7)

base_date = date(2024, 11, 24)

for i in range(520):
    Week.objects.get_or_create(end_date=base_date + i * week)
