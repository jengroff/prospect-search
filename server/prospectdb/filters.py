from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
from django.db.models import CharField, F, Func, Q, TextField, Value

from django_filters.rest_framework import CharFilter, FilterSet

from .models import Prospect, Team, Study, ConversationMessage


class ProspectFilterSet(FilterSet):
    """
    This class transcribes query string parameters into SQL queries
    via the Django ORM. The query searches for all documents that
    contain the value in the email, last_name, or phone fields.
    The database query is filtered further by country and gender,
    if they are also present in the HTTP request.
    """
    query = CharFilter(method='filter_query')

    def filter_query(self, queryset, name, value):
        search_query = Q(
            Q(search_vector=SearchQuery(value))
        )
        return queryset.annotate(
            search_vector=SearchVector('email', 'last_name', 'phone')
        ).filter(search_query)

    class Meta:
        model = Prospect
        fields = ('query', 'city', 'country')


class TeamFilterSet(FilterSet):
    query = CharFilter(method='filter_query')

    def filter_query(self, queryset, name, value):
        search_query = Q(
            Q(search_vector=SearchQuery(value))
        )
        return queryset.annotate(
            search_vector=SearchVector('id', 'name')
        ).filter(search_query)

    class Meta:
        model = Team
        fields = ('query',)


class StudyFilterSet(FilterSet):
    query = CharFilter(method='filter_query')

    def filter_query(self, queryset, name, value):
        search_query = Q(
            Q(search_vector=SearchQuery(value))
        )
        return queryset.annotate(
            search_vector=SearchVector('id', 'name', 'team_id')
        ).filter(search_query)

    class Meta:
        model = Study
        fields = ('query',)


class ConversationMessageFilterSet(FilterSet):
    query = CharFilter(method='filter_query')

    def filter_query(self, queryset, name, value):
        search_query = Q(
            Q(search_vector=SearchQuery(value))
        )
        return queryset.annotate(
            text_headline=Func(
                F('text'),
                SearchQuery(value, output_field=TextField()),
                Value('StartSel = <mark>, StopSel = </mark>, HighlightAll=True', output_field=TextField()),
                function='ts_headline'
            ),
            search_rank=SearchRank(F('search_vector'), SearchQuery(value))
        ).filter(search_query).order_by('-search_rank', 'id')

    class Meta:
        model = ConversationMessage
        fields = ('query',)

