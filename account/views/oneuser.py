from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response 
from ..serializers import UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from ..permissions import IsUserOrReadOnly

class OneUser(APIView):
    permission_classes = [IsUserOrReadOnly]
    def get_object(self, pk):
        object = get_object_or_404(User,id=pk)
        self.check_object_permissions(self.request, object)
        return object
        
    def get(self,request, pk):

        try:
            user = self.get_object(pk)
            serializer = UserSerializer(user)
            return Response (serializer.data,status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk):

        user = self.get_object(pk)
        serializer = UserSerializer(user, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_200_OK)
        else:
            return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

        
    def delete(self, request, pk):
        user = self.get_objects(pk)
        user.delete()
        return Response (status=status.HTTP_200_OK)
    
