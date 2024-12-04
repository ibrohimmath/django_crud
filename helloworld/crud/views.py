from django.http import HttpResponse
from django.shortcuts import render
from .models import Item, Post

def index(request):
  items = Item.objects.all()
  return render(request, "details.html", {"items": items})

def add(request):
  return render(request, "details_add.html")

def get_posts(request):
  posts = Post.objects.all()
  return render(request, "posts.html", {"posts": posts})

def get_post(request, post_id):
  post = Post.objects.get(id=post_id)
  return render(request, "post.html", {"post": post})
