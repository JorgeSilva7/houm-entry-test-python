from rest_framework import serializers

from houmer.errors.common_error import BadRequest, NotFound
from houmer.models import Property, Houmer


class PropertyService(object):

    def create(self, request, user):

        form = CreatePropertyValidation(data=request.data)
        if not form.is_valid():
            raise BadRequest.setDetail(None, form.errors)

        houmer = None
        try:
            houmer = Houmer.objects.get(user=user)
        except Exception:
            raise NotFound.setDetail(None, "Houmer")

        propertySaved = Property.objects.create(
            name=request.data.get('name', None),
            coordinates=request.data.get('coordinates', None),
            houmer=houmer)

        return propertySaved

    def list_by_logged(self, user):

        houmer = None
        try:
            houmer = Houmer.objects.get(user=user)
        except Exception:
            raise NotFound.setDetail(None, "Houmer")

        properties = Property.objects.filter(houmer=houmer)

        return properties


class CoordinatesSerializer(serializers.Serializer):
    latitude = serializers.FloatField(required=True)
    longitude = serializers.FloatField(required=True)


class CreatePropertyValidation(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=100, min_length=2)
    coordinates = CoordinatesSerializer()
