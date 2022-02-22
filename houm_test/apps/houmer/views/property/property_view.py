from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from houmer.serializers.property_serializer import PropertySerializer
from houmer.services.property.property_service import PropertyService

from houmer.utils.common_utilities import CommonUtilities


class PropertyView(viewsets.ModelViewSet):
    """."""

    def create(self, request, *args, **kwargs):

        user = CommonUtilities.get_user(request)
        service_response = PropertyService().create(request, user)

        to_response = PropertySerializer(service_response).data

        return Response(to_response, status.HTTP_201_CREATED)

    def list_by_logged(self, request, *args, **kwargs):

        user = CommonUtilities.get_user(request)
        service_response = PropertyService().list_by_logged(request, user)

        to_response = PropertySerializer(service_response, many=True).data

        return Response(to_response, status.HTTP_200_OK)
