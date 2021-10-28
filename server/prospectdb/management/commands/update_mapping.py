from django.core.management.base import BaseCommand, CommandError

from elasticsearch_dsl import connections


class Command(BaseCommand):
    help = 'Updates a mapping on an Elasticsearch index.'

    def handle(self, *args, **kwargs):
        index = 'prospects'
        self.stdout.write(f'Updating mapping on "{index}" index...')
        connection = connections.get_connection()
        if connection.indices.exists(index=index):
            connection.indices.put_mapping(index=index, body={
                'properties': {
                    'city': {
                        'type': 'text',
                        'analyzer': 'english',
                    },
                    'country': {
                        'type': 'text',
                        'analyzer': 'english',
                    },
                    'gender': {
                        'type': 'text',
                        'analyzer': 'english',
                    },
                    'last_name': {
                        'type': 'keyword',
                    },
                    'occupation': {
                        'type': 'text',
                        'analyzer': 'english',
                    },
                    'ethnicity': {
                        'type': 'text',
                        'analyzer': 'english',
                    }
                }
            })
            self.stdout.write(f'Updated mapping on "{index}" successfully')
        else:
            raise CommandError(f'Index "{index}" does not exist')