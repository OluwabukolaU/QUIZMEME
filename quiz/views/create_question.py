from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from quiz.permissions import IsAuthorOrReadOnly
from quiz.models import Quiz
from quiz.serializers import QuestionSerializer
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404

class CreateQuestion(APIView):
    """
    post:
    Create a new question.
    """
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_object(self, quiz_id):
        obj = get_object_or_404(Quiz, pk=quiz_id)
        self.check_object_permissions(self.request, obj)
        return obj

    @swagger_auto_schema(
        request_body=QuestionSerializer(),
        responses={
            201: QuestionSerializer(),
            400: "Bad request."
        }
    )
    def post(self, request, quiz_id):
        quiz = self.get_object(quiz_id)
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(quiz=quiz)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)