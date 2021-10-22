from django.contrib.postgres.search import SearchVector
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ConversationMessage


@receiver(post_save, sender=ConversationMessage, dispatch_uid='on_message_save')
def on_message_save(sender, instance, *args, **kwargs):
    sender.objects.filter(pk=instance.id).update(search_vector=(
        SearchVector('text')
    ))