from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  # return HttpResponse("Home page")
  return render(request, "main.html")