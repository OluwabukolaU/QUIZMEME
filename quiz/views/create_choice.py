from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from quiz.permissions import IsAuthorOrReadOnly
from quiz.models import Question
from quiz.serializers import ChoiceSerializer
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404

class CreateChoice(APIView):
    """
    post:
    Create a new choice.
    """
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_object(self, question_id):
        obj = get_object_or_404(Question, pk=question_id)
        self.check_object_permissions(self.request, obj)
        return obj

    @swagger_auto_schema(
        request_body=ChoiceSerializer(),
        responses={
            201: ChoiceSerializer(),
            400: "Bad request."
        }
    )
    def post(self, request, question_id):
        question = self.get_object(question_id)
        serializer = ChoiceSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(question=question)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)