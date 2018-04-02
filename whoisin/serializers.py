from rest_framework import serializers

from whoisin.models import Host


class HostSerializer(serializers.ModelSerializer):
    """```Serializer``` for ```Host```"""

    id = serializers.IntegerField()

    class Meta:
        model = Host
        fields = 'id ip mac online hostname visible alias'.split()
        read_only_fields = 'ip online mac hostname'.split()

    def create(self, validated_data):
        instance = Host.objects.get(id=validated_data["id"])

        instance.alias = validated_data.get('alias', instance.alias)
        instance.visible = validated_data.get('visible', instance.visible)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        self.create(validated_data)
