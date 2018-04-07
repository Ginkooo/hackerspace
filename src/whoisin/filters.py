from rest_framework import filters


class IsOnlineFilter(filters.BaseFilterBackend):
    """Gets only online==True elements"""

    def get_online(self, queryset):
        for item in queryset:
            if item.online:
                yield item

    def filter_queryset(self, request, queryset, view):
        try:
            if request.GET['online'].lower() != 'true':
                raise Exception('Not looking for online hosts')
        except:
            return queryset
        return self.get_online(queryset)
