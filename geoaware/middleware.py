from geo import get_geo_info
from django.utils.functional import SimpleLazyObject


class GeoAwareSessionMiddleware(object):
    """ Saves geo info in session if GeoIP is configured for city or country.

    geo_info = {
        'fqdn_or_ip': '',
        'city': '', 
        'continent_code': '', 
        'region': '',
        'charset': 0,
        'area_code': 0,
        'longitude': 0.0,
        'country_code3': '',
        'latitude': 0.0,
        'postal_code': None,
        'dma_code': 0,
        'country_code': '',
        'country_name': '',
    }
    """

    @staticmethod
    def process_request(request):
        """ Save or update geo info in session """

        request.location = SimpleLazyObject(lambda: get_geo_info(request))
        return None
