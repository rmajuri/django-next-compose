from django.db import models
from ckeditor.fields import RichTextField

class Creator(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    twitter = models.CharField(max_length=200, blank=True, null=True)
    facebook = models.CharField(max_length=200, blank=True, null=True)
    instagram = models.CharField(max_length=200, blank=True, null=True)
    linkedin = models.CharField(max_length=200, blank=True, null=True)
    youtube = models.CharField(max_length=200, blank=True, null=True)
    tiktok = models.CharField(max_length=200, blank=True, null=True)
    snapchat = models.CharField(max_length=200, blank=True, null=True)
    twitch = models.CharField(max_length=200, blank=True, null=True)

class Post(models.Model):
    creator = models.ForeignKey('app.Creator', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    content= RichTextField(blank=True, null=True)
    image = models.CharField(max_length=200, blank=True, null=True)
    video = models.CharField(max_length=200, blank=True, null=True)
    audio = models.CharField(max_length=200, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(blank=True, null=True)
    comments = models.IntegerField(blank=True, null=True)
    shares = models.IntegerField(blank=True, null=True)