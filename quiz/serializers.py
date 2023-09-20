from rest_framework import serializers
from .models import Quiz, Question, Choice

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'quiz_text', 'pub_date']

    def create(self, validated_data):
        if validated_data.get('author') != self.context['request'].user:
            raise serializers.ValidationError("You can't create a quiz for another user.")
        quiz = Quiz.objects.create(**validated_data)
        return quiz

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'quiz', 'question_text', 'question_type']

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'question', 'choice_text', 'correct']
