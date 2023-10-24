from rest_framework import viewsets
from quitutes.serializers import DocesSerializer
from quitutes.models import Doce
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class DoceViewSet(viewsets.ModelViewSet):
    '''Exibindo todos os doces'''
    queryset = Doce.objects.all()
    serializer_class = DocesSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['nome']
    ordering_fields = ['nome','valor','peso']
    filterset_fields = ['categoria']
    ordering = ['nome']
    http_method_names = ['get']