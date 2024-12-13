from django.contrib import admin
from .models import CustomUser, Item, Post

admin.site.register(Item)
admin.site.register(Post)
admin.site.register(CustomUser)