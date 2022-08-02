from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from integrations.api.tomtom_api import get_nearby_restaurants

class NearbyRestaurantsView(APIView):

    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        latitude = request.query_params.get('latitude')
        longitude = request.query_params.get('longitude')
        response = get_nearby_restaurants(latitude, longitude)
        if response != None:
            return Response(response)
        else:
            return Response(status=400)

        