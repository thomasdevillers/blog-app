from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User #User model
from django.urls import reverse #redirect to post-detail page after creating post

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) #timezone.now is a function, not a function call
    author = models.ForeignKey(User, on_delete=models.CASCADE) #if user is deleted, delete posts

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})


