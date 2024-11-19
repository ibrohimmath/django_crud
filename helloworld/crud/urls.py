from django.urls import path
from . import views 

urlpatterns = [
  path("", views.index, name = 'details'),
  path("add/", views.add, name='details_add'),
]