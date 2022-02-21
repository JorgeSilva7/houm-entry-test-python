from houmer.models import Houmer
from rest_framework import serializers


class HoumerSerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username or "NO_USERNAME"

    class Meta:
        """."""

        model = Houmer
        fields = ('name', 'username', 'id')
