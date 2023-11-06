from django.core.management.base import BaseCommand

from elasticsearch_dsl import connections


class Command(BaseCommand):
    help = 'Creates an Elasticsearch index.'

    def handle(self, *args, **kwargs):
        index = 'prospects'
        self.stdout.write(f'Creating index "{index}"...')
        connection = connections.get_connection()
        if connection.indices.exists(index=index):
            self.stdout.write(f'Index "{index}" already exists')
        else:
            connection.indices.create(index=index, body={
                'settings': {
                    'number_of_shards': 1,
                    'number_of_replicas': 0,
                }
            })
            self.stdout.write(f'Index "{index}" created successfully')