from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.GetQuiz.as_view(), name='get_quiz'),
    path('create/', views.CreateQuiz.as_view(), name='create_quiz'),
    path('question/<int:quiz_id>/create/', views.CreateQuestion.as_view(), name='create_question'),
    path('choice/<int:question_id>/create/', views.CreateChoice.as_view(), name='create_choice'),
    path('choice/<int:pk>/', views.GetChoice.as_view(), name='get_choice'),
    path('question/<int:pk>/', views.GetQuestion.as_view(), name='get_question'),
]