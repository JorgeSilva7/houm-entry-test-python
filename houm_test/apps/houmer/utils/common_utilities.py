from rest_framework_simplejwt.authentication import JWTAuthentication
from houmer.errors.common_error import Unauthorized, BadRequest
from math import radians, cos, sin, asin, sqrt

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

    @staticmethod
    def millisToMinutesAndSeconds(seconds):
        seconds = int(seconds)
        seconds_return=seconds%60
        minutes=(seconds/60)%60
        minutes = int(minutes)

        return minutes, seconds_return

    @staticmethod
    def haversine(coordinates1, coordinates2):
        """
        Calculate the great circle distance in kilometers between two points 
        on the earth (specified in decimal degrees)
        """
        # convert decimal degrees to radians 
        lat1 = coordinates1["latitude"]
        lon1 = coordinates1["longitude"]

        lat2 = coordinates2["latitude"]
        lon2 = coordinates2["longitude"]
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        # haversine formula 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
        return c * r