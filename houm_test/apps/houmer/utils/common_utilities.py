from rest_framework_simplejwt.authentication import JWTAuthentication
from houmer.errors.common_error import Unauthorized, BadRequest


class CommonUtilities(object):

    @staticmethod
    def get_user(request):
        try:
            auth_data = JWTAuthentication().authenticate(request)
            if auth_data is not None:
                return auth_data[0]
        except Exception:
            raise Unauthorized

    @staticmethod
    def get_page_limit(request):
        page = None
        limit = None
        try:
            page = int(request.GET.get('page', 1))
            limit = int(request.GET.get('limit', 10))

            if page < 0 or limit < 0:
                raise
        except Exception:
            raise BadRequest(
                "Page and limit must be a integer and more than 0")

        return page, limit
