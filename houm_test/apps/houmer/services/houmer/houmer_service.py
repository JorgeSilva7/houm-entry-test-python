import requests
from django.urls import reverse

from rest_framework import serializers
from houmer.models import Houmer
from django.contrib.auth.models import User
from houmer.utils.db_tools import wait_and_process_transaction

from houmer.errors.common_error import BadRequest


class HoumerService(object):

    @wait_and_process_transaction()
    def create(self, request):
        urls = {
            'rest_register': request.build_absolute_uri(reverse('rest_register'))
        }
        url = urls['rest_register']

        form = CreateHoumerValidation(data=request.data)
        if not form.is_valid():
            raise BadRequest.setDetail(None, form.errors)

        username = request.data.get("username", None)
        password1 = request.data.get("password1", None)
        password2 = request.data.get("password2", None)
        payload = {
            'username': username,
            'password1': password1,
            'password2': password2
        }
        response = requests.post(url, data=payload)
        if response.status_code != 201:
            raise BadRequest(response.text)

        created_user = User.objects.get(username=username)

        Houmer.objects.create(name=request.data.get(
            "name", None), user=created_user)

        return True


class CreateHoumerValidation(serializers.Serializer):
    """ """
    username = serializers.CharField(min_length=2, max_length=12)
    password1 = serializers.CharField(min_length=5, max_length=50)
    password2 = serializers.CharField(min_length=5, max_length=50)
    name = serializers.CharField(min_length=2, max_length=100)
