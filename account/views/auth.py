from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response 
from ..serializers import UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class Auth(APIView):

    @swagger_auto_schema(
        operation_summary='Login',
        operation_description='Login User.',
        request_body=UserSerializer,
        responses={201: UserSerializer, 400: 'Bad Request'}
    )

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user=authenticate(request, username=username, password=password)
        if not user:
            return Response (status=status.HTTP_400_BAD_REQUEST)
        login(request, user)
        serializer=UserSerializer(user)
        return Response (serializer.data)
    
    @swagger_auto_schema(
        operation_summary='Logout',
        operation_description='Logout User.',
        responses={200: 'OK'}
    )
    
    def get(self,request):
        logout(request)
        return Response(status=status.HTTP_200_OK)