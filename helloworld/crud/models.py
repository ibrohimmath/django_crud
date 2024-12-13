from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  image = models.ImageField(upload_to='img/', blank = True, null = True)

class Item(models.Model):
  name = models.CharField(max_length = 30)

  def __str__(self):
    return self.name
  
class Post(models.Model):
  id = models.PositiveIntegerField(primary_key=True)
  title = models.CharField(max_length = 50)
  description = models.TextField()

  def __str__(self):
    return self.title