from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.exceptions import NotAuthenticated
from django.contrib.auth.models import AnonymousUser

from intercom.intercom_handler import IntercomHandler


class IntercomViewSet(viewsets.ViewSet):
    """Api view to interact with intercom"""

    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, format=None):
        """call door opening procedure on authenticated request
        """
        if type(request.user) == AnonymousUser:
            raise NotAuthenticated()
        IntercomHandler.open()
        return Response({'status': 'opening'})
