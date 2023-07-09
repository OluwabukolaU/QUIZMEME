from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sign_up(request):
     return HttpResponse("<h1>Sign Up</h1>")

def sign_out(request):
     return HttpResponse("<h1>SIgn Out</h1>")