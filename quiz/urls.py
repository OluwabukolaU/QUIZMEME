from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.GetQuiz.as_view(), name='get_quiz'),
    path('create/', views.CreateQuiz.as_view(), name='create_quiz'),
]