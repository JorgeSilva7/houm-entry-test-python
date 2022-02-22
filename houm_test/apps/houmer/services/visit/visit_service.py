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

        for visit in visits:
            diff = visit.end_date - visit.start_date
            diff = diff.total_seconds()
            minutes, seconds = CommonUtilities.millisToMinutesAndSeconds(diff)
            visit.visit_duration = "{} minutes and {} seconds".format(minutes, seconds)
        
        return visits

    def list_by_logged_with_move_duration(self, user, request):

        visits = self.get_visits_by_day(user, request)
        
        visits_return = []
        for i, visit in enumerate(visits):
            if len(visits) > i + 1:
                visit.move_speed = '{0:.2f} km/hr'.format(self.calculate_speed(visit, visits[i+1]))
                visits_return.append(visit)
        
        return visits_return

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

        # Obtener entre start_date and end_date
        return Visit.objects.filter(houmer=houmer).order_by('-end_date')[(page-1)*limit:page*limit]

    def calculate_speed(self, visitEnd: Visit, visitInit: Visit):
        """ Calculate speed between two points in specific time in earth"""

        #Calculate linear distance between two points in earth with haversine method
        distance = CommonUtilities.haversine(visitEnd.property.coordinates, visitInit.property.coordinates)

        #Calculate difference between start date last visit and end date before visit
        date_diff = (visitEnd.start_date - visitInit.end_date).total_seconds() / 60 / 60
        
        return distance/date_diff

class CreateVisitValidation(serializers.Serializer):
    property_id = serializers.IntegerField(required=True, min_value=0)
