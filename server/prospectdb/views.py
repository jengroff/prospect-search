from django.shortcuts import render

from rest_framework.generics import ListAPIView

from elasticsearch_dsl import Search
from elasticsearch_dsl.query import Match, Term
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Prospect, Team, Study, ConversationMessage
from .serializers import ProspectSerializer, TeamSerializer, StudySerializer, ConversationMessageSerializer
from .filters import ProspectFilterSet, TeamFilterSet, StudyFilterSet, ConversationMessageFilterSet


class ProspectView(ListAPIView):
    """
    filterset_class handles query string parameter extraction and SQL query building;
    serializer_class handles response payload building.
    """
    queryset = Prospect.objects.all()
    serializer_class = ProspectSerializer
    filterset_class = ProspectFilterSet


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