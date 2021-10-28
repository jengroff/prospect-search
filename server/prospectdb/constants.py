ES_INDEX = 'prospects'

ES_MAPPING = {
    'properties': {
        'email': {
            'type': 'keyword',
        },
        'first_name': {
            'type': 'keyword',
        },
        'last_name': {
            'type': 'keyword',
        },
        'phone': {
            'type': 'keyword',
        },
        'gender': {
            'type': 'text',
            'analyzer': 'english',
        },
        'story': {
            'type': 'text',
            'analyzer': 'english',
        },
        'occupation': {
            'type': 'text',
            'analyzer': 'english',
        },
        'country': {
            'type': 'text',
            'analyzer': 'english',
        },
        'region': {
            'type': 'keyword',
        },
        'city': {
            'type': 'text',
            'analyzer': 'english',
        },
        'ethnicity': {
            'type': 'text',
            'analyzer': 'english',
        },
    }
}
