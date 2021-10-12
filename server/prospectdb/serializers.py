from rest_framework import serializers

from .models import Prospect


class ProspectSerializer(serializers.ModelSerializer):
    """
    This code tells the server how to serialize a Prospect entity
    from a database entry to a JSON string
    """
    class Meta:
        model = Prospect
        fields = ('id', 'email', 'first_name', 'last_name', 'phone', 'birthday', 'gender',
                  'story', 'occupation', 'country', 'region', 'city', 'ethnicity',
                  'registered_at', 'created_at')