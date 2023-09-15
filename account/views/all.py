from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response 
from ..serializers import UserSerializer
from django.contrib.auth.models import User
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class AllUsers(APIView):

    serializer_class = UserSerializer

    @swagger_auto_schema(
        operation_summary='List all users',
        operation_description='List all users',
        responses={201: UserSerializer, 400: 'Bad Request'}
    )

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)
            
            