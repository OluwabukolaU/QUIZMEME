from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response 
from ..serializers import UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from ..permissions import IsUserOrReadOnly

class OneUser(APIView):

    permission_classes = [IsUserOrReadOnly]

    serializer_class = UserSerializer

    def get_object(self, pk):
        object = get_object_or_404(User,id=pk)
        self.check_object_permissions(self.request, object)
        return object

    @swagger_auto_schema(
        operation_summary='Get a user',
        operation_description='Get a single user by id',
        responses={201: UserSerializer, 400: 'Bad Request', 404: 'Not Found'}
    )
        
    def get(self,request, pk):

        try:
            user = self.get_object(pk)
            serializer = UserSerializer(user)
            return Response (serializer.data,status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary='Update a user',
        operation_description='Update a single user by id',
        responses={201: UserSerializer, 400: 'Bad Request', 404: 'Not Found'}
    )
        
    def put(self, request, pk):

        user = self.get_object(pk)
        serializer = UserSerializer(user, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_200_OK)
        else:
            return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @swagger_auto_schema(
        operation_summary='Delete a user',
        operation_description='Delete a single user by id',
        responses={201: UserSerializer, 400: 'Bad Request', 404: 'Not Found'}
    )

        
    def delete(self, request, pk):
        user = self.get_objects(pk)
        user.delete()
        return Response (status=status.HTTP_200_OK)
    
