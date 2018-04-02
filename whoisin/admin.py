from django.contrib import admin

from whoisin.models import Host


class HostAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj=None):
        return self.readonly_fields + tuple('ip mac hostname'.split())


admin.site.register(Host, HostAdmin)
