from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response 
from ..serializers import UserSerializer
from django.contrib.auth.models import User


class AllUsers(APIView):


    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)
            
            