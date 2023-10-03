from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from ..models import Quiz, Question, Choice, Attempt, Answer
from ..serializers import QuizSerializer, QuestionSerializer, ChoiceSerializer, AttemptSerializer, AnswerSerializer
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404

class CreateAttempt(APIView):
    """
    post:
    Create a new attempt.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, quiz_id):
        obj = get_object_or_404(Quiz, pk=quiz_id)
        self.check_object_permissions(self.request, obj)
        return obj

    @swagger_auto_schema(
        request_body=AttemptSerializer(),
        responses={
            201: AttemptSerializer(),
            400: "Bad request."
        }
    )
    def post(self, request, quiz_id):
        quiz = self.get_object(quiz_id)
        serializer = AttemptSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user, quiz=quiz)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CreateAnswer(APIView):
    """
    post:
    Create a new answer.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, attempt_id):
        obj = get_object_or_404(Attempt, pk=attempt_id)
        self.check_object_permissions(self.request, obj)
        return obj

    @swagger_auto_schema(
        request_body=AnswerSerializer(),
        responses={
            201: AnswerSerializer(),
            400: "Bad request."
        }
    )
    def post(self, request, attempt_id):
        attempt = self.get_object(attempt_id)
        serializer = AnswerSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(attempt=attempt)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class GetAttempt(APIView):
    """
    get:
    Get a specific attempt.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, attempt_id):
        obj = get_object_or_404(Attempt, pk=attempt_id)
        self.check_object_permissions(self.request, obj)
        return obj

    @swagger_auto_schema(
        responses={
            200: AttemptSerializer(),
            404: "Not found."
        }
    )
    def get(self, request, attempt_id):
        attempt = self.get_object(attempt_id)
        serializer = AttemptSerializer(attempt)
        answers = Answer.objects.filter(attempt=attempt)
        answer_serializer = AnswerSerializer(answers, many=True)
        serializer.data['answers'] = answer_serializer.data
        return Response(serializer.data)
    
class GetMyAttempts(APIView):
    """
    get:
    Get all attempts of the current user.
    """
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={
            200: AttemptSerializer(many=True),
            404: "Not found."
        }
    )
    def get(self, request):
        attempts = Attempt.objects.filter(user=request.user)
        serializer = AttemptSerializer(attempts, many=True)
        return Response(serializer.data)