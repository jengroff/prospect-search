from django.core.management.base import BaseCommand

from elasticsearch_dsl import connections
from elasticsearch.helpers import bulk

from prospectdb.constants import ES_INDEX, ES_MAPPING

from prospectdb.models import Prospect


class Command(BaseCommand):
    help = 'Updates the Elasticsearch index.'

    def _document_generator(self):
        for prospect in Prospect.objects.iterator():
            yield {
                '_index': 'prospects',
                '_id': prospect.id,
                'email': prospect.email,
                'first_name': prospect.first_name,
                'last_name': prospect.last_name,
                'phone': prospect.phone,
                'gender': prospect.gender,
                'story': prospect.story,
                'occupation': prospect.occupation,
                'country': prospect.country,
                'region': prospect.region,
                'city': prospect.city,
                'ethnicity': prospect.ethnicity,
            }

    def handle(self, *args, **kwargs):
        connection = connections.get_connection()

        self.stdout.write(f'Checking if index "{ES_INDEX}" exists...')
        if connection.indices.exists(index=ES_INDEX):
            self.stdout.write(f'Index "{ES_INDEX}" already exists')
            self.stdout.write(f'Updating mapping on "{ES_INDEX}" index...')
            connection.indices.put_mapping(index=ES_INDEX, body=ES_MAPPING)
            self.stdout.write(f'Updated mapping on "{ES_INDEX}" successfully')
        else:
            self.stdout.write(f'Index "{ES_INDEX}" does not exist')
            self.stdout.write(f'Creating index "{ES_INDEX}"...')
            connection.indices.create(index=ES_INDEX, body={
                'settings': {
                    'number_of_shards': 1,
                    'number_of_replicas': 0,
                },
                'mappings': ES_MAPPING,
            })
            self.stdout.write(f'Index "{ES_INDEX}" created successfully')

        self.stdout.write(f'Bulk updating documents on "{ES_INDEX}" index...')
        succeeded, _ = bulk(connection, actions=self._document_generator(), stats_only=True)
        self.stdout.write(f'Updated {succeeded} documents on "{ES_INDEX}" successfully')