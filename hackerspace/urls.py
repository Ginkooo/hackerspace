from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from whoisin.views import HostViewSet
from whoisin.nmapthread import NmapThread
from utils import LockedContainer

router = routers.DefaultRouter()
router.register('hosts', HostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

container = LockedContainer()
nmap_thread = NmapThread(container)
nmap_thread.__class__.container = container
nmap_thread.setDaemon(True)
nmap_thread.start()
