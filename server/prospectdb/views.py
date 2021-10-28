from django.shortcuts import render

from rest_framework.generics import ListAPIView

from elasticsearch_dsl import Search
from elasticsearch_dsl.query import Match, Term
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Prospect, Team, Study, ConversationMessage, ProspectSearchWord
from .serializers import ProspectSerializer, TeamSerializer, StudySerializer, ConversationMessageSerializer, ProspectSearchWordSerializer
from .filters import ProspectFilterSet, TeamFilterSet, StudyFilterSet, ConversationMessageFilterSet, ProspectSearchWordFilterSet
from . import constants


class ProspectView(ListAPIView):
    """
    filterset_class handles query string parameter extraction and SQL query building;
    serializer_class handles response payload building.
    """
    queryset = Prospect.objects.all()
    serializer_class = ProspectSerializer
    filterset_class = ProspectFilterSet

    def filter_queryset(self, request):
        return super().filter_queryset(request)[:100]


class ProspectSearchWordsView(ListAPIView):
    queryset = ProspectSearchWord.objects.all()
    serializer_class = ProspectSearchWordSerializer
    filterset_class = ProspectSearchWordFilterSet


class ESProspectsView(APIView):
    def get(self, request, *args, **kwargs):
        query = self.request.query_params.get('query')
        last_name = self.request.query_params.get('last_name')
        occupation = self.request.query_params.get('occupation')
        # gender = self.request.query_params.get('gender')
        # city = self.request.query_params.get('city')
        # ethnicity = self.request.query_params.get('ethnicity')

        # Build Elasticsearch query.
        search = Search(index=constants.ES_INDEX)
        q = {'should': [], 'filter': []}

        # Build should clause.
        if query:
            q['should'] = [
                Match(gender={'query': query, 'boost': 3.0}),
                Match(city={'query': query, 'boost': 3.0}),
                Match(ethnicity={'query': query, 'boost': 2.0}),
            ]
            q['minimum_should_match'] = 3

            # Build highlighting.
            search = search.highlight_options(
                number_of_fragments=0,
                pre_tags=['<mark>'],
                post_tags=['</mark>']
            )
            search = search.highlight('gender', 'city', 'ethnicity')

        # Build filter clause.
        if last_name:
            q['filter'].append(Term(last_name=last_name))
        if occupation:
            q['filter'].append(Term(occupation=occupation))

        response = search.query('bool', **q).params(size=100).execute()

        if response.hits.total.value > 0:
            return Response(data=[{
                'id': hit.meta.id,
                'email': hit.email,
                'first_name': hit.first_name,
                'last_name': hit.last_name,
                'phone': hit.phone,
                'story': hit.story,
                'country': hit.country,
                'city': hit.city,
                'region': hit.region,
                'gender': hit.gender,
                'ethnicity': hit.ethnicity,
                'occupation': (
                    hit.meta.highlight.variety[0]
                    if 'highlight' in hit.meta and 'occupation' in hit.meta.highlight
                    else hit.occupation
                ),
            } for hit in response])
        else:
            return Response(data=[])


class ESProspectSearchWordsView(APIView):
    def get(self, request, *args, **kwargs):
        query = self.request.query_params.get('query')

        # Build Elasticsearch query.
        search = Search().suggest('result', query, term={
            'field': 'all_text'
        })

        response = search.execute()

        # Extract words.
        options = response.suggest.result[0]['options']
        words = [{'word': option['text']} for option in options]

        return Response(data=words)


class TeamView(ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filterset_class = TeamFilterSet


class StudyView(ListAPIView):
    queryset = Study.objects.all()
    serializer_class = StudySerializer
    filterset_class = StudyFilterSet


class ConversationMessageView(ListAPIView):
    queryset = ConversationMessage.objects.all()
    serializer_class = ConversationMessageSerializer
    filterset_class = ConversationMessageFilterSet

    def filter_queryset(self, request):
        return super().filter_queryset(request)[:10]


class ESMessagesView(APIView):
    def get(self, request, *args, **kwargs):
        query = self.request.query_params.get('query')

        # Build Elasticsearch query.
        search = Search()
        response = search.query('bool', should=[
            Match(text=query)
        ]).params(size=100).execute()

        if response.hits.total.value > 0:
            return Response(data=[{
                'id': hit.meta.id,
                'text': hit.text,
            } for hit in response])
        else:
            return Response(data=[])