from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.
def sign_in(request):
     if request.method == "POST":
          username = request.POST.get("username")
          password = request.POST.get("password")

          user = authenticate(request, username=username, password=password)
          
          if user != None:
               login(request, user)

               return HttpResponseRedirect("/")
          
          else:
               return HttpResponse ("Invalid")

          return HttpResponse (f"{username}: {password}")
     return render(request, 'auth/sign_in.html')