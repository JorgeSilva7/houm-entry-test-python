from houmer.serializers import HoumerSerializer, PropertySerializer
from houmer.models import Visit
from rest_framework import serializers


class VisitSerializer(serializers.ModelSerializer):

    houmer = HoumerSerializer(read_only=True)
    property = PropertySerializer(read_only=True)

    class Meta:
        """."""

        model = Visit
        fields = [
            'id',
            'houmer',
            'property',
            'start_date',
            'end_date'
        ]
