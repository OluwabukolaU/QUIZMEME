from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User

# Create your views here.
def sign_up(request):
     if request.method == "POST":
          username = request.POST.get("username")
          email = request.POST.get("email")
          password = request.POST.get("password")
          confirm_password = request.POST.get("confirm_password")

          if password == confirm_password:
               pass
          else:
               return HttpResponse("Password does not match")

          try:
               user = User.objects.create_user(username=username, email=email, password=password)
               user.save()
               login(request, user)
               return HttpResponseRedirect("/")

          except:
               return HttpResponse("Username or Email already exists")
          return HttpResponse("Request Sent")

     return render(request, 'auth/sign_up.html')

def sign_out(request):
     logout(request)
     return HttpResponseRedirect("/")