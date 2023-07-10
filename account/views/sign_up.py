from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, logout

# Create your views here.
def sign_up(request):
     if request.method == "POST":
          username = request.POST.get("username")
          email = request.POST.get("email")
          password = request.POST.get("password")
          print(f"{username}: {email}: {password}")
          return HttpResponse("Request Sent")
     return render(request, 'auth/sign_up.html')

def sign_out(request):
     logout(request)
     return HttpResponseRedirect("/")