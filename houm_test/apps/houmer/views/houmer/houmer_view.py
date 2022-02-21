# """

# """


from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from houmer.services.houmer.houmer_service import HoumerService


class HoumerView(viewsets.ModelViewSet):
    """."""

    def __init__(self):
        """."""
        self.permission_classes = ()

    def create(self, request, *args, **kwargs):
        service_response = HoumerService().create(request)

        return Response({"success": service_response}, status.HTTP_201_CREATED)
