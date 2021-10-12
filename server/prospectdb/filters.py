from django.db.models import Q

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
            Q(email__contains=value) |
            Q(last_name__contains=value) |
            Q(phone__contains=value)
        )
        return queryset.filter(search_query)

    class Meta:
        model = Prospect
        fields = ('query', 'city', 'country')


class TeamFilterSet(FilterSet):
    query = CharFilter(method='filter_query')

    def filter_query(self, queryset, name, value):
        search_query = Q(
            Q(id__contains=value) |
            Q(name__contains=value)
        )
        return queryset.filter(search_query)


class StudyFilterSet(FilterSet):
    query = CharFilter(method='filter_query')

    def filter_query(self, queryset, name, value):
        search_query = Q(
            Q(id__contains=value) |
            Q(name__contains=value) |
            Q(team_id__contains=value)
        )
        return queryset.filter(search_query)

    class Meta:
        model = Study
        fields = ('query', 'start_date')


class ConversationMessageFilterSet(FilterSet):
    query = CharFilter(method='filter_query')

    def filter_query(self, queryset, name, value):
        search_query = Q(
            Q(text__contains=value)
        )
        return queryset.filter(search_query)
