from django.contrib import admin
from django.contrib.auth.models import User

from whoisin.models import Host

try:
    User.objects.create_superuser('ginkooo', 'czajka@protonmail.com', 'dupa1234')
except:  # already created
    pass


class HostAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj=None):
        return self.readonly_fields + tuple('ip mac hostname'.split())


admin.site.register(Host, HostAdmin)
