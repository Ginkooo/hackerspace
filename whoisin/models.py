import logging

from django.db import models

from whoisin.nmapthread import NmapThread

logger = logging.getLogger(__name__)


class Host(models.Model):
    ip = models.GenericIPAddressField()
    mac = models.CharField(max_length=30, unique=True)
    hostname = models.CharField(max_length=50, null=True, blank=True)
    visible = models.BooleanField(default=True)
    alias = models.CharField(max_length=50, null=True, blank=True)

    @property
    def online(self):
        try:
            return self in NmapThread.container.value
        except TypeError:
            return None

    def __eq__(self, other):
        return self.mac == other.mac

    def __repr__(self):
        return (f"Host(ip={self.ip}, mac={self.mac}, hostname={self.hostname}, "
                f"visible={self.visible}, alias={self.alias}")
