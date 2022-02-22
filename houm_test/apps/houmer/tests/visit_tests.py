from datetime import datetime
from django.test import TestCase, Client
from rest_framework_simplejwt.tokens import RefreshToken
import json

from houmer.models import Houmer, Property
from django.contrib.auth.models import User


class VisitTestCase(TestCase):

    VISIT_PATH = '/v1/visits/'
    CONTENT_TYPE = 'application/json'

    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            password="test"
        )
        houmer = Houmer.objects.create(user=self.user, name="test")
        self.prop1 = Property.objects.create(houmer=houmer, name="Casa 1", coordinates={
            "latitude": -38.7288152829259,
            "longitude": -72.61304485137737
        })
        self.prop2 = Property.objects.create(houmer=houmer, name="Casa 2", coordinates={
            "latitude": -38.717392218041645,
            "longitude": -72.55483729888249
        })

        self.c = Client()

    def test_create_visit(self):
        """Create visit"""
        token = RefreshToken.for_user(self.user)

        # Create an instance of a POST request.
        response = self.c.post(self.VISIT_PATH, json.dumps({
            "property_id": self.prop1.id
        }), content_type=self.CONTENT_TYPE, HTTP_AUTHORIZATION='Bearer '+str(token.access_token))

        self.assertEqual(response.status_code, 201)

    def test_end_visit(self):
        """End visit not found"""
        token = RefreshToken.for_user(self.user)

        # Create an instance of a POST request.
        response = self.c.patch(self.VISIT_PATH+"1/end", content_type=self.CONTENT_TYPE,
                                HTTP_AUTHORIZATION='Bearer '+str(token.access_token))

        self.assertEqual(response.status_code, 404)

    def test_create_visit_unauthorized(self):
        token = RefreshToken.for_user(self.user)

        # Create an instance of a POST request.
        response = self.c.post(self.VISIT_PATH, json.dumps({
            "property_id": self.prop1.id
        }), content_type=self.CONTENT_TYPE, HTTP_AUTHORIZATION='Bearer '+str(token.access_token)+"asdasd123")

        self.assertEqual(response.status_code, 401)

    def test_create_visit_bad_request(self):
        token = RefreshToken.for_user(self.user)

        # Create an instance of a POST request.
        response = self.c.post(self.VISIT_PATH, json.dumps({
            "property_id": ""
        }), content_type=self.CONTENT_TYPE, HTTP_AUTHORIZATION='Bearer '+str(token.access_token))
        self.assertEqual(response.status_code, 400)

    def test_list_visits_with_duration(self):
        """List visits"""
        token = RefreshToken.for_user(self.user)

        date = datetime.now()
        date_string = date.strftime("%Y-%m-%d")
        # Create an instance of a POST request.
        response = self.c.get(
            self.VISIT_PATH+'?day='+str(date_string)+"&type=visit_duration", HTTP_AUTHORIZATION='Bearer '+str(token.access_token))

        self.assertEqual(response.status_code, 200)

    def test_list_visits_with_duration(self):
        """List visits"""
        token = RefreshToken.for_user(self.user)

        date = datetime.now()
        date_string = date.strftime("%Y-%m-%d")
        # Create an instance of a POST request.
        response = self.c.get(
            self.VISIT_PATH+'?day='+str(date_string)+"&type=move_speed", HTTP_AUTHORIZATION='Bearer '+str(token.access_token))

        self.assertEqual(response.status_code, 200)
