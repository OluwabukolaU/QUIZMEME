from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Quiz(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quiz_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.quiz_text

class Question(models.Model):

    types = ( 
        ("MCQ", "Multiple Choice Question"),
        ("TF", "True or False"),
        ("SA", "Short Answer"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    question_type = models.CharField(max_length=3, choices=types, default="MCQ")
    
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text
    
class Attempt(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    attempt_date = models.DateTimeField(default=datetime.now)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username + " " + self.quiz.quiz_text + " " + str(self.attempt_date) + " " + str(self.score)
    
class Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    attempt = models.ForeignKey(Attempt, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True)
    answer_text = models.CharField(max_length=200)
    def __str__(self):
        return self.attempt.user.username + " " + self.question.question_text + " " + self.answer_text
