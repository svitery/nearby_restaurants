from django.urls import re_path

from rest_framework.authtoken.views import obtain_auth_token

from core.api.logout_api import LogoutView
from core.api.restaurants_api import NearbyRestaurantsView
from core.api.sign_up_api import SignUpView

urlpatterns = [
    re_path( 'sign-up', SignUpView.as_view(), name='sign-up' ),
    re_path( 'login', obtain_auth_token, name = 'api-login' ),
    re_path( 'logout', LogoutView.as_view(), name = 'api-logout' ),
    re_path( 'nearby-restaurants', NearbyRestaurantsView.as_view(), name = 'api-nearby-restaurants' ),
]