from django.db import models

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', default=1)
    title = models.CharField(null=False, blank=False, max_length=256)
    content = models.TextField(null=False, blank=False,max_length=2048)
    uploaded_date = models.DateTimeField(auto_created=True, auto_now=True)

class Chat(models.Model):
    title = models.CharField(null=False, blank=False, max_length=256)
    created_date = models.DateTimeField(auto_created=True, auto_now=True)

class Message(models.Model):
    user = models.ForeignKey('auth.User', default=1)
    title = models.CharField(null=False, blank=False, max_length=256)
    created_date = models.DateTimeField(auto_created=True, auto_now=True)
    chat = models.ForeignKey('api.Chat', default=1)