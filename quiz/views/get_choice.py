from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from quiz.permissions import IsAuthorOrReadOnly
from quiz.models import Choice
from quiz.serializers import ChoiceSerializer
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404

class GetChoice(APIView):
    """
    get:
    Get a choice by id.
    """
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_object(self, pk):
        obj = get_object_or_404(Choice, pk=pk)
        self.check_object_permissions(self.request, obj)
        return obj
    
    @swagger_auto_schema(
        responses={
            200: ChoiceSerializer(),
            404: "Choice not found."
        }
    )
    def get(self, request, pk):
        choice = self.get_object(pk)
        serializer = ChoiceSerializer(choice)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=ChoiceSerializer(),
        responses={
            200: ChoiceSerializer(),
            400: "Bad request."
        }
    )
    def put(self, request, pk):
        choice = self.get_object(pk)
        serializer = ChoiceSerializer(choice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        responses={
            204: "Choice deleted.",
            404: "Choice not found."
        }
    )
    def delete(self, request, pk):
        choice = self.get_object(pk)
        choice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)