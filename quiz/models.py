from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Quiz(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
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
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    question_type = models.CharField(max_length=3, choices=types, default="MCQ")
    

    
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text