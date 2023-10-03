from django.urls import path
from . import views

urlpatterns = [
    path('<uuid:pk>/', views.GetQuiz.as_view(), name='get_quiz'),
    path('my/', views.GetMyQuizzes.as_view(), name='get_my_quizzes'),
    path('create/', views.CreateQuiz.as_view(), name='create_quiz'),
    path('<uuid:quiz_id>/question/create/', views.CreateQuestion.as_view(), name='create_question'),
    path('<uuid:question_id>/choice/create/', views.CreateChoice.as_view(), name='create_choice'),
    path('choice/<uuid:pk>/', views.GetChoice.as_view(), name='get_choice'),
    path('question/<uuid:pk>/', views.GetQuestion.as_view(), name='get_question'),
    path('<uuid:quiz_id>/attempt/create/', views.CreateAttempt.as_view(), name='create_attempt'),
    path('<uuid:attempt_id>/attempt/answer/create/', views.CreateAnswer.as_view(), name='create_answer'),
    path('attempt/<uuid:pk>/', views.GetAttempt.as_view(), name='get_attempt'),
    path('attempt/my/', views.GetMyAttempts.as_view(), name='get_my_attempts'),
]