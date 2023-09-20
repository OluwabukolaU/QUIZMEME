from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from quiz.permissions import IsAuthorOrReadOnly
from quiz.models import Quiz, Question, Choice
from quiz.serializers import QuizSerializer, QuestionSerializer, ChoiceSerializer
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

class CreateQuiz(APIView):
    """
    post:
    Create a new quiz.
    """
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=QuizSerializer(),
        responses={
            201: QuizSerializer(),
            400: "Bad request."
        }
    )
    def post(self, request):
        serializer = QuizSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)