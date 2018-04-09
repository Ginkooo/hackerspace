import logging

from rest_framework import serializers
from django.contrib.auth.models import User

from whoisin.models import Host

logger = logging.getLogger(__name__)


class HostSerializer(serializers.ModelSerializer):
    """```Serializer``` for ```Host```"""

    id = serializers.IntegerField()

    class Meta:
        model = Host
        fields = 'id ip mac online hostname visible alias'.split()
        read_only_fields = 'ip online mac hostname'.split()

    def create(self, validated_data):
        """just update existing host alias and visible on create

        :param validated_data: data passed from template
        """
        instance = Host.objects.get(id=validated_data["id"])

        instance.alias = validated_data.get('alias', instance.alias)
        instance.visible = validated_data.get('visible', instance.visible)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        """redirect validated_data to create, as it is already implementer.

        :param instance: object instance
        :param validated_data: data passed from template
        """
        self.create(validated_data)


class UserSerializer(serializers.ModelSerializer):
    """```Serializer``` for ```User```. Adds a few more properties to user"""

    class Meta:
        model = User
        fields = 'username online'.split()
