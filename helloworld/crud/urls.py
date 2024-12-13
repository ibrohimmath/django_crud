from django.urls import path
from . import views 

urlpatterns = [
  path("posts/", views.get_posts, name = 'posts'),
  path("<int:post_id>", views.get_post, name = 'post'),
  path("items/", views.index, name = 'items'),
  path("items/add/", views.add, name='details_add'),
  path("users/", views.get_users, name='users'),
  path("users/add", views.add_user, name="users_add"),
  path("users/edit/<int:id>/", views.update_user, name="users_edit")
]