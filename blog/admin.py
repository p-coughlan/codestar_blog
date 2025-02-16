from django.contrib import admin
from .models import Post
# Register your models here.

# This line registers the Post model with the admin site
admin.site.register(Post)
