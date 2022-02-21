from rest_framework_simplejwt.authentication import JWTAuthentication
from houmer.errors.common_error import Unauthorized


class CommonUtilities(object):

    @staticmethod
    def get_user(request):
        try:
            auth_data = JWTAuthentication().authenticate(request)
            if auth_data is not None:
                return auth_data[0]
        except Exception:
            raise Unauthorized
