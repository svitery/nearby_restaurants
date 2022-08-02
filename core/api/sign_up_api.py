from django.contrib.auth.models import User
from django.db import IntegrityError

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class SignUpView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        try:
            User.objects.create_user(username=username, password=password, email=email)
            return Response(status=200)
        except IntegrityError:
            return Response(status=400)