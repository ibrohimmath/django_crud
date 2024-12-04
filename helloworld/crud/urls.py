from django.urls import path
from . import views 

urlpatterns = [
  path("", views.get_posts, name = 'posts'),
  path("<int:post_id>", views.get_post, name = 'post'),
  path("items/", views.index, name = 'items'),
  path("items/add/", views.add, name='details_add'),
]