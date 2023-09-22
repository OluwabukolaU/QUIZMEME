from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from quiz.permissions import IsAuthorOrReadOnly
from quiz.models import Question
from quiz.serializers import QuestionSerializer
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404

class GetQuestion(APIView):
    """
    get:
    Get a question by id.
    """
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_object(self, pk):
        obj = get_object_or_404(Question, pk=pk)
        self.check_object_permissions(self.request, obj)
        return obj
    
    @swagger_auto_schema(
        responses={
            200: QuestionSerializer(),
            404: "Question not found."
        }
    )
    def get(self, request, pk):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=QuestionSerializer(),
        responses={
            200: QuestionSerializer(),
            400: "Bad request."
        }
    )
    def put(self, request, pk):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        responses={
            204: "Question deleted.",
            404: "Question not found."
        }
    )
    def delete(self, request, pk):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)