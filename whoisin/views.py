from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions

from whoisin.models import Host
from whoisin.serializers import HostSerializer
from whoisin.filters import IsOnlineFilter


class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer
    filter_backends = (DjangoFilterBackend, IsOnlineFilter)
    filter_fields = 'alias mac visible hostname ip'.split()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
