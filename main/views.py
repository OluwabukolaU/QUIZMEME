from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout as django_logout

# Create your views here.
def index(request):
     return render(request, 'index.html')

def logout(request):
     django_logout(request)
     return redirect('index')

def auth(request):
     return render(request, 'auth.html')
