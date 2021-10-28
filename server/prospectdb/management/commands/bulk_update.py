from django.core.management.base import BaseCommand

from elasticsearch_dsl import connections
from elasticsearch.helpers import bulk

from prospectdb.models import ConversationMessage


class Command(BaseCommand):
    help = 'Updates the Elasticsearch index.'

    def _document_generator(self):
        for message in ConversationMessage.objects.iterator():
            yield {
                '_index': 'messages',
                '_id': message.id,
                'text': message.text,
            }

    def handle(self, *args, **kwargs):
        index = 'messages'
        self.stdout.write(f'Bulk updating documents on "{index}" index...')
        connection = connections.get_connection()
        succeeded, _ = bulk(connection, actions=self._document_generator(), stats_only=True)
        self.stdout.write(f'Updated {succeeded} documents on "{index}" successfully')