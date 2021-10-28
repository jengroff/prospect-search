from rest_framework import serializers

from .models import Prospect, Team, Study, ConversationMessage, ProspectSearchWord


class ProspectSerializer(serializers.ModelSerializer):
    """
    This code tells the server how to serialize a Prospect entity
    from a database entry to a JSON string
    """
    def get_city(self, obj):
        if hasattr(obj, 'city_headline'):
            return getattr(obj, 'city_headline')
        return getattr(obj, 'city')

    def get_gender(self, obj):
        if hasattr(obj, 'gender_headline'):
            return getattr(obj, 'gender_headline')
        return getattr(obj, 'gender')

    def get_country(self, obj):
        if hasattr(obj, 'country_headline'):
            return getattr(obj, 'country_headline')
        return getattr(obj, 'country')

    def get_ethnicity(self, obj):
        if hasattr(obj, 'ethnicity_headline'):
            return getattr(obj, 'ethnicity_headline')
        return getattr(obj, 'ethnicity')

    class Meta:
        model = Prospect
        fields = ('id', 'email', 'first_name', 'last_name', 'phone', 'gender',
                  'story', 'occupation', 'country', 'region', 'city', 'ethnicity')


class ProspectSearchWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProspectSearchWord
        fields = ('word',)


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
    text = serializers.SerializerMethodField()

    def get_text(self, obj):
        if hasattr(obj, 'text_headline'):
            return getattr(obj, 'text_headline')
        return getattr(obj, 'text')

    class Meta:
        model = ConversationMessage
        fields = ('id', 'text', 'conversation_stream_id')
