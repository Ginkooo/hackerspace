from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny, IsAdminUser

from whoisin.models import Host
from whoisin.serializers import HostSerializer
from whoisin.filters import IsOnlineFilter


class HostViewSet(viewsets.ModelViewSet):
    """Provide views for Host model"""
    queryset = Host.objects.all()
    serializer_class = HostSerializer
    filter_backends = (DjangoFilterBackend, IsOnlineFilter)
    filter_fields = 'alias mac visible hostname ip'.split()

    def get_permissions(self):
        """Allow only admin to modify stuff"""
        if self.action in ('list', 'retrieve'):
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
