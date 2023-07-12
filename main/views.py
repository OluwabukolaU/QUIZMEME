from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def index(request):
     return HttpResponse(f"Hello, {request.user}")

@api_view(['GET'])
def test(request):
     return Response({"message": "Hello, World!", "status": "success"})
