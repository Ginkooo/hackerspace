from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from whoisin.views import HostViewSet
from whoisin.nmapthread import NmapThread
from intercom.views import IntercomViewSet
from utils import LockedContainer

router = routers.DefaultRouter()
router.register('hosts', HostViewSet)
router.register('intercom', IntercomViewSet, base_name='intercom')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


# start nmapthread here, because urls.py get executed only once
container = LockedContainer()
nmap_thread = NmapThread(container)
nmap_thread.__class__.container = container
nmap_thread.setDaemon(True)
nmap_thread.start()
