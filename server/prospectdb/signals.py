from django.contrib.postgres.search import SearchVector
from django.db import connection
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ConversationMessage, Prospect


@receiver(post_save, sender=ConversationMessage, dispatch_uid='on_message_save')
def on_message_save(sender, instance, *args, **kwargs):
    sender.objects.filter(pk=instance.id).update(search_vector=(
        SearchVector('text')
    ))


@receiver(post_save, sender=Prospect, dispatch_uid='on_prospect_save')
def on_prospect_save(sender, instance, *args, **kwargs):
    sender.objects.filter(pk=instance.id).update(search_vector=(
        SearchVector('city', weight='A') +
        SearchVector('gender', weight='A') +
        SearchVector('ethnicity', weight='B')

    ))

    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO catalog_prospectsearchword (word)
            SELECT word FROM ts_stat('
              SELECT to_tsvector(''simple'', city) ||
                     to_tsvector(''simple'', coalesce(ethnicity, ''''))
                FROM prospect-search_prospect
               WHERE id = '%s'
            ')
            ON CONFLICT (word) DO NOTHING;
        """, [str(instance.id),])
