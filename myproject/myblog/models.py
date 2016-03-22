from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

# class Tag (models.Model):
#     name = models.CharField(max_length=255)
#     description = models.Charfield(max_legnth=255, null=True, default'')

#     def __str__(self):
#         return self.name
 
# class MyBlog(models.Model)
#     title = models.CharField(max_legnth=255)
#     body = models.CharField(max_legnth=40000)
#     tags = models.ManyToManyField(Tag)

#     def __str__(self)
#         return self.title



