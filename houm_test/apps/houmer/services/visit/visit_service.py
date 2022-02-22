from datetime import datetime
from rest_framework import serializers

from houmer.errors.common_error import BadRequest, NotFound, NotAcceptable, Unauthorized
from houmer.models import Property, Houmer, Visit

from houmer.utils.db_tools import wait_and_process_transaction
from houmer.utils.common_utilities import CommonUtilities


class VisitService(object):

    @wait_and_process_transaction()
    def create(self, request, user):

        form = CreateVisitValidation(data=request.data)
        if not form.is_valid():
            raise BadRequest.setDetail(None, form.errors)

        houmer: Houmer = None
        try:
            houmer = Houmer.objects.get(user=user)
        except Exception:
            raise NotFound.setDetail(None, "Houmer")

        prop: Property = None
        try:
            prop = Property.objects.get(
                pk=request.data.get('property_id', None))
        except Exception:
            raise NotFound.setDetail(None, "Property")

        visit_in_process = Visit.objects.filter(
            houmer=houmer, end_date=None).order_by('-end_date')

        if visit_in_process.exists():
            msg_error = "Unauthorized: You has a pending visit (finish the visit '{}' first)".format(
                visit_in_process.first().property.name)
            raise NotAcceptable(msg_error)

        visit = Visit.objects.create(
            houmer=houmer, property=prop, start_date=datetime.now())

        return visit

    @wait_and_process_transaction()
    def end(self, pk, user):

        houmer: Houmer = None
        try:
            houmer = Houmer.objects.get(user=user)
        except Exception:
            raise NotFound.setDetail(None, "Houmer")

        visit: Visit = None
        try:
            visit = Visit.objects.get(pk=pk)
        except Exception:
            raise NotFound.setDetail(None, "Visit")

        print(visit.end_date)
        if visit.end_date != None:
            raise NotAcceptable("Visit already has a end date")

        if visit.houmer != houmer:
            raise Unauthorized(
                "Unauthorized: The visit creator is not the current houmer")

        visit.end_date = datetime.now()
        visit.save()

        return visit

    def list_by_logged_with_visit_duration(self, user, request):

        visits = self.get_visits_by_day(user, request)

        # TODO obtener duracion de cada una

        return visits

    def list_by_logged_with_move_duration(self, user, request):

        visits = self.get_visits_by_day(user, request)
        # TODO obtener duracion de movimiento

        return visits

    def get_visits_by_day(self, user, request):
        houmer = None
        try:
            houmer = Houmer.objects.get(user=user)
        except Exception:
            raise NotFound.setDetail(None, "Houmer")

        day = request.GET.get('day', None)
        if not day:
            raise BadRequest("day is required")

        try:
            day = datetime.strptime(day, "%Y-%m-%d")
        except Exception:
            raise BadRequest("the day does not match format YYYY-MM-DD")

        page, limit = CommonUtilities.get_page_limit(request)

        # Obtener start_date and end_date
        return Visit.objects.filter(houmer=houmer)[(page-1)*limit:page*limit]


class CreateVisitValidation(serializers.Serializer):
    property_id = serializers.IntegerField(required=True, min_value=0)
