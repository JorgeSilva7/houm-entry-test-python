from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from houmer.errors.common_error import BadRequest
from houmer.serializers.visit_serializer import VisitSerializer
from houmer.services.visit.visit_service import VisitService

from houmer.utils.common_utilities import CommonUtilities


class VisitView(viewsets.ModelViewSet):
    """."""

    def create(self, request, *args, **kwargs):

        user = CommonUtilities.get_user(request)
        service_response = VisitService().create(request, user)

        to_response = VisitSerializer(service_response).data

        return Response(to_response, status.HTTP_201_CREATED)

    def end(self, request, *args, **kwargs):

        user = CommonUtilities.get_user(request)
        service_response = VisitService().end(kwargs["pk"], user)

        to_response = VisitSerializer(service_response).data

        return Response(to_response, status.HTTP_200_OK)

    def getByHoumer(self, request, *args, **kwargs):

        user = CommonUtilities.get_user(request)

        service_response = None
        type_query = request.GET.get("type", None)
        if type_query == "visit_duration":
            service_response = VisitService().list_by_logged_with_visit_duration(user, request)
        elif type_query == "move_speed":
            service_response = VisitService().list_by_logged_with_move_duration(user, request)
        else:
            raise BadRequest(
                "The query 'type' is necessary and must be 'visit_duration' or 'move_speed'")

        to_response = VisitSerializer(service_response, many=True).data

        return Response(to_response, status.HTTP_200_OK)
