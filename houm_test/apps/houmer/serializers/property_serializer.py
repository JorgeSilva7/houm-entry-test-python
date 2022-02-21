from rest_framework import serializers
from houmer.serializers.houmer_serializer import HoumerSerializer
from houmer.models import Property


class PropertySerializer(serializers.ModelSerializer):

    houmer = HoumerSerializer(read_only=True)

    class Meta:
        """."""

        model = Property
        fields = [
            'id',
            'name',
            'houmer',
            'coordinates'
        ]
