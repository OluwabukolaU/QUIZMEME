from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from quiz.permissions import IsAuthorOrReadOnly
from quiz.models import Quiz, Question, Choice
from quiz.serializers import QuizSerializer, QuestionSerializer, ChoiceSerializer
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

class GetQuiz(APIView):
    """
    get:
    Get a quiz by id.
    """
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_object(self, pk):
        obj = get_object_or_404(Quiz, pk=pk)
        self.check_object_permissions(self.request, obj)
        return obj
    
    @swagger_auto_schema(
        responses={
            200: QuizSerializer(),
            404: "Quiz not found."
        }
    )
    def get(self, request, pk):
        quiz = self.get_object(pk)
        serializer = QuizSerializer(quiz)
        full_quiz = serializer.data
        questions = Question.objects.filter(quiz=quiz.id)
        full_quiz["questions"] = []
        for question in questions:
            question_serializer = QuestionSerializer(question)
            full_question = question_serializer.data
            choices = Choice.objects.filter(question=question.id)
            full_question["choices"] = []
            for choice in choices:
                choice_serializer = ChoiceSerializer(choice)
                full_question["choices"].append(choice_serializer.data)
            full_quiz["questions"].append(full_question)
        return Response(full_quiz, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=QuizSerializer(),
        responses={
            200: QuizSerializer(),
            400: "Bad request."
        }
    )
    def put(self, request, pk):
        quiz = self.get_object(pk)
        serializer = QuizSerializer(quiz, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @swagger_auto_schema(
        responses={
            204: "Quiz deleted.",
            404: "Quiz not found."
        }
    )

    def delete(self, request, pk):
        quiz = self.get_object(pk)
        quiz.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)