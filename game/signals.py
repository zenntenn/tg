# your_app_name/signals.py
from characters.models.core.character import CharacterModel
from django.db.models.signals import post_save
from django.dispatch import receiver
from game.models import Journal


@receiver(post_save)
def create_journal_for_character(sender, instance, created, **kwargs):
    # 'created' is True if this is a newly created object, not just an update
    if created and isinstance(instance, CharacterModel):
        Journal.objects.get_or_create(character=instance)
