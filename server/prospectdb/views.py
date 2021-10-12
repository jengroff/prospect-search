from django.shortcuts import render

from rest_framework.generics import ListAPIView

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