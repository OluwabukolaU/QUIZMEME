from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response 
from ..serializers import UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


class Auth(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user=authenticate(request, username=username, password=password)
        if not user:
            return Response (status=status.HTTP_400_BAD_REQUEST)
        login(request, user)
        serializer=UserSerializer(user)
        return Response (serializer.data)
    
    def get(self,request):
        logout(request)
        return Response(status=status.HTTP_200_OK)