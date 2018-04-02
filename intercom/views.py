from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions

from intercom.intercom_handler import IntercomHandler


class IntercomViewSet(viewsets.ViewSet):
    """Api view to interact with intercom"""

    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, format=None):
        IntercomHandler.open()
        return Response({'status': 'open'})
