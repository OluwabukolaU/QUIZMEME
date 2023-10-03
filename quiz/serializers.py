from rest_framework import serializers
from .models import Quiz, Question, Choice, Attempt, Answer

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

    def create(self, validated_data):
        if validated_data.get('quiz').author != self.context['request'].user:
            raise serializers.ValidationError("You can't create a question for another user's quiz.")
        question = Question.objects.create(**validated_data)
        return question

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'question', 'choice_text', 'correct']

    def create(self, validated_data):
        if validated_data.get('question').quiz.author != self.context['request'].user:
            raise serializers.ValidationError("You can't create a choice for another user's quiz.")
        choice = Choice.objects.create(**validated_data)
        return choice

class AttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attempt
        fields = ['id', 'user', 'quiz', 'attempt_date', 'score']

    def create(self, validated_data):
        if Attempt.objects.filter(user=self.context['request'].user, quiz=validated_data.get('quiz')).exists():
            raise serializers.ValidationError("You can't create more than one attempt for the same quiz.")

        if validated_data.get('user') != self.context['request'].user:
            raise serializers.ValidationError("You can't create an attempt for another user.")
        attempt = Attempt.objects.create(**validated_data)
        return attempt

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['attempt', 'question', 'option', 'answer_text']


    def create(self, validated_data):
        if validated_data.get('attempt').user != self.context['request'].user:
            raise serializers.ValidationError("You can't create an answer for another user's attempt.")
        answer = Answer.objects.create(**validated_data)
        correct = validated_data.get('question').choice_set.get(correct=True)
        if answer.option == correct:
            answer.attempt.score += 1
            answer.attempt.save()

        return answer