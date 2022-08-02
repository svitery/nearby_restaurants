import requests

from nearby_restaurants.settings import TOMTOM_API_KEY, TOMTOM_API_VERSION, TOMTOM_BASER_URL

def get_nearby_restaurants( latitude, longitude ):
    url = f'{ TOMTOM_BASER_URL }/search/{ TOMTOM_API_VERSION }/nearbySearch/.json'
    params = {
        'key': TOMTOM_API_KEY,
        'lat': latitude,
        'lon': longitude,
    }
    response = requests.get( url, params=params )
    if response.status_code == 200:
        return response.json()['results']
    else:
        return None