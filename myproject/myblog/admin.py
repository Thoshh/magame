# Location myproject>myblog>admin.py
# Register your models here.

from django.contrib import admin
from django import forms

from myblog.models import MyBlog, Tag

admin.site.register(MyBlog)
admin.site.register(Tag)
