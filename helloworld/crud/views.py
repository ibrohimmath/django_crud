from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CustomUserForm
from .models import CustomUser, Item, Post

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

def get_users(request):
  print("path", request.path)
  users = CustomUser.objects.all()
  return render(request, "users.html", {"users": users})

def add_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users')  # Redirect to the user list or another page
    else:
        form = CustomUserForm()
    return render(request, 'add_user.html', {'form': form})

def update_user(request, id):
    user = get_object_or_404(CustomUser, pk=id)

    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')  # Redirect to a page showing the updated list of users
    else:
        form = CustomUserForm(instance=user)

    return render(request, 'update_user.html', {'form': form, 'user': user})