from rest_framework import serializers

from .models import Prospect, Team, Study, ConversationMessage


class ProspectSerializer(serializers.ModelSerializer):
    """
    This code tells the server how to serialize a Prospect entity
    from a database entry to a JSON string
    """
    class Meta:
        model = Prospect
        fields = ('id', 'email', 'first_name', 'last_name', 'phone', 'gender',
                  'story', 'occupation', 'country', 'region', 'city', 'ethnicity')


class TeamSerializer(serializers.ModelSerializer):
    """
    This code tells the server how to serialize a Team entity
    from a database entry to a JSON string.
    """
    class Meta:
        model = Team
        fields = ('id', 'name')


class StudySerializer(serializers.ModelSerializer):
    """
    This code tells the server how to serialize a Study entity
    from a database entry to a JSON string.
    """
    class Meta:
        model = Study
        fields = ('id', 'name', 'objective', 'team_id')


class ConversationMessageSerializer(serializers.ModelSerializer):
    """
    This code tells the server how to serialize a ConversationMessage
    entity from a database entry to a JSON string.
    """
    class Meta:
        model = ConversationMessage
        fields = ('id', 'text', 'conversation_stream_id')
