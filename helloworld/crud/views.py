from django.http import HttpResponse
from django.shortcuts import render
from .models import Item

def index(request):
  items = Item.objects.all()
  context = {}
  return render(request, "details.html")

def add(request):
  return render(request, "details_add.html")