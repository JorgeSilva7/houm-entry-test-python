from houmer.serializers import HoumerSerializer, PropertySerializer
from houmer.models import Visit
from rest_framework import serializers


class VisitSerializer(serializers.ModelSerializer):

    houmer = HoumerSerializer(read_only=True)
    property = PropertySerializer(read_only=True)
    visit_duration = serializers.SerializerMethodField()
    move_speed = serializers.SerializerMethodField()

    def get_visit_duration(self, obj):
        return obj.visit_duration if hasattr(obj, 'visit_duration') else None

    def get_move_speed(self, obj):
        return obj.move_speed if hasattr(obj, 'move_speed') else None

    class Meta:
        """."""

        model = Visit
        fields = [
            'id',
            'houmer',
            'property',
            'start_date',
            'end_date',
            'visit_duration',
            'move_speed'
        ]
