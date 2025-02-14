from django.db import models
from django.contrib.auth.models import User

# STATUS is a tuple that will be used for the status field in the Post model
STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True) # unique=True means that each title must be unique
    slug = models.SlugField(max_length=200, unique=True) # slug is a URL friendly version of the title
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts') # ForeignKey is a one-to-many relationship. on_delete=models.CASCADE means that if the user is deleted, all of their posts will be deleted as well
    content = models.TextField() # TextField is for long text without a limit, this is where the blog post content will go
    created_on = models.DateTimeField(auto_now_add=True) # auto_now_add=True means that the date and time will be set when the post is created
    status = models.IntegerField(choices=STATUS, default=0) # status is an integer field with choices from the STATUS tuple, default is 0