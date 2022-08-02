from django.urls import re_path

from rest_framework.authtoken.views import obtain_auth_token

from core.api.logout_api import logout
from core.api.restaurants_api import NearbyRestaurantsView

urlpatterns = [
    re_path( 'login', obtain_auth_token, name = 'api-login' ),
    re_path( 'logout', logout, name = 'api-logout' ),
    re_path( 'nearby-restaurants', NearbyRestaurantsView.as_view(), name = 'api-nearby-restaurants' ),
]