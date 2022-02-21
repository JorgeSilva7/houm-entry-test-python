"""
Common error's list.

part of errors module.
"""
from rest_framework.exceptions import APIException


class InternalError(APIException):
    status_code = 500
    default_detail = 'An internal error has ocurred'
    default_code = 'common_internal_error'

    def setDetail(self, error=None):
        if error:
            e = APIException(detail=str(error))
            e.status_code = 500
            return e
        else:
            return InternalError


class BadRequest(APIException):
    status_code = 400
    default_detail = 'An error exists in the request (BAD REQUEST)'
    default_code = 'common_bad_request'

    def setDetail(self, error=None):
        if error:
            e = APIException(detail=error)
            e.status_code = 400
            return e
        else:
            return BadRequest


class NotFound(APIException):
    status_code = 404
    default_detail = 'Register not found'
    default_code = 'common_not_found'

    def setDetail(self, error=None):
        if error:
            e = APIException(detail=str(error)+' not found')
            e.status_code = 404
            return e
        else:
            return NotFound


class Unauthorized(APIException):
    status_code = 403
    default_detail = "Unauthorized"
    default_code = 'common_no_permission'

    def setDetail(self, error=None):
        if error:
            e = APIException(detail=str(error))
            e.status_code = 403
            return e
        else:
            return Unauthorized
