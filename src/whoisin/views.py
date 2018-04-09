from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny, IsAdminUser
from django.contrib.auth.models import User

from whoisin.models import Host
from whoisin.serializers import HostSerializer, UserSerializer
from whoisin.filters import IsOnlineFilter


class PermissionsMixin:
    """Provides permission mixin, for restricting modification capabilities for normal and anonymous users,
    this must be first class accessed through MRO resolution chain (```super()```)"""

    def get_permissions(self):
        """Allow only admin to modify stuff"""
        if self.action in ('list', 'retrieve'):
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class HostViewSet(PermissionsMixin, viewsets.ModelViewSet):
    """Provide views for Host model"""
    queryset = Host.objects.all()
    serializer_class = HostSerializer
    filter_backends = (DjangoFilterBackend, IsOnlineFilter)
    filter_fields = 'alias mac visible hostname ip'.split()


class UserViewSet(PermissionsMixin, viewsets.ModelViewSet):
    """Provide views form User model"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend, IsOnlineFilter)

    get_permissions = HostViewSet.get_permissions
