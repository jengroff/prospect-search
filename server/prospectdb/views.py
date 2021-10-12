from django.shortcuts import render

from rest_framework.generics import ListAPIView

from .models import Prospect
from .serializers import ProspectSerializer
from .filters import ProspectFilterSet


class ProspectView(ListAPIView):
    """
    filterset_class handles query string parameter extraction and SQL query building;
    serializer_class handles response payload building.
    """
    queryset = Prospect.objects.all()
    serializer_class = ProspectSerializer
    filterset_class = ProspectFilterSet
