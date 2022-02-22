from django.test import TestCase, Client
from rest_framework_simplejwt.tokens import RefreshToken
import json

from houmer.models import Houmer
from django.contrib.auth.models import User


class PropertyTestCase(TestCase):

    PROPERTY_PATH = '/v1/properties/'
    CONTENT_TYPE = 'application/json'

    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            password="test"
        )
        Houmer.objects.create(user=self.user, name="test")

        self.c = Client()

    def test_create_property(self):
        """Create property"""
        token = RefreshToken.for_user(self.user)

        # Create an instance of a POST request.
        response = self.c.post(self.PROPERTY_PATH, json.dumps({
            "name": "Casa 1",
            "coordinates": {
                "latitude": -38.7288152829259,
                "longitude": -72.61304485137737
            }
        }), content_type=self.CONTENT_TYPE, HTTP_AUTHORIZATION='Bearer '+str(token.access_token))

        self.assertEqual(response.status_code, 201)

    def test_create_property_unauthorized(self):
        """Create property"""
        token = RefreshToken.for_user(self.user)

        # Create an instance of a POST request.
        response = self.c.post(self.PROPERTY_PATH, json.dumps({
            "name": "Casa 2",
            "coordinates": {
                "latitude": -38.7288152829259,
                "longitude": -72.61304485137737
            }
        }), content_type=self.CONTENT_TYPE, HTTP_AUTHORIZATION='Bearer '+str(token.access_token)+"asdasd123")

        self.assertEqual(response.status_code, 401)

    def test_create_property_bad_request(self):
        """Create property"""
        token = RefreshToken.for_user(self.user)

        # Create an instance of a POST request.
        response = self.c.post(self.PROPERTY_PATH, json.dumps({
            "name": "Casa 3",
            "coordinates": {

            }
        }), content_type=self.CONTENT_TYPE, HTTP_AUTHORIZATION='Bearer '+str(token.access_token))
        self.assertEqual(response.status_code, 400)

    def test_list_properties(self):
        """List properties"""
        token = RefreshToken.for_user(self.user)

        # Create an instance of a POST request.
        response = self.c.get(
            self.PROPERTY_PATH, HTTP_AUTHORIZATION='Bearer '+str(token.access_token))

        self.assertEqual(response.status_code, 200)
