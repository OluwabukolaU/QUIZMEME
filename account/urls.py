from django.urls import path

from . import views

urlpatterns = [
     path('',views.AllUsers.as_view()),
     path('create', views.CreateUser.as_view()),
     path('<int:pk>',views.OneUser.as_view()),
     path('auth', views.Auth.as_view()),
     path('verify/<int:pk>/<uuid:token>', views.verify),
]